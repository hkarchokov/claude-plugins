# Orchestration Platform v4

**Version**: 4.0.0

Simplified multi-agent investigation system using built-in Explore agents.

## Architecture

- **Commands**: Define orchestration workflow (Scout → Investigate → Validate)
- **Skills**: Provide methodology and patterns
- **Agents**: Specialized capabilities (clarifier, docs-researcher)

## Commands

- `/investigate` - Multi-agent codebase investigation using Explore agents
- `/clarify` - Extract structured requirements from ambiguous requests
- `/lookup` - Quick codebase lookup with single Explore agent

## Investigation Pattern

```
Phase 1: Scout (haiku) → Quick structure scan
Phase 2: Investigate (sonnet, parallel) → Multiple focused Explore agents
Phase 3: Validate (sonnet, optional) → Adversarial review
```

## Skills

- `investigation-pattern` - Scout → Investigate → Validate methodology
- `request-clarification` - Systematic requirement extraction
- `documentation-research` - Fetching and validating against official docs
- `platform-guide` - Reference for commands and capabilities

## Agents

- `clarifier` - Requirement extraction for ambiguous requests
- `docs-researcher` - Documentation fetching and pattern validation (optional)

## Design Principles

1. **Use built-in Explore agents**: No custom investigation agents needed
2. **Scout first**: Understand structure before deep diving
3. **Parallel execution**: Phase 2 agents in single message
4. **Right model for the job**: haiku for speed, sonnet for depth
5. **Trust Claude**: Native ability to decompose and prompt effectively
