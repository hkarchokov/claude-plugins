---
description: Multi-agent codebase investigation using Explore agents
argument-hint: topic to investigate
---

Investigate: $ARGUMENTS

## Overview

This command orchestrates a thorough codebase investigation using the **Scout → Investigate → Validate** pattern with built-in Explore agents.

## Workflow

### Phase 1: Scout (haiku)

Deploy a single Explore agent to quickly understand the project structure:

```
Task(subagent_type="Explore", model="haiku",
     prompt="Quick scan for investigating [$ARGUMENTS]:
             - What's the project structure? Key directories?
             - What naming conventions are used?
             - Where might [$ARGUMENTS]-related code live?
             Return: key directories, relevant file patterns, initial findings.")
```

**After scout completes**: Extract key directories and patterns to inform Phase 2 prompts.

### Phase 2: Focused Investigation (sonnet, parallel)

Using scout findings, deploy **3-5 Explore agents in parallel** (all in a single message).

Each agent covers a different angle based on what scout discovered:

1. **Main implementations** - Core code for the topic
2. **Tests** - Test files and patterns
3. **Configuration** - Config files, environment handling
4. **Error handling** - Error paths, edge cases
5. **Dependencies** - Related/dependent code

**Example** (adjust based on scout findings):
```
Task(subagent_type="Explore", model="sonnet",
     prompt="In [directories from scout], find main implementations of [$ARGUMENTS].
             Look for: entry points, core logic, key functions.
             Return: file:line references, code patterns, relationships.")

Task(subagent_type="Explore", model="sonnet",
     prompt="Find tests related to [$ARGUMENTS] in [test directories].
             Look for: test patterns, edge cases covered, gaps.
             Return: test locations, patterns tested, coverage notes.")

... (more agents for other angles)
```

**Key**: All Phase 2 agents must be deployed in a **single message** for parallel execution.

### Phase 3: Validation (sonnet, optional)

Deploy a final Explore agent to challenge findings:

```
Task(subagent_type="Explore", model="sonnet",
     prompt="Review these investigation findings with skepticism:
             [Summary of Phase 2 findings]

             Questions to answer:
             - What did we miss?
             - What assumptions might be wrong?
             - What edge cases weren't covered?
             - Are there inconsistencies?

             Do targeted searches to verify or challenge key findings.")
```

### Synthesis

Combine all findings into a structured report:

1. **Summary** - Key findings in 3-5 bullets
2. **Details** - Organized by investigation angle
3. **File References** - All relevant files with line numbers
4. **Gaps/Concerns** - From validation phase
5. **Next Steps** - Suggested follow-up actions

## Optional: Documentation Research

If the user requests it, or if the topic involves external libraries/frameworks, you can add a documentation research step:

```
Task(subagent_type="orchestration:docs-researcher",
     prompt="Research official documentation for [technologies found].
             Validate patterns against best practices.")
```

## Success Criteria

- Scout provides clear direction for focused investigation
- Phase 2 agents cover multiple angles (not just one perspective)
- All findings include file:line references
- Validation challenges assumptions
- Final synthesis is actionable
