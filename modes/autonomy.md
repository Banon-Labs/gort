# Mode: autonomy

Load this file by default.

Use autonomy mode when the user or repo-local policy has **not** explicitly requested tighter approval/checkpoint behavior.

## Core meaning

- Continue across `KLAATU` / `BERADA` loops, decomposition, follow-on reducer tasks, and research until `NIKTO` or a real hard boundary.
- Treat visibility bundles, checkpoints, compaction, session persistence, and other resumability/evidence mechanisms as **non-halting by default**.
- Ask the user only for true stakeholder-owned decisions: scope, acceptance, risk tolerance, explicit artifact approval, or high-risk / irreversible / permission-bound actions that policy already marks as human-gated.
- If the next uncertainty is factual, researchable, or decomposable into a smaller reducer task, stay autonomous and keep moving.

## Structured-output rule

- A non-terminal structured `STATE:` update may not end the turn while executable next work already exists and no explicit approval gate, compaction handoff, or hard terminal condition is active.
- If a block would merely say `Next:` / `Next move:` and executable work is ready, suppress that block and keep executing.

## Visibility / checkpoint rule

- The visibility bundle emit is an observability artifact, not a halt signal.
- After a visibility bundle or other checkpoint/resumability emit, continue autonomously unless a compaction handoff, explicit approval gate, or hard terminal condition is already active.
- Do not treat decomposition checkpoints or visibility artifacts as permission to stop; use them to preserve autonomous continuity.

## Per-state implications

### KLAATU

- Re-check ready tasks and repeat without waiting for routine user confirmation unless an explicit approval gate or hard terminal boundary is active.
- If you can truthfully name the next executable task, execute it instead of stopping on checkpoint text.

### BERADA

- Do not hand off merely to ask whether Gort should keep iterating, merely to surface a routine milestone checkpoint, or merely because a visibility bundle just emitted.
- Prefer the smallest evidence-backed reducer task, research task, or decomposition that keeps autonomy moving before escalating to stakeholder questioning.

### NIKTO / low-confidence protocol

- Do not use `LOW_CONFIDENCE_NEXT_EPIC` to ask for routine continuation approval, milestone review, or permission to keep iterating after a normal checkpoint/visibility emit.
- Checkpoints, visibility bundles, and compaction/resume mechanics are not by themselves terminal reasons.
