# Gort Prompt Pack Instructions

This repository contains the shared Gort prompt pack and supporting documentation.

## Scope

- `gort.md`, `context-compaction.md`, and `states/*.md` are reusable controller instructions.
- This repository is **not** the default execution root for work happening in another repository.
- Consumer repositories should keep their own repo-root `AGENTS.md` authoritative and delegate here only for shared Gort controller logic.

## Entry-point rule

- When Gort is used from another repository, prefer the exact reinjection cue `KLAATU BERADA NIKTO` from that active repository.
- Only reinject directly into `/home/choza/projects/gort/gort.md` when the active work itself is on the Gort prompt-pack repository.
- Treat the active repository's Beads state, worktree, and runtime files as authoritative for transient execution state.
- On fresh-context bootstrap, the first grounding `read` should come from the active repository's authoritative `AGENTS.md` when the current Gort action is already anchored to that repo/worktree; `~/projects/AGENTS.md` is only the fallback when no more specific active-repo authority is available.

- When this repo is referenced from another repository only as shared controller logic, that alone does **not** authorize reading or mutating `/home/choza/projects/gort/.beads`.
- Gort repo Beads becomes authoritative only after the active work explicitly switches to `/home/choza/projects/gort` or the user explicitly requests cross-repo migration/cleanup into this tracker.

## Editing Gort

- When editing `gort.md`, `context-compaction.md`, or `states/*.md`, update `gort.citations.md` with supporting evidence.

## Working style for Gort changes

- Act as a prompt-systems research engineer: optimize controller behavior with small, surgical edits backed by explicit evidence.
- Prefer the minimum change set that can plausibly fix the observed behavior while preserving existing invariants.
- Define the user goal and pass/fail criteria before changing prompts or state-machine files.
- Favor provable results over speculative elegance: validate with local evidence, diffs, and interactive Kitty/Pi smoke tests using the exact reinjection flow the user cares about.
- Treat prompt rules as checkable specifications. Prefer trace assertions over subjective "felt better" judgments.
- Use the scenario-based regression guidance in `EVALS.md` when evaluating Gort changes, and expand that scenario corpus when a new real failure mode is discovered.
- For routing, terminal-state, resume, or bootstrap changes, include at least one adversarial or compatibility case in addition to the primary happy-path smoke.
- When behavior and instructions diverge, align Gort with the user's operational goal rather than preserving a broken prior wording.
- Treat prompt-pack edits as experiments: record what failed, what changed, and what evidence shows improvement in `gort.citations.md`.
- When local repo evidence is not enough to justify a Gort behavior change, do targeted web research on the interaction pattern you are proposing and cite it in `gort.citations.md` rather than relying on taste alone.
- If the user expresses a design preference or proposed fix, treat that as a hypothesis to test rather than a conclusion to adopt. Perform at least one explicit adversarial research pass that looks for reasons the preference may be suboptimal, over-broad, or unsafe.
- After that adversarial pass, summarize any objective pushback calmly and succinctly before recommending a change. If the evidence supports a narrower or different rule than the user's preferred framing, prefer the evidence-backed correction and say so plainly.
- Do not preserve the user's exact framing when a smaller, more objective correction is better supported. Prefer the best supported rule, then explain why it differs.
- Avoid broad persona inflation or stylistic churn; improve reasoning quality through clearer rules, recovery paths, and verification gates.
- Be especially conservative about terminal states, autonomous recovery, resume behavior, and anything that can cause Gort to stop instead of continuing.
- Keep Gort prompt entrypoints stable and state-agnostic; transient execution state should be recovered from external runtime sources, not embedded in reinjected prompt text.
- Treat this repository as a prompt-pack/documentation boundary: do not change Pi.dev source code, watchers, subagents, or extension/runtime implementation from here.
- If a requested behavior would require Pi.dev or extension source changes, document the limitation and boundary in `AGENTS.md` or `README.md` and keep the fix inside Markdown prompt-pack/docs files only.
- When external frameworks or benchmarks are helpful, use them as reference material; the authoritative evals for this repo are still the local Kitty/Pi scenario traces described in `EVALS.md`.

## Artifact readback for milestone reporting

- When reporting a meaningful milestone, checkpoint, or smoke-test result that depends on a local artifact, prefer reading that artifact back in-session before citing it.
- For text-like artifacts (`.txt`, `.md`, `.json`, ANSI captures, logs), use the `read` tool and quote the key lines that support the claim.
- For images, use `read` on the image path when the harness can surface it inline as an attachment.
- For large artifacts, read the relevant excerpt and still include the full artifact path.
- Do not reference a local artifact path alone when a short inline readback would make the evidence easier for the user to inspect immediately.

<!-- BEGIN BEADS INTEGRATION -->
## Issue Tracking with bd (beads)

**IMPORTANT**: This project uses **bd (beads)** for ALL issue tracking. Do NOT use markdown TODOs, task lists, or other tracking methods.

### Why bd?

- Dependency-aware: Track blockers and relationships between issues
- Git-friendly: Dolt-powered version control with native sync
- Agent-optimized: JSON output, ready work detection, discovered-from links
- Prevents duplicate tracking systems and confusion

### Quick Start

**Check for ready work:**

```bash
bd ready --json
```

**Create new issues:**

```bash
bd create "Issue title" --description="Detailed context" -t bug|feature|task -p 0-4 --json
bd create "Issue title" --description="What this issue is about" -p 1 --deps discovered-from:bd-123 --json
```

**Claim and update:**

```bash
bd update <id> --claim --json
bd update bd-42 --priority 1 --json
```

**Complete work:**

```bash
bd close bd-42 --reason "Completed" --json
```

### Issue Types

- `bug` - Something broken
- `feature` - New functionality
- `task` - Work item (tests, docs, refactoring)
- `epic` - Large feature with subtasks
- `chore` - Maintenance (dependencies, tooling)

### Priorities

- `0` - Critical (security, data loss, broken builds)
- `1` - High (major features, important bugs)
- `2` - Medium (default, nice-to-have)
- `3` - Low (polish, optimization)
- `4` - Backlog (future ideas)

### Workflow for AI Agents

1. **Check ready work**: `bd ready` shows unblocked issues
2. **Claim your task atomically**: `bd update <id> --claim`
3. **Work on it**: Implement, test, document
4. **Discover new work?** Create linked issue:
   - `bd create "Found bug" --description="Details about what was found" -p 1 --deps discovered-from:<parent-id>`
5. **Complete**: `bd close <id> --reason "Done"`

### Auto-Sync

bd automatically syncs via Dolt:

- Each write auto-commits to Dolt history
- Use `bd dolt push`/`bd dolt pull` for remote sync
- No manual export/import needed!

### Important Rules

- ✅ Use bd for ALL task tracking
- ✅ Always use `--json` flag for programmatic use
- ✅ Link discovered work with `discovered-from` dependencies
- ✅ Check `bd ready` before asking "what should I work on?"
- ❌ Do NOT create markdown TODO lists
- ❌ Do NOT use external issue trackers
- ❌ Do NOT duplicate tracking systems

For more details, see README.md and docs/QUICKSTART.md.

## Landing the Plane (Session Completion)

**When ending a work session**, you MUST complete ALL steps below. Work is NOT complete until `git push` succeeds.

**MANDATORY WORKFLOW:**

1. **File issues for remaining work** - Create issues for anything that needs follow-up
2. **Run quality gates** (if code changed) - Tests, linters, builds
3. **Update issue status** - Close finished work, update in-progress items
4. **PUSH TO REMOTE** - This is MANDATORY:
   ```bash
   git pull --rebase
   bd dolt push
   git push
   git status  # MUST show "up to date with origin"
   ```
5. **Clean up** - Clear stashes, prune remote branches
6. **Verify** - All changes committed AND pushed
7. **Hand off** - Provide context for next session

**CRITICAL RULES:**
- Work is NOT complete until `git push` succeeds
- NEVER stop before pushing - that leaves work stranded locally
- NEVER say "ready to push when you are" - YOU must push
- If push fails, resolve and retry until it succeeds

<!-- END BEADS INTEGRATION -->
