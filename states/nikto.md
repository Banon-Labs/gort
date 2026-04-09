# STATE: NIKTO

Terminal state. `NO_EPICS` means true completion/quiescence. `LOW_CONFIDENCE_NEXT_EPIC` is the non-quiescent uncertainty branch and runs a bounded clarification/research protocol before final stop.

## On entry

1. Run:

   ```bash
   bd dolt push
   ```

2. If `NIKTO_REASON` is `LOW_CONFIDENCE_NEXT_EPIC`, run the **LOW-CONFIDENCE NEXT-EPIC PROTOCOL** before emitting the final stop summary.
3. If that protocol gathers enough information to define one bounded next epic or ticket with acceptance criteria, transition immediately to `BERADA` with `CURRENT_EPIC=NONE` and `LOOP=1` instead of stopping.
4. If `NIKTO_REASON` is `NO_EPICS`, emit one terse completion/quiescence summary only.
5. If `NIKTO_REASON` is `LOW_CONFIDENCE_NEXT_EPIC`, emit a terse uncertainty summary naming the smallest remaining decision or evidence gap.
6. If the visible stop summary mentions plausible meaningful follow-on work, unresolved next-step ambiguity, or a smallest remaining decision, the reason may not be `NO_EPICS`.
7. Include the `NIKTO_REASON`.
8. Stop.

## NIKTO entry rule

Enter `NIKTO` only when one of these is true:

| Rule | Condition | NIKTO_REASON |
|---|---|---|
| 1 | No epics remain after a fresh `bd ready --json --limit 100`, an authoritative open-task check, a BERADA no-epics recovery pass, a post-completion continuation scan, confirmed repo quiescence, and confirmation that no plausible unfinished meaningful work or unresolved next-step ambiguity remains | `NO_EPICS` |
| 2 | Permanent error | `PERMANENT_ERROR: <detail>` |
| 3 | `bd` unavailable after 8 classified transient retries | `BD_UNAVAILABLE` |
| 4 | LOOP exceeded 10 in one state without progress | `LOOP_EXCEEDED: <state>` |
| 5 | All remaining work blocked by a confirmed external blocker that BERADA cannot reduce after the required blocked-frontier freshness / reduction pass | `EXTERNAL_BLOCKER: <detail>` |
| 6 | Meaningful follow-on work may exist, but no concrete next epic can be justified without subjective guidance or higher-confidence evidence | `LOW_CONFIDENCE_NEXT_EPIC` |

## Terminal reason exclusivity

- `NO_EPICS` and `LOW_CONFIDENCE_NEXT_EPIC` are mutually exclusive.
- `NO_EPICS` means the machine has finished recovery/continuation scanning and found no plausible meaningful follow-on work.
- `LOW_CONFIDENCE_NEXT_EPIC` means plausible meaningful follow-on work still exists, but the next bounded epic cannot yet be justified.
- Therefore, a visible `NO_EPICS` summary may not speculate about possible next work, and any visible uncertainty about follow-on work must route through `LOW_CONFIDENCE_NEXT_EPIC` instead.

## LOW-CONFIDENCE NEXT-EPIC PROTOCOL

Use this protocol only when `NIKTO_REASON` is `LOW_CONFIDENCE_NEXT_EPIC`.

If the user explicitly says you are already in low-confidence next-epic mode, or provides normalized next-epic constraints and asks for exactly one stakeholder question, treat that as an active protocol invocation for the current turn.

- The next action must be the structured low-confidence turn itself.
- If that invocation arrives after bootstrap or startup work has already begun in the current session, discard the pending startup plan immediately and switch straight to the structured low-confidence turn.
- Do not rerun session-start bootstrap, `bd prime`, compaction-policy reads, `context-compaction.md`, `states/klaatu.md`, `states/berada.md`, `states/nikto.md`, other controller/state-file reads, or broad repo-triage before producing that turn unless an explicit non-visual compaction request or runtime signal is already known to require immediate handoff.
- Do not insert any file reads, shell commands, or visible reasoning steps between the explicit low-confidence invocation and the first structured low-confidence turn.

1. Before asking anything, classify the missing uncertainty:
   - stakeholder decision: scope, preference, risk tolerance, legal boundary, acceptance rule
   - delegated evidence question: factual, ecosystem, reverse-engineering, implementation-order, or research-planning uncertainty
2. Ask the user only for stakeholder decisions. Handle delegated evidence questions through research or internal planning instead of asking the user to micromanage the next research step.
3. If the user answers with delegation language such as “if research supports it,” “you’ll need to research that,” “we need to figure that out,” or equivalent, mark that branch delegated to evidence and stop asking preference-shaped follow-ups in that branch.
4. Ask one focused question at a time, and say why the answer matters.
5. A “single stakeholder question” must resolve one decision axis only. Do not bundle multiple axes such as target selection + runtime/platform + license policy + mod/plugin allowance into one prompt.
6. Prefer the smallest unresolved stakeholder decision that unlocks the next bounded epic. If one narrower decision would unlock the epic shape, ask that instead of a broader catch-all target-selection question.
7. Before asking a stakeholder question, normalize the known constraints and identify the single highest-information unresolved stakeholder decision. Do not fall back to a generic product-priority question when the conversation already contains a narrower domain-specific unresolved decision.
8. Use skip logic: ask only unanswered must-have questions; skip categories the user already resolved.
9. After each answer, normalize the current source of truth in a short summary. The latest explicit user answer overrides earlier draft heuristics.
10. When already in `LOW_CONFIDENCE_NEXT_EPIC`, do not bounce back into general repo triage before the next structured turn. Do not run `bd prime`, `bd ready`, or broad readiness discovery ahead of the next question unless the user explicitly asked for status verification or the missing durable state is truly required to justify the next bounded epic.
11. If durable-state verification is truly needed, keep it minimal and do not surface the verification chatter before the next structured turn unless the verification itself changes the question, research branch, or synthesis decision.
12. If the user is unsure, recommend a simple default or present 2–3 bounded options instead of forcing open-ended brainstorming.
13. If the missing uncertainty is factual or externally verifiable, switch to research instead of asking the user to guess.
14. Apply continuation/pause behavior from the active mode file. Do not mix autonomy-mode and safe-mode checkpoint semantics in this file.
15. Update the NIKTO header on every questionnaire turn with truthful adaptive-status fields:
   - `QMODE=CLARIFY` while asking a stakeholder question
   - `QMODE=RESEARCH` while gathering delegated factual evidence
   - `QMODE=SYNTHESIZE` once enough is known to define the next bounded epic or ticket
   - `QSTEP=<asked>/<budget>` using the current stakeholder-question count against the current clarification budget
   - `QVALUE=GO|MAYBE|NO_GO` based on whether another stakeholder question is still likely to add material value
   - `NEXT=ASK|RESEARCH|BERADA|STOP` for the most likely immediate transition
   - if the visible body contains any stakeholder question, `NEXT` must be `ASK`
   - the question label is exactly `Next question:`; do not substitute `Stakeholder question:` or other variants
   - if the current visible turn includes a stakeholder question, `QSTEP` must count that question already; do not show `0/<budget>` while actively asking the first question
   - `NEXT=ASK` is allowed only when `QMODE=CLARIFY` and `QVALUE` is `GO` or `MAYBE`
   - `QVALUE=NO_GO` forbids `NEXT=ASK`; the next move must be `RESEARCH`, `BERADA`, or `STOP`
   - if `NEXT=ASK`, the visible body must include a normalized summary, `Next question:`, exactly one focused stakeholder question, and `I’m asking because ...`
   - if `NEXT` is not `ASK`, do not emit `Next question:`
16. Do not show a fake `% complete` for adaptive questioning when the remaining question count is not actually known.
17. Do not ask planning-shaped questions such as “Should my next research pass focus on … ?” or “Should I investigate X before Y?” unless the user explicitly asked to control research order.
18. After each answer or research result, run a sufficiency check:
   - if enough information exists to define one bounded next epic or ticket with acceptance criteria, and the remaining uncertainty can be expressed as child research or decomposition tasks, stop questioning and transition to `BERADA`
   - otherwise continue only with the single highest-information unresolved stakeholder question
19. If 3 consecutive clarification questions fail to materially reduce uncertainty, stop the questionnaire, summarize what is known, identify the smallest remaining stakeholder decision, and either present bounded options or remain terminal in `LOW_CONFIDENCE_NEXT_EPIC`.
20. Questionnaire turns must stay terse and structured: optional normalized summary, then `Next question:`, then exactly one focused question, then `I’m asking because ...`.
21. The first user-visible turn after any resume, new user answer, or research result must be one of these exact shapes only:
   - header + normalized summary + one stakeholder question
   - header + normalized summary + explicit switch to research because the remaining uncertainty is factual or delegated to evidence
   - header + normalized summary + explicit transition to `BERADA` because enough is known to synthesize
22. Do not emit any other visible preamble before that first structured turn.
23. If any setup narration or other noncompliant preamble would be emitted, suppress it internally and continue until a compliant first structured turn is ready. If any noncompliant preamble slips out anyway, treat it as a protocol failure and immediately replace it with the compliant structured turn rather than continuing the preamble.
24. Do not emit internal meta-commentary such as “Framing questions,” “Planning content retrieval,” or similar reasoning traces.

## Forbidden NIKTO triggers

Never enter `NIKTO` because:

- no ready task exists
- all tasks are blocked but may be reduced locally
- planning is needed
- current epic appears empty before recovery or planning
- intermediate tasks have not yet been created
- all Beads issues are closed but durable local work still needs to be converted into a new epic
- a stale `STATE: NIKTO | ... | NIKTO_REASON: NO_EPICS` snapshot was merely resumed at session start
- an epic just completed, but BERADA has not yet run the post-completion continuation scan
- a fresh session recovered only a blocked Beads frontier, but BERADA has not yet run the required blocker freshness / reduction pass for that frontier
- enough information already exists to define one bounded next epic or ticket, but the clarification protocol has not yet transitioned back to `BERADA`
- the remaining uncertainty is factual or researchable and has already been delegated to evidence, but the protocol has not yet converted it into research or child tasks
- a command failed before classification and TRIAGE routing was attempted
