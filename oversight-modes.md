# Gort oversight modes

This file is only an index.

To keep mutually exclusive oversight semantics from competing in the same always-loaded prompt surface, the executable mode guidance lives in dedicated files:

- default: [`./modes/autonomy.md`](./modes/autonomy.md)
- explicit override: [`./modes/safe-mode.md`](./modes/safe-mode.md)

Keep `gort.md` for universal invariants and state-machine rules. Load exactly one mode file for the active run.
