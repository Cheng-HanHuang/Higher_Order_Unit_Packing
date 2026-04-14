#!/usr/bin/env python3
from __future__ import annotations

import argparse
import csv
import json
import subprocess
import sys
from dataclasses import dataclass
from pathlib import Path
from typing import Any


@dataclass(frozen=True)
class ProblemSpec:
    problem_id: str
    family: str
    params: dict[str, Any]
    note: str


def build_specs() -> list[ProblemSpec]:
    return [
        ProblemSpec("RU1", "random_unit", {"n": 40, "m": 80, "row_min": 4, "row_max": 8, "capacity_mode": "mixed"}, "Medium-large mixed-capacity random unit packing."),
        ProblemSpec("RU2", "random_unit", {"n": 60, "m": 120, "row_min": 5, "row_max": 10, "capacity_mode": "mixed"}, "Larger mixed-capacity random unit packing."),
        ProblemSpec("RU3", "random_unit", {"n": 60, "m": 120, "row_min": 5, "row_max": 10, "capacity_mode": "set_packing"}, "Capacity-1 variant with larger rows."),
        ProblemSpec("RU4", "random_unit", {"n": 80, "m": 160, "row_min": 5, "row_max": 10, "capacity_mode": "tight"}, "Tight-capacity regime at larger scale."),
        ProblemSpec("RU5", "random_unit", {"n": 80, "m": 160, "row_min": 6, "row_max": 12, "capacity_mode": "half"}, "Half-capacity larger-row regime."),
        ProblemSpec("RU6", "random_unit", {"n": 100, "m": 200, "row_min": 6, "row_max": 12, "capacity_mode": "mixed"}, "Largest random-unit stress setting in this suite."),
        ProblemSpec("KS1", "kset", {"n_sets": 60, "universe_size": 30, "k": 4, "density": 1.0}, "Denser 4-set packing baseline."),
        ProblemSpec("KS2", "kset", {"n_sets": 100, "universe_size": 40, "k": 5, "density": 1.0}, "Dense 5-set packing at larger size."),
        ProblemSpec("KS3", "kset", {"n_sets": 100, "universe_size": 40, "k": 5, "density": 0.7}, "Sparser 5-set packing at same size."),
        ProblemSpec("KS4", "kset", {"n_sets": 120, "universe_size": 50, "k": 5, "density": 1.0}, "Larger dense 5-set packing."),
        ProblemSpec("KS5", "kset", {"n_sets": 150, "universe_size": 60, "k": 6, "density": 0.7}, "Large sparse 6-set packing."),
        ProblemSpec("KS6", "kset", {"n_sets": 180, "universe_size": 70, "k": 6, "density": 0.7}, "Largest k-set stress setting in this suite."),
    ]


def load_json(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))


def save_json(obj: Any, path: Path) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(obj, indent=2), encoding="utf-8")


def latex_escape(s: str) -> str:
    repl = {"\\": r"\textbackslash{}", "&": r"\&", "%": r"\%", "$": r"\$", "#": r"\#", "_": r"\_", "{": r"\{", "}": r"\}", "~": r"\textasciitilde{}", "^": r"\textasciicircum{}"}
    return "".join(repl.get(ch, ch) for ch in s)


def call_wrapper(wrapper: Path, base_script: Path, out_json: Path, spec: ProblemSpec, seed: int, runs: int, tune_runs: int, tol_pg: float, max_iter: int) -> None:
    cmd = [sys.executable, str(wrapper), "--base-script", str(base_script), spec.family]
    if spec.family == "random_unit":
        cmd += ["--n", str(spec.params["n"]), "--m", str(spec.params["m"]), "--row-min", str(spec.params["row_min"]), "--row-max", str(spec.params["row_max"]), "--capacity-mode", str(spec.params["capacity_mode"])]
    else:
        cmd += ["--n-sets", str(spec.params["n_sets"]), "--universe-size", str(spec.params["universe_size"]), "--k", str(spec.params["k"]), "--density", str(spec.params["density"])]
    cmd += ["--runs", str(runs), "--tune-runs", str(tune_runs), "--seed", str(seed), "--tol-pg", str(tol_pg), "--max-iter", str(max_iter), "--out", str(out_json)]
    subprocess.run(cmd, check=True, stdout=subprocess.DEVNULL, stderr=subprocess.STDOUT)


def problem_statement_md(problem: dict[str, Any], result_rel_path: str) -> str:
    lines = [f"# Original problem: {problem['name']}\n", "This file records the exact original binary packing problem used for the matching run result.", "", "## Optimization model\n", "\\[", r"\max_{x\in\{0,1\}^n}\ \sum_{i=1}^n w_i x_i", r"\qquad\text{s.t.}\qquad", r"\sum_{i\in S_k} x_i \le B_k,\quad k=1,\dots,m.", "\\]", "", f"- Number of variables: `{problem['n']}`", f"- Number of constraints: `{len(problem['constraints'])}`", f"- Matching run-result file: `{result_rel_path}`", ""]
    md = problem.get("metadata", {})
    if md:
        lines.append("## Metadata\n")
        for k, v in md.items():
            if k == "candidate_sets":
                continue
            lines.append(f"- `{k}`: `{v}`")
        lines.append("")
    lines.append("## Weights\n")
    lines.append(", ".join(f"w_{i+1}={float(w):.8g}" for i, w in enumerate(problem["weights"])))
    lines.append("")
    if "candidate_sets" in md:
        lines.append("## Candidate sets (variables)\n")
        for j, subset in enumerate(md["candidate_sets"], start=1):
            lines.append(f"- Variable `x_{j}` corresponds to set `A_{j} = {{{', '.join(str(u+1) for u in subset)}}}`")
        lines.append("")
    lines.append("## Exact constraints\n")
    for k, c in enumerate(problem["constraints"], start=1):
        lhs = " + ".join(f"x_{i+1}" for i in c["indices"])
        lines.append(f"- Constraint `{k}`: {lhs} <= {c['capacity']}")
    lines.append("")
    return "\n".join(lines)


def problem_statement_tex(problem: dict[str, Any], result_rel_path: str) -> str:
    lines = [r"\documentclass[11pt]{article}", r"\usepackage[margin=1in]{geometry}", r"\usepackage{amsmath,amssymb}", r"\usepackage[T1]{fontenc}", r"\begin{document}", rf"\section*{{Original problem: {latex_escape(problem['name'])}}}", "This document records the exact original binary packing problem used for the matching run result.", r"\[", r"\max_{x\in\{0,1\}^n}\ \sum_{i=1}^n w_i x_i", r"\qquad\text{s.t.}\qquad", r"\sum_{i\in S_k} x_i \le B_k,\quad k=1,\dots,m.", r"\]", rf"Number of variables: {problem['n']}.\\", rf"Number of constraints: {len(problem['constraints'])}.\\", rf"Matching run-result file: \texttt{{{latex_escape(result_rel_path)}}}."]
    md = problem.get("metadata", {})
    if md:
        lines += [r"\subsection*{Metadata}", r"\begin{itemize}"]
        for k, v in md.items():
            if k == "candidate_sets":
                continue
            lines.append(rf"\item \texttt{{{latex_escape(str(k))}}}: \texttt{{{latex_escape(str(v))}}}")
        lines.append(r"\end{itemize}")
    lines += [r"\subsection*{Weights}", r"\begin{itemize}"]
    for i, w in enumerate(problem["weights"], start=1):
        lines.append(rf"\item $w_{{{i}}} = {float(w):.8g}$")
    lines.append(r"\end{itemize}")
    if "candidate_sets" in md:
        lines += [r"\subsection*{Candidate sets (variables)}", r"\begin{itemize}"]
        for j, subset in enumerate(md["candidate_sets"], start=1):
            elems = ", ".join(str(u + 1) for u in subset)
            lines.append(rf"\item $x_{{{j}}}$ corresponds to $A_{{{j}}}=\{{{elems}\}}$.")
        lines.append(r"\end{itemize}")
    lines += [r"\subsection*{Exact constraints}", r"\begin{itemize}"]
    for k, c in enumerate(problem["constraints"], start=1):
        lhs = " + ".join(f"x_{{{i+1}}}" for i in c["indices"])
        lines.append(rf"\item Constraint {k}: ${lhs} \le {c['capacity']}$")
    lines += [r"\end{itemize}", r"\end{document}"]
    return "\n".join(lines) + "\n"


def summarize_result(result_path: Path, spec: ProblemSpec, replicate: int, seed: int, instance_json: Path, problem_md: Path, problem_tex: Path) -> dict[str, Any]:
    data = load_json(result_path)
    records = data["records"]
    return {
        "problem_id": spec.problem_id,
        "family": spec.family,
        "replicate": replicate,
        "seed": seed,
        "note": spec.note,
        "instance_name": data["instance_name"],
        "n": data["n"],
        "num_constraints": data["num_constraints"],
        "gamma": data["gamma"],
        "eta0_tuned": data["eta0_tuned"],
        "num_runs": data["num_runs"],
        "all_converged_to_stationary": data["all_converged_to_stationary"],
        "all_binary": data["all_binary"],
        "all_feasible": data["all_feasible"],
        "all_strict_local_min_certified": data["all_strict_local_min_certified"],
        "any_saddle_evidence": data["any_saddle_evidence"],
        "avg_iterations": sum(r["iterations"] for r in records) / len(records),
        "avg_runtime_sec": sum(r["runtime_sec"] for r in records) / len(records),
        "max_binarity_error": max(r["binarity_error"] for r in records),
        "result_json": str(result_path),
        "instance_json": str(instance_json),
        "problem_md": str(problem_md),
        "problem_tex": str(problem_tex),
        **spec.params,
    }


def write_csv(rows: list[dict[str, Any]], path: Path) -> None:
    fields = []
    for row in rows:
        for k in row:
            if k not in fields:
                fields.append(k)
    with path.open("w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=fields)
        writer.writeheader()
        writer.writerows(rows)


def write_index_md(rows: list[dict[str, Any]], path: Path) -> None:
    lines = ["# Exact-problem index for recorded stress-suite runs\n", "| problem_id | family | rep | seed | result_json | instance_json | problem_md | problem_tex |", "|---|---|---:|---:|---|---|---|---|"]
    for r in rows:
        lines.append(f"| {r['problem_id']} | {r['family']} | {r['replicate']} | {r['seed']} | {r['result_json']} | {r['instance_json']} | {r['problem_md']} | {r['problem_tex']} |")
    path.write_text("\n".join(lines) + "\n", encoding="utf-8")


def main() -> None:
    parser = argparse.ArgumentParser(description="Run the stress suite and record exact instances beside the results.")
    parser.add_argument("--wrapper", type=str, default="/mnt/data/higher_order_pgd_record_instances_wrapper.py")
    parser.add_argument("--base-script", type=str, default="/mnt/data/higher_order_pgd_packing(1).py")
    parser.add_argument("--outdir", type=str, default="/mnt/data/higher_order_pgd_recorded_stress_results")
    parser.add_argument("--runs", type=int, default=12)
    parser.add_argument("--tune-runs", type=int, default=4)
    parser.add_argument("--tol-pg", type=float, default=1e-7)
    parser.add_argument("--max-iter", type=int, default=50000)
    parser.add_argument("--replicates", type=int, default=2)
    parser.add_argument("--seed-base", type=int, default=2000)
    parser.add_argument("--skip-existing", action="store_true")
    args = parser.parse_args()

    wrapper = Path(args.wrapper)
    base_script = Path(args.base_script)
    outdir = Path(args.outdir)
    outdir.mkdir(parents=True, exist_ok=True)

    rows = []
    counter = 0
    for spec in build_specs():
        for rep in range(1, args.replicates + 1):
            seed = args.seed_base + counter
            counter += 1
            run_dir = outdir / f"{spec.problem_id}_rep{rep}"
            result_json = run_dir / "result.json"
            instance_json = run_dir / "instance.json"
            problem_md = run_dir / "problem.md"
            problem_tex = run_dir / "problem.tex"
            if not (args.skip_existing and result_json.exists() and instance_json.exists() and problem_md.exists() and problem_tex.exists()):
                run_dir.mkdir(parents=True, exist_ok=True)
                call_wrapper(wrapper, base_script, result_json, spec, seed, args.runs, args.tune_runs, args.tol_pg, args.max_iter)
                result = load_json(result_json)
                problem = result["problem_instance"]
                save_json(problem, instance_json)
                problem_md.write_text(problem_statement_md(problem, "result.json"), encoding="utf-8")
                problem_tex.write_text(problem_statement_tex(problem, "result.json"), encoding="utf-8")
            rows.append(summarize_result(result_json, spec, rep, seed, instance_json, problem_md, problem_tex))

    write_csv(rows, outdir / "recorded_stress_summary.csv")
    write_index_md(rows, outdir / "recorded_problem_index.md")
    print(json.dumps({"recorded_problem_runs": len(rows), "outdir": str(outdir)}, indent=2))


if __name__ == "__main__":
    main()
