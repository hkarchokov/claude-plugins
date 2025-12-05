# Orchestration Platform v4

Simplified multi-agent investigation system using built-in Explore agents.

## Architecture

```
┌─────────────────────────────────────────────────────────────┐
│ USER                                                         │
│  ↓                                                          │
│  /investigate "authentication system"                       │
└────────────────────────────────┬────────────────────────────┘
                                 ↓
┌─────────────────────────────────────────────────────────────┐
│ COMMAND (commands/investigate.md)                           │
│ - Phase 1: Scout (haiku) - Quick structure scan             │
│ - Phase 2: Investigate (sonnet, parallel) - Deep dives      │
│ - Phase 3: Validate (sonnet, optional) - Challenge findings │
│ - Synthesize results                                        │
└────────────────────────────────┬────────────────────────────┘
                                 ↓
┌─────────────────────────────────────────────────────────────┐
│ EXPLORE AGENTS (built-in)                                   │
│                                                              │
│ Phase 1:                                                    │
│ ┌─────────────────────────────────────────────────────────┐│
│ │ Scout (haiku)                                            ││
│ │ - Project structure                                      ││
│ │ - Naming conventions                                     ││
│ │ - Where topic-related code lives                         ││
│ └─────────────────────────────────────────────────────────┘│
│                          ↓                                  │
│ Phase 2 (parallel):                                         │
│ ┌───────────────┐ ┌───────────────┐ ┌───────────────┐      │
│ │ Explore       │ │ Explore       │ │ Explore       │      │
│ │ (sonnet)      │ │ (sonnet)      │ │ (sonnet)      │      │
│ │               │ │               │ │               │      │
│ │ Main impls    │ │ Tests         │ │ Config        │      │
│ └───────────────┘ └───────────────┘ └───────────────┘      │
│        ↓                 ↓                 ↓                │
│   Report 1          Report 2          Report 3             │
└─────────────────────────────────────────────────────────────┘
```

## Key Concepts

### Scout → Investigate → Validate Pattern

1. **Scout (haiku)** - Fast, cheap scan to understand project structure
2. **Investigate (sonnet, parallel)** - Multiple focused agents on different angles
3. **Validate (sonnet, optional)** - Adversarial review of findings

### Model Selection

- **haiku** - For quick scans where speed/cost matters
- **sonnet** - For deep analysis requiring understanding

### Parallel Execution

Phase 2 agents MUST deploy in a **single message** for parallel execution:
```
Task(subagent_type="Explore", model="sonnet", prompt="...angle 1...")
Task(subagent_type="Explore", model="sonnet", prompt="...angle 2...")
Task(subagent_type="Explore", model="sonnet", prompt="...angle 3...")
```

## Commands

### /investigate [topic]
Multi-agent codebase investigation using Scout → Investigate → Validate pattern.

### /clarify [topic]
Requirement extraction for ambiguous requests using clarifier agent.

### /lookup [topic]
Quick single-agent codebase lookup.

## Agents

### orchestration:clarifier
- Systematic ambiguity detection
- Produces CONTEXT REPORT with structured requirements

### orchestration:docs-researcher (optional)
- Fetches official documentation
- Validates patterns against best practices

## Skills

### investigation-pattern
- Scout → Investigate → Validate methodology
- Model selection guidance
- Parallel deployment patterns

### request-clarification
- Ambiguity detection methodology
- Question formulation patterns

### documentation-research
- Technology detection
- Documentation fetching

### platform-guide
- Reference for commands and capabilities

## Directory Structure

```
orchestration/
├── PLUGIN.md              # Plugin manifest
├── README.md              # This file
├── commands/
│   ├── investigate.md     # Multi-agent investigation
│   ├── clarify.md         # Requirement clarification
│   └── lookup.md          # Quick lookup
├── skills/
│   ├── investigation-pattern/   # Investigation methodology
│   ├── request-clarification/   # Clarification methodology
│   ├── documentation-research/  # Docs research methodology
│   └── platform-guide/          # Platform reference
├── agents/
│   ├── clarifier.md       # Requirement extraction
│   └── docs-researcher.md # Documentation research
└── hooks/
    └── session_start.py   # Session initialization
```

## Design Principles

1. **Use built-in agents** - Explore agents are powerful, no need for custom investigators
2. **Scout first** - Always understand structure before deep diving
3. **Parallel execution** - Deploy multiple agents in single message
4. **Right model for the job** - haiku for speed, sonnet for depth
5. **Trust Claude** - Native ability to decompose topics and craft prompts
