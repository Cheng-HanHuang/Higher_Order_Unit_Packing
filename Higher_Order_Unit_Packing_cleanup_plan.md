# Higher_Order_Unit_Packing cleanup and refactor plan

## Goal

Clean up the repository into a small, reproducible experiment framework for higher-order unit packing that supports:

1. clear instance generation,
2. a main solver with both simple PGD and line-search PGD,
3. a runner for broad stress testing with automatic master summaries,
4. preservation of current theorem-facing behavior and existing experiment outputs where possible.

## What is in the repo now

From the current `README.md`, the repository already contains these main components:

- `higher_order_pgd_packing.py`: main solver and CLI
- `run_higher_order_pgd_sweep.sh`: batch sweep shell runner
- `summarize_higher_order_pgd_results.py`: result aggregator
- `run_higher_order_pgd_stress_suite.py`: fixed hard-suite runner
- `higher_order_pgd_record_instances_wrapper.py`: exact-instance wrapper
- `run_higher_order_pgd_stress_suite_record_instances.py`: recorded stress-suite runner
- two focused READMEs for experiment workflows
- checked-in output folders with prior generated results

This means the repo already has most required functionality, but it is currently split across several overlapping scripts and experiment modes.

## Recommended design direction

I recommend refactoring toward a **single small package + thin CLI scripts** rather than keeping many semi-independent scripts.

### Proposed target structure

```text
Higher_Order_Unit_Packing/
├── README.md
├── requirements.txt
├── src/
│   └── higher_order_unit_packing/
│       ├── __init__.py
│       ├── instance.py          # dataclasses and shared serialization
│       ├── generators.py        # random_unit, k-set, json loader
│       ├── objective.py         # elementary symmetric penalties, value/grad
│       ├── solver.py            # PGD variants and diagnostics
│       ├── experiment.py        # run one instance many times
│       ├── runner.py            # sweep/stress orchestration helpers
│       ├── summarize.py         # master summary builder
│       └── report.py            # md/tex/json per-instance reporting
├── scripts/
│   ├── run_experiment.py
│   ├── run_stress_suite.py
│   ├── run_sweep.py
│   └── summarize_results.py
├── configs/
│   ├── stress_suite.json
│   └── sweep_defaults.json
├── docs/
│   ├── plan.md
│   ├── experiment_schema.md
│   └── repo_layout.md
└── artifacts/
    └── ... generated outputs, gitignored by default
```

This is a larger cleanup than just editing one file, but it gives the clearest long-term separation between:

- math/core logic,
- experiment orchestration,
- generated outputs.

## Scope of the cleanup

### 1. Generator cleanup

### Current state

Generation logic exists inside the main solver script, which makes the solver harder to read and reuse.

### Proposed change

Move all instance creation and loading into `generators.py` and `instance.py`.

### Concrete generator goals

- keep one canonical `PackingInstance` dataclass,
- keep exactly three entry paths:
  - `generate_random_unit_packing(...)`
  - `generate_random_k_set_packing(...)`
  - `load_instance_from_json(...)`
- store exact seeds and generation metadata inside each instance,
- add `to_dict()` / `from_dict()` helpers for reproducibility,
- optionally add a `difficulty_tag` or `family` field for later summary tables.

### Suggested improvements

- make generators return instances only, with no optimizer-side logic mixed in,
- expose a compact naming helper so filenames are generated in one place,
- validate rows and capacities centrally:
  - deduplicate row indices,
  - sort row indices,
  - drop empty or trivial rows,
  - check `1 <= B_k < |S_k|`.

## 2. Main solver cleanup

### Current state

The current main solver already has Armijo backtracking PGD and theorem-facing diagnostics. That should remain. But for theorem presentation and debugging, the repo should also expose a simpler fixed-step PGD option.

### Proposed change

Split the current solver into:

- core objective code in `objective.py`,
- solver code in `solver.py`,
- experiment-loop code in `experiment.py`.

### Required solver modes

I recommend supporting **two official optimization modes**:

1. `pgd_fixed`
   - simple projected gradient descent with constant step size,
   - intended for theorem-consistency demonstrations and easier debugging,
   - minimal moving parts.

2. `pgd_armijo`
   - projected gradient descent with monotone Armijo backtracking,
   - intended for practical runs and robustness.

### Why keep both

- `pgd_fixed` is easier to explain in the paper and to sanity-check against theorem statements.
- `pgd_armijo` is more reliable in practice and should remain the default for broad sweeps.

### Suggested solver API

```python
result = run_solver(
    instance,
    method="pgd_armijo",   # or "pgd_fixed"
    gamma_mode="max_weight_plus_margin",
    gamma_margin=0.1,
    options=SolverOptions(...),
    seed=123,
)
```

### Concrete solver cleanup tasks

- separate pure math from stopping/IO/reporting,
- keep one common result schema regardless of solver mode,
- move all line-search-specific logic behind one method switch,
- preserve current diagnostics:
  - projected-gradient norm,
  - binarity error,
  - feasibility,
  - local-minimum certificate / saddle evidence,
  - runtime and iteration count.

### Additional recommendation

Add a `method` field and a `gamma` field explicitly to every result JSON, so mixed runs can be summarized cleanly.

## 3. Runner cleanup

### Current state

The repo currently has separate sweep scripts, stress-suite scripts, wrapper scripts, and summarizers. Functionality overlaps.

### Proposed change

Unify these into one main runner layer with two modes:

- `stress_suite`
- `parameter_sweep`

and one summary layer that always writes a master summary automatically when the run finishes.

### Runner goals

- run a list of experiment specs,
- support replicates,
- support both solver methods,
- optionally record exact instances,
- automatically write:
  - per-run JSON,
  - per-suite CSV,
  - per-suite Markdown summary,
  - optional instance artifacts (`instance.json`, `problem.md`, `problem.tex`).

### Recommended runner design

Use a Python runner instead of shell as the canonical path.

#### Keep shell only as a thin convenience wrapper

`run_higher_order_pgd_sweep.sh` can remain if useful on cluster systems, but it should just call:

```bash
python scripts/run_sweep.py ...
```

### Suggested outputs

For every suite output directory:

```text
results/<suite_name>/
├── runs/
│   ├── <run_id>/result.json
│   ├── <run_id>/instance.json
│   ├── <run_id>/problem.md
│   └── <run_id>/problem.tex
├── master_summary.csv
├── master_summary.md
├── aggregate_by_family.csv
└── run_index.json
```

### Summary behavior

The runner should automatically call the summarizer at the end of every successful batch.

The master summary should include at least:

- run id
- family (`random_unit`, `kset`, `json`, stress id)
- solver method
- seed
- gamma
- convergence status
- binary? feasible? local-min certified?
- average and max binarity error
- average runtime / iterations
- any saddle evidence

## 4. Simplify the exact-instance workflow

### Current state

Exact-instance recording currently requires a wrapper plus a dedicated runner.

### Proposed change

Fold this into the main runner using a flag such as:

```bash
--record-instance-artifacts
```

Then the wrapper script becomes unnecessary.

### Why this is better

- fewer entry points,
- fewer code paths to keep consistent,
- less chance of schema drift between plain runs and recorded runs.

## 5. Documentation cleanup

### Proposed docs set

- `README.md`
  - short repo overview,
  - install,
  - quick-start examples.

- `docs/repo_layout.md`
  - file/module map.

- `docs/experiment_schema.md`
  - exact JSON result schema,
  - meaning of each metric.

- `docs/plan.md`
  - this cleanup plan.

### Recommended README simplification

The current README is very detailed, which is useful for archival context. I recommend:

- keep top-level README shorter and task-oriented,
- move deep file-by-file explanation into `docs/repo_layout.md`.

## 6. Output and git hygiene

### Proposed change

Move generated outputs under `artifacts/` and add them to `.gitignore` by default.

Keep only:

- a tiny sample artifact set if needed,
- or no generated results in git at all.

### Why

This will keep the repo cleaner and make code review easier.

## 7. Minimal implementation phases

I recommend doing the cleanup in four phases.

### Phase 1: noninvasive reorganization

- add `docs/plan.md`
- add `requirements.txt`
- add `.gitignore` cleanup for artifacts
- create `src/higher_order_unit_packing/`
- move pure utilities without changing behavior

### Phase 2: solver split

- move instance/objective/generator/solver logic into modules
- preserve current CLI behavior through thin wrappers
- add `pgd_fixed`
- keep `pgd_armijo` as default

### Phase 3: runner unification

- replace overlapping runners/wrappers with one Python runner layer
- add automatic master summary writing
- keep backward-compatible command aliases if easy

### Phase 4: documentation and polishing

- rewrite README to match new structure
- add schema docs
- verify example commands
- optionally add SLURM templates later if needed

## 8. Suggested concrete deliverables for the next execution step

For the actual code cleanup, I recommend we implement these first:

1. create `docs/plan.md` in the repo,
2. refactor the current single main script into:
   - `generators.py`
   - `objective.py`
   - `solver.py`
   - `experiment.py`
3. add `pgd_fixed` alongside the current Armijo PGD,
4. replace separate sweep/stress wrappers with one Python runner,
5. make automatic `master_summary.csv` and `master_summary.md` mandatory outputs.

## 9. My suggested changes to your original three-item list

Your three requested categories are right. I would only adjust them slightly.

### Your list

1. Generator
2. Main code with simple PGD also available
3. Runner with automatic master summary

### My refined version

1. **Generator + instance schema**
   - split cleanly from solver,
   - centralize validation and serialization.

2. **Main solver with two official methods**
   - `pgd_fixed` for theorem-facing consistency,
   - `pgd_armijo` for practical robustness.

3. **Unified Python runner + built-in summarizer**
   - one code path for stress, sweep, and recorded instances,
   - automatic summary generation,
   - optional exact instance artifacts.

4. **Docs and repo hygiene**
   - necessary to keep the cleanup maintainable.

## 10. Success criteria

The cleanup is complete if, after refactor:

- one can generate any supported instance family without touching solver code,
- one can switch between `pgd_fixed` and `pgd_armijo` via one CLI flag,
- one runner can execute a whole suite and always write a master summary,
- result JSON schema is stable and documented,
- old experiment capabilities are preserved or cleanly replaced.
