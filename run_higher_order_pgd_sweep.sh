#!/usr/bin/env bash
set -euo pipefail

# Batch sweep runner for higher_order_pgd_packing(1).py
# Usage:
#   bash /mnt/data/run_higher_order_pgd_sweep.sh
#   bash /mnt/data/run_higher_order_pgd_sweep.sh /path/to/higher_order_pgd_packing.py results_dir

SCRIPT_PATH="${1:-/egr/research-pac/huang248/higer_order_unit_packing/higher_order_pgd_packing.py}"
OUTDIR="${2:-/egr/research-pac/huang248/higer_order_unit_packing/higher_order_pgd_sweep_results}"
RUNS="${RUNS:-20}"
TUNE_RUNS="${TUNE_RUNS:-6}"
TOL_PG="${TOL_PG:-1e-7}"
MAX_ITER="${MAX_ITER:-50000}"
SEED_BASE="${SEED_BASE:-100}"

mkdir -p "$OUTDIR"
mkdir -p "$OUTDIR/random_unit" "$OUTDIR/kset"

if [[ ! -f "$SCRIPT_PATH" ]]; then
  echo "Error: script not found at $SCRIPT_PATH" >&2
  exit 1
fi

run_random_unit() {
  local n="$1"
  local m="$2"
  local row_min="$3"
  local row_max="$4"
  local mode="$5"
  local seed="$6"
  local tag="n${n}_m${m}_r${row_min}-${row_max}_${mode}_s${seed}"
  local out="$OUTDIR/random_unit/${tag}.json"

  echo "[random_unit] $tag"
  python "$SCRIPT_PATH" random_unit \
    --n "$n" \
    --m "$m" \
    --row-min "$row_min" \
    --row-max "$row_max" \
    --capacity-mode "$mode" \
    --runs "$RUNS" \
    --tune-runs "$TUNE_RUNS" \
    --seed "$seed" \
    --tol-pg "$TOL_PG" \
    --max-iter "$MAX_ITER" \
    --out "$out"
}

run_kset() {
  local n_sets="$1"
  local universe_size="$2"
  local k="$3"
  local density="$4"
  local seed="$5"
  local tag="u${universe_size}_n${n_sets}_k${k}_d${density}_s${seed}"
  local out="$OUTDIR/kset/${tag}.json"

  echo "[kset] $tag"
  python "$SCRIPT_PATH" kset \
    --n-sets "$n_sets" \
    --universe-size "$universe_size" \
    --k "$k" \
    --density "$density" \
    --runs "$RUNS" \
    --tune-runs "$TUNE_RUNS" \
    --seed "$seed" \
    --tol-pg "$TOL_PG" \
    --max-iter "$MAX_ITER" \
    --out "$out"
}

# -----------------------------
# Sweep 1: random unit packing
# -----------------------------
seed="$SEED_BASE"
for mode in mixed tight half set_packing; do
  for n in 20 30; do
    for m in 30 45; do
      for row_spec in "3 5" "4 7"; do
        read -r row_min row_max <<< "$row_spec"
        run_random_unit "$n" "$m" "$row_min" "$row_max" "$mode" "$seed"
        seed=$((seed + 1))
      done
    done
  done
done

# -----------------------------
# Sweep 2: k-set packing
# -----------------------------
for k in 3 4; do
  for universe_size in 20 30; do
    for n_sets in 30 50; do
      for density in 1.0 0.7; do
        run_kset "$n_sets" "$universe_size" "$k" "$density" "$seed"
        seed=$((seed + 1))
      done
    done
  done
done

# Aggregate results if summarizer exists.
SUMMARY_PY="$(dirname "$0")/summarize_higher_order_pgd_results.py"
if [[ -f "$SUMMARY_PY" ]]; then
  python "$SUMMARY_PY" "$OUTDIR" --csv "$OUTDIR/summary.csv" --md "$OUTDIR/summary.md"
  echo
  echo "Wrote aggregate summary to:"
  echo "  $OUTDIR/summary.csv"
  echo "  $OUTDIR/summary.md"
fi

echo
find "$OUTDIR" -maxdepth 2 -type f | sort
