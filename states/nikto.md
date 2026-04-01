# STATE: NIKTO

Terminal state.

## On entry

1. Run:

   ```bash
   bd dolt push
   ```

2. Emit one terse summary of completed work.
3. Include the `NIKTO_REASON`.
4. Stop.

## NIKTO entry rule

Enter `NIKTO` only when one of these is true:

| Rule | Condition | NIKTO_REASON |
|---|---|---|
| 1 | No epics remain, confirmed by fresh `bd ready --json --limit 100` and authoritative open-task check | `NO_EPICS` |
| 2 | Permanent error | `PERMANENT_ERROR: <detail>` |
| 3 | `bd` unavailable after 8 classified transient retries | `BD_UNAVAILABLE` |
| 4 | LOOP exceeded 10 in one state without progress | `LOOP_EXCEEDED: <state>` |
| 5 | All remaining work blocked by a confirmed external blocker that BERADA cannot reduce | `EXTERNAL_BLOCKER: <detail>` |

## Forbidden NIKTO triggers

Never enter `NIKTO` because:

- no ready task exists
- all tasks are blocked but may be reduced locally
- planning is needed
- current epic appears empty before recovery or planning
- intermediate tasks have not yet been created
- a command failed before classification and TRIAGE routing was attempted
