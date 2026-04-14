#!/usr/bin/env python3
"""
Experiments for higher-order theorem-guided penalties on unit multi-constraint packing.

The code supports:
- Random unit multi-constraint packing instances with varying row capacities.
- Random k-set packing instances (B_k = 1 after hypergraph-to-incidence conversion).
- PGD with monotone Armijo backtracking and automatic eta0 tuning.
- Checks for binarity, feasibility, first-order stationarity, and a practical
  certificate for strict local minimality.

The penalty for a row S_k with capacity B_k is e_{B_k+1}(x_{S_k}), i.e. the
sum of all squarefree monomials of degree B_k+1 supported on S_k.
"""

from __future__ import annotations

import argparse
import itertools
import json
import math
import time
from dataclasses import dataclass, asdict
from pathlib import Path
from typing import Dict, Iterable, List, Optional, Sequence, Tuple

import numpy as np


Array = np.ndarray


# -----------------------------------------------------------------------------
# Elementary symmetric polynomial helpers
# -----------------------------------------------------------------------------

def elementary_symmetric_all(z: Array, r_max: int) -> Array:
    """Return values [e_0(z), ..., e_{r_max}(z)] via DP.

    Complexity: O(len(z) * r_max).
    """
    r_max = max(0, min(r_max, z.size))
    e = np.zeros(r_max + 1, dtype=float)
    e[0] = 1.0
    for val in z:
        upper = min(r_max, z.size)
        for r in range(r_max, 0, -1):
            e[r] += val * e[r - 1]
    return e


def elementary_symmetric_value(z: Array, r: int) -> float:
    if r < 0:
        return 0.0
    if r == 0:
        return 1.0
    if r > z.size:
        return 0.0
    return float(elementary_symmetric_all(z, r)[r])


@dataclass
class RowCache:
    indices: Array           # variable indices for this row
    capacity: int            # B_k
    degree: int              # B_k + 1
    value: float             # e_degree(z)
    grad_local: Array        # d/d z_i e_degree(z) = e_{degree-1}(z without i)



def row_value_and_grad(x_sub: Array, capacity: int) -> Tuple[float, Array]:
    """Compute e_{capacity+1}(x_sub) and its gradient wrt x_sub.

    Uses prefix/suffix DP so the gradient is exact and efficient.
    """
    m = x_sub.size
    degree = capacity + 1
    if degree > m:
        return 0.0, np.zeros(m, dtype=float)

    # Prefix and suffix elementary symmetric polynomials.
    pref = np.zeros((m + 1, degree + 1), dtype=float)
    suff = np.zeros((m + 1, degree + 1), dtype=float)
    pref[0, 0] = 1.0
    suff[m, 0] = 1.0

    for a in range(1, m + 1):
        pref[a] = pref[a - 1]
        val = x_sub[a - 1]
        upper = min(a, degree)
        for r in range(upper, 0, -1):
            pref[a, r] += val * pref[a - 1, r - 1]

    for a in range(m - 1, -1, -1):
        suff[a] = suff[a + 1]
        val = x_sub[a]
        upper = min(m - a, degree)
        for r in range(upper, 0, -1):
            suff[a, r] += val * suff[a + 1, r - 1]

    value = pref[m, degree]
    grad = np.zeros(m, dtype=float)
    # grad_i = e_degree-1(x without i)
    d = degree - 1
    if d >= 0:
        for i in range(m):
            total = 0.0
            for left_deg in range(d + 1):
                right_deg = d - left_deg
                total += pref[i, left_deg] * suff[i + 1, right_deg]
            grad[i] = total
    return float(value), grad


# -----------------------------------------------------------------------------
# Problem definition
# -----------------------------------------------------------------------------

@dataclass
class PackingInstance:
    name: str
    n: int
    weights: Array
    rows: List[Array]
    capacities: Array
    metadata: Dict[str, object]

    def validate(self) -> None:
        assert self.weights.shape == (self.n,)
        assert len(self.rows) == self.capacities.size
        for row, b in zip(self.rows, self.capacities):
            assert row.ndim == 1
            assert row.size >= 2
            assert 1 <= int(b) < row.size
            assert np.all((row >= 0) & (row < self.n))
            assert len(np.unique(row)) == row.size


class HigherOrderPackingObjective:
    def __init__(self, instance: PackingInstance, gamma: float):
        self.instance = instance
        self.gamma = float(gamma)
        instance.validate()

    def penalty_value(self, x: Array) -> float:
        total = 0.0
        for row, b in zip(self.instance.rows, self.instance.capacities):
            total += elementary_symmetric_value(x[row], int(b) + 1)
        return total

    def value_and_grad(self, x: Array) -> Tuple[float, Array, List[RowCache]]:
        grad = -self.instance.weights.copy()
        penalty = 0.0
        caches: List[RowCache] = []
        for row, b in zip(self.instance.rows, self.instance.capacities):
            x_sub = x[row]
            value, g_local = row_value_and_grad(x_sub, int(b))
            penalty += value
            grad[row] += self.gamma * g_local
            caches.append(RowCache(indices=row, capacity=int(b), degree=int(b) + 1,
                                   value=value, grad_local=g_local))
        value = -float(np.dot(self.instance.weights, x)) + self.gamma * penalty
        return value, grad, caches

    def value(self, x: Array) -> float:
        return self.value_and_grad(x)[0]

    def gradient(self, x: Array) -> Array:
        return self.value_and_grad(x)[1]

    def feasibility_violations(self, x: Array, tol: float = 1e-8) -> Array:
        vals = np.array([np.sum(x[row]) - b for row, b in zip(self.instance.rows, self.instance.capacities)], dtype=float)
        vals[np.abs(vals) < tol] = 0.0
        return vals

    def is_feasible(self, x: Array, tol: float = 1e-8) -> bool:
        return bool(np.all(self.feasibility_violations(x, tol=tol) <= tol))

    def binarity_error(self, x: Array) -> float:
        return float(np.max(np.minimum(np.abs(x), np.abs(1.0 - x))))


# -----------------------------------------------------------------------------
# Generators / loaders
# -----------------------------------------------------------------------------

def generate_random_unit_packing(
    n: int,
    m: int,
    row_size_range: Tuple[int, int] = (3, 6),
    capacity_mode: str = "mixed",
    rng: Optional[np.random.Generator] = None,
    name: str = "rand_unit_packing",
) -> PackingInstance:
    """Random theorem-matching unit multi-constraint packing instance.

    capacity_mode:
      - 'mixed': sample B_k uniformly from {1,...,|S_k|-1}
      - 'tight': B_k = |S_k|-1
      - 'set_packing': B_k = 1
      - 'half': B_k = floor(|S_k|/2)
    """
    rng = np.random.default_rng() if rng is None else rng
    min_r, max_r = row_size_range
    rows: List[Array] = []
    caps: List[int] = []
    used = set()
    attempts = 0
    while len(rows) < m and attempts < 50 * m:
        attempts += 1
        size = int(rng.integers(min_r, max_r + 1))
        size = max(2, min(size, n))
        row = np.sort(rng.choice(n, size=size, replace=False))
        key = tuple(int(v) for v in row)
        if key in used:
            continue
        used.add(key)
        rows.append(row.astype(int))
        if capacity_mode == "mixed":
            caps.append(int(rng.integers(1, size)))
        elif capacity_mode == "tight":
            caps.append(size - 1)
        elif capacity_mode == "set_packing":
            caps.append(1)
        elif capacity_mode == "half":
            caps.append(max(1, size // 2))
        else:
            raise ValueError(f"Unknown capacity_mode={capacity_mode}")
    if len(rows) < m:
        raise RuntimeError("Failed to generate enough distinct rows.")
    weights = rng.uniform(0.5, 2.0, size=n)
    return PackingInstance(
        name=name,
        n=n,
        weights=weights,
        rows=rows,
        capacities=np.array(caps, dtype=int),
        metadata={"generator": "random_unit_packing", "row_size_range": row_size_range, "capacity_mode": capacity_mode},
    )


def generate_random_k_set_packing(
    n_sets: int,
    universe_size: int,
    k: int,
    density: float = 1.0,
    rng: Optional[np.random.Generator] = None,
    name: str = "rand_k_set_packing",
) -> PackingInstance:
    """Generate a random weighted k-set packing instance.

    Variables correspond to candidate k-sets. For each universe element u we impose
    sum_{set i containing u} x_i <= 1. Rows with fewer than 2 incident variables are
    dropped because they are never binding.
    """
    rng = np.random.default_rng() if rng is None else rng
    n_sets = int(n_sets)
    universe_size = int(universe_size)
    k = int(k)
    if not (1 < k <= universe_size):
        raise ValueError("Require 1 < k <= universe_size")

    sets: List[Tuple[int, ...]] = []
    used = set()
    target = max(1, n_sets)
    attempts = 0
    while len(sets) < target and attempts < 100 * target:
        attempts += 1
        subset = tuple(sorted(int(v) for v in rng.choice(universe_size, size=k, replace=False)))
        if subset in used:
            continue
        used.add(subset)
        # density<1 can sparsify by rejecting some candidate sets
        if rng.random() <= density:
            sets.append(subset)
    if len(sets) < target:
        raise RuntimeError("Failed to generate enough distinct k-sets.")

    incidence: List[List[int]] = [[] for _ in range(universe_size)]
    for idx, subset in enumerate(sets):
        for u in subset:
            incidence[u].append(idx)
    rows = [np.array(v, dtype=int) for v in incidence if len(v) >= 2]
    capacities = np.ones(len(rows), dtype=int)
    weights = rng.uniform(0.5, 2.0, size=n_sets)
    return PackingInstance(
        name=name,
        n=n_sets,
        weights=weights,
        rows=rows,
        capacities=capacities,
        metadata={"generator": "random_k_set_packing", "universe_size": universe_size, "k": k, "density": density},
    )


def load_instance_from_json(path: str | Path) -> PackingInstance:
    """Load an instance from a simple JSON format.

    Expected format:
    {
      "name": "instance_name",
      "weights": [.. n floats ..],
      "constraints": [
        {"indices": [0,2,5], "capacity": 1},
        ...
      ]
    }
    """
    path = Path(path)
    data = json.loads(path.read_text())
    weights = np.array(data["weights"], dtype=float)
    rows = [np.array(c["indices"], dtype=int) for c in data["constraints"]]
    capacities = np.array([c["capacity"] for c in data["constraints"]], dtype=int)
    return PackingInstance(
        name=data.get("name", path.stem),
        n=weights.size,
        weights=weights,
        rows=rows,
        capacities=capacities,
        metadata={"generator": "json_loader", "source": str(path)},
    )


# -----------------------------------------------------------------------------
# PGD with tuning and diagnostics
# -----------------------------------------------------------------------------

def project_box(x: Array) -> Array:
    return np.clip(x, 0.0, 1.0)


def projected_gradient_mapping_norm(x: Array, grad: Array, eta: float) -> float:
    y = project_box(x - eta * grad)
    return float(np.linalg.norm((x - y) / eta))


@dataclass
class PGDResult:
    x: Array
    f: float
    pg_norm: float
    grad_norm: float
    iterations: int
    converged: bool
    eta_final: float
    runtime_sec: float
    history_f: List[float]
    history_pg: List[float]
    stop_reason: str


@dataclass
class PGDOptions:
    eta0: float = 1.0
    armijo_c: float = 1e-4
    backtrack: float = 0.5
    grow: float = 1.2
    max_iter: int = 50_000
    tol_pg: float = 1e-7
    min_eta: float = 1e-14
    stall_window: int = 200
    stall_tol: float = 1e-12
    verbose: bool = False



def run_pgd(obj: HigherOrderPackingObjective, x0: Array, opts: PGDOptions) -> PGDResult:
    x = project_box(x0.copy())
    t0 = time.time()
    eta = opts.eta0
    history_f: List[float] = []
    history_pg: List[float] = []

    f, grad, _ = obj.value_and_grad(x)
    for it in range(1, opts.max_iter + 1):
        accepted = False
        eta_try = eta
        while eta_try >= opts.min_eta:
            x_trial = project_box(x - eta_try * grad)
            diff = x_trial - x
            sqnorm = float(np.dot(diff, diff))
            f_trial = obj.value(x_trial)
            # Standard projected Armijo condition.
            if f_trial <= f - (opts.armijo_c / eta_try) * sqnorm + 1e-16:
                accepted = True
                break
            eta_try *= opts.backtrack

        if not accepted:
            pg_norm = projected_gradient_mapping_norm(x, grad, max(eta_try, opts.min_eta))
            return PGDResult(
                x=x,
                f=f,
                pg_norm=pg_norm,
                grad_norm=float(np.linalg.norm(grad)),
                iterations=it - 1,
                converged=False,
                eta_final=max(eta_try, opts.min_eta),
                runtime_sec=time.time() - t0,
                history_f=history_f,
                history_pg=history_pg,
                stop_reason="line_search_failed",
            )

        x = x_trial
        f = f_trial
        eta = min(eta_try * opts.grow, 1e6)
        f, grad, _ = obj.value_and_grad(x)
        pg_norm = projected_gradient_mapping_norm(x, grad, eta_try)

        history_f.append(f)
        history_pg.append(pg_norm)

        if opts.verbose and (it == 1 or it % 1000 == 0):
            print(f"iter={it:6d} f={f: .6e} pg={pg_norm: .3e} eta={eta_try: .3e}")

        if pg_norm <= opts.tol_pg:
            return PGDResult(
                x=x,
                f=f,
                pg_norm=pg_norm,
                grad_norm=float(np.linalg.norm(grad)),
                iterations=it,
                converged=True,
                eta_final=eta_try,
                runtime_sec=time.time() - t0,
                history_f=history_f,
                history_pg=history_pg,
                stop_reason="pg_tol",
            )

        if len(history_f) >= opts.stall_window:
            recent = history_f[-opts.stall_window:]
            if max(recent) - min(recent) < opts.stall_tol and pg_norm > 10.0 * opts.tol_pg:
                return PGDResult(
                    x=x,
                    f=f,
                    pg_norm=pg_norm,
                    grad_norm=float(np.linalg.norm(grad)),
                    iterations=it,
                    converged=False,
                    eta_final=eta_try,
                    runtime_sec=time.time() - t0,
                    history_f=history_f,
                    history_pg=history_pg,
                    stop_reason="stall_without_stationarity",
                )

    pg_norm = projected_gradient_mapping_norm(x, grad, max(opts.min_eta, eta))
    return PGDResult(
        x=x,
        f=f,
        pg_norm=pg_norm,
        grad_norm=float(np.linalg.norm(grad)),
        iterations=opts.max_iter,
        converged=False,
        eta_final=max(opts.min_eta, eta),
        runtime_sec=time.time() - t0,
        history_f=history_f,
        history_pg=history_pg,
        stop_reason="max_iter",
    )


# -----------------------------------------------------------------------------
# Classification helpers
# -----------------------------------------------------------------------------

def local_minimum_certificate(obj: HigherOrderPackingObjective, x: Array, tol: float = 1e-8) -> Dict[str, object]:
    """Practical certificate / evidence for local minimum vs saddle.

    Binary points:
      strict local minimum certified if gradient is strictly inside the normal cone:
        x_i = 0 => grad_i > 0, x_i = 1 => grad_i < 0.
      non-strict first-order stationary if inequalities are weak.

    Non-binary points:
      inspect Hessian on free variables via finite differences. If the smallest
      eigenvalue is negative -> saddle evidence. If all eigenvalues are positive
      and box first-order conditions hold -> local-min evidence.
    """
    f, grad, _ = obj.value_and_grad(x)
    free = np.where((x > tol) & (x < 1.0 - tol))[0]
    at_zero = np.where(x <= tol)[0]
    at_one = np.where(x >= 1.0 - tol)[0]

    info: Dict[str, object] = {
        "binary": free.size == 0,
        "strict_local_min_certified": False,
        "local_min_evidence": False,
        "saddle_evidence": False,
        "stationary_first_order": True,
        "min_free_hessian_eig": None,
    }

    # Box first-order signs.
    if np.any(grad[at_zero] < -tol) or np.any(grad[at_one] > tol):
        info["stationary_first_order"] = False
        return info

    if free.size == 0:
        strict_zero = np.all(grad[at_zero] > tol)
        strict_one = np.all(grad[at_one] < -tol)
        if strict_zero and strict_one:
            info["strict_local_min_certified"] = True
            info["local_min_evidence"] = True
        else:
            # weak KKT only; not enough for a clean certificate
            info["local_min_evidence"] = True
        return info

    # Finite-difference Hessian on free subspace.
    h = 1e-6
    H = np.zeros((free.size, free.size), dtype=float)
    base_grad = grad[free].copy()
    for a, idx in enumerate(free):
        xp = x.copy()
        xm = x.copy()
        xp[idx] = min(1.0, xp[idx] + h)
        xm[idx] = max(0.0, xm[idx] - h)
        gp = obj.gradient(xp)[free]
        gm = obj.gradient(xm)[free]
        H[:, a] = (gp - gm) / (xp[idx] - xm[idx])
    H = 0.5 * (H + H.T)
    eigvals = np.linalg.eigvalsh(H)
    lam_min = float(np.min(eigvals))
    info["min_free_hessian_eig"] = lam_min
    if lam_min < -1e-6:
        info["saddle_evidence"] = True
    elif lam_min > 1e-6:
        info["local_min_evidence"] = True
    return info


@dataclass
class RunRecord:
    run_id: int
    seed: int
    eta0_tuned: float
    converged: bool
    stop_reason: str
    iterations: int
    runtime_sec: float
    final_value: float
    pg_norm: float
    grad_norm: float
    binarity_error: float
    feasible: bool
    strict_local_min_certified: bool
    local_min_evidence: bool
    saddle_evidence: bool
    stationary_first_order: bool
    min_free_hessian_eig: Optional[float]


# -----------------------------------------------------------------------------
# Tuning + experiment harness
# -----------------------------------------------------------------------------

def tune_eta0(
    obj: HigherOrderPackingObjective,
    pilot_inits: Sequence[Array],
    candidate_eta0: Sequence[float],
    base_opts: PGDOptions,
) -> float:
    """Select eta0 by failure rate, then median iterations, then median runtime."""
    summaries = []
    for eta0 in candidate_eta0:
        converged_flags = []
        iterations = []
        runtimes = []
        for x0 in pilot_inits:
            opts = PGDOptions(**{**asdict(base_opts), "eta0": float(eta0), "verbose": False})
            res = run_pgd(obj, x0, opts)
            converged_flags.append(res.converged)
            iterations.append(res.iterations)
            runtimes.append(res.runtime_sec)
        fail_rate = 1.0 - float(np.mean(converged_flags))
        median_iter = float(np.median(iterations))
        median_rt = float(np.median(runtimes))
        summaries.append((fail_rate, median_iter, median_rt, float(eta0)))
    summaries.sort()
    return summaries[0][-1]


def random_initial_points(n: int, num: int, rng: np.random.Generator) -> List[Array]:
    return [rng.random(n) for _ in range(num)]


def run_experiment(
    instance: PackingInstance,
    num_runs: int = 20,
    tune_runs: int = 6,
    candidate_eta0: Sequence[float] = (8.0, 4.0, 2.0, 1.0, 0.5, 0.25, 0.125),
    tol_pg: float = 1e-7,
    max_iter: int = 50_000,
    seed: int = 0,
) -> Dict[str, object]:
    rng = np.random.default_rng(seed)
    gamma = float(np.max(instance.weights) + 0.1)
    obj = HigherOrderPackingObjective(instance, gamma=gamma)

    base_opts = PGDOptions(tol_pg=tol_pg, max_iter=max_iter)
    pilot = random_initial_points(instance.n, tune_runs, rng)
    eta0 = tune_eta0(obj, pilot, candidate_eta0, base_opts)

    records: List[RunRecord] = []
    for run_id in range(num_runs):
        x0 = rng.random(instance.n)
        res = run_pgd(obj, x0, PGDOptions(**{**asdict(base_opts), "eta0": eta0}))
        cert = local_minimum_certificate(obj, res.x)
        records.append(
            RunRecord(
                run_id=run_id,
                seed=seed + run_id,
                eta0_tuned=eta0,
                converged=res.converged,
                stop_reason=res.stop_reason,
                iterations=res.iterations,
                runtime_sec=res.runtime_sec,
                final_value=res.f,
                pg_norm=res.pg_norm,
                grad_norm=res.grad_norm,
                binarity_error=obj.binarity_error(res.x),
                feasible=obj.is_feasible(res.x),
                strict_local_min_certified=bool(cert["strict_local_min_certified"]),
                local_min_evidence=bool(cert["local_min_evidence"]),
                saddle_evidence=bool(cert["saddle_evidence"]),
                stationary_first_order=bool(cert["stationary_first_order"]),
                min_free_hessian_eig=cert["min_free_hessian_eig"],
            )
        )

    summary = {
        "instance_name": instance.name,
        "n": instance.n,
        "num_constraints": len(instance.rows),
        "gamma": gamma,
        "max_w": float(np.max(instance.weights)),
        "eta0_tuned": eta0,
        "num_runs": num_runs,
        "all_converged_to_stationary": all(r.converged for r in records),
        "all_binary": all(r.binarity_error <= 1e-7 for r in records),
        "all_feasible": all(r.feasible for r in records),
        "all_strict_local_min_certified": all(r.strict_local_min_certified for r in records),
        "any_saddle_evidence": any(r.saddle_evidence for r in records),
        "records": [asdict(r) for r in records],
        "metadata": instance.metadata,
    }
    return summary


# -----------------------------------------------------------------------------
# CLI / batch helpers
# -----------------------------------------------------------------------------

def build_demo_instances(rng: np.random.Generator) -> List[PackingInstance]:
    instances = [
        generate_random_k_set_packing(n_sets=30, universe_size=20, k=3, density=1.0, rng=rng, name="kset_3_u20_n30"),
        generate_random_unit_packing(n=25, m=35, row_size_range=(3, 6), capacity_mode="mixed", rng=rng, name="unit_mixed_n25_m35"),
        generate_random_unit_packing(n=25, m=35, row_size_range=(4, 7), capacity_mode="tight", rng=rng, name="unit_tight_n25_m35"),
        generate_random_unit_packing(n=25, m=40, row_size_range=(3, 5), capacity_mode="half", rng=rng, name="unit_half_n25_m40"),
    ]
    return instances


def save_json(obj: Dict[str, object], path: str | Path) -> None:
    path = Path(path)
    path.write_text(json.dumps(obj, indent=2))



def main() -> None:
    parser = argparse.ArgumentParser(description="PGD experiments for theorem-guided higher-order packing penalties.")
    sub = parser.add_subparsers(dest="cmd", required=True)

    demo = sub.add_parser("demo", help="Run a small suite of synthetic theorem-matching instances.")
    demo.add_argument("--outdir", type=str, default="results_demo")
    demo.add_argument("--runs", type=int, default=20)
    demo.add_argument("--tune-runs", type=int, default=6)
    demo.add_argument("--seed", type=int, default=0)
    demo.add_argument("--tol-pg", type=float, default=1e-7)
    demo.add_argument("--max-iter", type=int, default=50000)

    rand = sub.add_parser("random_unit", help="Run one random unit multi-constraint packing instance.")
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
    rand.add_argument("--out", type=str, default="random_unit_result.json")

    ksp = sub.add_parser("kset", help="Run one random k-set packing instance.")
    ksp.add_argument("--n-sets", type=int, default=30)
    ksp.add_argument("--universe-size", type=int, default=20)
    ksp.add_argument("--k", type=int, default=3)
    ksp.add_argument("--density", type=float, default=1.0)
    ksp.add_argument("--runs", type=int, default=20)
    ksp.add_argument("--tune-runs", type=int, default=6)
    ksp.add_argument("--seed", type=int, default=0)
    ksp.add_argument("--tol-pg", type=float, default=1e-7)
    ksp.add_argument("--max-iter", type=int, default=50000)
    ksp.add_argument("--out", type=str, default="kset_result.json")

    load = sub.add_parser("json", help="Run an instance from a JSON file.")
    load.add_argument("path", type=str)
    load.add_argument("--runs", type=int, default=20)
    load.add_argument("--tune-runs", type=int, default=6)
    load.add_argument("--seed", type=int, default=0)
    load.add_argument("--tol-pg", type=float, default=1e-7)
    load.add_argument("--max-iter", type=int, default=50000)
    load.add_argument("--out", type=str, default="json_instance_result.json")

    args = parser.parse_args()
    rng = np.random.default_rng(args.seed)

    if args.cmd == "demo":
        outdir = Path(args.outdir)
        outdir.mkdir(parents=True, exist_ok=True)
        results = []
        for inst in build_demo_instances(rng):
            res = run_experiment(inst, num_runs=args.runs, tune_runs=args.tune_runs,
                                 tol_pg=args.tol_pg, max_iter=args.max_iter, seed=args.seed)
            path = outdir / f"{inst.name}.json"
            save_json(res, path)
            results.append({k: res[k] for k in [
                "instance_name", "gamma", "eta0_tuned", "all_converged_to_stationary",
                "all_binary", "all_feasible", "all_strict_local_min_certified", "any_saddle_evidence"]})
        save_json({"results": results}, outdir / "summary.json")
        print(json.dumps({"results": results}, indent=2))

    elif args.cmd == "random_unit":
        inst = generate_random_unit_packing(
            n=args.n, m=args.m, row_size_range=(args.row_min, args.row_max),
            capacity_mode=args.capacity_mode, rng=rng,
            name=f"random_unit_n{args.n}_m{args.m}_{args.capacity_mode}",
        )
        res = run_experiment(inst, num_runs=args.runs, tune_runs=args.tune_runs,
                             tol_pg=args.tol_pg, max_iter=args.max_iter, seed=args.seed)
        save_json(res, args.out)
        print(json.dumps({k: res[k] for k in res if k != "records"}, indent=2))

    elif args.cmd == "kset":
        inst = generate_random_k_set_packing(
            n_sets=args.n_sets, universe_size=args.universe_size, k=args.k,
            density=args.density, rng=rng,
            name=f"kset_u{args.universe_size}_n{args.n_sets}_k{args.k}",
        )
        res = run_experiment(inst, num_runs=args.runs, tune_runs=args.tune_runs,
                             tol_pg=args.tol_pg, max_iter=args.max_iter, seed=args.seed)
        save_json(res, args.out)
        print(json.dumps({k: res[k] for k in res if k != "records"}, indent=2))

    elif args.cmd == "json":
        inst = load_instance_from_json(args.path)
        res = run_experiment(inst, num_runs=args.runs, tune_runs=args.tune_runs,
                             tol_pg=args.tol_pg, max_iter=args.max_iter, seed=args.seed)
        save_json(res, args.out)
        print(json.dumps({k: res[k] for k in res if k != "records"}, indent=2))


if __name__ == "__main__":
    main()
