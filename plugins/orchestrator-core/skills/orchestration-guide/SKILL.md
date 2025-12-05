---
name: orchestration-guide
description: Reference for orchestrator slash commands (/investigate, /implement, /review, /impact) and multi-phase workflow patterns. Load when explaining available commands, choosing between workflows, or understanding phase-based execution.
triggers:
  - orchestration
  - commands
  - slash-commands
  - investigate
  - implement
  - review
  - impact
  - find-pattern
  - workflow
  - phase
  - agents
  - subagents
  - available-commands
  - which-command
  - how-to-use
  - command-reference
---

# Multi-Agent Orchestrator Quick Guide

## Available Slash Commands

### `/investigate [topic]`
**When to use**: Research and understand existing code without making changes
**Output**: Structured investigation reports from specialized agents
**Example**: `/investigate authentication` or `/investigate How does the API work?`

### `/implement [feature]`
**When to use**: Build new features with full Phase 0-3 workflow
**Phases**: Prompt Engineering → Investigation → Planning → Execution
**Example**: `/implement Add JWT refresh tokens`

### `/review [optional: scope]`
**When to use**: Check code quality, security, and best practices
**Default scope**: Unstaged git changes
**Example**: `/review` or `/review src/auth/`

### `/impact [change description]`
**When to use**: Analyze cross-project dependencies and breaking changes
**Checks**: All symlinked projects and dependencies
**Example**: `/impact Changing user authentication API`

### `/find-pattern [topic]`
**When to use**: Search memory and codebase for existing solutions
**Searches**: Neo4j memory + codebase patterns
**Example**: `/find-pattern error handling`

## Phase-Based Workflow

**Phase 0**: Prompt Engineering (task-decomposer)
**Phase 1**: Investigation (parallel agents gather context)
**Phase 2**: Planning (implementation-planner creates routine)
**Phase 3**: Execution (code-executor implements changes)
**Phase 4**: Review (you verify and commit)

## Quick Decision Tree

```
Need to understand existing code?
  → Use /investigate

Ready to build something?
  → Use /implement

Want to check code quality?
  → Use /review

Worried about breaking changes?
  → Use /impact

Looking for past solutions?
  → Use /find-pattern
```

## Tips

- **Use slash commands for consistency**: They guarantee the full workflow runs
- **Conversational requests work too**: But may skip agent deployment
- **Parallel agents are automatic**: Phase 1 runs multiple agents simultaneously
- **Each phase verifies before proceeding**: Built-in circuit breakers prevent runaway execution
