#!/usr/bin/env python3
from __future__ import annotations

import argparse
import csv
import json
import statistics
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


def build_specs(profile: str) -> list[ProblemSpec]:
    specs: list[ProblemSpec] = []
    if profile == "standard":
        specs.extend([
            ProblemSpec("RU1", "random_unit", {"n": 40, "m": 80, "row_min": 4, "row_max": 8, "capacity_mode": "mixed"}, "Medium-large mixed-capacity random unit packing."),
            ProblemSpec("RU2", "random_unit", {"n": 60, "m": 120, "row_min": 5, "row_max": 10, "capacity_mode": "mixed"}, "Larger mixed-capacity random unit packing."),
            ProblemSpec("RU3", "random_unit", {"n": 60, "m": 120, "row_min": 5, "row_max": 10, "capacity_mode": "set_packing"}, "Capacity-1 variant with larger rows."),
            ProblemSpec("RU4", "random_unit", {"n": 80, "m": 160, "row_min": 5, "row_max": 10, "capacity_mode": "tight"}, "Tight-capacity regime at larger scale."),
            ProblemSpec("RU5", "random_unit", {"n": 80, "m": 160, "row_min": 6, "row_max": 12, "capacity_mode": "half"}, "Half-capacity larger-row regime."),
            ProblemSpec("RU6", "random_unit", {"n": 100, "m": 200, "row_min": 6, "row_max": 12, "capacity_mode": "mixed"}, "Largest random-unit stress setting in the standard suite."),
        ])
        specs.extend([
            ProblemSpec("KS1", "kset", {"n_sets": 60, "universe_size": 30, "k": 4, "density": 1.0}, "Denser 4-set packing baseline."),
            ProblemSpec("KS2", "kset", {"n_sets": 100, "universe_size": 40, "k": 5, "density": 1.0}, "Dense 5-set packing at larger size."),
            ProblemSpec("KS3", "kset", {"n_sets": 100, "universe_size": 40, "k": 5, "density": 0.7}, "Sparser 5-set packing at same size."),
            ProblemSpec("KS4", "kset", {"n_sets": 120, "universe_size": 50, "k": 5, "density": 1.0}, "Larger dense 5-set packing."),
            ProblemSpec("KS5", "kset", {"n_sets": 150, "universe_size": 60, "k": 6, "density": 0.7}, "Large sparse 6-set packing."),
            ProblemSpec("KS6", "kset", {"n_sets": 180, "universe_size": 70, "k": 6, "density": 0.7}, "Largest k-set stress setting in the standard suite."),
        ])
    elif profile == "extreme":
        specs.extend([
            ProblemSpec("RU7", "random_unit", {"n": 120, "m": 260, "row_min": 7, "row_max": 14, "capacity_mode": "mixed"}, "Extreme mixed-capacity random unit packing."),
            ProblemSpec("RU8", "random_unit", {"n": 140, "m": 300, "row_min": 8, "row_max": 16, "capacity_mode": "tight"}, "Extreme tight-capacity random unit packing."),
            ProblemSpec("RU9", "random_unit", {"n": 140, "m": 300, "row_min": 8, "row_max": 16, "capacity_mode": "half"}, "Extreme half-capacity random unit packing."),
            ProblemSpec("RU10", "random_unit", {"n": 160, "m": 360, "row_min": 8, "row_max": 18, "capacity_mode": "set_packing"}, "Extreme capacity-1 random unit packing."),
        ])
        specs.extend([
            ProblemSpec("KS7", "kset", {"n_sets": 220, "universe_size": 80, "k": 6, "density": 0.7}, "Extreme sparse 6-set packing."),
            ProblemSpec("KS8", "kset", {"n_sets": 260, "universe_size": 90, "k": 7, "density": 0.8}, "Extreme mixed-density 7-set packing."),
            ProblemSpec("KS9", "kset", {"n_sets": 300, "universe_size": 100, "k": 7, "density": 1.0}, "Extreme dense 7-set packing."),
            ProblemSpec("KS10", "kset", {"n_sets": 340, "universe_size": 120, "k": 8, "density": 0.8}, "Largest k-set stress setting in the extreme suite."),
        ])
    else:
        raise ValueError(f"Unknown profile: {profile}")
    return specs


def load_json(path: Path) -> dict[str, Any]:
    with path.open("r", encoding="utf-8") as f:
        return json.load(f)


def latex_escape(s: str) -> str:
    repl = {
        "\\": r"\textbackslash{}",
        "&": r"\&",
        "%": r"\%",
        "$": r"\$",
        "#": r"\#",
        "_": r"\_",
        "{": r"\{",
        "}": r"\}",
        "~": r"\textasciitilde{}",
        "^": r"\textasciicircum{}",
    }
    return "".join(repl.get(ch, ch) for ch in s)


def call_solver(solver_path: Path, out_json: Path, spec: ProblemSpec, seed: int, runs: int, tune_runs: int, tol_pg: float, max_iter: int) -> None:
    cmd = [sys.executable, str(solver_path), spec.family]
    if spec.family == "random_unit":
        cmd += [
            "--n", str(spec.params["n"]),
            "--m", str(spec.params["m"]),
            "--row-min", str(spec.params["row_min"]),
            "--row-max", str(spec.params["row_max"]),
            "--capacity-mode", str(spec.params["capacity_mode"]),
        ]
    elif spec.family == "kset":
        cmd += [
            "--n-sets", str(spec.params["n_sets"]),
            "--universe-size", str(spec.params["universe_size"]),
            "--k", str(spec.params["k"]),
            "--density", str(spec.params["density"]),
        ]
    else:
        raise ValueError(f"Unknown family: {spec.family}")

    cmd += [
        "--runs", str(runs),
        "--tune-runs", str(tune_runs),
        "--seed", str(seed),
        "--tol-pg", str(tol_pg),
        "--max-iter", str(max_iter),
        "--out", str(out_json),
    ]
    subprocess.run(cmd, check=True, stdout=subprocess.DEVNULL, stderr=subprocess.STDOUT)


def summarize_result(path: Path, spec: ProblemSpec, replicate: int, seed: int) -> dict[str, Any]:
    data = load_json(path)
    records = data["records"]
    avg_iterations = sum(r["iterations"] for r in records) / len(records)
    avg_runtime_sec = sum(r["runtime_sec"] for r in records) / len(records)
    max_binarity_error = max(r["binarity_error"] for r in records)
    strict_local_rate = sum(bool(r["strict_local_min_certified"]) for r in records) / len(records)
    feasible_rate = sum(bool(r["feasible"]) for r in records) / len(records)
    stationary_rate = sum(bool(r["converged"]) for r in records) / len(records)
    saddle_rate = sum(bool(r["saddle_evidence"]) for r in records) / len(records)
    row: dict[str, Any] = {
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
        "stationary_rate": stationary_rate,
        "feasible_rate": feasible_rate,
        "strict_local_rate": strict_local_rate,
        "saddle_rate": saddle_rate,
        "avg_iterations": avg_iterations,
        "avg_runtime_sec": avg_runtime_sec,
        "max_binarity_error": max_binarity_error,
        "metadata": json.dumps(data.get("metadata", {}), sort_keys=True),
        "output_json": str(path),
    }
    for k, v in spec.params.items():
        row[k] = v
    return row


def write_csv(rows: list[dict[str, Any]], path: Path) -> None:
    if not rows:
        return
    fieldnames: list[str] = []
    for row in rows:
        for k in row.keys():
            if k not in fieldnames:
                fieldnames.append(k)
    with path.open("w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(rows)


def bool_to_mark(v: Any) -> str:
    return "yes" if bool(v) else "no"


def aggregate_rows(rows: list[dict[str, Any]]) -> dict[str, Any]:
    total = len(rows)
    passed = [r for r in rows if r["all_converged_to_stationary"] and r["all_binary"] and r["all_feasible"] and r["all_strict_local_min_certified"] and (not r["any_saddle_evidence"])]
    hardest_iter = max(rows, key=lambda r: r["avg_iterations"])
    slowest = max(rows, key=lambda r: r["avg_runtime_sec"])
    family_stats = {}
    for fam in sorted({r["family"] for r in rows}):
        sub = [r for r in rows if r["family"] == fam]
        family_stats[fam] = {
            "count": len(sub),
            "mean_iterations": statistics.mean(r["avg_iterations"] for r in sub),
            "mean_runtime_sec": statistics.mean(r["avg_runtime_sec"] for r in sub),
            "all_pass": all(r in passed for r in sub),
        }
    return {
        "total_problems": total,
        "fully_successful_problems": len(passed),
        "hardest_by_iterations": hardest_iter,
        "slowest_by_runtime": slowest,
        "family_stats": family_stats,
    }


def write_md(rows: list[dict[str, Any]], path: Path, args: argparse.Namespace) -> None:
    agg = aggregate_rows(rows)
    lines: list[str] = []
    lines.append("# Higher-order PGD stress-suite report\n")
    lines.append("## Run configuration\n")
    lines.append(f"- Solver script: `{args.solver}`")
    lines.append(f"- Stress profile: `{args.profile}`")
    lines.append(f"- Runs per problem: `{args.runs}`")
    lines.append(f"- Tuning runs per problem: `{args.tune_runs}`")
    lines.append(f"- PG tolerance: `{args.tol_pg}`")
    lines.append(f"- Max iterations: `{args.max_iter}`")
    lines.append(f"- Replicates per structural setting: `{args.replicates}`")
    lines.append(f"- Total problems executed: `{agg['total_problems']}`")
    lines.append(f"- Fully successful problems: `{agg['fully_successful_problems']}`")
    lines.append("")
    hard = agg["hardest_by_iterations"]
    slow = agg["slowest_by_runtime"]
    lines.append("## Headline findings\n")
    lines.append(f"- Hardest problem by average iterations: `{hard['problem_id']}` replicate {hard['replicate']} (`{hard['instance_name']}`), avg iterations = `{hard['avg_iterations']:.2f}`.")
    lines.append(f"- Slowest problem by average runtime: `{slow['problem_id']}` replicate {slow['replicate']} (`{slow['instance_name']}`), avg runtime = `{slow['avg_runtime_sec']:.4f}` sec.")
    for fam, stat in agg["family_stats"].items():
        lines.append(f"- Family `{fam}`: {stat['count']} problems, mean avg-iterations = `{stat['mean_iterations']:.2f}`, mean avg-runtime = `{stat['mean_runtime_sec']:.4f}` sec, all-pass = `{stat['all_pass']}`.")
    lines.append("")
    lines.append("## Problem-by-problem table\n")
    headers = [
        "problem_id", "family", "replicate", "seed", "n", "num_constraints", "num_runs",
        "avg_iterations", "avg_runtime_sec", "eta0_tuned",
        "all_converged_to_stationary", "all_binary", "all_feasible",
        "all_strict_local_min_certified", "any_saddle_evidence", "max_binarity_error",
        "output_json",
    ]
    lines.append("| " + " | ".join(headers) + " |")
    lines.append("|" + "|".join(["---"] * len(headers)) + "|")
    for r in rows:
        vals = []
        for h in headers:
            v = r.get(h, "")
            if isinstance(v, float):
                vals.append(f"{v:.6g}")
            else:
                vals.append(str(v))
        lines.append("| " + " | ".join(vals) + " |")
    lines.append("")
    lines.append("## Structural settings\n")
    for pid in sorted({r["problem_id"] for r in rows}):
        sub = [r for r in rows if r["problem_id"] == pid]
        first = sub[0]
        lines.append(f"### {pid}")
        lines.append(f"- Family: `{first['family']}`")
        lines.append(f"- Note: {first['note']}")
        if first["family"] == "random_unit":
            lines.append(f"- Parameters: `n={first['n']}`, `m={first['m']}`, `row_min={first['row_min']}`, `row_max={first['row_max']}`, `capacity_mode={first['capacity_mode']}`")
        else:
            lines.append(f"- Parameters: `n_sets={first['n_sets']}`, `universe_size={first['universe_size']}`, `k={first['k']}`, `density={first['density']}`")
        lines.append(f"- Replicates executed: {', '.join(str(x['replicate']) for x in sub)}")
        lines.append("")
    path.write_text("\n".join(lines) + "\n", encoding="utf-8")


def write_tex(rows: list[dict[str, Any]], path: Path, args: argparse.Namespace) -> None:
    agg = aggregate_rows(rows)
    hard = agg["hardest_by_iterations"]
    slow = agg["slowest_by_runtime"]
    lines: list[str] = []
    lines.append(r"\documentclass[11pt]{article}")
    lines.append(r"\usepackage[margin=1in]{geometry}")
    lines.append(r"\usepackage{booktabs}")
    lines.append(r"\usepackage{longtable}")
    lines.append(r"\usepackage{array}")
    lines.append(r"\begin{document}")
    lines.append(r"\section*{Higher-order PGD stress-suite report}")
    lines.append(r"\subsection*{Run configuration}")
    lines.append(r"\begin{itemize}")
    lines.append(rf"\item Solver script: \texttt{{{latex_escape(str(args.solver))}}}")
    lines.append(rf"\item Stress profile: \texttt{{{latex_escape(args.profile)}}}")
    lines.append(rf"\item Runs per problem: {args.runs}")
    lines.append(rf"\item Tuning runs per problem: {args.tune_runs}")
    lines.append(rf"\item PG tolerance: {args.tol_pg}")
    lines.append(rf"\item Max iterations: {args.max_iter}")
    lines.append(rf"\item Replicates per structural setting: {args.replicates}")
    lines.append(rf"\item Total problems executed: {agg['total_problems']}")
    lines.append(rf"\item Fully successful problems: {agg['fully_successful_problems']}")
    lines.append(r"\end{itemize}")
    lines.append(r"\subsection*{Headline findings}")
    lines.append(r"\begin{itemize}")
    lines.append(rf"\item Hardest problem by average iterations: \texttt{{{latex_escape(hard['problem_id'])}}} replicate {hard['replicate']} (\texttt{{{latex_escape(hard['instance_name'])}}}), average iterations = {hard['avg_iterations']:.2f}.")
    lines.append(rf"\item Slowest problem by average runtime: \texttt{{{latex_escape(slow['problem_id'])}}} replicate {slow['replicate']} (\texttt{{{latex_escape(slow['instance_name'])}}}), average runtime = {slow['avg_runtime_sec']:.4f} sec.")
    for fam, stat in agg["family_stats"].items():
        lines.append(rf"\item Family \texttt{{{latex_escape(fam)}}}: {stat['count']} problems, mean average iterations = {stat['mean_iterations']:.2f}, mean average runtime = {stat['mean_runtime_sec']:.4f} sec, all-pass = {stat['all_pass']}. ")
    lines.append(r"\end{itemize}")
    lines.append(r"\subsection*{Problem-by-problem table}")
    lines.append(r"\small")
    lines.append(r"\begin{longtable}{llrrrrrrrrrrrrr}")
    lines.append(r"\toprule")
    lines.append(r"ID & Family & Rep & Seed & $n$ & $m$ & Runs & AvgIter & AvgTime & $\eta_0$ & Stat & Bin & Feas & StrictLM & Saddle \\")
    lines.append(r"\midrule")
    lines.append(r"\endhead")
    for r in rows:
        m_val = r.get("num_constraints", "")
        line = (
            f"{latex_escape(str(r['problem_id']))} & {latex_escape(str(r['family']))} & {r['replicate']} & {r['seed']} & {r['n']} & {m_val} & {r['num_runs']} & "
            f"{r['avg_iterations']:.2f} & {r['avg_runtime_sec']:.4f} & {r['eta0_tuned']:.3g} & "
            f"{bool_to_mark(r['all_converged_to_stationary'])} & {bool_to_mark(r['all_binary'])} & {bool_to_mark(r['all_feasible'])} & "
            f"{bool_to_mark(r['all_strict_local_min_certified'])} & {bool_to_mark(r['any_saddle_evidence'])} \\")
        lines.append(line)
    lines.append(r"\bottomrule")
    lines.append(r"\end{longtable}")
    lines.append(r"\subsection*{Structural settings}")
    for pid in sorted({r["problem_id"] for r in rows}):
        sub = [r for r in rows if r["problem_id"] == pid]
        first = sub[0]
        lines.append(rf"\paragraph{{{latex_escape(pid)}}} Family: \texttt{{{latex_escape(first['family'])}}}. {latex_escape(first['note'])}")
        if first["family"] == "random_unit":
            lines.append(rf"Parameters: \texttt{{n={first['n']}, m={first['m']}, row\_min={first['row_min']}, row\_max={first['row_max']}, capacity\_mode={first['capacity_mode']}}}.\\")
        else:
            lines.append(rf"Parameters: \texttt{{n\_sets={first['n_sets']}, universe\_size={first['universe_size']}, k={first['k']}, density={first['density']}}}.\\")
        reps = ", ".join(str(x["replicate"]) for x in sub)
        lines.append(rf"Replicates executed: {latex_escape(reps)}.\\")
    lines.append(r"\end{document}")
    path.write_text("\n".join(lines) + "\n", encoding="utf-8")


def main() -> None:
    parser = argparse.ArgumentParser(description="Run a harder higher-order PGD stress suite and write report files.")
    parser.add_argument("--solver", type=str, default="higher_order_pgd_packing.py")
    parser.add_argument("--outdir", type=str, default="higher_order_pgd_stress_results")
    parser.add_argument("--profile", type=str, default="standard", choices=["standard", "extreme"])
    parser.add_argument("--runs", type=int, default=12)
    parser.add_argument("--tune-runs", type=int, default=4)
    parser.add_argument("--tol-pg", type=float, default=1e-7)
    parser.add_argument("--max-iter", type=int, default=50000)
    parser.add_argument("--replicates", type=int, default=2)
    parser.add_argument("--seed-base", type=int, default=700)
    args = parser.parse_args()

    solver_path = Path(args.solver)
    outdir = Path(args.outdir)
    outdir.mkdir(parents=True, exist_ok=True)
    result_dir = outdir / "json_results"
    result_dir.mkdir(parents=True, exist_ok=True)

    specs = build_specs(args.profile)
    rows: list[dict[str, Any]] = []
    seed = args.seed_base
    manifest = []
    for spec in specs:
        for replicate in range(1, args.replicates + 1):
            out_json = result_dir / f"{spec.problem_id}_rep{replicate}.json"
            print(f"Running {spec.problem_id} replicate {replicate} -> {out_json.name}")
            if not out_json.exists():
                call_solver(solver_path, out_json, spec, seed, args.runs, args.tune_runs, args.tol_pg, args.max_iter)
            row = summarize_result(out_json, spec, replicate, seed)
            rows.append(row)
            manifest.append({"problem_id": spec.problem_id, "replicate": replicate, "seed": seed, "output_json": str(out_json)})
            seed += 1

    rows.sort(key=lambda r: (r["family"], r["problem_id"], r["replicate"]))
    write_csv(rows, outdir / "stress_summary.csv")
    write_md(rows, outdir / "stress_report.md", args)
    write_tex(rows, outdir / "stress_report.tex", args)
    (outdir / "manifest.json").write_text(json.dumps(manifest, indent=2), encoding="utf-8")

    print(json.dumps({
        "num_problems": len(rows),
        "outdir": str(outdir),
        "csv": str(outdir / 'stress_summary.csv'),
        "md": str(outdir / 'stress_report.md'),
        "tex": str(outdir / 'stress_report.tex'),
    }, indent=2))


if __name__ == "__main__":
    main()
