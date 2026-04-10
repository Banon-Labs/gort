# STATE: KLAATU

Goal: execute one ready task for the current epic per loop.

## Execution cycle

1. Run `bd ready --json --limit 100`.
2. Recover or confirm the current epic.
3. Select exactly one ready task for the current epic.
4. Run:

   ```bash
   bd update <id> --claim --json
   ```

5. Execute the task and any validation needed to prove it done.
6. If the task is complete, run:

   ```bash
   bd close <id> --reason "Done" --json
   ```

   and confirm close succeeded in the JSON response.
7. Run:

   ```bash
   git commit -m "<description> (<id>)"
   ```

   when there is a commit-worthy code change.
8. Run:

   ```bash
   /home/choza/projects/scripts/bd-visibility-bundle.sh --updated-id <id>
   ```

9. Apply the compaction handoff policy at the safe boundary using [../context-compaction.md](../context-compaction.md).
10. Increment LOOP.
11. Re-check ready tasks and repeat, applying checkpoint/pause behavior from the active mode file.

### Git commit normalization

Treat `git commit` reporting "nothing to commit" as **Success** if:

- the task was validly closed, and
- no tracked code change was required for completion.

## KLAATU transition guards

Evaluate after each cycle. Transition immediately on the first match:

- ready tasks still exist for current epic → repeat `KLAATU`
- no ready task exists for current epic, but current epic is not complete → transition to `BERADA`, reset LOOP
- current epic is complete → advance to next epic, reset LOOP, re-enter `KLAATU`
- all remaining work in current epic is blocked by a confirmed external, permission-bound, human-decision, missing-approval, missing-credential, or unavailable-external-dependency blocker that cannot be reduced locally, and no still-hot local implementation/debugging branch remains active for the same in-progress work → transition to `NIKTO`
- all remaining work is blocked but the blocker may be reduced by decomposition, research, dependency repair, or another local corrective action → transition to `BERADA`, reset LOOP
- no epics remain → transition to `NIKTO`
