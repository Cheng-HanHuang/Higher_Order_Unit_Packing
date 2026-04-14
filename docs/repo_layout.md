# Repository layout

This repo now has a cleaner top-level structure while preserving all existing
legacy workflows for fallback.

## Preferred entry points (new)

- `scripts/run_experiment.py`
- `scripts/run_sweep.py`
- `scripts/run_stress_suite.py`
- `scripts/summarize_results.py`

These are thin wrappers over the existing scripts so behavior is unchanged.

## Legacy implementation (kept for fallback)

- `higher_order_pgd_packing.py`
- `run_higher_order_pgd_sweep.sh`
- `run_higher_order_pgd_stress_suite.py`
- `summarize_higher_order_pgd_results.py`
- `higher_order_pgd_record_instances_wrapper.py`
- `run_higher_order_pgd_stress_suite_record_instances.py`

## Package scaffold (for gradual refactor)

- `src/higher_order_unit_packing/__init__.py`

This creates a stable location for future module splits without forcing a
breaking move right now.

## Output hygiene

- `artifacts/` is reserved for generated outputs.
- Existing checked-in results remain untouched for reproducibility.
