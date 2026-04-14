#!/usr/bin/env bash
set -euo pipefail

# Comprehensive experiment orchestrator for this repository.
#
# It can run any combination of:
#  1) parameter grid sweep
#  2) stress suite
#  3) stress suite with exact instance recording
# and then build summaries/reports.
#
# Usage examples:
#   bash run_comprehensive_experiments.sh
#   MODE=all RUNS=30 TUNE_RUNS=8 bash run_comprehensive_experiments.sh
#   MODE=sweep SWEEP_OUTDIR=artifacts/my_sweep bash run_comprehensive_experiments.sh
#   MODE=stress_record REPLICATES=2 bash run_comprehensive_experiments.sh
#
# Main controls (env vars):
#   MODE            one of: all | sweep | stress | stress_record
#   PYTHON          python executable (default: python)
#   SOLVER          path to solver script
#   RUNS            runs per instance
#   TUNE_RUNS       eta0 tuning runs
#   TOL_PG          projected-gradient tolerance
#   MAX_ITER        maximum PGD iterations
#   SEED_BASE       base random seed
#   REPLICATES      stress-suite replicates
#   SKIP_EXISTING   if 1, pass --skip-existing to stress scripts
#
# Output controls:
#   ROOT_OUTDIR          root output directory (default: artifacts/experiments)
#   SWEEP_OUTDIR         default: $ROOT_OUTDIR/sweep
#   STRESS_OUTDIR        default: $ROOT_OUTDIR/stress
#   STRESS_RECORD_OUTDIR default: $ROOT_OUTDIR/stress_recorded

MODE="${MODE:-all}"
PYTHON="${PYTHON:-python}"
SOLVER="${SOLVER:-./higher_order_pgd_packing.py}"

RUNS="${RUNS:-20}"
TUNE_RUNS="${TUNE_RUNS:-6}"
TOL_PG="${TOL_PG:-1e-7}"
MAX_ITER="${MAX_ITER:-50000}"
SEED_BASE="${SEED_BASE:-100}"
REPLICATES="${REPLICATES:-1}"
SKIP_EXISTING="${SKIP_EXISTING:-1}"

ROOT_OUTDIR="${ROOT_OUTDIR:-artifacts/experiments}"
SWEEP_OUTDIR="${SWEEP_OUTDIR:-$ROOT_OUTDIR/sweep}"
STRESS_OUTDIR="${STRESS_OUTDIR:-$ROOT_OUTDIR/stress}"
STRESS_RECORD_OUTDIR="${STRESS_RECORD_OUTDIR:-$ROOT_OUTDIR/stress_recorded}"

log() {
  printf '[%s] %s\n' "$(date -u +'%Y-%m-%dT%H:%M:%SZ')" "$*"
}

usage() {
  cat <<'USAGE'
run_comprehensive_experiments.sh

Runs larger experiment workflows using the existing project scripts.

Env vars:
  MODE=all|sweep|stress|stress_record
  PYTHON=<python executable>
  SOLVER=<path to higher_order_pgd_packing.py>
  RUNS=<int>
  TUNE_RUNS=<int>
  TOL_PG=<float>
  MAX_ITER=<int>
  SEED_BASE=<int>
  REPLICATES=<int>
  SKIP_EXISTING=0|1

  ROOT_OUTDIR=<path>
  SWEEP_OUTDIR=<path>
  STRESS_OUTDIR=<path>
  STRESS_RECORD_OUTDIR=<path>

Example:
  MODE=all RUNS=30 TUNE_RUNS=8 ROOT_OUTDIR=artifacts/exp_full \
    bash run_comprehensive_experiments.sh
USAGE
}

if [[ "${1:-}" == "-h" || "${1:-}" == "--help" ]]; then
  usage
  exit 0
fi

if [[ ! -f "$SOLVER" ]]; then
  echo "Error: solver not found: $SOLVER" >&2
  exit 1
fi

mkdir -p "$ROOT_OUTDIR"

run_sweep() {
  log "Starting sweep -> $SWEEP_OUTDIR"
  RUNS="$RUNS" \
  TUNE_RUNS="$TUNE_RUNS" \
  TOL_PG="$TOL_PG" \
  MAX_ITER="$MAX_ITER" \
  SEED_BASE="$SEED_BASE" \
  bash ./run_higher_order_pgd_sweep.sh "$SOLVER" "$SWEEP_OUTDIR"

  if [[ -f ./summarize_higher_order_pgd_results.py ]]; then
    "$PYTHON" ./summarize_higher_order_pgd_results.py "$SWEEP_OUTDIR" \
      --csv "$SWEEP_OUTDIR/summary.csv" \
      --md "$SWEEP_OUTDIR/summary.md"
  fi
}

run_stress() {
  log "Starting stress suite -> $STRESS_OUTDIR"
  local skip_flag=""
  if [[ "$SKIP_EXISTING" == "1" ]]; then
    skip_flag="--skip-existing"
  fi

  "$PYTHON" ./run_higher_order_pgd_stress_suite.py \
    --solver "$SOLVER" \
    --outdir "$STRESS_OUTDIR" \
    --runs "$RUNS" \
    --tune-runs "$TUNE_RUNS" \
    --tol-pg "$TOL_PG" \
    --max-iter "$MAX_ITER" \
    --replicates "$REPLICATES" \
    --seed-base "$SEED_BASE" \
    $skip_flag
}

run_stress_record() {
  log "Starting stress suite with exact instance recording -> $STRESS_RECORD_OUTDIR"
  local skip_flag=""
  if [[ "$SKIP_EXISTING" == "1" ]]; then
    skip_flag="--skip-existing"
  fi

  "$PYTHON" ./run_higher_order_pgd_stress_suite_record_instances.py \
    --solver "$SOLVER" \
    --outdir "$STRESS_RECORD_OUTDIR" \
    --runs "$RUNS" \
    --tune-runs "$TUNE_RUNS" \
    --tol-pg "$TOL_PG" \
    --max-iter "$MAX_ITER" \
    --replicates "$REPLICATES" \
    --seed-base "$SEED_BASE" \
    $skip_flag
}

case "$MODE" in
  all)
    run_sweep
    run_stress
    run_stress_record
    ;;
  sweep)
    run_sweep
    ;;
  stress)
    run_stress
    ;;
  stress_record)
    run_stress_record
    ;;
  *)
    echo "Error: invalid MODE='$MODE' (expected all|sweep|stress|stress_record)" >&2
    exit 1
    ;;
esac

log "Completed MODE=$MODE"
log "Outputs root: $ROOT_OUTDIR"
find "$ROOT_OUTDIR" -maxdepth 2 -type d | sort
