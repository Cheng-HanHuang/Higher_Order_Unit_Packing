#!/usr/bin/env python3
"""Thin wrapper for the legacy experiment CLI.

This keeps the original `higher_order_pgd_packing.py` intact while exposing a
cleaner entry point under `scripts/`.
"""

from __future__ import annotations

import subprocess
import sys
from pathlib import Path


REPO_ROOT = Path(__file__).resolve().parents[1]
LEGACY_SCRIPT = REPO_ROOT / "higher_order_pgd_packing.py"


if __name__ == "__main__":
    cmd = [sys.executable, str(LEGACY_SCRIPT), *sys.argv[1:]]
    raise SystemExit(subprocess.call(cmd))
