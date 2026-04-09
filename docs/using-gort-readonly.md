# Using Gort from another repository (read-only / consumer mode)

Use this guidance when the current work is happening in some other repository and this repo is being referenced only as the shared Gort controller/prompt pack.

## Authority and execution root

- The active consumer repository remains the execution root.
- The consumer repo's repo-root `AGENTS.md` stays authoritative when it exists.
- This Gort repo is shared controller logic, not the default worktree or Beads authority for consumer-repo work.
- Reading `/home/choza/projects/gort/gort.md` does **not** authorize reading or mutating `/home/choza/projects/gort/.beads`.

## Entry-point rule

- Prefer the canonical reinjection cue `KLAATU BERADA NIKTO` from the active consumer repo.
- Only reinject directly into `/home/choza/projects/gort/gort.md` when the active work itself is on this Gort repo.
- On fresh-context bootstrap, the first grounding read should come from the active repo's authoritative `AGENTS.md` when the current Gort action is already anchored there.
- Use `~/projects/AGENTS.md` only as a fallback when no more specific active-repo `AGENTS.md` is available.

## How to load Gort

- Start with [`../gort.md`](../gort.md).
- Load state files and `context-compaction.md` only as the root contract requires.
- Load exactly one mode file for the active run:
  - default: [`../modes/autonomy.md`](../modes/autonomy.md)
  - explicit tighter gating only: [`../modes/safe-mode.md`](../modes/safe-mode.md)

## Behavioral boundary

- Treat the active repository's Beads state, worktree, runtime files, and validation surface as authoritative for transient execution state.
- Do not switch repo authority to Gort just because Gort instructions were loaded.
- If the work requires changing Pi.dev/runtime implementation rather than Markdown prompt-pack behavior, record that boundary and hand the implementation to the owning runtime surface instead of editing this repo beyond its Markdown scope.
