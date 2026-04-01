# STATE: BERADA

Goal: make the current epic execution-ready, then transition immediately.

## Execution cycle

1. Run `bd ready --json --limit 100`.
2. Inspect the current epic tree and current blockers.
3. Determine why `KLATU` cannot continue:
   - missing child tasks
   - task too large
   - dependency gap
   - missing risk-reducing intermediate
   - ambiguity requiring research
   - hierarchy/dependency conflation
   - missing acceptance parent or acceptance gate conflated with executable work
   - dependency cycle or no-ready-work structural stall
   - real external blocker
4. Identify splits, redundancies, missing intermediates, and any task-tree shape that leaves open work with no ready executable task.
5. If user-visible validation requires explicit approval of captures or other artifacts, create or preserve a long-lived acceptance parent for that outcome. Keep that parent open until explicit approval, and allow narrower child tasks to close independently.
6. Repair task-tree structure now when open work remains but `bd ready --json --limit 100` is empty:
   - separate acceptance gating from executable child work
   - use parent-child relations for decomposition only
   - use `blocks` / `blocked by` for true execution sequencing only
   - remove or rewrite cycles and blocker shapes that eliminate ready work
7. Create every create-ready task now under the current epic, inserting between the epic and existing work without restarting the list.
8. If a task is not create-ready, state exactly what must be clarified, research it, then create tasks from the result.
9. Make any durable task-tree or code changes needed to make the epic execution-ready.
10. If code changed in BERADA, commit it before leaving BERADA.
11. Perform the context-compaction check at the safe boundary using [../context-compaction.md](../context-compaction.md).
12. Evaluate transition guards immediately.

### BERADA may perform durable work

BERADA may make durable changes including:

- `bd create`
- `bd update`
- dependency or blocker relation updates
- code edits
- validation runs
- commits

If only `bd` state changed, the `bd` write itself is sufficient durable state. No extra manual git commit is required unless the workflow explicitly requires it.

## BERADA transition guards

Evaluate after each cycle. Transition immediately on the first match:

- one or more ready executable tasks now exist for current epic → transition to `KLATU`, reset LOOP
- current epic is fully complete → advance to next epic, reset LOOP
- no further task creation or decomposition is possible because of a confirmed external blocker BERADA cannot reduce → transition to `NIKTO`
- no epics remain → transition to `NIKTO`
