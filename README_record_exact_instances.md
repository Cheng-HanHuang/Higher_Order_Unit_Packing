# Recording exact generated problems with the PGD results

This workflow adds the exact original problem instance to each result JSON and also writes companion files:

- `result.json`: run summary + per-run diagnostics + embedded `problem_instance`
- `instance.json`: exact original problem only
- `problem.md`: human-readable statement of the original problem
- `problem.tex`: LaTeX statement of the original problem

## Single run

```bash
python higher_order_pgd_record_instances_wrapper.py \
  --base-script /path/to/higher_order_pgd_packing.py \
  random_unit \
  --n 25 --m 40 --row-min 3 --row-max 6 --capacity-mode mixed \
  --runs 20 --tune-runs 6 --seed 0 --out /path/to/result.json
```

The resulting `result.json` will contain a top-level key named `problem_instance`.

## Harder stress suite with exact problem records

```bash
python run_higher_order_pgd_stress_suite_record_instances.py \
  --wrapper /path/to/higher_order_pgd_record_instances_wrapper.py \
  --base-script /path/to/higher_order_pgd_packing.py \
  --outdir /path/to/recorded_results
```

For each run directory, you get:

```text
<outdir>/RU1_rep1/
  result.json
  instance.json
  problem.md
  problem.tex
```

At the top level you also get:

- `recorded_stress_summary.csv`
- `recorded_problem_index.md`

## Important note

Past runs cannot be retroactively enriched unless you rerun them, because the old result files do not store the exact generated rows/sets. This new workflow fixes that for future runs.
