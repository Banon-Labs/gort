# Gort

Gort is a state-machine prompt pack for autonomous project execution.

## Layout

- `gort.md` — canonical root contract, global invariants, routing, and shared procedures
- `states/klaatu.md` — execute one ready task for the current epic per loop
- `states/berada.md` — make the current epic execution-ready
- `states/nikto.md` — terminal halt behavior and allowed entry reasons
- `context-compaction.md` — tmux/Pi compaction and resume procedure
- `gort.citations.md` — evidence log for edits and design changes

## Usage

Use the canonical cue `KLAATU BERADA NIKTO` to enter the controller from a consumer repo. Recognition is case-insensitive and may accept common alternate spellings for compatibility (for example `Klatu Berata Nicto`), but docs and examples should always use the canonical form. Start with `gort.md`. When the current state is known, read the matching state file and `context-compaction.md` before acting.

## Editing rule

Changes to `gort.md`, the state files, or compaction behavior must be backed by citations in `gort.citations.md`.
