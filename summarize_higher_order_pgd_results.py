#!/usr/bin/env python3
from __future__ import annotations

import argparse
import csv
import json
from pathlib import Path
from typing import Any


def load_json(path: Path) -> dict[str, Any]:
    with path.open("r", encoding="utf-8") as f:
        return json.load(f)


def discover_result_files(root: Path) -> list[Path]:
    files = []
    for p in root.rglob("*.json"):
        if p.name == "summary.json":
            continue
        try:
            data = load_json(p)
        except Exception:
            continue
        if isinstance(data, dict) and "instance_name" in data and "records" in data:
            files.append(p)
    return sorted(files)


def summarize_one(path: Path) -> dict[str, Any]:
    data = load_json(path)
    records = data.get("records", [])
    avg_iterations = sum(r["iterations"] for r in records) / max(1, len(records))
    avg_runtime_sec = sum(r["runtime_sec"] for r in records) / max(1, len(records))
    max_binarity_error = max((r["binarity_error"] for r in records), default=0.0)
    return {
        "file": str(path),
        "instance_name": data.get("instance_name"),
        "n": data.get("n"),
        "num_constraints": data.get("num_constraints"),
        "gamma": data.get("gamma"),
        "eta0_tuned": data.get("eta0_tuned"),
        "num_runs": data.get("num_runs"),
        "all_converged_to_stationary": data.get("all_converged_to_stationary"),
        "all_binary": data.get("all_binary"),
        "all_feasible": data.get("all_feasible"),
        "all_strict_local_min_certified": data.get("all_strict_local_min_certified"),
        "any_saddle_evidence": data.get("any_saddle_evidence"),
        "avg_iterations": avg_iterations,
        "avg_runtime_sec": avg_runtime_sec,
        "max_binarity_error": max_binarity_error,
        "metadata": json.dumps(data.get("metadata", {}), sort_keys=True),
    }


def write_csv(rows: list[dict[str, Any]], path: Path) -> None:
    if not rows:
        return
    fieldnames = list(rows[0].keys())
    with path.open("w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(rows)


def write_md(rows: list[dict[str, Any]], path: Path) -> None:
    if not rows:
        path.write_text("No result files found.\n", encoding="utf-8")
        return

    headers = [
        "instance_name", "n", "num_constraints", "num_runs",
        "all_converged_to_stationary", "all_binary", "all_feasible",
        "all_strict_local_min_certified", "any_saddle_evidence",
        "avg_iterations", "avg_runtime_sec", "max_binarity_error",
    ]
    lines = []
    lines.append("| " + " | ".join(headers) + " |")
    lines.append("|" + "|".join(["---"] * len(headers)) + "|")
    for row in rows:
        vals = []
        for h in headers:
            v = row[h]
            if isinstance(v, float):
                vals.append(f"{v:.6g}")
            else:
                vals.append(str(v))
        lines.append("| " + " | ".join(vals) + " |")
    path.write_text("\n".join(lines) + "\n", encoding="utf-8")


def main() -> None:
    parser = argparse.ArgumentParser(description="Aggregate higher-order PGD sweep results.")
    parser.add_argument("root", type=str)
    parser.add_argument("--csv", type=str, default="")
    parser.add_argument("--md", type=str, default="")
    args = parser.parse_args()

    root = Path(args.root)
    files = discover_result_files(root)
    rows = [summarize_one(p) for p in files]

    if args.csv:
        write_csv(rows, Path(args.csv))
    if args.md:
        write_md(rows, Path(args.md))

    print(json.dumps({"num_result_files": len(rows)}, indent=2))


if __name__ == "__main__":
    main()
