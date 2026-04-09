# Editing Gort in this repository (write / maintainer mode)

Use this guidance when the active work itself is on `/home/choza/projects/gort` and you are changing the prompt pack or its supporting docs.

## Editing contract

- Treat this repo as a Markdown-only prompt-pack/documentation boundary.
- Do not patch Pi.dev source code, watchers, subagents, or runtime implementation from here.
- If the requested behavior would require non-Markdown runtime changes, document that limitation in repo docs and keep the fix inside Markdown prompt-pack/docs files only.

## Required evidence standard

- Act as a prompt-systems research engineer: optimize controller behavior with small, surgical edits backed by explicit evidence.
- Prefer the minimum change set that can plausibly fix the observed behavior while preserving invariants.
- Define the user goal and pass/fail criteria before changing prompts or state-machine files.
- Favor provable results over speculative elegance: validate with local evidence, diffs, and interactive Kitty/Pi smoke tests using the exact reinjection flow the user cares about.
- Treat prompt rules as checkable specifications. Prefer trace assertions over subjective "felt better" judgments.
- Use [`../EVALS.md`](../EVALS.md) as the scenario-based regression guide, and expand that corpus when a new real failure mode is discovered.
- For routing, terminal-state, resume, or bootstrap changes, include at least one adversarial or compatibility case in addition to the primary happy-path smoke.
- Treat prompt-pack edits as experiments: record what failed, what changed, and what evidence shows improvement.

## Research-first decision framing

- When local repo evidence is not enough to justify a Gort behavior change, do targeted web research on the interaction pattern you are proposing instead of relying on taste alone.
- If the user expresses a design preference or proposed fix, treat that as a hypothesis to test rather than a conclusion to adopt. Perform at least one explicit adversarial research pass that looks for reasons the preference may be suboptimal, over-broad, or unsafe.
- After that adversarial pass, summarize objective pushback succinctly before recommending a change.
- Do not ask preference-shaped questions when research, repo evidence, or runtime traces should determine the answer. Default to evidence-first recommendations.
- Reserve user questions for true stakeholder-owned choices only: authorization boundaries, scope/intent, risk tolerance, or acceptance decisions that evidence cannot settle. When a question is required, say why it is required.

## Required maintenance steps

- When editing `gort.md`, `context-compaction.md`, or `states/*.md`, update [`../gort.citations.md`](../gort.citations.md) with supporting evidence.
- Run the duplicate-line guard after Markdown-heavy edits:

```bash
python3 scripts/check_markdown_duplicates.py
```

- Run an interactive Kitty/Pi smoke test before claiming completion when the change affects Pi-facing runtime behavior or AGENTS-driven startup behavior.
