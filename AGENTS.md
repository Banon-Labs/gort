# Gort Prompt Pack Instructions

This repository contains the shared Gort prompt pack and supporting documentation.

## Scope

- `gort.md`, `context-compaction.md`, and `states/*.md` are reusable controller instructions.
- This repository is **not** the default execution root for work happening in another repository.
- Consumer repositories should keep their own repo-root `AGENTS.md` authoritative and delegate here only for shared Gort controller logic.

## Entry-point rule

- When Gort is used from another repository, prefer reinjection text like `read AGENTS.md and follow the instructions` from that active repository.
- Only reinject directly into `/home/choza/projects/gort/gort.md` when the active work itself is on the Gort prompt-pack repository.
- Treat the active repository's Beads state, worktree, and runtime files as authoritative for transient execution state.

## Editing Gort

- When editing `gort.md`, `context-compaction.md`, or `states/*.md`, update `gort.citations.md` with supporting evidence.
- Keep Gort prompt entrypoints stable and state-agnostic; transient execution state should be recovered from external runtime sources, not embedded in reinjected prompt text.
