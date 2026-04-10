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

## Pre-edit proof gate for Gort changes

Before changing `gort.md`, `context-compaction.md`, `modes/*.md`, or `states/*.md`, build the smallest evidence chain that answers all of the following:

1. **Which exact session failed?** Record the Pi session jsonl path first. Prefer locating the failure from a distinctive user-provided snippet rather than starting from Kitty chrome.
2. **What instruction source did the failing session actually follow?** Prove whether it read the active repo `AGENTS.md`, live `gort.md`, a cached `.gort/prompt...` snapshot, mode files, or other runtime-state files. Do not assume a stale prompt replay or a live-Gort failure without trace evidence.
3. **What part is portable vs repo-coupled?** Reproduce in a controlled `/tmp` sandbox repo before broad Gort edits when the observed behavior may be caused by a consumer repo's Beads tree, runtime files, or task topology.
4. **Was the failure actually reproduced?** Attribution alone is not enough. Before editing Gort, prefer at least one fresh-session repro with explicit pass/fail criteria and saved artifacts.
5. **What is the minimal justified fix surface?** Classify the issue before editing:
   - stale prompt/runtime plumbing
   - live Gort contract failure
   - mixed-source failure
   - consumer-repo-specific interaction

Use this decision rule:

- **Edit Gort** when a failing session is shown to follow live Gort instructions and the behavior is reproduced or otherwise clearly contradicts the live contract.
- **Fix prompt/runtime plumbing first** when cached prompt snapshots, reinjection payloads, or runtime-state files explain the failure better than the live prompt pack.
- **Use a richer sandbox before broad edits** when a minimal `/tmp` repro proves only a portable bootstrap leak but not the higher-level continuation failure you are trying to fix.
- **Stop widening the sandbox and switch to real-session continuity diffing** when progressively richer `/tmp` repros still collapse to `NIKTO` while the real consumer session shows repeated visible `STATE: KLAATU ... Executing now ...` turns on one still-hot in-progress branch. In that case, treat long-lived issue-branch continuity, unresolved multi-file implementation work, and real runtime/tool failure carry-over as the leading hypothesis instead of inventing more synthetic local topology.

### Recommended evidence bundle

For every Gort behavior change, prefer collecting and citing:

- exact failing session jsonl path
- exact repro session jsonl path
- sandbox root (for example `/tmp/<name>-fix`)
- relevant Kitty ANSI captures before/after injection
- the exact trigger text used
- a short note of what reproduced and what did not
- if the exact visible loop did **not** reproduce, a short continuity diff note stating what persisted in the real session across loop turns (for example the same in-progress issue, the same hot code path, repeated edits across the same files, or intermediate tool/edit failures that kept the branch locally executable)

## Required maintenance steps

- When editing `gort.md`, `context-compaction.md`, `modes/*.md`, or `states/*.md`, update [`../gort.citations.md`](../gort.citations.md) with supporting evidence.
- Run the duplicate-line guard after Markdown-heavy edits:

```bash
python3 scripts/check_markdown_duplicates.py
```

- Run an interactive Kitty/Pi smoke test before claiming completion when the change affects Pi-facing runtime behavior or AGENTS-driven startup behavior.
