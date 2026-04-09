# Gort evaluation strategy

This repo is a Markdown-only prompt pack. The goal is to make Gort **objectively better** without relying on Pi.dev source-code changes.

## Principles

- Treat prompt rules as **checkable specifications**, not style preferences.
- Prefer **scenario-based regression testing** over one-off manual impressions.
- Use the real runtime surface — **Kitty + Pi** — as the primary proof path.
- Prefer the **smallest set of high-signal assertions** that proves the intended behavior.
- Preserve ANSI-rich artifacts so trace review can inspect the actual terminal behavior.

## Primary validation surface

Use these helpers as the default runtime harness:

- `/home/choza/projects/scripts/pi-kitty-smoke.sh`
- `/home/choza/projects/scripts/kitty-orchestrate.sh`

They provide the closest available prompt-pack-level eval harness for Gort because they exercise:

- fresh Pi startup
- real repo grounding
- real reinjection text
- real terminal output
- reproducible ANSI-preserved artifacts

## How to evaluate a Gort change

For each meaningful prompt-pack change:

1. Define the exact behavior under test.
2. Name one or more concrete scenarios.
3. Run a fresh Kitty/Pi smoke for each changed scenario.
4. Assert on the trace, not on a vague overall impression.
5. Save the artifact path(s) in notes or citations.
6. Keep one adversarial or compatibility case when the change affects routing or terminal behavior.

## Preferred assertion types

Use assertions like these:

- correct first grounding read
- no forbidden visible preamble before the required structured block
- correct `STATE`, `EPIC`, `LOOP`, and terminal reason
- correct handling of `bd ready`, blocked frontiers, and stale runtime state
- correct transition to `BERADA`, `KLAATU`, or `NIKTO`
- correct suppression of generic help churn or visible controller leakage
- correct blocked-frontier reduction pass before terminal `EXTERNAL_BLOCKER`

Avoid relying on assertions like:

- "felt smarter"
- "seems better"
- "looked okay"

## Scenario matrix

Keep using and expanding a small regression corpus built from real failures.

### S1 — Fresh bootstrap in consumer repo

- Repo: target consumer repo with repo-root `AGENTS.md`
- Cue: canonical or explicitly required compatibility phrase
- Assert:
  - first grounding read comes from the active repo's authoritative `AGENTS.md`
  - no stray preamble before structured output

### S2 — Fresh session with no `.gort` runtime state

- Repo: consumer repo with no saved runtime state
- Assert:
  - controller recovers from repo/runtime evidence rather than inventing state from prompt text

### S3 — Blocked-only Beads frontier

- Repo: consumer repo where `bd ready --json` is empty and only blocked work remains
- Assert:
  - controller does not immediately treat the repo as quiescent
  - controller performs a bounded blocker freshness / reduction pass before terminal `EXTERNAL_BLOCKER`

### S4 — Low-confidence direct entry

- User turn explicitly invokes low-confidence next-epic clarification
- Assert:
  - first visible compliant block is the structured NIKTO clarification turn
  - no extra bootstrap chatter or broad discovery detour appears first

### S5 — No-epics recovery

- Start from a stale or resumed `NO_EPICS` snapshot
- Assert:
  - controller treats it as recoverable when durable evidence suggests unfinished meaningful work

### S6 — Output-invariant guard

- Any autonomous startup/work scenario
- Assert:
  - no visible non-STATE reasoning leakage appears before the next required structured block

### S7 — Compatibility cue handling

- Use one recognized non-canonical cue variant when compatibility behavior matters
- Assert:
  - controller still grounds correctly
  - docs/examples remain canonical even if recognition is compatibility-tolerant

### S8 — Compaction / fresh-session handoff

- Scenario involving staged handoff or resumed session after `/new`
- Assert:
  - reinjected prompt remains state-agnostic
  - runtime state is recovered from external sources when available

### S9 — Roadmap seeding after a meaningful implementation transition

- Repo: target repo where a just-completed change exposes multiple adjacent follow-ons
- Assert:
  - BERADA defaults to one bounded follow-on epic unless multiple near-term workstreams are simultaneously justified
  - when roadmap seeding is justified, the controller creates one parent roadmap epic plus only adjacent create-ready child epics/tasks
  - those roadmap children are attached with parent-child decomposition rather than invalid task→epic blocker links
  - no speculative distant branches are created merely because more work is imaginable

### S10 — Non-terminal `STATE:` progress block must not strand ready work

- Repo: real consumer repo smoke such as `oni-tas`
- Setup: fresh session, inject `KLAATU BERADA NIKTO`, then wait for the settled output
- Assert:
  - the settled trace does **not** end on a non-terminal structured `STATE:` block whose body merely says `Next:` / `Next move:` while executable work is ready
  - if a ready next task exists and no explicit approval gate, compaction handoff, or hard terminal condition is active, the session keeps executing instead of returning control on checkpoint text alone
  - if mode selection is ambiguous, the observed behavior still matches autonomy mode by default rather than accidental safe-mode pausing
- Reference artifacts:
  - failing trace: `/tmp/oni-tas-fresh-klaatu-20260409T145528/prompt-after-longwait.txt`
  - improved trace after mode split: `/tmp/oni-tas-mode-split-smoke-20260409T151057/prompt-after-longwait.txt`

## Public research to mirror locally

Use these external resources as reference material, not as a replacement for local scenario tests:

- Anthropic context-engineering guidance
- Microsoft Agent-Pex / PromptPex style specification-driven evaluation
- Inspect Evals as a general eval substrate and example library
- SWE-bench / Tau² style realistic multi-step task thinking

The repo-local scenario harness remains authoritative because Gort is coupled to a specific prompt pack, Beads workflow, and Kitty/Pi runtime surface.

## Boundary

Do not respond to evaluation gaps here by patching Pi.dev source code, watchers, subagents, or runtime implementation from this repo.

If a needed improvement would require source changes outside the prompt pack, document the limitation in `AGENTS.md` or `README.md`, keep the Gort-side evaluation expectation explicit, and stop at the Markdown boundary.
