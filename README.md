# Higher-Order Unit Packing: Repository Guide

This repository is an experiment harness for stress-testing a higher-order exact-penalty formulation for binary unit-coefficient packing:

\[
\hat f(x) = -w^\top x + \gamma\sum_{k=1}^K e_{B_k+1}(x_{S_k}),\qquad x\in[0,1]^n,
\]

with \(\gamma = \max_i w_i + 0.1\) in the current code.

The code numerically evaluates whether projected gradient descent (PGD) on the relaxed objective consistently converges to binary, feasible local minimizers, as predicted by the theorem you provided.

---

## Quick cleanup note (non-destructive)

To keep the workspace tidier **without losing fallback paths**, this repo now also includes:

- `scripts/` thin entry points (`run_experiment.py`, `run_sweep.py`, `run_stress_suite.py`, `summarize_results.py`),
- `docs/repo_layout.md` and `docs/plan.md` for structure-first navigation,
- `src/higher_order_unit_packing/` as a gradual refactor scaffold,
- `artifacts/` as the preferred home for new generated outputs.

All existing legacy scripts and historical result files remain in place intentionally.

## 1) Repository layout at a glance

### Core solver + experiment scripts

- `higher_order_pgd_packing.py`  
  Main implementation: instance generators/loaders, objective and gradients, PGD with Armijo backtracking, local-minimum/saddle diagnostics, and CLI entry points (`demo`, `random_unit`, `kset`, `json`).

- `run_higher_order_pgd_sweep.sh`  
  Batch shell runner for a grid sweep of `random_unit` and `kset` settings. Produces many JSON outputs and then calls the summarizer.

- `summarize_higher_order_pgd_results.py`  
  Aggregates a directory of result JSON files into `summary.csv` and/or `summary.md`.

- `run_higher_order_pgd_stress_suite.py`  
  Runs a fixed “harder” stress suite (RU1–RU6 and KS1–KS6), with configurable replicates, then writes CSV+Markdown summaries.

- `higher_order_pgd_record_instances_wrapper.py`  
  Wrapper that runs the base solver and augments each run output with the exact generated problem instance under `problem_instance`.

- `run_higher_order_pgd_stress_suite_record_instances.py`  
  Stress-suite driver that uses the wrapper above, and writes per-run folders containing:
  - `result.json`
  - `instance.json`
  - `problem.md`
  - `problem.tex`
  plus top-level index/summary files.

### Documentation already present

- `README_higher_order_pgd_experiments.md`  
  Focused usage notes for running the base experiments.

- `README_record_exact_instances.md`  
  Focused usage notes for the “record exact instances” workflow.

### Output directories currently checked in

- `higher_order_pgd_sweep_results/`  
  Output from the batch sweep script:
  - `random_unit/*.json`
  - `kset/*.json`
  - `summary.csv`
  - `summary.md`

- `recorded_results/`  
  Output from the recorded stress-suite workflow:
  - one directory per problem/replicate (`RU*_rep*`, `KS*_rep*`), each containing
    `result.json`, `instance.json`, `problem.md`, `problem.tex`
  - `recorded_stress_summary.csv`
  - `recorded_problem_index.md`

---

## 2) What each main code file does (algorithms + parameters)

## `higher_order_pgd_packing.py` (main solver)

### A. Mathematical/objective implementation

- Implements elementary symmetric polynomial helpers (`elementary_symmetric_all`, `elementary_symmetric_value`).
- For each constraint row \((S_k, B_k)\), computes penalty term \(e_{B_k+1}(x_{S_k})\).
- Computes exact row gradients efficiently via prefix/suffix DP (`row_value_and_grad`).
- Full relaxed objective:
  - value: `-w^T x + gamma * penalty`
  - gradient: `-w + gamma * (sum of row local grads)`

### B. Instance models and generation/loading

- `PackingInstance` dataclass fields:
  - `name`, `n`, `weights`, `rows`, `capacities`, `metadata`
- `generate_random_unit_packing(...)`
  - Inputs: `n`, `m`, `row_size_range=(row_min,row_max)`, `capacity_mode`, `rng`, `name`
  - `capacity_mode` options:
    - `mixed`: random \(B_k\in\{1,...,|S_k|-1\}
    - `tight`: \(B_k=|S_k|-1\)
    - `set_packing`: \(B_k=1\)
    - `half`: \(B_k=\lfloor|S_k|/2\rfloor\) with min 1
  - Weights sampled uniform in `[0.5, 2.0]`.

- `generate_random_k_set_packing(...)`
  - Inputs: `n_sets`, `universe_size`, `k`, `density`, `rng`, `name`
  - Generates candidate k-subsets as variables.
  - Converts to incidence constraints per universe element:
    \(\sum_{i\ni u} x_i \le 1\).
  - Drops rows with fewer than 2 incident variables.
  - Weights uniform in `[0.5, 2.0]`.

- `load_instance_from_json(path)`
  - Expects JSON with `weights` and `constraints` (`indices`, `capacity`).

### C. Optimization algorithm (PGD)

- Uses projected gradient descent on box `[0,1]^n` (`project_box`).
- Line search: monotone Armijo backtracking in `run_pgd`.
- `PGDOptions` hyperparameters:
  - `eta0` (initial stepsize)
  - `armijo_c` (default `1e-4`)
  - `backtrack` (default `0.5`)
  - `grow` (default `1.2`)
  - `max_iter` (default `50000`)
  - `tol_pg` (projected-gradient mapping norm tolerance, default `1e-7`)
  - `min_eta`, stall detection window/tolerance
- Convergence/stopping diagnostics include:
  - `pg_tol` reached
  - line-search failure
  - stall without stationarity
  - max iterations

### D. Stability/correctness diagnostics per run

- `binarity_error = max_i min(|x_i|, |1-x_i|)`.
- Feasibility check uses all row sums \(\sum_{i\in S_k}x_i\le B_k\).
- `local_minimum_certificate(...)`:
  - Binary case: strict local min certified by strict normal-cone sign conditions on gradient.
  - Non-binary case: approximates free-subspace Hessian via finite differences and inspects min eigenvalue:
    - negative => saddle evidence
    - positive => local-min evidence

### E. Experiment harness logic

- `gamma` set to `max(weights)+0.1`.
- Tunes `eta0` by pilot runs (`tune_eta0`) over candidates `(8, 4, 2, 1, 0.5, 0.25, 0.125)`.
- Selection criterion: lowest failure rate, then median iterations, then median runtime.
- Final summary booleans:
  - `all_converged_to_stationary`
  - `all_binary`
  - `all_feasible`
  - `all_strict_local_min_certified`
  - `any_saddle_evidence`

### F. CLI commands and parameters

- `demo`
  - Args: `--outdir`, `--runs`, `--tune-runs`, `--seed`, `--tol-pg`, `--max-iter`
- `random_unit`
  - Args: `--n`, `--m`, `--row-min`, `--row-max`, `--capacity-mode`, plus shared run args and `--out`
- `kset`
  - Args: `--n-sets`, `--universe-size`, `--k`, `--density`, plus shared run args and `--out`
- `json`
  - Args: `path`, shared run args, and `--out`

---

## `run_higher_order_pgd_sweep.sh` (batch sweep runner)

This script automates a larger grid experiment.

### Inputs/controls

- Positional:
  1. solver script path (default points to external location)
  2. output directory (default points to external location)
- Environment overrides:
  - `RUNS`, `TUNE_RUNS`, `TOL_PG`, `MAX_ITER`, `SEED_BASE`

### Sweep design

1. **random_unit sweep** over:
   - `mode in {mixed, tight, half, set_packing}`
   - `n in {20, 30}`
   - `m in {30, 45}`
   - row size in `{3-5, 4-7}`
2. **kset sweep** over:
   - `k in {3, 4}`
   - `universe_size in {20, 30}`
   - `n_sets in {30, 50}`
   - `density in {1.0, 0.7}`

### Outputs

- Writes one JSON per configuration into:
  - `higher_order_pgd_sweep_results/random_unit/`
  - `higher_order_pgd_sweep_results/kset/`
- Then runs `summarize_higher_order_pgd_results.py` to create:
  - `higher_order_pgd_sweep_results/summary.csv`
  - `higher_order_pgd_sweep_results/summary.md`

---

## `summarize_higher_order_pgd_results.py` (aggregator)

- Scans recursively for JSON files containing both `instance_name` and `records`.
- Computes per-file aggregates:
  - average iterations/runtime
  - max binarity error
  - pass/fail booleans copied from file
- Optional outputs:
  - `--csv <path>`
  - `--md <path>`

Typical use:

```bash
python summarize_higher_order_pgd_results.py higher_order_pgd_sweep_results \
  --csv higher_order_pgd_sweep_results/summary.csv \
  --md higher_order_pgd_sweep_results/summary.md
```

---

## `run_higher_order_pgd_stress_suite.py` (fixed hard suite)

Defines stress specs (`build_specs`) and executes each with replicates.

### Problem families and IDs

- `--profile standard`: `RU1`–`RU6` and `KS1`–`KS6` (hard baseline suite).
- `--profile extreme`: `RU7`–`RU10` and `KS7`–`KS10` (larger/harder stability suite).

### Key parameters

CLI args include:
- `--solver`
- `--outdir`
- `--profile {standard,extreme}`
- `--runs`
- `--tune-runs`
- `--tol-pg`
- `--max-iter`
- `--replicates`
- `--seed-base`
- `--skip-existing`

### Outputs

- Per-run result JSON files in output directory.
- Suite-level files:
  - `stress_summary.csv`
  - `stress_report.md`

(Names depend on script defaults/arguments; this repo primarily checks in the recorded variant output under `recorded_results/`.)

---

## `higher_order_pgd_record_instances_wrapper.py` (embed exact instances)

Purpose: run the base solver and ensure output includes exact generated problem data under `problem_instance`.

### How it works

- Dynamically loads base solver script via `--base-script`.
- Recreates instance by invoking base generators with the same seed/arguments.
- Runs base `run_experiment(...)`.
- Adds:
  - `result["problem_instance"] = {name, n, weights, constraints, metadata}`
- For k-set, it also reconstructs `candidate_sets` and stores them in metadata.

### CLI

Subcommands mirror base solver:
- `random_unit`
- `kset`
- `json`
with the same major run controls (`--runs`, `--tune-runs`, `--seed`, `--tol-pg`, `--max-iter`, `--out`).

---

## `run_higher_order_pgd_stress_suite_record_instances.py` (recorded stress suite)

Runs the RU/KS stress suite through the wrapper so every run has reproducible exact instance artifacts.

### Inputs

- `--wrapper` path to `higher_order_pgd_record_instances_wrapper.py`
- `--base-script` path to `higher_order_pgd_packing.py`
- run controls (`--runs`, `--tune-runs`, `--tol-pg`, `--max-iter`, `--replicates`, `--seed-base`)
- `--outdir`

### Per-run outputs

For each `<problem_id>_rep<r>/`:
- `result.json` (full experiment summary + `problem_instance`)
- `instance.json` (exact original problem only)
- `problem.md` (human-readable statement)
- `problem.tex` (LaTeX statement)

### Top-level outputs

- `recorded_stress_summary.csv`
- `recorded_problem_index.md`

---

## 3) Data files currently present and how they relate

## `higher_order_pgd_sweep_results/`

Generated by the sweep workflow:

1. `run_higher_order_pgd_sweep.sh` runs many solver jobs.
2. Each job writes a JSON under either `random_unit/` or `kset/`.
3. `summarize_higher_order_pgd_results.py` reads those JSON files and produces:
   - `summary.csv`
   - `summary.md`

Filename conventions encode parameters and seed, e.g.:
- `random_unit/n30_m45_r4-7_mixed_s107.json`
- `kset/u30_n50_k4_d0.7_s147.json`

## `recorded_results/`

Generated by the exact-instance recording workflow:

1. `run_higher_order_pgd_stress_suite_record_instances.py` loops through RU/KS specs and replicates.
2. It calls `higher_order_pgd_record_instances_wrapper.py` for each run.
3. Wrapper runs base solver and embeds exact `problem_instance`.
4. Driver splits/writes companion artifacts (`instance.json`, `problem.md`, `problem.tex`) and summary/index tables.

Directory naming:
- `RU#_rep#` for random-unit stress suite entries.
- `KS#_rep#` for k-set stress suite entries.

---

## 4) Notes on SLURM / cluster scripts

There are **no SLURM job scripts** (`*.slurm`, `sbatch` files) in this repository snapshot.

The only batch orchestration script present is shell-based (`run_higher_order_pgd_sweep.sh`).

If you want, I can add a clean `sbatch` template (single-job and array-job versions) that wraps either the sweep script or the stress-suite scripts.

---

## 5) Recommended cleanup and reproducibility improvements

Given your comment that the repo is currently messy, these low-risk improvements would make it much easier to maintain:

1. **Normalize script defaults to relative local paths**  
   Several scripts still default to older absolute paths (`/mnt/data/...` or `/egr/...`).

2. **Separate code from generated data**  
   Keep scripts in `src/` (or root) and outputs in a dedicated `artifacts/` folder ignored by git (except selected snapshots).

3. **Add a small `requirements.txt` or `pyproject.toml`**  
   Current code assumes `numpy` is installed.

4. **Add one canonical top-level entrypoint**  
   Example: `make sweep`, `make stress`, `make summarize`.

5. **Add schema docs for result JSONs**  
   A short schema section in README helps downstream parsing.

If you want, I can do this cleanup in a follow-up PR while preserving all current data files.
