# Gort citation log

This page records supporting evidence for edits and substantial reasoning changes to `gort.md`, the per-state files, and `context-compaction.md`.

## Rule

Any edit to the Gort prompt pack should add or update supporting evidence here. Do not change Gort without citations and evidence that justify the change.

## 2026-03-29 — modular split into a dedicated project

### Local evidence

- [`./gort.md`](./gort.md)
- [`./states/klatu.md`](./states/klatu.md)
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
