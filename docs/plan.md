# Cleanup Plan (Working Copy)

This file mirrors the root cleanup plan and acts as the docs-home version for
future incremental refactors.

See the canonical detailed plan in:

- `Higher_Order_Unit_Packing_cleanup_plan.md`

## Current cleanup status

To keep fallback safety, this phase is intentionally non-destructive:

- legacy scripts remain in place,
- tidy `scripts/` entry points were added,
- a package scaffold was added under `src/`,
- an `artifacts/` directory was added for future generated outputs,
- docs were reorganized with a repository layout page.
