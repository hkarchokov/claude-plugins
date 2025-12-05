---
name: platform-guide
description: Reference guide for orchestration slash commands and platform capabilities. Use when working with orchestration features or when users ask about available commands.
---

# Orchestration Platform Guide

## Overview

This platform provides multi-agent investigation and clarification capabilities using built-in Explore agents.

## Available Commands

### /investigate [topic]

Triggers a multi-agent codebase investigation using the **Scout → Investigate → Validate** pattern.

**Workflow**:
1. **Scout** (haiku) - Quick structure scan to understand the codebase
2. **Investigate** (sonnet, parallel) - 3-5 focused Explore agents on different angles
3. **Validate** (sonnet, optional) - Adversarial review of findings
4. **Synthesize** - Combine into structured report

**Example**:
```
/investigate how authentication works
```

### /clarify [topic]

Triggers requirement extraction for ambiguous requests.

**What it does**: Deploys clarifier agent to systematically detect ambiguities, ask targeted questions, and produce a CONTEXT REPORT with structured requirements.

**Example**:
```
/clarify add user authentication
```

### /lookup [topic]

Quick codebase lookup using a single Explore agent.

**Example**:
```
/lookup where is the database connection configured
```

## Investigation Pattern

When `/investigate` runs, it follows this pattern:

### Phase 1: Scout (haiku)
Deploy single Explore agent to understand project structure:
```
Task(subagent_type="Explore", model="haiku",
     prompt="Quick scan: project structure, conventions, where topic-related code lives")
```

### Phase 2: Focused Investigation (sonnet, parallel)
Deploy 3-5 Explore agents in parallel (single message) covering different angles:
- Main implementations
- Tests and patterns
- Configuration
- Error handling
- Dependencies

### Phase 3: Validation (optional)
Deploy Explore agent with adversarial prompt:
- What did we miss?
- What assumptions are wrong?
- What edge cases weren't covered?

## Available Agents

### orchestration:clarifier
- Systematic ambiguity detection
- Requirement extraction through questioning
- Produces CONTEXT REPORT

### orchestration:docs-researcher (optional)
- Fetches official documentation
- Validates patterns against best practices

## Available Skills

### orchestration:investigation-pattern
- Scout → Investigate → Validate methodology
- Model selection guidance (haiku vs sonnet)
- Parallel deployment patterns

### orchestration:request-clarification
- Ambiguity detection methodology
- Question formulation patterns
- CONTEXT REPORT structure

### orchestration:documentation-research
- Technology detection
- Documentation fetching
- Pattern validation

## Best Practices

1. **Scout first** - Always understand structure before deep diving
2. **Parallel execution** - Deploy Phase 2 agents in a single message
3. **Use appropriate models** - haiku for speed, sonnet for depth
4. **Include file:line references** - All findings should be traceable
5. **Validate assumptions** - Optional but recommended for complex topics
