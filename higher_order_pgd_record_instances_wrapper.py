#!/usr/bin/env python3
from __future__ import annotations

import argparse
import importlib.util
import json
import sys
from pathlib import Path
from typing import Any, Dict

import numpy as np


def load_base_module(path: str | Path):
    path = Path(path)
    spec = importlib.util.spec_from_file_location("higher_order_pgd_base", str(path))
    if spec is None or spec.loader is None:
        raise ImportError(f"Could not load base solver from {path}")
    mod = importlib.util.module_from_spec(spec)
    sys.modules[spec.name] = mod
    spec.loader.exec_module(mod)
    return mod


def instance_to_dict(instance: Any) -> Dict[str, Any]:
    metadata = dict(instance.metadata)
    return {
        "name": instance.name,
        "n": int(instance.n),
        "weights": [float(v) for v in np.asarray(instance.weights).tolist()],
        "constraints": [
            {
                "indices": [int(i) for i in np.asarray(row).tolist()],
                "capacity": int(b),
            }
            for row, b in zip(instance.rows, instance.capacities)
        ],
        "metadata": metadata,
    }


def maybe_add_candidate_sets(problem: Dict[str, Any], family: str, args: argparse.Namespace, rng: np.random.Generator) -> None:
    if family != "kset":
        return
    n_sets = int(args.n_sets)
    universe_size = int(args.universe_size)
    k = int(args.k)
    density = float(args.density)

    sets = []
    used = set()
    target = max(1, n_sets)
    attempts = 0
    while len(sets) < target and attempts < 100 * target:
        attempts += 1
        subset = tuple(sorted(int(v) for v in rng.choice(universe_size, size=k, replace=False)))
        if subset in used:
            continue
        used.add(subset)
        if rng.random() <= density:
            sets.append(subset)
    if len(sets) != target:
        raise RuntimeError("Failed to reconstruct exact candidate sets for k-set instance.")
    problem.setdefault("metadata", {})["candidate_sets"] = [list(s) for s in sets]


def save_json(obj: Dict[str, Any], path: str | Path) -> None:
    path = Path(path)
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(obj, indent=2), encoding="utf-8")


def run_one(base, family: str, args: argparse.Namespace) -> Dict[str, Any]:
    rng = np.random.default_rng(args.seed)
    if family == "random_unit":
        inst = base.generate_random_unit_packing(
            n=args.n,
            m=args.m,
            row_size_range=(args.row_min, args.row_max),
            capacity_mode=args.capacity_mode,
            rng=rng,
            name=f"random_unit_n{args.n}_m{args.m}_{args.capacity_mode}",
        )
    elif family == "kset":
        inst = base.generate_random_k_set_packing(
            n_sets=args.n_sets,
            universe_size=args.universe_size,
            k=args.k,
            density=args.density,
            rng=rng,
            name=f"kset_u{args.universe_size}_n{args.n_sets}_k{args.k}",
        )
    elif family == "json":
        inst = base.load_instance_from_json(args.path)
    else:
        raise ValueError(f"Unknown family: {family}")

    result = base.run_experiment(
        inst,
        num_runs=args.runs,
        tune_runs=args.tune_runs,
        tol_pg=args.tol_pg,
        max_iter=args.max_iter,
        seed=args.seed,
    )
    problem = instance_to_dict(inst)
    if family == "kset":
        # base generator does not persist candidate sets, so reconstruct them using the same RNG path
        maybe_add_candidate_sets(problem, family, args, np.random.default_rng(args.seed))
    result["problem_instance"] = problem
    return result


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description="Wrapper that records exact generated instances along with run results.")
    parser.add_argument("--base-script", type=str, default="/mnt/data/higher_order_pgd_packing(1).py")
    sub = parser.add_subparsers(dest="cmd", required=True)

    rand = sub.add_parser("random_unit")
    rand.add_argument("--n", type=int, default=25)
    rand.add_argument("--m", type=int, default=40)
    rand.add_argument("--row-min", type=int, default=3)
    rand.add_argument("--row-max", type=int, default=6)
    rand.add_argument("--capacity-mode", type=str, default="mixed", choices=["mixed", "tight", "set_packing", "half"])
    rand.add_argument("--runs", type=int, default=20)
    rand.add_argument("--tune-runs", type=int, default=6)
    rand.add_argument("--seed", type=int, default=0)
    rand.add_argument("--tol-pg", type=float, default=1e-7)
    rand.add_argument("--max-iter", type=int, default=50000)
    rand.add_argument("--out", type=str, required=True)

    ksp = sub.add_parser("kset")
    ksp.add_argument("--n-sets", type=int, default=30)
    ksp.add_argument("--universe-size", type=int, default=20)
    ksp.add_argument("--k", type=int, default=3)
    ksp.add_argument("--density", type=float, default=1.0)
    ksp.add_argument("--runs", type=int, default=20)
    ksp.add_argument("--tune-runs", type=int, default=6)
    ksp.add_argument("--seed", type=int, default=0)
    ksp.add_argument("--tol-pg", type=float, default=1e-7)
    ksp.add_argument("--max-iter", type=int, default=50000)
    ksp.add_argument("--out", type=str, required=True)

    load = sub.add_parser("json")
    load.add_argument("path", type=str)
    load.add_argument("--runs", type=int, default=20)
    load.add_argument("--tune-runs", type=int, default=6)
    load.add_argument("--seed", type=int, default=0)
    load.add_argument("--tol-pg", type=float, default=1e-7)
    load.add_argument("--max-iter", type=int, default=50000)
    load.add_argument("--out", type=str, required=True)
    return parser


def main() -> None:
    parser = build_parser()
    args = parser.parse_args()
    base = load_base_module(args.base_script)
    result = run_one(base, args.cmd, args)
    save_json(result, args.out)
    print(json.dumps({k: v for k, v in result.items() if k not in {"records", "problem_instance"}}, indent=2))


if __name__ == "__main__":
    main()
