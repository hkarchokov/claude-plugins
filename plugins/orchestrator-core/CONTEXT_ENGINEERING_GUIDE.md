# Context Engineering Guide

## Overview

This guide codifies the context engineering principles applied to the orchestrator-core plugin. These principles are based on 2025 industry research from Anthropic, Microsoft, and real-world implementations showing that **conciseness outperforms comprehensiveness** in LLM prompting.

**Key Finding**: Reducing context from 1,285→587 lines (54% reduction) improved quality scores from 62→85 ([Young Leaders, 2025](https://www.youngleaders.tech/p/claude-skills-commands-subagents-plugins)).

## Core Principles

### 1. Surgeon-Assistant Architecture

**Orchestrator = Surgeon** (strategic decision-maker)
- Makes strategic decisions
- Coordinates overall operation
- Synthesizes findings from assistants
- Maintains situational awareness
- Controls workflow phases

**Agents/Commands = Surgical Assistants** (specialized executors)
- Specialized experts with specific roles
- Execute bounded, focused procedures
- Report structured findings back
- Follow strict protocols (circuit breakers)
- Stay within their area of expertise

### 2. Signal-to-Noise Optimization

**Target Metrics**:
- Redundancy: <15% (from 42%)
- Signal-to-Noise Ratio: >75% (from 59%)
- Token efficiency: Eliminate duplication, preserve quality

**Techniques**:
- Single source of truth for shared patterns
- Centralize common procedures
- Reference instead of duplicate
- Compress verbose descriptions to actionable procedures

### 3. Safety Through Constraints

**Circuit Breakers** (mandatory for all investigation agents):
- Token Budget: 10k-18k tokens maximum
- Time Ceiling: 8-15 minutes maximum
- File Read Limit: 5-30 files maximum
- Graceful Degradation: Return partial results when approaching limits
- Violation Handling: Stop immediately, return INCOMPLETE status

## Structural Patterns

### Skill Structure (Standardized)

All skills MUST follow this structure:

```markdown
---
name: skill-name
description: One-line description
triggers: [trigger, words, list]
---

# Skill Name

## Overview
Brief (2-3 sentence) description

## When to Use This Skill
Bulleted list of use cases

## When NOT to Use This Skill
Bulleted list of anti-patterns (prevents misuse)

## [Name] Process
Numbered steps (concise, actionable)

## Decision Criteria (if applicable)
Quantitative thresholds for decisions

## Output Structure (if applicable)
What this skill produces

## Integration with Other Skills (if applicable)
How this connects to other skills

## Best Practices
Concise guidance (no verbose explanations)
```

### Command Structure (Standardized)

All commands MUST follow this structure:

```markdown
---
description: One-line description
argument-hint: what arguments mean
skills: [list, of, skills, used]
---

Command: $ARGUMENTS

Brief description of what this command does.

Follow these steps:

**Step 0: Load Orchestration Skills**
Reference WORKFLOW_SETUP.md configuration

**Step 1-N: Execution Steps**
Concise, actionable steps

**Agent Prompt Validation**: Follow agent-delegation:prompt-validation checklist
```

**NO "Skills Used" sections** - that information is in frontmatter already.

### Agent Structure (Standardized)

All agents MUST include:

```markdown
---
name: agent-name
description: Brief description
tools: List, of, tools
model: sonnet
color: color-name
---

## Agent Role
One sentence

## Circuit Breakers (MANDATORY)
- Token Budget: X tokens maximum
- Time Ceiling: X minutes maximum
- File Read Limit: X files maximum
- Graceful Degradation Protocol
- Violation Handling

## Workflow
Numbered steps

## Output Format (MANDATORY)
Structured template that MUST be followed
```

## Centralization Patterns

### Single Source of Truth

**Pattern**: Instead of duplicating common patterns, create centralized references.

**Examples**:
1. **Validation Checklist** → `/skills/agent-delegation/SKILL.md`
   - Commands reference: `Follow agent-delegation:prompt-validation checklist`
   - Saved: 750 tokens (90% reduction)

2. **Workflow Setup** → `/WORKFLOW_SETUP.md`
   - Commands reference: `Execute standard workflow setup (see WORKFLOW_SETUP.md): [configuration type]`
   - Saved: 720 tokens (86% reduction)

3. **Project Detection** → `/skills/project-detection/SKILL.md`
   - Agents reference: `Execute project-detection skill protocol`
   - Saved: 1,050 tokens (87% reduction)

**When to Centralize**:
- Pattern appears in ≥3 locations
- Content is identical or near-identical (>80% similarity)
- Updates should be synchronized
- Pattern is stable (not experimental)

**When NOT to Centralize**:
- Unique to single file
- Requires context-specific variations
- Rapidly evolving pattern
- Centralization overhead exceeds benefit

### Reference Pattern

**Template**:
```markdown
## [Section Name]

**Execute [skill-name]:[section-name] protocol**

OR

**Follow [skill-name]:[procedure-name] checklist**

OR

**See [FILE.md] for [configuration type]**
```

**Benefits**:
- Single update point
- Guaranteed consistency
- Reduced token consumption
- Easier maintenance

## Quality Gates

### Skill Quality Checklist

Before adding/modifying a skill, verify:

- [ ] Overview is concise (2-3 sentences)
- [ ] WHEN to use is clear (3-7 bullets)
- [ ] WHEN NOT to use prevents misuse (3-7 bullets)
- [ ] Process is actionable (numbered steps, not philosophy)
- [ ] Decision criteria are quantitative (if applicable)
- [ ] No duplicate content from other skills
- [ ] No verbose capability descriptions (procedures only)
- [ ] Integration points are explicit

### Command Quality Checklist

Before adding/modifying a command, verify:

- [ ] Description is one clear sentence
- [ ] Argument hint explains what goes in $ARGUMENTS
- [ ] Skills list in frontmatter is complete
- [ ] NO "Skills Used" duplication section
- [ ] References WORKFLOW_SETUP.md for skill loading
- [ ] References agent-delegation for validation
- [ ] Steps are concise and actionable
- [ ] No redundant explanations

### Agent Quality Checklist

Before adding/modifying an agent, verify:

- [ ] Circuit breakers are defined (token/time/file limits)
- [ ] Graceful degradation protocol exists
- [ ] Violation handling is explicit
- [ ] Output format is mandatory and structured
- [ ] No project detection duplication (uses skill)
- [ ] Workflow is procedural (not philosophical)
- [ ] All tool uses are justified

## Decision Criteria Patterns

### Quantitative Thresholds

**Pattern**: Use measurable criteria for decisions, not subjective judgment.

**Good Examples**:
```
- `subtasks >= 3`: Decomposition justified
- `confidence >= 0.8`: Proceed without caveats
- `completeness_score >= 0.8`: Ready for synthesis
- `task_duration > 2x_expected`: Flag as slow
```

**Bad Examples**:
```
- "If complex enough": Too vague
- "When appropriate": No guidance
- "Use best judgment": Defeats purpose of criteria
```

**When to Add Decision Criteria**:
- Skill makes binary decisions (proceed/block, complete/incomplete)
- Numeric thresholds naturally exist (counts, percentages, ratios)
- Multiple conditions determine readiness
- Historical confusion about when to apply skill

### Threshold Design

**Guidelines**:
1. **Three-tier**: High/Medium/Low or Proceed/Caution/Block
2. **Explicit actions**: What happens at each tier
3. **Measurable**: Can be computed, not guessed
4. **Conservative**: Err on side of safety

**Example**:
```
Completeness Thresholds:
- >= 1.0: All expected agents reported → PROCEED
- >= 0.8: Most agents reported → PROCEED WITH CAUTION
- >= 0.6: Majority reported → REQUEST DECISION
- < 0.6: Insufficient data → FAIL
```

## Compression Techniques

### 1. Remove Verbose Capabilities

**Before** (verbose):
```markdown
## Core Capabilities

### Agent Selection
Match task requirements to agent capabilities by analyzing task
characteristics, required expertise, and available agent specializations.
Select the most appropriate agent type for each subtask considering
complexity, domain, and execution context.

### Context Preparation
Prepare focused, relevant context packages for each deployed agent...
```

**After** (procedural):
```markdown
## Delegation Process

1. **Task Analysis**: Review decomposed tasks
2. **Agent Matching**: Select appropriate agent types
3. **Context Packaging**: Prepare focused context
4. **Deployment**: Launch agents with constraints
```

**Savings**: ~150-200 tokens per skill

### 2. Consolidate Redundant Workflows

**Before** (three separate workflows):
```markdown
### Success Capture:
When capturing a success, the system will:
1. CHECK FOR DUPLICATES FIRST (mandatory)
2. Analyze the implementation that worked
3. Extract the pattern with full context
...

### Failure Capture:
When recording a failure, the system will:
1. CHECK FOR DUPLICATES FIRST (mandatory)
2. Analyze what went wrong and why
...

### Session Analysis (all):
When analyzing the full session:
1. Review entire conversation history
2. CHECK FOR DUPLICATES for each potential memory
...
```

**After** (unified):
```markdown
### Capture Workflow:
**All capture types follow same protocol**:
1. CHECK FOR DUPLICATES FIRST (mandatory)
2. Analyze (implementation/failure/session)
3. Store with appropriate confidence
4. Tag for discovery
5. Link to related patterns
```

**Savings**: ~300-400 tokens

### 3. Compress Verbose Sections

**Before**:
```markdown
## When to Use

### Regular Maintenance
- **Weekly**: Light grooming for recent additions
- **Monthly**: Comprehensive audit and optimization
- **Quarterly**: Deep reorganization and pattern extraction

### Triggered Maintenance
- After major project completion
- When duplicate patterns are noticed
- Before starting new major initiatives
- When search results seem inconsistent
```

**After**:
```markdown
## When to Use

**Regular**: Weekly (light), Monthly (comprehensive), Quarterly (deep)
**Triggered**: After major projects, when duplicates noticed, before initiatives
```

**Savings**: ~100-150 tokens

## Maintenance Guidelines

### Adding New Skills

1. **Check for duplication** against existing skills
2. **Follow standard structure** exactly
3. **Add WHEN NOT section** to prevent misuse
4. **Centralize** any shared patterns
5. **Add decision criteria** if skill makes binary choices
6. **Keep procedures concise** (no verbose explanations)

### Adding New Commands

1. **Use frontmatter** for metadata (don't duplicate in body)
2. **Reference centralized** workflow setup and validation
3. **Keep steps actionable** (numbered, concise)
4. **No "Skills Used" section** (it's in frontmatter)
5. **Specify agent deployment** patterns if multi-agent

### Adding New Agents

1. **Add circuit breakers** (mandatory - token/time/file limits)
2. **Use project-detection skill** (don't duplicate detection logic)
3. **Define output format** explicitly (mandatory template)
4. **Keep workflow procedural** (no verbose philosophy)
5. **Add graceful degradation** handling

### Refactoring Existing Content

**Red flags** (refactor immediately):
- Same content in ≥3 files
- Verbose capability descriptions (convert to procedures)
- Missing WHEN NOT section (add to prevent misuse)
- No circuit breakers in investigation agents (add safety)
- Duplicate skill lists (move to frontmatter)

**Refactoring process**:
1. Identify duplication (search for similar blocks)
2. Create centralized version
3. Replace all instances with references
4. Verify no functionality lost
5. Measure token savings

## Metrics & Targets

### Token Efficiency

**Baseline** (before optimization):
- Total context: ~15,000 tokens
- Redundancy rate: 42%
- Signal-to-noise: 59%

**Target** (after optimization):
- Total context: ~13,000 tokens
- Redundancy rate: <15%
- Signal-to-noise: >75%

**Current** (after Phases 1-2):
- Token savings: ~1,920 tokens
- Redundancy: <20% (estimated)
- Signal-to-noise: ~70% (estimated)

### Quality Metrics

**Measure**:
- Agent success rate (% completing without errors)
- Circuit breaker triggers (should be rare, <5%)
- User clarification requests (measure WHEN NOT effectiveness)
- Time to complete workflows (efficiency gain)

**Track**:
- Number of duplicate patterns found during grooming
- Number of reference links vs duplicated content
- Token consumption per agent type
- Phase completion rates

## Version History

### v2.0 (Current) - Context Engineering Optimization

**Phase 1: Critical Redundancy Elimination**
- Created validation, workflow setup, project detection centralizations
- Added circuit breakers to 12 investigation agents
- Net savings: +120 tokens (accounting for circuit breakers)

**Phase 2: Signal-to-Noise Optimization**
- Added WHEN NOT sections to 7 skills
- Converted capabilities to procedures in 6 skills
- Compressed verbose content in 2 commands
- Removed metadata duplication from 8 commands
- Total savings: ~1,800 tokens

**Phase 3: Standardization & Documentation**
- Standardized skill/command/agent structures
- Added quantitative decision criteria to 4 skills
- Created CONTEXT_ENGINEERING_GUIDE.md

**Overall Impact**:
- Total token savings: ~1,920 tokens
- Quality improvements: Redundancy ↓42%→<20%, SNR ↑59%→~70%
- Safety improvements: All agents have circuit breakers
- Maintainability: Single source of truth for common patterns

### v1.0 - Initial Release

Original implementation with:
- 42% redundancy
- 59% signal-to-noise
- No circuit breakers
- Verbose capability descriptions
- Duplicated patterns across files

## Further Reading

**Research Foundation**:
- Anthropic Context Engineering Guide (2025)
- Microsoft Multi-Agent Orchestration Patterns (2025)
- Young Leaders: "Conciseness Outperforms Comprehensiveness" (2025)

**Internal Documentation**:
- `/WORKFLOW_SETUP.md` - Centralized workflow configurations
- `/skills/agent-delegation/SKILL.md` - Prompt validation checklist
- `/skills/project-detection/SKILL.md` - Project type detection protocol

## Summary

**Modern context engineering principles**:
1. **Conciseness over comprehensiveness** - Eliminate redundancy
2. **Procedures over philosophy** - Actionable steps, not descriptions
3. **Safety through constraints** - Circuit breakers prevent runaway execution
4. **Single source of truth** - Centralize, then reference
5. **Quantitative criteria** - Measurable thresholds, not subjective judgment
6. **Surgeon-assistant model** - Clear separation of orchestration vs execution
7. **Prevention patterns** - WHEN NOT sections prevent misuse

**Result**: Higher quality, lower token cost, better maintainability.
