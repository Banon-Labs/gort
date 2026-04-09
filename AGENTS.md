# Gort Prompt Pack Instructions

This repository contains the shared Gort prompt pack and supporting documentation.

## Scope

- `gort.md`, `context-compaction.md`, and `states/*.md` are reusable controller instructions.
- This repository is **not** the default execution root for work happening in another repository.
- Consumer repositories should keep their own repo-root `AGENTS.md` authoritative and delegate here only for shared Gort controller logic.

## Instruction split

Use the split guidance below instead of mixing consumer/read-only and maintainer/write instructions in one long file.

- **Using Gort from another repository (read-only / consumer mode):** [`./docs/using-gort-readonly.md`](./docs/using-gort-readonly.md)
- **Editing Gort in this repository (write / maintainer mode):** [`./docs/editing-gort-write.md`](./docs/editing-gort-write.md)

If the current task is to modify files in `/home/choza/projects/gort`, read the write/maintainer guide. If this repo is only being loaded as shared controller logic while work continues somewhere else, read the read-only/consumer guide.

## Repo-wide invariants

- When Gort is used from another repository, prefer the exact reinjection cue `KLAATU BERADA NIKTO` from that active repository.
- Only reinject directly into `/home/choza/projects/gort/gort.md` when the active work itself is on the Gort prompt-pack repository.
- Treat the active repository's Beads state, worktree, and runtime files as authoritative for transient execution state.
- Reading this repo as shared controller logic does **not** authorize reading or mutating `/home/choza/projects/gort/.beads`.
- If the work requires changing Pi.dev/runtime implementation rather than Markdown prompt-pack behavior, document that boundary and keep this repo's changes inside Markdown prompt-pack/docs files.

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

**When ending a work session**, complete the repo work, update/close the relevant `bd` issue, and sync Beads/Dolt as allowed by workspace policy.

<!-- END BEADS INTEGRATION -->
