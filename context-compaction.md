# Context compaction

Gort runs inside tmux and can inspect its own pane. After every safe loop boundary, check context usage and compact if needed. This check is required.

## Session-start pre-flight context check

Immediately after session start or resume, and before entering `KLATU` or `BERADA`, run the same pane-capture check used at safe boundaries.

- If the authoritative context percentage is above `50`, run the compaction sequence immediately.
- If the parse is missing, ambiguous, stale, or otherwise suspect, fail closed and compact immediately.
- This pre-flight check happens in addition to the safe-boundary checks; it does not replace them.

## Safe boundary rule

A safe boundary is:

- after the visibility bundle emit
- after all confirmed `bd create` operations in a BERADA batch
- never during TRIAGE
- never between claim and close on the same task
- never mid-create before confirmation

If a compaction check becomes due at a forbidden point, defer it to the next safe boundary.

## Run-local compaction files

To avoid collisions between multiple Gort runs while still surviving `/new` within the same tmux pane, keep runtime files in the current project root rather than `~`, and key the durable runtime state by pane identity rather than process id.

Resolve the root like this:

```bash
GORT_ROOT="$(git rev-parse --show-toplevel 2>/dev/null || pwd)"
mkdir -p "$GORT_ROOT/.gort"
```

Then define pane-local paths:

```bash
GORT_PANE_KEY="${TMUX_PANE##*.}"
GORT_STATE="$GORT_ROOT/.gort/state.pane-${GORT_PANE_KEY}.env"
GORT_PROMPT="$GORT_ROOT/.gort/prompt.pane-${GORT_PANE_KEY}.md"
GORT_PAYLOAD="$GORT_ROOT/.gort/payload.pane-${GORT_PANE_KEY}.md"
GORT_REINJECT="$GORT_ROOT/.gort/reinject.pane-${GORT_PANE_KEY}.sh"
```

This provides:

- per-project isolation
- stable resume state across `/new` within the same pane
- per-pane isolation between concurrent Gort runs

## Per-loop context check

At a safe boundary, run:

```bash
PANE_TEXT=$(tmux capture-pane -p -t "$TMUX_PANE")
CONTEXT_PCT=$(echo "$PANE_TEXT" | grep -oP '\d+(?=%)' | tail -1)
```

If `CONTEXT_PCT` is greater than `50`, run the compaction sequence before continuing.

### Compaction trigger rule

Only the authoritative percentage captured from the current tmux pane may trigger compaction.

The `/new` sequence is the **action** taken after the threshold/parsing rules say to compact. It is **not** itself a trigger.

Do **not** trigger compaction merely because:

- the user mentions `/new`, old compaction wording, `tmux`, or `read ~/gort.md and follow the instructions`
- the prompt text itself contains the compaction procedure
- you are rereading these instructions

Compaction is triggered only when the pre-flight or safe-boundary pane capture shows the authoritative context percentage above the threshold, or when the parse must fail closed.

### Fail-closed parsing rule

The simple `tail -1` percentage extraction is only acceptable when it is known to correspond to the live context meter.

If the pane capture is missing the context meter, ambiguous, stale, or otherwise not trustworthy, you must **fail closed**:

- do not assume the low parsed number is correct
- do not keep working for multiple safe boundaries on a suspect parse
- stage and run the compaction sequence immediately at the next safe boundary

Treat the parse as suspect when any of these is true:

- no percentage is captured
- you cannot verify which percentage is the context meter
- the UI layout changed
- the extracted number is implausibly low relative to the visible workload and remains so across repeated safe boundaries
- a human reports that actual context usage is already above threshold

### UI parsing note

The extracted percentage is only valid if the last percentage shown in the pane is the authoritative context-usage indicator. If the UI format changes, or if reality conflicts with the extracted number, update this extraction rule or compact immediately instead of trusting the stale parse.

## Compaction sequence

Compaction is a Pi session handoff, not a shell command. Stage everything to disk first, then target the tmux pane that is already running Pi at the safe boundary. Send `/new` to the Pi prompt in that pane; do **not** type Pi slash commands at a shell prompt.

This follows tmux `send-keys` best practice: always target the exact pane, send literal text explicitly, and keep shell commands separate from application commands.

The payload sent after `/new` is the exact text that must appear in the fresh Pi session and then be submitted with `Enter`. The payload is not optional, and `/new` does not replace it.

First initialize the pane-local file paths:

```bash
GORT_ROOT="$(git rev-parse --show-toplevel 2>/dev/null || pwd)"
mkdir -p "$GORT_ROOT/.gort"
GORT_PANE_KEY="${TMUX_PANE##*.}"
GORT_STATE="$GORT_ROOT/.gort/state.pane-${GORT_PANE_KEY}.env"
GORT_PROMPT="$GORT_ROOT/.gort/prompt.pane-${GORT_PANE_KEY}.md"
GORT_PAYLOAD="$GORT_ROOT/.gort/payload.pane-${GORT_PANE_KEY}.md"
GORT_REINJECT="$GORT_ROOT/.gort/reinject.pane-${GORT_PANE_KEY}.sh"
```

Then write the pane-local runtime state:

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
cat > "$GORT_REINJECT" <<SCRIPT
#!/bin/bash
set -euo pipefail
PAYLOAD=$(cat "$GORT_PAYLOAD")
tmux send-keys -t "$TMUX_PANE" -l "$PAYLOAD"
tmux send-keys -t "$TMUX_PANE" Enter
SCRIPT
chmod +x "$GORT_REINJECT"
```

Then run:

```bash
tmux send-keys -t "$TMUX_PANE" -l "/new"
tmux send-keys -t "$TMUX_PANE" Enter
sleep 1
"$GORT_REINJECT"
```

Do not stop after sending `/new`; always enqueue the follow-up payload and submit it with `Enter` into the fresh Pi prompt.

If the pane is no longer showing Pi, stop and recover manually; never inject `/new` into a shell.

## Resume behavior

When Gort starts after compaction or any fresh session:

1. Resolve `GORT_ROOT` and the pane-local file paths using the current `TMUX_PANE`.
2. If `GORT_STATE` exists, read `CURRENT_STATE`, `CURRENT_EPIC`, and `CURRENT_LOOP` from that external file instead of from prompt text.
3. Restore the last known machine position from that file when it is present and valid.
4. Treat compaction as occurring immediately after a completed safe boundary.
5. Do not re-run steps already completed in the interrupted loop.
6. If the pane-local runtime state is missing, stale, or invalid, recover from `bd` state and the normal Gort rules instead of inventing state from the prompt.
