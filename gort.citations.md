# Gort citation log

This page records supporting evidence for edits and substantial reasoning changes to `gort.md`, the per-state files, and `context-compaction.md`.

## Rule

Any edit to the Gort prompt pack should add or update supporting evidence here. Do not change Gort without citations and evidence that justify the change.

## 2026-04-05 — restore fresh-context bootstrap to the active repo's authoritative `AGENTS.md`

### Local evidence

- Fresh prompt-pack review in this workspace found that the top bootstrap paragraph in [`./gort.md`](./gort.md) now explicitly preferred `~/projects/AGENTS.md` unless a repo-local `AGENTS.md` was already known and forbade discovering `<cwd>/AGENTS.md` during bootstrap.
- That wording directly conflicted with [`./AGENTS.md`](./AGENTS.md), which already says consumer repositories keep their own repo-root `AGENTS.md` authoritative and that the active repository's worktree/runtime state is authoritative for transient execution state.
- In a fresh context, that conflict makes the fallback rule win operationally, so the first motion can skip the active repo's grounding `AGENTS.md` even when the current Gort action is clearly anchored to that repo/worktree.
- Related `bd` issue trail: `gort-2t0`
- Updated files: [`./gort.md`](./gort.md), [`./AGENTS.md`](./AGENTS.md)

### Primary supporting sources

- [Anthropic — Effective context engineering for AI agents](https://www.anthropic.com/engineering/effective-context-engineering-for-ai-agents)
- [Claude Docs — General principles](https://docs.claude.com/en/docs/build-with-claude/prompt-engineering/general-principles)

### Why these sources support the repair

- Anthropic's context-engineering guidance supports keeping the authority chain explicit and internally consistent so the controller starts from the right local instructions instead of a broader fallback context.
- Claude's prompt-engineering guidance supports removing contradictory directives and expressing the desired first-step behavior directly at the high-priority bootstrap boundary.
- Together with the local wording conflict, these sources justify a narrow repair: restore active-repo `AGENTS.md` precedence for fresh-context bootstrap while keeping `~/projects/AGENTS.md` as a fallback only when no more specific authority is already anchored to the current Gort action.

## 2026-04-03 — canonical `KLAATU BERADA NIKTO` cue with compatibility-tolerant recognition

### Local evidence

- Fresh interactive tmux smoke artifact for the canonical cue: `/tmp/gort-cue-smoke-20260402T223139/final.ansi.txt`
- Related `bd` issue trail: `gort-ef4`
- In that smoke, the canonical user input `KLAATU BERADA NIKTO` entered the controller without appended prose, then immediately bootstrapped through `read ~/projects/gort/AGENTS.md` and `read ~/projects/gort/gort.md` before continuing normal startup work.
- Follow-up review of the landed prompt-pack docs found that they had overshot the intended compatibility policy by saying the cue must be an exact string / exact phrase. The intended contract is stricter for emitted docs/examples than for recognition: canonical visible spelling, compatibility-tolerant input matching.
- Updated files: [`./README.md`](./README.md), [`./gort.md`](./gort.md)

### Primary supporting sources

- [Anthropic — Effective context engineering for AI agents](https://www.anthropic.com/engineering/effective-context-engineering-for-ai-agents)
- [Claude Docs — General principles](https://docs.claude.com/en/docs/build-with-claude/prompt-engineering/general-principles)
- [W3C WAI — Accept different input formats](https://www.w3.org/WAI/WCAG2/supplemental/patterns/o4p08-input-formats/)

### Why these sources support the repair

- Anthropic's context-engineering guidance supports keeping the public entry cue stable, minimal, and unambiguous so the agent has one canonical visible phrase to anchor on.
- Claude's prompt-engineering guidance supports being explicit about the desired output format and constraints, which maps cleanly to "always emit the canonical cue" while still documenting compatibility behavior separately.
- W3C's guidance to accept different input formats supports making recognition forgiving where format variations are not semantically important. Applied here, the controller can prefer one canonical visible spelling while still accepting case-only and common near-variant inputs for compatibility.
- Together with the smoke artifact, these sources justify standardizing docs/examples on `KLAATU BERADA NIKTO`, treating `Gort mode` as legacy v1 wording, and avoiding brittle exact-string-only trigger wording in the prompt pack.

## 2026-04-02 — low-confidence answer barrier and first-epic seeding discipline after sandbox E2E

### Local evidence

- Fresh sandbox E2E ANSI artifact: `/tmp/gort-e2e-followup-20260402T034743Z.ansi.txt`
- Related `bd` evidence and issue trail: `gort-z5a`
- The sandbox run succeeded end-to-end, but the first stakeholder-question turn still missed the strict low-confidence NIKTO template even when the user explicitly asked Gort to start by asking the single smallest stakeholder question needed to shape the first bounded epic.
- After the user answered that question, the next visible output still leaked thoughts such as `Structuring the turn`, `Evaluating pre-flight checks`, and `Planning project structure` before the structured `BERADA` transition.
- In the same run, BERADA seeded the first epic only after generic help churn (`bd --help`, `bd create --help`, `bd update --help`, `bd epic --help`, `bd children --help`) even though the standard create / claim flow was already specified by the controller.
- Fresh rerun sandbox ANSI artifact after the first repair: `/tmp/gort-e2e-rerun-preanswer.ansi.txt`
- That rerun still leaked visible thought (`Clarifying instructions`) and still paraphrased the required low-confidence body labels as `Question:` / `Why this one:` instead of `Next question:` / `I’m asking because ...`.
- Fresh second rerun ANSI artifact after moving the rule higher in the file was needed because the first rerun still leaked before reaching the deeper low-confidence section: `/tmp/gort-e2e-rerun-preanswer-2.ansi.txt`
- That second rerun showed the root cause more clearly: the model was still operating only on the early truncated excerpt of `gort.md`, so the low-confidence direct-entry template had to be duplicated higher in the bootstrap section rather than living only deeper in the file.
- Fresh third rerun ANSI artifact after moving the exact low-confidence template into the top bootstrap section: `/tmp/gort-e2e-rerun-preanswer-3.ansi.txt`
- That third rerun finally emitted the exact `STATE: NIKTO ... | QMODE: CLARIFY | QSTEP: 1/1 | QVALUE: MAYBE | NEXT: ASK` block with the correct `Resolved facts:` / `Next question:` / `I’m asking because ...` labels, but it still leaked visible thought (`Asking clear questions`) immediately before the block.
- Fresh post-answer rerun ANSI artifact: `/tmp/gort-e2e-rerun-postanswer-3.ansi.txt`
- The post-answer rerun still read `states/*.md`, `context-compaction.md`, `README.md`, and performed generic repo inspection before the structured BERADA transition, confirming the need for a top-level post-answer barrier in the same early excerpt.
- Updated files: [`./gort.md`](./gort.md), [`./states/berada.md`](./states/berada.md)
- Updated files: [`./gort.md`](./gort.md), [`./states/berada.md`](./states/berada.md)
- Updated files: [`./gort.md`](./gort.md), [`./states/berada.md`](./states/berada.md)
- Updated files: [`./gort.md`](./gort.md), [`./states/berada.md`](./states/berada.md)

### Primary supporting sources

- [Anthropic — Building effective agents](https://www.anthropic.com/research/building-effective-agents)
- [Anthropic prompt engineering tutorial — Building Complex Prompts](https://deepwiki.com/anthropics/prompt-eng-interactive-tutorial/6.2-building-complex-prompts)
- [Qualaroo — Skip Logic Survey: A Complete Guide](https://qualaroo.com/blog/skip-logic-survey/)

### Why these sources support the repair

- The sandbox artifact shows a narrower control-flow failure than the earlier startup smokes: once Gort is explicitly told to begin with one smallest stakeholder question, the controller still needs an equally explicit post-question barrier so the answer transitions directly into the next structured block instead of leaking thoughts and state-file churn.
- Anthropic's agent / prompt-structure guidance supports replacing ambiguous continuation behavior with short exact transition templates at high-risk control points.
- Skip-logic guidance supports moving directly from a resolved stakeholder choice into synthesis rather than re-opening broad discovery or exploratory help lookup.
- Together these sources justify two focused repairs: broaden the low-confidence direct-entry trigger so "start by asking the smallest stakeholder question" uses the strict template, and tighten BERADA so first-epic seeding in a fresh repo skips generic help churn when the standard `bd` flow is already known.

## 2026-04-02 — bootstrap hard block for visible startup sequence

### Local evidence

- Initial failing ANSI smoke artifact: `/tmp/gort-smoke-oe-q8z5.1-fail-20260402T015531Z.ansi.txt`
- Mid-run ANSI smoke artifact after the first startup-shape tightening: `/tmp/gort-smoke-oe-q8z5.1-mid-20260402T015742Z.ansi.txt`
- Final passing ANSI smoke artifact after adding the bootstrap hard block and banned bootstrap headings: `/tmp/gort-smoke-oe-q8z5.2-pass-20260402T020452Z.ansi.txt`
- Related `bd` evidence and issue trail: `oe-q8z5`, `oe-q8z5.1`, `oe-q8z5.2`, and `oe-q8z5.3`
- The first failing smoke still leaked visible startup thoughts such as `Deciding output structure` before the required `STATE:` block.
- The second failing smoke regressed further and leaked visible bootstrap thoughts such as `Reviewing controller behavior` before the first grounding `read`, then continued into pre-flight/state-file work before any structured startup turn.
- The passing smoke showed the desired visible order under the same reinjection flow in thinking mode: user trigger → grounding `read` → controller `read` → `STATE: BERADA | EPIC: NONE | LOOP: 1`.
- A later live controller run in this workspace emitted the required `STATE: BERADA | EPIC: NONE | LOOP: 1` startup block but then yielded the turn instead of continuing startup, showing that `first structured turn` still allowed a stop-after-block misread.
- Fresh ANSI smoke artifact for the narrow continuation repair: `/tmp/gort-smoke-gort-4c6-20260401T201906/final.ansi.txt`.
- That smoke shows the startup path now continues past `STATE: BERADA | EPIC: NONE | LOOP: 1` into post-marker startup reads, so the startup marker no longer ends the response; the remaining visible reasoning leak and `bd onboard` detour are separate follow-up work.
- Updated file: [`./gort.md`](./gort.md)

### Primary supporting sources

- [Anthropic — Building effective agents](https://www.anthropic.com/research/building-effective-agents)
- [Anthropic prompt engineering tutorial — Building Complex Prompts](https://deepwiki.com/anthropics/prompt-eng-interactive-tutorial/6.2-building-complex-prompts)

### Why these sources support the repair

- The local smokes demonstrate that general bootstrap-silence wording was not enough to preserve the required visible startup sequence under the actual tmux reinjection flow.
- Anthropic's agent/prompt-structure guidance supports turning a critical control-flow contract into a short explicit sequence with banned failure examples, instead of relying on a distributed set of softer instructions.
- That combination justifies a top-level bootstrap hard block that names the exact visible order (`read`, `read`, then `STATE:`) and explicitly bans the observed leaked bootstrap headings.

## 2026-04-02 — startup first-turn barrier before normal-start tooling

### Local evidence

- Fresh ANSI smoke artifact from `/home/choza/projects/scripts`: `/tmp/gort-smoke-oe-y2re1-20260402T0140Z.ansi.txt`
- Related `bd` evidence and issue trail: `oe-y2re`, `oe-y2re.1`, and `oe-y2re.2`
- The smoke showed that plain `KLAATU BERADA NIKTO. Read AGENTS.md and follow the instructions.` still triggered extra controller file reads (`context-compaction.md` and `states/*.md`), visible startup deliberation (`Determining start method`), and startup shell/tmux inspection before any structured `STATE:` turn.
- Follow-up direct-entry ANSI smoke artifact after adding the first explicit template: `/tmp/gort-smoke-oe-y2re4b-20260402T0152Z.ansi.txt`
- That follow-up smoke showed partial improvement: the structured `STATE: NIKTO ...` / `Next question:` / `I’m asking because ...` block eventually appeared, but visible thought headings and budget-deliberation prose still leaked before the structured block.

- A later live controller run in this workspace emitted the required `STATE: BERADA | EPIC: NONE | LOOP: 1` startup block but then yielded the turn instead of continuing startup, showing that `first structured turn` still allowed a stop-after-block misread.
- Updated file: [`./gort.md`](./gort.md)

### Primary supporting sources

- [Anthropic — Building effective agents](https://www.anthropic.com/research/building-effective-agents)
- [Anthropic — Prompt engineering for Claude's long context window](https://www.anthropic.com/news/prompting-long-context)
- [Anthropic prompt engineering tutorial — Building Complex Prompts](https://deepwiki.com/anthropics/prompt-eng-interactive-tutorial/6.2-building-complex-prompts)

### Why these sources support the repair

- The local smoke demonstrates a concrete sequencing failure: the startup path leaks tool chatter and visible deliberation before the required first structured turn.
- The Anthropic agent/prompt-structure guidance supports making critical sequence boundaries explicit and front-loading the highest-priority constraints instead of relying on later instructions to override earlier operational habits.
- That combination justifies a new startup first-turn barrier, plus an explicit rule that normal-start tooling (`bd prime`, state-file reads, tmux inspection) happens only after the first structured BERADA transition turn.

- The same evidence also supports a narrower follow-up repair: when a required startup marker sits at the start of a response, the prompt should explicitly say it is not the end of the response if autonomous continuation is mandatory.

## 2026-04-02 — exact direct-entry low-confidence output template

### Local evidence

- Fresh direct-entry ANSI smoke artifact from `/home/choza/projects/scripts`: `/tmp/gort-smoke-oe-y2re3-20260402T0148Z.ansi.txt`
- Related `bd` evidence and issue trail: `oe-y2re.3` and `oe-y2re.4`
- The smoke showed that even after the startup-barrier repair, explicit `LOW_CONFIDENCE_NEXT_EPIC` direct entry still leaked visible thought (`Crafting a stakeholder question`), omitted the required `STATE: NIKTO ...` header, and answered with a bare question instead of the required `Next question:` / `I’m asking because ...` structure.
- A later follow-up smoke (`/tmp/gort-smoke-oe-y2re4c-20260402T0154Z.ansi.txt`) showed another specific failure mode: after the direct-entry template existed near the top of `gort.md`, the model still emitted visible thought (`Clarifying template details`) and reread `gort.md` because the initial tool output was truncated before finally producing the correct structured NIKTO block.
- Updated file: [`./gort.md`](./gort.md)

### Primary supporting sources

- [Anthropic — Building effective agents](https://www.anthropic.com/research/building-effective-agents)
- [Qualaroo — Skip Logic Survey: A Complete Guide](https://qualaroo.com/blog/skip-logic-survey/)
- [CyberEdge Group — 12 Simple Strategies for Avoiding Survey Fatigue](https://cyberedgegroup.com/12-simple-strategies-for-avoiding-survey-fatigue/)
- [Jama Software — A Guide to Requirements Elicitation for Product Teams](https://www.jamasoftware.com/requirements-management-guide/requirements-gathering-and-management-processes/a-guide-to-requirements-elicitation/)

### Why these sources support the repair

- The local smoke demonstrates that general "ask one stakeholder question" wording is not enough to reliably preserve the required direct-entry structure.
- Anthropic's agent guidance supports giving the model a concrete output scaffold at critical control-flow boundaries instead of expecting later formatting rules to be inferred.
- Skip-logic, survey-fatigue, and requirements-elicitation guidance all support a short fixed questionnaire frame: summarize only the resolved facts needed for context, ask exactly one question, and give a concise rationale for why that decision matters.
- Together these sources justify an exact direct-entry output template with an explicit no-thought / no-bare-question rule.

## 2026-03-29 — modular split into a dedicated project

### Local evidence

- [`./gort.md`](./gort.md)
- [`./states/klaatu.md`](./states/klaatu.md)
- [`./states/berada.md`](./states/berada.md)
- [`./states/nikto.md`](./states/nikto.md)
- [`./context-compaction.md`](./context-compaction.md)
- legacy source consulted during split: `/home/choza/gort.md`
- legacy citation log consulted during split: `/home/choza/gort.citations.md`

### Primary supporting sources

- [Anthropic — Prompt engineering for Claude's long context window](https://www.anthropic.com/news/prompting-long-context)
- [Anthropic prompt engineering tutorial — Building Complex Prompts](https://deepwiki.com/anthropics/prompt-eng-interactive-tutorial/6.2-building-complex-prompts)
- [OpenSearch — Plan-execute-reflect agents](https://docs.opensearch.org/latest/ml-commons-plugin/agents-tools/agents/plan-execute-reflect/)
- [Planner-Executor Agentic Framework | Emergent Mind](https://www.emergentmind.com/topics/planner-executor-agentic-framework)
- [ADaPT: As-Needed Decomposition and Planning for complex Tasks](https://arxiv.org/abs/2311.05772)

### Why these sources support the split

- Long-context and prompt-structure guidance supports keeping a concise top-level controller and loading only the detailed instructions needed for the active subproblem.
- Planner/executor and plan-execute-reflect material supports modular decomposition with a stable top-level controller plus specialized execution modules.
- ADaPT supports as-needed decomposition rather than forcing all behavior into one flat instruction block.

## 2026-04-01 — state-transition / replanning analysis

### Local evidence

- legacy root prompt: `/home/choza/gort.md`
- Workspace evidence consulted from `bd` state in `/home/choza/projects/oni-tas`, especially `bd ready --json --limit 100`, `bd list --status=in_progress --json`, and `bd show` on `oni-tas-8rp`, `oni-tas-jgh`, `oni-tas-3oq`, and `oni-tas-6lv`

### Primary supporting sources

- [Anthropic — Building effective agents](https://www.anthropic.com/research/building-effective-agents)
- [OpenSearch — Plan-execute-reflect agents](https://docs.opensearch.org/latest/ml-commons-plugin/agents-tools/agents/plan-execute-reflect/)
- [ADaPT: As-Needed Decomposition and Planning for complex Tasks](https://arxiv.org/abs/2311.05772)
- [Discovery and Planning Agents | DeepWiki](https://deepwiki.com/rjmurillo/ai-agents/3.4-discovery-and-planning-agents)

### Additional reviewed sources consulted the same day

- [ApX — Iterative Planning and Re-planning with Prompt Adjustments](https://apxml.com/courses/prompt-engineering-agentic-workflows/chapter-4-prompts-agent-planning-task-management/iterative-planning-re-planning-prompts)
- [Planner + Executor Pattern — Architecting Reliable Agents](https://blogs.utilia.dev/planner-executor-pattern-architecting-reliable-agents)
- [Planning with Backtracking and Replanning for Resilient Adaptive Agents](https://notes.muthu.co/2025/11/planning-with-backtracking-and-replanning-for-resilient-adaptive-agents/)
- [CrewAI forum — empty executor results and triggering replanning](https://community.crewai.com/t/how-to-handle-empty-results-from-executor-agent-and-trigger-querybuilder-agent-to-simplify-the-query/6617)
- [Plan-and-execute AI agents: the architecture behind autonomous task completion](https://ronniehuss.co.uk/building-ai-multiplied-teams-plan-and-execute-agents/)
- [Claude Code issue #30155 — state machine lifecycle bugs](https://github.com/anthropics/claude-code/issues/30155)
- [How Do You Stop AI Agents From Infinite Loops?](https://docs.bswen.com/blog/2026-03-11-prevent-ai-agent-infinite-loops/)
- [zeroclaw issue #2308 — agent lifecycle state machine](https://github.com/zeroclaw-labs/zeroclaw/issues/2308)
- [openclaw issue #27332 — queued messages and stop lifecycle gap](https://github.com/openclaw/openclaw/issues/27332)
- [Planner-Executor Agentic Framework | Emergent Mind](https://www.emergentmind.com/topics/planner-executor-agentic-framework)
- [Planning and Decomposition | Arun Baby](https://www.arunbaby.com/ai-agents/0015-planning-and-decomposition/)
- [Build Dynamic ‘Plan-and-Execute’ Agents with LangGraph](https://medium.com/%40ujjwal-basnet-ml/build-dynamic-plan-and-execute-agents-with-langgraph-1b4dfee9d08c)
- [Built with LangGraph! #33: Plan & Execute](https://python.plainenglish.io/built-with-langgraph-33-plan-execute-ea64377fccb1)
- [Orchestrator workflow in Langgraph](https://medium.com/@simantini.jadhav79/orchestrator-workflow-in-langgraph-923db4a677c5)
- [How to Build Powerful AI Agents with LangGraph](https://medium.com/%40pankajshakya627/how-to-build-powerful-ai-agents-with-langgraph-60fd11bcbd2b)
- [Building Multi-Step AI Agents with LangGraph](https://botmonster.com/posts/building-multi-step-ai-agents-with-langgraph/)
- [LangGraph forum — Edit state for dynamic planning](https://forum.langchain.com/t/edit-state-for-dynamic-planning/1661)
- [Building AI Agents: ReAct, Planning, and Tool Use](https://letsdatascience.com/blog/building-ai-agents-react-planning-tool-use)
- [You're Not Building Agents: Learn the Fundamentals From Scratch](https://www.decodingai.com/p/ai-agents-planning)
- [Designing a State-of-the-Art Multi-Agent System](https://polarixdata.com/en/blog/designing-a-state-of-the-art-multi-agent-system/)
- [As-Needed Decomposition & Planning Using Large Language Models](https://cobusgreyling.medium.com/as-needed-decomposition-planning-using-large-language-models-adapt-f9e2d065a39b)
- [Dynamic Decomposition and Planning for LLMs in Complex Decision-Making](https://promptengineering.org/adapt-dynamic-decomposition-and-planning-for-llms-in-complex-decision-making/)
- [ApX — Implementing Plan-and-Execute Agents](https://apxml.com/courses/getting-started-with-llm-toolkit/chapter-8-developing-autonomous-agents/plan-and-execute-agents)
- [Decompose, Analyze and Rethink: Solving Intricate Problems with Human-like Reasoning Cycle](https://www.proceedings.com/content/079/079017-0012open.pdf)
- [GPT-4 Task Decomposition / HTN Planner repo](https://github.com/marawan1805/GPT-4-Task-Decomposition)

## 2026-04-01 — acceptance-parent and dependency-hygiene repair

### Local evidence

- Current stuck Beads shape reproduced from `/home/choza/projects/radiance-neoforge-minecraft` using `bd ready --json --limit 100`, `bd list --status open --json`, `bd blocked --json`, `bd dep cycles --json`, `bd dep tree oe-3pzz --json`, and `bd show` on `oe-3pzz`, `oe-xa4z`, and `oe-3pzz.4`
- Local prompt files updated: [`./gort.md`](./gort.md) and [`./states/berada.md`](./states/berada.md)
- Research-backed wording review performed against official tracker documentation before editing

### Primary supporting sources

- [Atlassian — Epics, Stories, and Initiatives](https://www.atlassian.com/agile/project-management/epics-stories-themes)
- [Atlassian Support — Configure the work type hierarchy](https://support.atlassian.com/jira-cloud-administration/docs/configure-the-issue-type-hierarchy/)
- [Atlassian Support — Link work items](https://support.atlassian.com/jira-software-cloud/docs/link-issues/)
- [Atlassian Support — Add an approval step to a workflow](https://support.atlassian.com/jira-service-management-cloud/docs/add-an-approval-to-a-workflow/)
- [GitHub Docs — Adding sub-issues](https://docs.github.com/en/issues/tracking-your-work-with-issues/using-issues/adding-sub-issues)
- [GitHub Docs — Creating issue dependencies](https://docs.github.com/en/issues/tracking-your-work-with-issues/using-issues/creating-issue-dependencies)

### Why these sources support the repair

- Atlassian and GitHub both distinguish hierarchy used to break down larger work from dependency links used to express blocked-by / blocking execution order.
- Atlassian documents explicit approval gates as workflow concepts, which supports keeping a long-lived acceptance parent open until stakeholder approval rather than overloading executable child tasks with that closure rule.
- The local Beads stall showed the practical failure mode these docs warn against in effect: open work remained, but hierarchy and dependency roles were conflated enough that `bd ready` returned no executable work.

## 2026-04-01 — state-agnostic reinjection and external runtime recovery

### Local evidence

- The prior compaction payload in [`./context-compaction.md`](./context-compaction.md) embedded `STATE`, `EPIC`, and `LOOP` directly into the reinjected prompt text.
- A live tmux pane replay (`%0`) showed that over-specific reinjection text caused the fresh session to inherit prompt-coupled transient state instead of recovering it autonomously from external sources.
- Updated prompt files: [`./gort.md`](./gort.md) and [`./context-compaction.md`](./context-compaction.md)

### Primary supporting sources

- [LangGraph — Persistence](https://docs.langchain.com/oss/python/langgraph/persistence)
- [LangGraph — Interrupts](https://docs.langchain.com/oss/python/langgraph/interrupts)
- [Temporal — Workflow Execution](https://docs.temporal.io/workflow-execution)
- [Temporal — Event History](https://docs.temporal.io/workflow-execution/event)

### Why these sources support the repair

- LangGraph persistence/checkpointing uses a stable external pointer (`thread_id`) and saved checkpoints to resume execution, which supports keeping reinjected prompts minimal and recovering transient state from external runtime storage instead of from the prompt body.
- LangGraph interrupts explicitly resume by re-invoking against the persisted thread state, not by restating the full execution state in the next prompt.
- Temporal durable execution and event history show the same architectural pattern at workflow-system level: execution resumes from persisted history/replay, while prompt-like metadata is not the authoritative execution state.
- Together these sources support a Gort design where the prompt is only the entrypoint to the instructions, while pane-local runtime state and Beads data remain the authority for recovery.

## 2026-04-01 — no-epics recovery and epic seeding from durable local evidence

### Local evidence

- Live pane `%0` in `/home/choza/projects/oni-tas` resumed to `STATE: NIKTO | EPIC: NONE | LOOP: 1 | NIKTO_REASON: NO_EPICS` even though durable local work remained (`src/launch.rs`, capture artifacts, fixtures, and related session data were still present in `git status --short`).
- In that same pane, `bd ready --json --limit 100` and `bd list --status=open --json` both returned empty arrays, proving that Beads alone was insufficient to infer the next workstream for a partially-complete repo.
- Pane-local runtime state in `/home/choza/projects/oni-tas/.gort/resume.%0.39149` still pointed at `STATE: BERADA | EPIC: oe-3pzz | LOOP: 1`, showing that a stale `NO_EPICS` terminal snapshot can be resumed even when the correct behavior is to recover and reseed work.
- Updated prompt files: [`./gort.md`](./gort.md), [`./states/berada.md`](./states/berada.md), [`./states/nikto.md`](./states/nikto.md), and [`./context-compaction.md`](./context-compaction.md)

### Primary supporting sources

- [Anthropic — Building effective agents](https://www.anthropic.com/research/building-effective-agents)
- [ADaPT: As-Needed Decomposition and Planning for complex Tasks](https://arxiv.org/abs/2311.05772)
- [LangGraph — Persistence](https://docs.langchain.com/oss/python/langgraph/persistence)
- [Temporal — Workflow Execution](https://docs.temporal.io/workflow-execution)

### Why these sources support the repair

- Anthropic's agent guidance supports steering agents toward explicit recovery paths and evaluator-driven correction when a naive terminal decision would conflict with the user's operational goal.
- ADaPT supports dynamic replanning and decomposition when the current plan frontier is empty, which maps directly to seeding a next logical epic instead of halting on an empty ready queue.
- LangGraph and Temporal both support resuming from durable external state rather than treating the most recent visible terminal message as authoritative forever.
- Together with the local pane evidence, these sources justify a narrow repair: `NO_EPICS` should only be terminal after BERADA performs a fresh no-epics recovery pass, checks durable local evidence, and still finds the repo genuinely quiescent.
- Together these sources support a Gort design where the prompt is only the entrypoint to the instructions, while pane-local runtime state and Beads data remain the authority for recovery.

## 2026-04-01 — post-completion continuation scan before terminal stop

### Local evidence

- After the first repair succeeded, live pane `%0` in `/home/choza/projects/oni-tas` autonomously seeded and completed follow-on epics including `oni-tas-vs7(.1)`, `oni-tas-kog(.1)`, and `oni-tas-3ev(.1)`, proving the no-epics recovery path could restart work.
- The same pane later re-entered `STATE: NIKTO | EPIC: NONE | LOOP: 1 | NIKTO_REASON: NO_EPICS` immediately after a completion/sync/cleanup cycle, showing a second gap: Gort still lacked an explicit post-completion scan for evidence-backed adjacent work before stopping.
- The terminal summary in `%0` showed recent commits (`29c14ea`, `1da4742`, `eefa39b`), validation, cleanup, and fresh repo-state checks immediately before the stop, which is exactly the kind of durable evidence a continuation scan should inspect.
- Updated prompt files: [`./gort.md`](./gort.md), [`./states/berada.md`](./states/berada.md), and [`./states/nikto.md`](./states/nikto.md)

### Primary supporting sources

- [Anthropic — Building effective agents](https://www.anthropic.com/research/building-effective-agents)
- [ADaPT: As-Needed Decomposition and Planning for complex Tasks](https://arxiv.org/abs/2311.05772)
- [Temporal — Workflow Execution](https://docs.temporal.io/workflow-execution)

### Why these sources support the repair

- Anthropic's guidance favors explicit evaluator/replanner steps after completed work rather than letting an agent silently collapse to a terminal state when fresh evidence may justify another bounded task.
- ADaPT supports as-needed decomposition and replanning from newly revealed evidence, which fits a follow-on scan that seeds only concrete, high-confidence adjacent work after a completion cycle.
- Temporal's workflow model supports distinguishing true workflow completion from a point where additional work cannot be justified without new input; this maps to separating `NO_EPICS` from `LOW_CONFIDENCE_NEXT_EPIC`.
- Together with the local pane evidence, these sources justify a minimal repair: before terminal stop, BERADA should inspect just-completed durable work for concrete follow-ons, continue automatically when evidence is strong, and stop with a low-confidence reason only when the next epic would require subjective guidance.

## 2026-04-01 — low-confidence next-epic questionnaire protocol

### Local evidence

- Live pane `%0` in `/home/choza/projects/oni-tas` entered `STATE: NIKTO | EPIC: NONE | LOOP: 1 | NIKTO_REASON: LOW_CONFIDENCE_NEXT_EPIC` and then ran a long one-question-at-a-time clarification interview instead of either synthesizing a next epic or stopping cleanly.
- The pane showed good behavior mixed with fatigue-inducing behavior: focused questions with rationale, but also repeated serial questioning, lingering stale draft heuristics, and user-visible internal meta-commentary such as “Framing questions effectively,” “Clarifying requirements,” and “Planning content retrieval.”
- The same conversation showed the desired recovery triggers: the user answered bounded questions, simplified prior heuristics into a cleaner rule, and explicitly requested web research when the next uncertainty was factual rather than preference-based.
- Updated prompt files: [`./AGENTS.md`](./AGENTS.md), [`./gort.md`](./gort.md), [`./states/berada.md`](./states/berada.md), and [`./states/nikto.md`](./states/nikto.md)

### Primary supporting sources

- [Qualaroo — Skip Logic Survey: A Complete Guide](https://qualaroo.com/blog/skip-logic-survey/)
- [SurveyMonkey Help — Question Skip Logic](https://help.surveymonkey.com/en/surveymonkey/create/question-skip-logic/)
- [CyberEdge Group — 12 Simple Strategies for Avoiding Survey Fatigue](https://cyberedgegroup.com/12-simple-strategies-for-avoiding-survey-fatigue/)
- [Jama Software — A Guide to Requirements Elicitation for Product Teams](https://www.jamasoftware.com/requirements-management-guide/requirements-gathering-and-management-processes/a-guide-to-requirements-elicitation-for-product-teams/)
- [Bridging the Gap — What Questions Do I Ask During Requirements Elicitation?](https://www.bridging-the-gap.com/what-questions-do-i-ask-during-requirements-elicitation/)

### Why these sources support the repair

- Qualaroo and SurveyMonkey both support skip logic / conditional branching so only relevant next questions are asked, which maps directly to avoiding repetitive serial questioning once a category has already been resolved.
- CyberEdge’s survey-fatigue guidance supports keeping only must-have questions, offering bounded alternatives when respondents are uncertain, and avoiding unnecessary length.
- Jama’s elicitation guidance supports collaborative clarification, active validation of understanding, and stopping when enough information has been gathered to define the need.
- Bridging the Gap explicitly recommends using a prepared questionnaire to guide the conversation rather than marching through questions one by one, which directly matches the hidden substate discovered in the live `%0` conversation.
- Together with the local pane evidence, these sources justify a narrow repair: keep the top-level states unchanged, but define `LOW_CONFIDENCE_NEXT_EPIC` as a bounded clarification/research protocol with skip logic, normalization, sufficiency checks, and a clean transition back to `BERADA` once enough information exists.

## 2026-04-01 — evidence delegation and epic-sufficiency threshold inside low-confidence clarification

### Local evidence

- The later `%0` conversation showed repeated delegated-evidence answers such as “You'll have to do more web research,” “If research supports it yes,” “We will need to figure that out,” and architecture-bounding constraints like “vanilla ONLY” and “local only.”
- Despite that delegation, Gort kept asking planning-shaped follow-ups such as whether the next research pass should focus on one factual branch before another, even though those were now agent-planning choices rather than remaining stakeholder decisions.
- The same conversation already contained enough information to define a bounded next epic around vanilla ONI bootstrap memory/state access, with the remaining uncertainty naturally expressible as child research or decomposition tasks.
- Updated prompt files: [`./gort.md`](./gort.md), [`./states/berada.md`](./states/berada.md), and [`./states/nikto.md`](./states/nikto.md)

### Primary supporting sources

- [Qualaroo — Skip Logic Survey: A Complete Guide](https://qualaroo.com/blog/skip-logic-survey/)
- [CyberEdge Group — 12 Simple Strategies for Avoiding Survey Fatigue](https://cyberedgegroup.com/12-simple-strategies-for-avoiding-survey-fatigue/)
- [Jama Software — A Guide to Requirements Elicitation for Product Teams](https://www.jamasoftware.com/requirements-management-guide/requirements-gathering-and-management-processes/a-guide-to-requirements-elicitation-for-product-teams/)
- [Bridging the Gap — What Questions Do I Ask During Requirements Elicitation?](https://www.bridging-the-gap.com/what-questions-do-i-ask-during-requirements-elicitation/)

### Why these sources support the repair

- Skip-logic guidance supports branching only on unresolved relevant categories instead of continuing to ask follow-ups in already-resolved branches.
- Survey-fatigue guidance supports cutting non-essential questions once the remaining unknowns can be handled another way.
- Requirements-elicitation guidance supports asking stakeholders only for information they uniquely control, then stopping when enough is known to define the work.
- Bridging the Gap’s questionnaire guidance reinforces that the question list should guide the conversation rather than mechanically force every possible follow-up, which directly supports converting delegated factual uncertainty into research tasks instead of more preference-shaped questions.
- Together with the local pane evidence, these sources justify a tighter repair: distinguish stakeholder decisions from delegated evidence questions, avoid asking users to micromanage research order, and treat “enough for a bounded epic plus child research tasks” as sufficient to exit the low-confidence questionnaire.

## 2026-04-01 — truthful adaptive questionnaire status in the NIKTO header

### Local evidence

- The live `%0` low-confidence conversation produced long runs of one-question-at-a-time questioning where the user explicitly reported that it felt like they were answering questions forever unless the added value was visible.
- The same conversation showed that a static notion of linear completion would have been misleading because the remaining number of questions changed as Gort discovered new branches, delegated factual research, or reached synthesis.
- The desired operator signal was not “percent complete” but a truthful indication of whether the questionnaire was still adding value and whether the next move was another question, research, synthesis, or stop.
- Updated prompt files: [`./gort.md`](./gort.md) and [`./states/nikto.md`](./states/nikto.md)

### Primary supporting sources

- [Survey Fatigue Benchmarks 2026: Data-Backed Insights](https://surveysparrow.com/blog/survey-fatigue-benchmarks-2026/)
- [12 Simple Strategies for Avoiding Survey Fatigue — CyberEdge Group](https://cyberedgegroup.com/12-simple-strategies-for-avoiding-survey-fatigue/)
- [The effects of the progress indicator's design on online surveys](https://koasas.kaist.ac.kr/handle/10203/295297)
- [Effects of progress bars in web surveys](https://www.gu.se/sites/default/files/2020-06/1531700_lore_methodological_note_2014_4.pdf)
- [Confidence Intervals for Adaptive Trial Designs I: A Methodological Review](https://pmc.ncbi.nlm.nih.gov/articles/PMC12333484/)

### Why these sources support the repair

- Survey-fatigue guidance supports giving respondents visible progress and expectation management rather than making them guess how much longer the process will take.
- CyberEdge specifically supports progress indicators, realistic completion expectations, skip logic, and cutting non-essential questions.
- The progress-indicator design literature supports communicating progress truthfully and warns against deceptive or confusing progress signals that increase mental load.
- Adaptive-design literature supports stop rules based on diminishing returns / confidence thresholds rather than pretending every path has a fixed linear completion percentage.
- Together with the local pane evidence, these sources justify a Gort-specific repair: in low-confidence questionnaire mode, expose truthful adaptive status in the header (`QMODE`, `QSTEP`, `QVALUE`, `NEXT`) instead of a fake `% complete`.

## 2026-04-01 — adaptive-header consistency and domain-specific stakeholder questioning

### Local evidence

- A fresh tmux smoke showed the new questionnaire header appearing, but with an inconsistent combination like `QSTEP: 1/1`, `QVALUE: GO`, and `NEXT: ASK`, which made the progress signal less trustworthy.
- The same smoke also showed Gort falling back to a generic question such as “user-facing feature work, bug fixes, performance, or cleanup/tech debt?” despite the surrounding ONI conversation already containing much narrower domain-specific constraints.
- These failures indicated two remaining gaps: the adaptive header needed consistency rules, and the questionnaire needed a stronger requirement to ask only from the unresolved domain-specific decision set rather than generic product-triage defaults.
- Updated prompt files: [`./gort.md`](./gort.md) and [`./states/nikto.md`](./states/nikto.md)

### Primary supporting sources

- [Survey Fatigue Benchmarks 2026: Data-Backed Insights](https://surveysparrow.com/blog/survey-fatigue-benchmarks-2026/)
- [12 Simple Strategies for Avoiding Survey Fatigue — CyberEdge Group](https://cyberedgegroup.com/12-simple-strategies-for-avoiding-survey-fatigue/)
- [The effects of the progress indicator's design on online surveys](https://koasas.kaist.ac.kr/handle/10203/295297)
- [Bridging the Gap — What Questions Do I Ask During Requirements Elicitation?](https://www.bridging-the-gap.com/what-questions-do-i-ask-during-requirements-elicitation/)

### Why these sources support the repair

- Progress-indicator guidance only helps when the indicator is truthful and internally consistent; contradictory status signals undermine the user’s ability to judge whether continued questioning is worthwhile.
- Survey-fatigue guidance supports clear expectation management and cutting non-essential questioning, which directly supports refusing a stale `GO/ASK` status when the current budget is already exhausted.
- Requirements-elicitation guidance supports using the known domain context to ask the most relevant unresolved question rather than reverting to broad generic prompts.
- Together with the smoke evidence, these sources justify a narrow repair: add consistency rules for `QSTEP`/`QVALUE`/`NEXT`, and force stakeholder questions to come from the single highest-information unresolved domain-specific decision set.

## 2026-04-01 — first-visible-turn discipline for low-confidence questioning

### Local evidence

- Repeated tmux smokes continued to show good stakeholder questions wrapped in low-value visible preambles such as “Preparing for Gort session,” “Searching for AGENTS files,” and similar setup narration before the actual structured low-confidence turn.
- The later smokes showed that once Gort reached the structured turn, the question quality and adaptive header were already useful, so the remaining user-facing problem was the noisy lead-in rather than the question itself.
- This meant the strongest remaining improvement was not another decision rule about what to ask, but a formatting/protocol rule about what may appear first after a resume, answer, or research result.
- Updated prompt files: [`./gort.md`](./gort.md) and [`./states/nikto.md`](./states/nikto.md)

### Primary supporting sources

- [Survey Fatigue Benchmarks 2026: Data-Backed Insights](https://surveysparrow.com/blog/survey-fatigue-benchmarks-2026/)
- [12 Simple Strategies for Avoiding Survey Fatigue — CyberEdge Group](https://cyberedgegroup.com/12-simple-strategies-for-avoiding-survey-fatigue/)
- [Bridging the Gap — What Questions Do I Ask During Requirements Elicitation?](https://www.bridging-the-gap.com/what-questions-do-i-ask-during-requirements-elicitation/)

### Why these sources support the repair

- Survey-fatigue guidance supports reducing unnecessary respondent burden and making the visible interaction as concise as possible.
- Requirements-elicitation guidance supports using the question list to guide the interaction rather than cluttering the meeting with process chatter.
- Together with the smoke evidence, these sources justify a final formatting repair: require the first visible low-confidence turn to be only a header plus one of three value-bearing outcomes—question, research switch, or synthesis transition.

## 2026-04-01 — protocol-failure handling for leaked low-confidence preambles

### Local evidence

- Even after tightening the allowed first visible turn shape, fresh tmux smokes still leaked setup narration before the structured low-confidence turn.
- The useful content only appeared after the leak, which showed that the formatting contract itself was right but the model still needed an explicit suppress-or-rewrite rule when it started drifting into preamble text.
- Updated prompt files: [`./gort.md`](./gort.md) and [`./states/nikto.md`](./states/nikto.md)

### Primary supporting sources

- [Survey Fatigue Benchmarks 2026: Data-Backed Insights](https://surveysparrow.com/blog/survey-fatigue-benchmarks-2026/)
- [12 Simple Strategies for Avoiding Survey Fatigue — CyberEdge Group](https://cyberedgegroup.com/12-simple-strategies-for-avoiding-survey-fatigue/)
- [Bridging the Gap — What Questions Do I Ask During Requirements Elicitation?](https://www.bridging-the-gap.com/what-questions-do-i-ask-during-requirements-elicitation/)

### Why these sources support the repair

- The same survey-fatigue and elicitation guidance that supports concise, value-bearing questioning also supports cutting non-essential lead-in text before the real question.
- Together with the smoke evidence, these sources justify adding a fail-closed formatting rule: suppress noncompliant preambles internally, and if one slips through, immediately replace it with the compliant structured turn instead of continuing the drift.

## 2026-04-01 — silent Gort-trigger bootstrap and no-ENOENT grounding

### Local evidence

- Fresh tmux smokes still leaked user-visible setup text before the structured low-confidence turn, including visible trigger-interpretation chatter and speculative `read ~/projects/oni-tas/AGENTS.md` attempts that emitted `ENOENT` before the controller settled onto the shared Gort flow.
- That leak happened before the shared controller was fully in effect, which meant part of the remaining problem lived in the generic Gort-trigger bootstrap path, not only inside the later `LOW_CONFIDENCE_NEXT_EPIC` protocol.
- Updated prompt files: [`./gort.md`](./gort.md) and [`/home/choza/projects/AGENTS.md`](/home/choza/projects/AGENTS.md)

### Primary supporting sources

- [Survey Fatigue Benchmarks 2026: Data-Backed Insights](https://surveysparrow.com/blog/survey-fatigue-benchmarks-2026/)
- [12 Simple Strategies for Avoiding Survey Fatigue — CyberEdge Group](https://cyberedgegroup.com/12-simple-strategies-for-avoiding-survey-fatigue/)
- [Bridging the Gap — What Questions Do I Ask During Requirements Elicitation?](https://www.bridging-the-gap.com/what-questions-do-i-ask-during-requirements-elicitation/)

### Why these sources support the repair

- The same concise-interaction guidance used for the questionnaire also applies to controller bootstrap: the user should not have to watch speculative discovery chatter before the useful turn starts.
- Together with the smoke evidence, these sources justify a bootstrap-specific repair: resolve the authoritative `AGENTS.md` path first, avoid speculative missing-file reads that create `ENOENT` noise, and forbid visible debate about whether the exact `Gort mode` reinjection text was intended.

## 2026-04-01 — deterministic workspace bootstrap for the exact `KLAATU BERADA NIKTO` cue

### Local evidence

- Even after adding a generic silent-bootstrap rule, fresh tmux smokes still showed the model speculating that the current repo "probably" had `AGENTS.md`, then immediately trying `~/projects/oni-tas/AGENTS.md` and surfacing `ENOENT`.
- In this workspace, `~/projects/AGENTS.md` is already a known authoritative parent for repos under `~/projects`, so the speculative repo-root read was unnecessary noise.
- Updated prompt files: [`./gort.md`](./gort.md) and [`/home/choza/projects/AGENTS.md`](/home/choza/projects/AGENTS.md)

### Primary supporting sources

- [Survey Fatigue Benchmarks 2026: Data-Backed Insights](https://surveysparrow.com/blog/survey-fatigue-benchmarks-2026/)
- [12 Simple Strategies for Avoiding Survey Fatigue — CyberEdge Group](https://cyberedgegroup.com/12-simple-strategies-for-avoiding-survey-fatigue/)

### Why these sources support the repair

- Concise-interaction guidance supports removing avoidable bootstrap churn before the real interaction begins.
- The smoke evidence justifies making the workspace bootstrap deterministic: in `~/projects`, start from the already-known parent authority instead of guessing at a repo-local `AGENTS.md` path and leaking `ENOENT` noise.

## 2026-04-01 — no visible reasoning after grounding reads

### Local evidence

- After the deterministic workspace-bootstrap repair, the speculative `ENOENT` noise disappeared, but fresh smokes still showed visible deliberation immediately after the grounding reads and just before the structured low-confidence turn.
- This narrowed the remaining leak to a specific slot: the gap between the final grounding/controller read and the first controller-compliant visible turn.
- Updated prompt files: [`./gort.md`](./gort.md) and [`/home/choza/projects/AGENTS.md`](/home/choza/projects/AGENTS.md)

### Primary supporting sources

- [Survey Fatigue Benchmarks 2026: Data-Backed Insights](https://surveysparrow.com/blog/survey-fatigue-benchmarks-2026/)
- [12 Simple Strategies for Avoiding Survey Fatigue — CyberEdge Group](https://cyberedgegroup.com/12-simple-strategies-for-avoiding-survey-fatigue/)

### Why these sources support the repair

- The same concise-interaction evidence supports removing visible reasoning not just before grounding, but also in the handoff from grounding into the actual controller output.
- Together with the smoke evidence, this justifies a narrower handoff rule: once the last grounding read finishes, the next visible text must be the controller output itself, not an intermediate reasoning trace.

## 2026-04-01 — explicit `QVALUE`/`NEXT` compatibility rules

### Local evidence

- A fresh tmux smoke produced a strong stakeholder question but showed an internally inconsistent header/body combination: `QVALUE: NO_GO` together with `NEXT: ASK`.
- The same smoke also confirmed that the body shape still matters: when `NEXT=ASK`, the turn should carry the full low-confidence question structure instead of drifting into partial variants.
- Updated prompt files: [`./gort.md`](./gort.md) and [`./states/nikto.md`](./states/nikto.md)

### Primary supporting sources

- [The effects of the progress indicator's design on online surveys](https://koasas.kaist.ac.kr/handle/10203/295297)
- [Survey Fatigue Benchmarks 2026: Data-Backed Insights](https://surveysparrow.com/blog/survey-fatigue-benchmarks-2026/)

### Why these sources support the repair

- Progress/status indicators are only helpful when their internal semantics are coherent.
- The smoke evidence justifies making the compatibility rules explicit: `NO_GO` cannot point to another stakeholder question, and `NEXT=ASK` must always bring the full question-body shape with summary, question label, single question, and rationale.

## 2026-04-01 — remove ambiguous "nearest authoritative" bootstrap wording

### Local evidence

- Fresh smokes still sometimes opened with a speculative read of `<cwd>/AGENTS.md` even after a no-guess fallback rule had been added.
- The remaining ambiguity was that the earlier wording still told the model to first "resolve and read the active repo's nearest authoritative `AGENTS.md`", which encouraged a probe of the repo-local path before the later fallback rule applied.
- Updated prompt files: [`./gort.md`](./gort.md) and [`/home/choza/projects/AGENTS.md`](/home/choza/projects/AGENTS.md)

### Primary supporting sources

- [Survey Fatigue Benchmarks 2026: Data-Backed Insights](https://surveysparrow.com/blog/survey-fatigue-benchmarks-2026/)
- [12 Simple Strategies for Avoiding Survey Fatigue — CyberEdge Group](https://cyberedgegroup.com/12-simple-strategies-for-avoiding-survey-fatigue/)

### Why these sources support the repair

- The smoke evidence showed that the bootstrap policy still had an internal ambiguity: "nearest authoritative" versus "do not guess".
- Removing that ambiguity and replacing it with "nearest known authoritative" plus a deterministic `~/projects/AGENTS.md` default is the smallest prompt repair that directly targets the observed speculative read behavior.

## 2026-04-01 — `QSTEP` must include the currently displayed question

### Local evidence

- A fresh tmux smoke produced a structurally good low-confidence turn but rendered `QSTEP: 0/1` while simultaneously asking the first stakeholder question.
- That made the adaptive status less truthful because, from the user's point of view, the first question was already being asked.
- Updated prompt files: [`./gort.md`](./gort.md) and [`./states/nikto.md`](./states/nikto.md)

### Primary supporting sources

- [The effects of the progress indicator's design on online surveys](https://koasas.kaist.ac.kr/handle/10203/295297)

### Why these sources support the repair

- Progress/status signals are only useful when their counts align with the interaction the user is currently seeing.
- The smoke evidence justifies an explicit rule: if the current visible turn includes a stakeholder question, `QSTEP` must already count that question.

## 2026-04-01 — direct-entry exception for explicit low-confidence turns

### Local evidence

- Fresh smokes still showed extra visible controller work before the first low-confidence question even after bootstrap cleanup: reading `context-compaction.md`, running `bd prime`, and drifting through generic startup/state-discovery behavior.
- In those smokes, the user had already explicitly supplied the operative state (`LOW_CONFIDENCE_NEXT_EPIC`) plus normalized constraints and a request for exactly one stakeholder question, so the extra startup work was redundant for the current turn.
- Updated prompt files: [`./gort.md`](./gort.md), [`./states/nikto.md`](./states/nikto.md), and [`./context-compaction.md`](./context-compaction.md)

### Primary supporting sources

- [Survey Fatigue Benchmarks 2026: Data-Backed Insights](https://surveysparrow.com/blog/survey-fatigue-benchmarks-2026/)
- [12 Simple Strategies for Avoiding Survey Fatigue — CyberEdge Group](https://cyberedgegroup.com/12-simple-strategies-for-avoiding-survey-fatigue/)
- [Bridging the Gap — What Questions Do I Ask During Requirements Elicitation?](https://www.bridging-the-gap.com/what-questions-do-i-ask-during-requirements-elicitation/)

### Why these sources support the repair

- Once the user has already supplied the active clarification state and the current decision frame, repeating general startup/triage steps before the next question increases visible friction without increasing question quality.
- The smoke evidence justifies a direct-entry exception: for an explicit low-confidence turn, go straight into the structured NIKTO clarification output and defer generic bootstrap/triage/compaction reads until after that first value-bearing turn unless immediate compaction is already known to be required.

## 2026-04-02 — exact bootstrap sequence and one-axis-only stakeholder questions

### Local evidence

- Even after several bootstrap repairs, some tmux smokes still showed a non-failing repo-local `AGENTS.md` existence check during the initial Gort trigger path. That check no longer produced `ENOENT`, but it still added avoidable controller churn before the first useful turn.
- Separate smokes showed strong question quality but occasional multi-axis bundling, where one “single stakeholder question” asked for several decisions at once (for example target/runtime/mod-policy together) instead of resolving the smallest blocker first.
- Updated prompt files: [`/home/choza/projects/AGENTS.md`](/home/choza/projects/AGENTS.md), [`./gort.md`](./gort.md), and [`./states/nikto.md`](./states/nikto.md)

### Primary supporting sources

- [Survey Fatigue Benchmarks 2026: Data-Backed Insights](https://surveysparrow.com/blog/survey-fatigue-benchmarks-2026/)
- [12 Simple Strategies for Avoiding Survey Fatigue — CyberEdge Group](https://cyberedgegroup.com/12-simple-strategies-for-avoiding-survey-fatigue/)
- [Bridging the Gap — What Questions Do I Ask During Requirements Elicitation?](https://www.bridging-the-gap.com/what-questions-do-i-ask-during-requirements-elicitation/)

### Why these sources support the repair

- The concise-interaction evidence supports replacing “minimal but still exploratory” bootstrap behavior with an exact deterministic sequence when the workspace already has a known parent authority.
- Requirements-elicitation guidance supports narrowing questions to the smallest unresolved stakeholder decision rather than bundling multiple decision axes into one prompt.
- Together with the smoke evidence, these sources justify two surgical repairs: make the `~/projects` Gort bootstrap path an exact two-read sequence unless a repo-local authority is already known, and define a valid low-confidence stakeholder question as one decision axis only.

## 2026-04-02 — direct-entry classification must happen before `bd prime`

### Local evidence

- After the one-axis repair, a fresh tmux smoke showed a clear improvement in question shape: the resulting stakeholder question resolved one scope axis rather than bundling several decisions.
- But the same smoke still ran `bd prime` and read `context-compaction.md` before the first structured low-confidence turn, despite the direct-entry exception already existing.
- The remaining failure was ordering: the global session-start rule still presented `bd prime` first and the direct-entry exception second, which left room for the model to execute startup before noticing the exception.
- Updated prompt file: [`./gort.md`](./gort.md)

### Primary supporting sources

- [Survey Fatigue Benchmarks 2026: Data-Backed Insights](https://surveysparrow.com/blog/survey-fatigue-benchmarks-2026/)
- [12 Simple Strategies for Avoiding Survey Fatigue — CyberEdge Group](https://cyberedgegroup.com/12-simple-strategies-for-avoiding-survey-fatigue/)

### Why these sources support the repair

- The concise-interaction evidence supports evaluating the direct-entry shortcut before generic startup work, not after it.
- The smoke evidence justifies a small but important reorder: classify the turn first, then either go straight into low-confidence clarification or run normal startup (`bd prime` + later pre-flight checks) only when the turn is not an explicit direct-entry clarification.

## 2026-04-02 — direct-entry low-confidence turn may not insert commands or rereads

### Local evidence

- A subsequent smoke still produced the improved one-axis stakeholder question, but it inserted visible reasoning plus `bd prime` and `context-compaction.md` reads between the explicit low-confidence invocation and the first structured turn.
- This showed that merely saying “defer startup work” was still too soft; the model needed an explicit no-intervening-actions rule for direct-entry clarification turns.
- Updated prompt files: [`./gort.md`](./gort.md) and [`./states/nikto.md`](./states/nikto.md)

### Primary supporting sources

- [Survey Fatigue Benchmarks 2026: Data-Backed Insights](https://surveysparrow.com/blog/survey-fatigue-benchmarks-2026/)
- [12 Simple Strategies for Avoiding Survey Fatigue — CyberEdge Group](https://cyberedgegroup.com/12-simple-strategies-for-avoiding-survey-fatigue/)

### Why these sources support the repair

- The concise-interaction evidence supports not only deferring low-value work, but forbidding any intervening commands or reasoning steps when the user has already requested a direct low-confidence clarification turn.
- The smoke evidence justifies a stronger repair: once a direct-entry low-confidence turn is recognized, the next action must be the structured clarification output itself.

## 2026-04-02 — name the forbidden direct-entry rereads explicitly

### Local evidence

- After strengthening the direct-entry no-intervening-actions rule, the next smoke still chose to read `context-compaction.md` and `states/*.md` before the structured low-confidence turn.
- That suggested the abstract phrase “controller/state-file reads” was still too lossy for the model at runtime.
- Updated prompt files: [`./gort.md`](./gort.md) and [`./states/nikto.md`](./states/nikto.md)

### Why this supports the repair

- The smallest next repair was to spell out the forbidden rereads by name so the runtime prohibition is concrete at the exact point where the model tends to drift.

## 2026-04-02 — explicit low-confidence turns override pending startup plans

### Local evidence

- The strongest remaining churn pattern appeared when the pane had already bootstrapped from the `KLAATU BERADA NIKTO` cue, and then a later user turn explicitly invoked `LOW_CONFIDENCE_NEXT_EPIC`. The model sometimes kept following a pending startup plan (`bd prime`, state/context reads) instead of switching immediately to the structured clarification turn.
- Updated prompt files: [`/home/choza/projects/AGENTS.md`](/home/choza/projects/AGENTS.md), [`./gort.md`](./gort.md), and [`./states/nikto.md`](./states/nikto.md)

### Why this supports the repair

- The remaining bug was not just “too much startup,” but “failure to cancel startup once a direct-entry clarification turn arrives.”
- The smallest repair is to make the override rule explicit: a later explicit low-confidence turn cancels any pending startup/onboarding plan and must immediately become the structured NIKTO clarification turn.

## 2026-04-02 — question body implies `NEXT=ASK` and exact label `Next question:`

### Local evidence

- A fresh smoke produced a solid one-axis stakeholder question but still rendered an inconsistent header/body combination: `NEXT: RESEARCH` while visibly asking a stakeholder question.
- The same smoke also varied the body label to `Stakeholder question:` instead of the existing canonical `Next question:` shape.
- Updated prompt files: [`./gort.md`](./gort.md) and [`./states/nikto.md`](./states/nikto.md)

### Why this supports the repair

- Once question quality improved, the next remaining inconsistency was presentation semantics: if the body is visibly asking a stakeholder question, `NEXT` must be `ASK`, and the question label should stay canonical.
- The smallest repair is to bind those two things explicitly so header and body cannot describe different immediate actions.

## 2026-04-02 — normal-start bootstrap must stay silent until the turn’s real output

### Local evidence

- Live tmux pane `%0` in `/home/choza/projects/radiance-neoforge-minecraft` reproduced the user's stall exactly: after `read AGENTS.md` and `read ~/projects/gort/gort.md`, the controller emitted `STATE: BERADA | EPIC: NONE | LOOP: 1` plus `Normal startup. Transitioning into BERADA and continuing controller bootstrap now.` and then immediately yielded the turn instead of running `bd prime`, state loading, or no-epics recovery.
- The current repo already carried a prompt hint that the startup marker was "not the end of the response," but the live pane still stopped at that marker, so the remaining bug was not wording softness alone; it was an impossible sequencing contract for a tool-using agent turn.
- Updated file: [`./gort.md`](./gort.md)

### Primary supporting sources

- [Anthropic Claude API docs — How tool use works](https://console.anthropic.com/docs/en/agents-and-tools/tool-use/how-tool-use-works)
- [OpenAI API docs — Function calling](https://platform.openai.com/docs/guides/function-calling?api-mode=responses&lang=javascript)

### Why these sources support the repair

- Anthropic's tool-use contract describes a client-tool loop where the model requests tools, the application executes them, and the loop exits on `end_turn` when Claude has produced a final answer. That makes the visible assistant message the end of the active loop iteration, not a midpoint after which more client-executed tools can still run in the same turn.
- OpenAI's function-calling flow likewise describes tool execution first, then a final response from the model (or another tool-call round). The final user-visible answer is the result of the loop, not a progress marker that safely precedes more tool work in the same turn.
- Together with the live pane evidence, these sources justify a narrow but important repair: keep direct-entry clarification turns strict and structured, but make normal startup silent after the two grounding reads so Gort can actually run `bd prime`, context checks, state loading, and recovery work before emitting the next complete `STATE:` block.

## 2026-04-02 — silent startup must execute directly instead of self-looking up the prompt

### Local evidence

- A fresh tmux smoke after the first silent-startup repair still failed: the pane opened with no BERADA startup banner, but then grepped `~/projects/gort/gort.md` for `bd prime|normal-start|startup|resume|STATE:|bd ready|epic`, reread `gort.md`, and emitted new visible narration such as `Investigating bd prime execution` and `Checking pre-flight context` before continuing.
- The same smoke showed that a softer global ban on worklog headings was not enough by itself; the startup path needed an exact "execute, don't re-derive" rule at the point where the model was still self-looking up the controller.
- Updated file: [`./gort.md`](./gort.md)

### Primary supporting sources

- [Anthropic — Building effective agents](https://www.anthropic.com/research/building-effective-agents)
- [Anthropic — Prompt engineering for Claude's long context window](https://www.anthropic.com/news/prompting-long-context)

### Why these sources support the repair

- The smoke evidence shows a remaining prompt-following failure mode: once startup becomes silent, the model can still waste turns by rereading its own controller instead of executing the already-specified startup actions.
- Anthropic's guidance supports making high-priority control-flow steps explicit and keeping the active context focused on the task-relevant evidence rather than repeatedly reloading the policy text itself.
- Together these sources justify a tighter repair: during normal startup, execute the listed startup steps directly, ban prompt self-lookup for those steps, and suppress all user-visible assistant prose until the next complete `STATE:` block is actually ready.

## 2026-04-02 — ordinary repo work may not emit interim prose between tool calls

### Local evidence

- Fresh tmux smoke artifact after the self-lookup repair: `/tmp/gort-no-narration-20260401T214812/final.ansi.txt`
- That smoke improved one failure mode: the pane no longer grepped or reread `gort.md` to decide whether startup was silent.
- But it still emitted free-form narration during ordinary repo work, including `Inspecting task status`, before and between shell commands while no structured `STATE:` block was ready.
- Updated files: [`./gort.md`](./gort.md), [`./states/berada.md`](./states/berada.md)

### Primary supporting sources

- [Anthropic — Building effective agents](https://www.anthropic.com/research/building-effective-agents)
- [Anthropic — Prompt engineering for Claude's long context window](https://www.anthropic.com/news/prompting-long-context)

### Why these sources support the repair

- The new smoke shows that banning a few example headings is still too weak when the model is mid-investigation: the stronger invariant has to be that ordinary autonomous work produces no assistant prose at all until a complete `STATE:` block is ready.
- Anthropic's guidance supports simplifying the active control contract and keeping the model focused on task execution and relevant evidence rather than narrating intermediate work.
- Together these sources justify a narrower and stronger repair: outside grounding reads and complete `STATE:` blocks, ordinary repo work should stay silent, and BERADA's evidence-gathering path should explicitly ban interim worklog narration.

## 2026-04-02 — ban visible worklog headings and controller self-lookup during ordinary repo work

### Local evidence

- After the silent-startup repair, the same live Radiance pane `%0` continued past the old startup stop point, but it still emitted visible meta headings such as `Inspecting scripts and logs`, `Considering coordinate mapping`, `Analyzing screenshot data`, and `Evaluating the setup process` while it was doing ordinary repo triage.
- The same pane also grepped `bd prime` in `~/projects/gort` and reread `gort.md` mid-run to decide what to do next, even though the controller had already bootstrapped and the target work evidence lived in the Radiance repo plus pane/runtime state.
- Updated files: [`./gort.md`](./gort.md), [`./states/berada.md`](./states/berada.md)

### Primary supporting sources

- [Anthropic — Building effective agents](https://www.anthropic.com/research/building-effective-agents)
- [Anthropic — Prompt engineering for Claude's long context window](https://www.anthropic.com/news/prompting-long-context)

### Why these sources support the repair

- The live-pane evidence shows a remaining failure mode after startup: the controller is still narrating its own intermediate inspection steps and treating its prompt files as runtime evidence, which adds user-visible churn without improving state recovery.
- Anthropic's guidance supports keeping the active instruction hierarchy simple and explicit at high-risk control points, and keeping working memory focused on task-relevant context instead of repeatedly re-ingesting the controller itself.
- Together these sources justify a small follow-up repair: ban visible worklog headings globally and forbid ordinary BERADA/no-epics recovery from using shared Gort prompt files as substitute evidence for the target repo's next workstream.

## 2026-04-02 — normal startup may show tool rows, but not assistant prose, before the next `STATE:` block

### Local evidence

- Fresh tmux smoke artifact after the interim-prose repair: `/tmp/gort-silent-prose-20260401T215020/final.ansi.txt`
- That smoke still leaked assistant prose during startup and state recovery, including `Evaluating current state` and `Inspecting tmux panes`, even though those messages appeared between tool rows rather than as a terminal banner.
- The same smoke confirmed that tool rows themselves are acceptable; the remaining bug is specifically assistant prose appearing before the next complete structured `STATE:` block is ready.
- Updated file: [`./gort.md`](./gort.md)

### Primary supporting sources

- [Anthropic — Building effective agents](https://www.anthropic.com/research/building-effective-agents)
- [Anthropic — Prompt engineering for Claude's long context window](https://www.anthropic.com/news/prompting-long-context)

### Why these sources support the repair

- The smoke evidence narrows the rule further: after grounding, normal startup sometimes needs visible tool rows for real work, but it should never emit free-form assistant narration until the next complete `STATE:` block is ready.
- Anthropic's guidance supports making the control contract concrete at the exact failure boundary instead of relying on broad stylistic bans.
- Together these sources justify an exact sequencing repair: after the two grounding reads on normal startup, only tool actions may appear until the next real `STATE:` block.
