#!/usr/bin/env python3
"""Thin wrapper for the current stress suite runner."""

from __future__ import annotations

import subprocess
import sys
from pathlib import Path


REPO_ROOT = Path(__file__).resolve().parents[1]
LEGACY_SCRIPT = REPO_ROOT / "run_higher_order_pgd_stress_suite.py"


if __name__ == "__main__":
    cmd = [sys.executable, str(LEGACY_SCRIPT), *sys.argv[1:]]
    raise SystemExit(subprocess.call(cmd, cwd=REPO_ROOT))
