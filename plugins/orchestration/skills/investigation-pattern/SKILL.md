---
description: Scout → Investigate → Validate pattern for codebase investigations
---

# Investigation Pattern

Use this pattern when running `/investigate` or conducting thorough codebase investigations.

## The Pattern

1. **Scout** (haiku) - Quick structure scan to understand the codebase
2. **Investigate** (sonnet, parallel) - Multiple focused Explore agents
3. **Validate** (sonnet, optional) - Adversarial review of findings

## Phase 1: Scout

Deploy a single Explore agent with `model="haiku"` to quickly understand:
- Project structure and key directories
- Naming conventions and patterns
- Where the topic-related code likely lives

This is fast and cheap - just getting bearings.

## Phase 2: Focused Investigation

Using scout findings, deploy **3-5 Explore agents in parallel** (single message, multiple Task calls) with `model="sonnet"`.

Each agent covers a different angle:
- Entry points / main implementations
- Tests and test patterns
- Configuration and environment handling
- Error handling and edge cases
- Related/dependent code

**Key**: Use specific paths and patterns discovered by scout to craft targeted prompts.

## Phase 3: Validation (Optional)

Deploy a final Explore agent with `model="sonnet"` using an adversarial prompt:
- What did we miss?
- What assumptions might be wrong?
- What edge cases weren't covered?
- Are there inconsistencies in the findings?

## Key Points

- Scout uses haiku for speed/cost efficiency
- Investigators use sonnet for deeper understanding
- All Phase 2 agents deploy in a **SINGLE message** for parallel execution
- Use scout findings to craft specific, targeted prompts
- Include file:line references in synthesis
