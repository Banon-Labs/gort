# Gort

Gort is a state-machine prompt pack for autonomous project execution.

## Layout

- `gort.md` — canonical root contract, global invariants, routing, and shared procedures
- `states/klaatu.md` — execute one ready task for the current epic per loop
- `states/berada.md` — make the current epic execution-ready
- `states/nikto.md` — terminal halt behavior and allowed entry reasons
- `context-compaction.md` — kitty/Pi compaction and resume procedure
- `gort.citations.md` — evidence log for edits and design changes

## Usage

Use the canonical cue `KLAATU BERADA NIKTO` to enter the controller from a consumer repo. Recognition is case-insensitive and may accept common alternate spellings for compatibility (for example `Klatu Berata Nicto`), but docs and examples should always use the canonical form. Start with `gort.md`. When the current state is known, read the matching state file and `context-compaction.md` before acting.

## Validation

Run the lightweight duplicate-line guard before finishing Markdown-heavy edits:

```bash
python3 scripts/check_markdown_duplicates.py
```

The checker fails on accidental adjacent duplicate non-empty Markdown lines outside fenced code blocks.

## Editing rule

Changes to `gort.md`, the state files, or compaction behavior must be backed by citations in `gort.citations.md`.

This repository is intentionally Markdown-only prompt-pack scope. Do not use it to patch Pi.dev source code, watchers, subagents, or other runtime implementation. If a requested behavior would require source changes outside this prompt pack, document that limitation here or in `AGENTS.md` and keep this repo's changes inside Markdown prompt-pack/docs files.
