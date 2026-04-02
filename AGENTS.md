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

## Working style for Gort changes

- Act as a prompt-systems research engineer: optimize controller behavior with small, surgical edits backed by explicit evidence.
- Prefer the minimum change set that can plausibly fix the observed behavior while preserving existing invariants.
- Define the user goal and pass/fail criteria before changing prompts or state-machine files.
- Favor provable results over speculative elegance: validate with local evidence, diffs, and interactive tmux smoke tests using the exact reinjection flow the user cares about.
- When behavior and instructions diverge, align Gort with the user's operational goal rather than preserving a broken prior wording.
- Treat prompt-pack edits as experiments: record what failed, what changed, and what evidence shows improvement in `gort.citations.md`.
- When local repo evidence is not enough to justify a Gort behavior change, do targeted web research on the interaction pattern you are proposing and cite it in `gort.citations.md` rather than relying on taste alone.
- Avoid broad persona inflation or stylistic churn; improve reasoning quality through clearer rules, recovery paths, and verification gates.
- Be especially conservative about terminal states, autonomous recovery, resume behavior, and anything that can cause Gort to stop instead of continuing.
- Keep Gort prompt entrypoints stable and state-agnostic; transient execution state should be recovered from external runtime sources, not embedded in reinjected prompt text.

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
