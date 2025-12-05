# Orchestrator Core Plugin

## Overview

The orchestrator-core plugin provides foundational orchestration capabilities for Claude, enabling multi-agent workflows, task decomposition, agent delegation, and context synthesis. This plugin is designed to be bundled with Claude installations to provide consistent orchestration behavior across all projects.

## Installation

This plugin is intended to be bundled with Claude installations. For standalone installation:

```bash
claude plugins install orchestrator-core
```

## Architecture

### Bundling Strategy

The orchestrator-core plugin is designed as a **bundled plugin** that should be extracted and installed in each Claude project's local `.claude/plugins/` directory. This approach ensures:

- **Consistency**: All projects have access to the same orchestration capabilities
- **Versioning**: Plugin updates are controlled and predictable
- **Isolation**: Each project can customize orchestration behavior if needed
- **No Global State**: Avoids global configuration conflicts

### Extraction Path

During Claude initialization or project setup, this plugin should be extracted to:

```
<project_root>/.claude/plugins/orchestrator-core/
```

This makes orchestration skills available to all agents in the project while maintaining clear plugin boundaries.

## Skills

The orchestrator-core plugin provides four foundational orchestration skills:

### 1. Task Decomposition

**Purpose**: Break down complex user requests into manageable subtasks, phases, and actionable steps.

**Triggers**: `decompose`, `breakdown`, `split`, `subtasks`, `phases`, `planning`, `organize`

**Use Cases**:
- Complex feature requests requiring multi-phase execution
- Investigation tasks needing parallel information gathering
- Infrastructure changes with dependencies and risk assessment
- Any request where scope and success criteria need clarification

**Key Capabilities**:
- Hierarchical task breakdown with parent-child relationships
- Dependency analysis and execution ordering
- Scope definition with clear boundaries
- Phase planning and complexity assessment

### 2. Agent Delegation

**Purpose**: Deploy and coordinate specialized agents for parallel or sequential execution of subtasks.

**Triggers**: `delegate`, `assign`, `agents`, `deployment`, `parallel`, `subagents`, `orchestrate`

**Use Cases**:
- Parallel investigation requiring multiple specialized agents
- Sequential workflows with clear handoff points
- Complex implementations needing focused agent attention
- Result aggregation from multiple concurrent tasks

**Key Capabilities**:
- Agent selection and matching to task requirements
- Context preparation for deployed agents
- Parallel and sequential coordination patterns
- Progress monitoring and result collection

### 3. Request Clarification

**Purpose**: Identify ambiguities in user requests and formulate precise clarification questions.

**Triggers**: `clarify`, `ambiguous`, `unclear`, `requirements`, `vague`, `specify`, `questions`

**Use Cases**:
- Vague or underspecified requirements
- Multiple valid interpretation paths
- Missing critical implementation details
- Conflicting requirements requiring prioritization

**Key Capabilities**:
- Ambiguity detection and gap analysis
- Assumption identification and validation
- Question formulation with context and examples
- Priority assessment of clarifications

### 4. Context Synthesis

**Purpose**: Aggregate findings from multiple agents and sources into coherent, actionable summaries.

**Triggers**: `synthesize`, `consolidate`, `aggregate`, `findings`, `reports`, `summary`, `combine`

**Use Cases**:
- Multi-agent investigation results requiring integration
- Phase transition points needing consolidated findings
- Decision support requiring comprehensive situational awareness
- Executive summaries for complex workflows

**Key Capabilities**:
- Information aggregation and pattern recognition
- Conflict resolution between sources
- Insight extraction and recommendation formulation
- Hierarchical summarization with detail levels

## Orchestration Guide

The plugin includes a comprehensive orchestration guide that documents:
- Available slash commands (`/investigate`, `/implement`, `/review`, `/impact`, `/find-pattern`)
- Phase-based workflow (Phase 0-4 execution model)
- Quick decision tree for choosing appropriate commands
- Tips for effective multi-agent orchestration

Access the guide via trigger words: `orchestration`, `investigate`, `implement`, `workflow`, `phase`, `agents`, `subagents`

## Usage Patterns

### Typical Workflow

1. **User Request** → Orchestrator analyzes and may use **request-clarification**
2. **Task Analysis** → Orchestrator applies **task-decomposition** to break down work
3. **Agent Deployment** → Orchestrator uses **agent-delegation** to deploy specialized agents
4. **Result Collection** → Orchestrator applies **context-synthesis** to integrate findings
5. **Next Phase** → Orchestrator transitions to next workflow phase or returns to user

### Skill Interactions

The four core skills work together in orchestration workflows:

- **Task Decomposition** feeds **Agent Delegation** (tasks → agents)
- **Agent Delegation** produces inputs for **Context Synthesis** (agent outputs → synthesis)
- **Context Synthesis** may reveal needs for **Request Clarification** (gaps → questions)
- **Request Clarification** informs **Task Decomposition** refinement (answers → better tasks)

## Configuration

No additional configuration is required for basic orchestration functionality. The skills are automatically available to the orchestrator agent based on trigger word detection.

### Customization

Projects can customize orchestration behavior by:
- Adding project-specific skills in `.claude/plugins/orchestrator-core/skills/`
- Modifying trigger words in skill frontmatter (though this may affect consistency)
- Creating custom agent types referenced in delegation patterns

## Development

### Adding New Skills

To add new orchestration skills:

1. Create skill directory: `skills/<skill-name>/`
2. Create `SKILL.md` with proper frontmatter:
   ```yaml
   ---
   name: skill-name
   description: Brief description
   triggers:
     - trigger1
     - trigger2
     - trigger3
   ---
   ```
3. Add comprehensive markdown content following orchestration-guide pattern
4. Update this README to document the new skill

### Skill Structure Requirements

Each skill must include:
- Valid YAML frontmatter (name, description, 7 triggers minimum)
- Comprehensive markdown content (>1500 characters recommended)
- Clear sections: Overview, When to Use, Core Capabilities, Process, Output Structure, Integration, Best Practices, Examples

## License

[License information for the plugin]

## Version

**Current Version**: 1.0.0

## Changelog

### 1.0.0 (2025-10-24)
- Initial release with four core orchestration skills
- Added orchestration guide
- Established bundled plugin architecture
- Documented extraction and installation patterns
