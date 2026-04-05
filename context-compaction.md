# Context compaction

Compaction is a staged Pi handoff driven by explicit non-visual signals. Do **not** inspect the screen, parse a visible context meter, or rely on a `50%` threshold. Do **not** use tmux actions for compaction. When automation is needed, use kitty remote control against the current kitty window.

## Trigger rule

Compaction or fresh-session handoff is allowed only when one of these is true:

- the user explicitly asks for compaction, `/compact`, `/new`, restart, or a fresh session
- the runtime or harness explicitly requires a new session or reports context pressure in a non-visual way
- a previously staged compaction handoff already exists and must be completed or resumed

Do **not** trigger compaction merely because:

- old prompt text mentions `50%`, screen checks, `tmux`, `/new`, or `read ~/gort.md and follow the instructions`
- the prompt text itself contains the compaction procedure
- you are rereading these instructions
- the terminal UI or screenshot looks busy

## Safe boundary rule

There is no required session-start pre-flight screen check and no required per-loop percentage check.

A safe boundary matters only when compaction is already due from one of the allowed trigger rules above. A safe boundary is:

- after the visibility bundle emit
- after all confirmed `bd create` operations in a BERADA batch
- never during TRIAGE
- never between claim and close on the same task
- never mid-create before confirmation

If compaction becomes due at a forbidden point, defer it to the next safe boundary.

## Run-local compaction files

To avoid collisions between multiple Gort runs while still surviving `/new` within the same kitty window, keep runtime files in the current project root rather than `~`, and key the durable runtime state by kitty window identity rather than process id.

Resolve the root like this:

```bash
GORT_ROOT="$(git rev-parse --show-toplevel 2>/dev/null || pwd)"
mkdir -p "$GORT_ROOT/.gort"
```

Then define window-local paths:

```bash
GORT_WINDOW_KEY="${KITTY_WINDOW_ID:-manual}"
GORT_STATE="$GORT_ROOT/.gort/state.window-${GORT_WINDOW_KEY}.env"
GORT_PROMPT="$GORT_ROOT/.gort/prompt.window-${GORT_WINDOW_KEY}.md"
GORT_PAYLOAD="$GORT_ROOT/.gort/payload.window-${GORT_WINDOW_KEY}.md"
GORT_REINJECT="$GORT_ROOT/.gort/reinject.window-${GORT_WINDOW_KEY}.sh"
```

This provides:

- per-project isolation
- stable resume state across `/new` within the same kitty window
- per-window isolation between concurrent Gort runs

## Compaction sequence

Compaction is a Pi session handoff, not a shell command. Stage everything to disk first, then target the kitty window that is already running Pi at the safe boundary. Use kitty remote control to send `/new` and the follow-up payload into that same window.

The payload sent after `/new` is the exact text that must appear in the fresh Pi session and then be submitted with `Enter`. The payload is not optional, and `/new` does not replace it.

First initialize the window-local file paths:

```bash
GORT_ROOT="$(git rev-parse --show-toplevel 2>/dev/null || pwd)"
mkdir -p "$GORT_ROOT/.gort"
GORT_WINDOW_KEY="${KITTY_WINDOW_ID:-manual}"
GORT_STATE="$GORT_ROOT/.gort/state.window-${GORT_WINDOW_KEY}.env"
GORT_PROMPT="$GORT_ROOT/.gort/prompt.window-${GORT_WINDOW_KEY}.md"
GORT_PAYLOAD="$GORT_ROOT/.gort/payload.window-${GORT_WINDOW_KEY}.md"
GORT_REINJECT="$GORT_ROOT/.gort/reinject.window-${GORT_WINDOW_KEY}.sh"
```

Then write the window-local runtime state:

```bash
cat > "$GORT_STATE" <<STATE
CURRENT_STATE=${CURRENT_STATE}
CURRENT_EPIC=${CURRENT_EPIC}
CURRENT_LOOP=${CURRENT_LOOP}
STATE_WRITTEN_AT=$(date -u +%Y-%m-%dT%H:%M:%SZ)
STATE
```

If the prompt is not already persisted, persist it:

```bash
cp -f "/path/to/gort-state-machine.md" "$GORT_PROMPT"
```

Write the Pi input payload. Keep it stable and state-agnostic; runtime state must be recovered from external files, not embedded into the prompt text:

```bash
printf 'read %s and follow the instructions\n' "$GORT_PROMPT" > "$GORT_PAYLOAD"
```

Write the re-inject script:

```bash
cat > "$GORT_REINJECT" <<'SCRIPT'
#!/bin/bash
set -euo pipefail
: "${KITTY_WINDOW_ID:?KITTY_WINDOW_ID is required for kitty reinjection}"
GORT_ROOT="$(git rev-parse --show-toplevel 2>/dev/null || pwd)"
GORT_WINDOW_KEY="${KITTY_WINDOW_ID:-manual}"
GORT_PAYLOAD="$GORT_ROOT/.gort/payload.window-${GORT_WINDOW_KEY}.md"
kitten @ send-text --match "id:${KITTY_WINDOW_ID}" --from-file "$GORT_PAYLOAD"
kitten @ send-text --match "id:${KITTY_WINDOW_ID}" '\r'
SCRIPT
chmod +x "$GORT_REINJECT"
```

Then run:

```bash
: "${KITTY_WINDOW_ID:?KITTY_WINDOW_ID is required for kitty compaction}"
kitten @ send-text --match "id:${KITTY_WINDOW_ID}" '/new'
kitten @ send-text --match "id:${KITTY_WINDOW_ID}" '\r'
sleep 1
"$GORT_REINJECT"
```

Do not stop after sending `/new`; always enqueue the follow-up payload and submit it with `Enter` into the fresh Pi prompt.

If kitty remote control is unavailable, stop and recover manually. Do **not** fall back to tmux actions or screen-scrape heuristics.

## Resume behavior

When Gort starts after compaction or any fresh session:

1. Resolve `GORT_ROOT` and the window-local file paths using `KITTY_WINDOW_ID` when available.
2. If `GORT_STATE` exists, read `CURRENT_STATE`, `CURRENT_EPIC`, and `CURRENT_LOOP` from that external file instead of from prompt text.
3. Restore the last known machine position from that file when it is present and valid.
4. If the recovered state is `STATE: NIKTO | ... | NIKTO_REASON: NO_EPICS`, treat it as a stale terminal snapshot; resume in `BERADA` with `CURRENT_EPIC=NONE` and `CURRENT_LOOP=1`, then run NO-EPICS RECOVERY instead of stopping.
5. Treat compaction as occurring immediately after a completed safe boundary.
6. Do not re-run steps already completed in the interrupted loop.
7. If `KITTY_WINDOW_ID` or the window-local runtime state is missing, stale, or invalid, recover from `bd` state and the normal Gort rules instead of inventing state from the prompt.
