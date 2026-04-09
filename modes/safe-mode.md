# Mode: safe mode

Load this file only when the user or repo-local policy explicitly requests tighter approval/checkpoint behavior.

## Core meaning

- Safe mode is a higher-touch oversight override, not the default posture.
- Use it when routine milestone review or tighter approval gating is itself a desired behavior.
- Safe mode should tighten approval boundaries; it must never be silently inferred from a visibility bundle, checkpoint, or compaction event alone.

## Pause / approval rule

Safe mode may pause at defined review boundaries such as:

- major milestone completions
- stepping into adjacent follow-on work that materially changes stakeholder scope
- elevated, destructive, irreversible, or otherwise risk-sensitive actions
- repo-local policy gates that explicitly require approval-style pauses

## Constraints

- Even in safe mode, do not ask for approval when the next uncertainty is purely factual or otherwise researchable.
- Even in safe mode, do not turn every tool call into a question; prefer bounded milestone review over continuous babysitting.
- If a checkpoint exists only to preserve continuity or provide evidence and no explicit review boundary is active, continue.

## Output posture

- When pausing in safe mode, make the approval/review boundary explicit rather than implying that every status update is a stop.
- Keep the request narrow: identify the exact scope/risk/approval reason for the pause.
