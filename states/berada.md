# STATE: BERADA

Goal: make the current epic execution-ready, or seed the next logical epic when none exists, then transition immediately.

## Execution cycle

1. Run `bd ready --json --limit 100`.
2. Inspect the current epic tree, current blockers, whether a current epic actually exists, whether the current or immediately preceding loop just completed meaningful durable work, and whether the current session is recovering without usable window-local runtime state.
3. If no current epic exists, run **NO-EPICS RECOVERY** before allowing terminal `NIKTO`:
   - confirm `bd ready --json --limit 100` is empty and perform an authoritative open-task check that inspects open / blocked issues, their dependency shape, and whether one blocked frontier still clearly defines the current workstream
   - inspect durable local evidence for the next logical workstream, in this order:
     1. window-local Gort runtime state under `$GORT_ROOT/.gort/`
     2. tracked source / docs / config changes from `git status --short`
     3. recent commits, repo docs, and nearby project instructions that indicate the active workstream
     4. the latest explicit user goal and any durable session notes already available locally
   - do not inspect shared Gort controller files (`/home/choza/projects/gort/gort.md`, `gort.citations.md`, `context-compaction.md`, or `states/*.md`) as evidence for what the target repo should do next; use repo/runtime evidence instead
   - ignore pure runtime noise unless it is itself the bug under investigation, including `.gort/`, `.beads/push-state.json`, capture bundles, caches, logs, and other generated artifacts
   - if the open-task check reveals one clear blocked frontier, recover `CURRENT_EPIC` from that existing frontier, keep working under it, and do not seed a duplicate replacement epic just because the frontier is currently blocked
   - if the evidence reveals unfinished or next-highest-value work beyond any recovered blocked frontier, create exactly one epic for that work plus the first create-ready child tasks needed to resume execution
   - when the repo is fresh or nearly empty and the user has already supplied a concrete product target, seed the first epic and first executable child directly instead of browsing generic command help or rediscovering standard `bd` operations
   - do not emit interim worklog narration such as `Inspecting task status`, `Exploring recent commits`, or similar prose while gathering that evidence; inspect silently and speak only with the next complete structured state block
   - during that first-epic seeding path, suppress visible thoughts or headings such as `Considering database tasks`, `Planning project structure`, and `Creating issues for transition`
   - do not run generic help commands such as `bd --help`, `bd create --help`, `bd update --help`, `bd epic --help`, `bd show --help`, or `bd children --help` merely to remember standard create/claim/show flows already specified by the controller
   - if the repo is truly quiescent after those checks, keep `EPIC: NONE` and continue to transition evaluation
   - do not call the repo quiescent if plausible meaningful follow-on work still exists but the next bounded epic is not yet justified; that case must route through `LOW_CONFIDENCE_NEXT_EPIC`, not `NO_EPICS`
4. If the current or immediately preceding loop just completed meaningful durable work, run **POST-COMPLETION CONTINUATION SCAN** before allowing terminal `NIKTO`:
   - inspect the most recent closed issues, recent commits, validation results, fresh `git status --short` or diff evidence, nearby repo docs, and the latest explicit user goal or durable session notes
   - look specifically for concrete follow-on work directly exposed by the completed change: regression protection, missing validation, cleanup needed to stabilize the result, docs or config updates needed to preserve the behavior, or adjacent hardening with a clear risk-reduction link
   - create exactly one follow-on epic only when the evidence supports a concrete next step with clear acceptance criteria
   - if only speculative or preference-dependent ideas remain, do not invent work; continue to transition evaluation so terminal handling can distinguish true quiescence from low-confidence next-step ambiguity
   - classify the result explicitly: no plausible meaningful follow-on work => quiescence candidate; plausible follow-on work with unresolved justification => `LOW_CONFIDENCE_NEXT_EPIC`
5. Determine why `KLAATU` cannot continue:
   - missing child tasks
   - task too large
   - dependency gap
   - missing risk-reducing intermediate
   - ambiguity requiring research
   - hierarchy/dependency conflation
   - missing acceptance parent or acceptance gate conflated with executable work
   - dependency cycle or no-ready-work structural stall
   - real external blocker
   - no current epic or no seeded epic yet
   - no concrete next epic can be justified with high confidence
6. If the only blocker is low confidence about the next epic:
   - treat this as the branch for cases where meaningful follow-on work still plausibly exists, but the next bounded epic cannot yet be justified with the current evidence
   - prepare a concise normalized summary of resolved facts, unresolved must-have stakeholder decisions, and delegated evidence questions
   - classify each unresolved item before asking anything else:
     - stakeholder decision → may require one focused user question
     - factual / ecosystem / implementation-order uncertainty → convert into research or decomposition work
   - if enough information already exists to define one bounded epic and the remaining uncertainty can be turned into child research or decomposition tasks, create that epic now instead of handing off to `NIKTO_REASON: LOW_CONFIDENCE_NEXT_EPIC`
   - do not hand off to `NO_EPICS` while that plausible follow-on branch still exists
   - only hand off to `LOW_CONFIDENCE_NEXT_EPIC` when a true stakeholder decision or evidence gap still blocks the next bounded epic
7. If ready work is empty but open blocked work remains:
   - recover or keep `CURRENT_EPIC` from the clearest still-open blocked frontier rather than leaving the machine at `EPIC: NONE`
   - on a fresh session, or whenever window-local runtime state is missing, stale, or invalid, run exactly one bounded blocker freshness / reduction pass before allowing `NIKTO_REASON: EXTERNAL_BLOCKER`
   - inspect the freshest blocker evidence first: issue notes/comments/timestamps, dependency shape, recent commits or validation artifacts, and repo-local instructions about researching under uncertainty or rechecking external facts
   - rerun the cheapest truthful local probe, repo-specific verification step, or research pass that could show the blocker is stale, partially reduced, or workaroundable
   - if that pass reveals a narrower reducer task, research task, decomposition step, or durable blocker-update action, create or update that work instead of parking in `NIKTO`
   - only when the blocker remains externally confirmed after that bounded pass, and BERADA still cannot create any reducer task or decomposition, may terminal `EXTERNAL_BLOCKER` handling proceed
8. If user-visible validation requires explicit approval of captures or other artifacts, create or preserve a long-lived acceptance parent for that outcome. Keep that parent open until explicit approval, and allow narrower child tasks to close independently.
9. Repair task-tree structure now when open work remains but `bd ready --json --limit 100` is empty:
   - separate acceptance gating from executable child work
   - use parent-child relations for decomposition only
   - use `blocks` / `blocked by` for true execution sequencing only
   - remove or rewrite cycles and blocker shapes that eliminate ready work
10. Create every create-ready task now under the current epic, inserting between the epic and existing work without restarting the list.
11. If a task is not create-ready, state exactly what must be clarified, research it, then create tasks from the result.
12. Make any durable task-tree or code changes needed to make the epic execution-ready.
13. If code changed in BERADA, commit it before leaving BERADA.
14. Apply the compaction handoff policy at the safe boundary using [../context-compaction.md](../context-compaction.md).
15. Evaluate transition guards immediately.

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

- one or more ready executable tasks now exist for current epic → transition to `KLAATU`, reset LOOP
- no current epic exists, but NO-EPICS RECOVERY created an epic with ready work → transition to `KLAATU`, reset LOOP
- no current epic exists, but NO-EPICS RECOVERY created an epic that still needs decomposition → remain in `BERADA` on that epic, reset LOOP
- POST-COMPLETION CONTINUATION SCAN created a follow-on epic with ready work → transition to `KLAATU`, reset LOOP
- POST-COMPLETION CONTINUATION SCAN created a follow-on epic that still needs decomposition → remain in `BERADA` on that epic, reset LOOP
- current epic is fully complete → advance to next epic, reset LOOP
- no further task creation or decomposition is possible because of a confirmed external blocker BERADA cannot reduce after the required blocked-frontier freshness / reduction pass → transition to `NIKTO`
- no epics remain only after NO-EPICS RECOVERY and POST-COMPLETION CONTINUATION SCAN found no plausible unfinished meaningful work or credible follow-on epic, repo quiescence was confirmed, and no unresolved next-step ambiguity remains → transition to `NIKTO` with `NIKTO_REASON: NO_EPICS`
- meaningful opportunities may remain, but no concrete next epic can be justified without subjective guidance or confidence beyond local evidence → transition to `NIKTO` with `NIKTO_REASON: LOW_CONFIDENCE_NEXT_EPIC`, carrying the normalized summary and smallest unresolved decision into the clarification protocol
