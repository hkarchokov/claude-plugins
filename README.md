# Claude Code Plugin Marketplace

Transform Claude Code into a powerful multi-agent orchestration system for structured codebase investigation and analysis.

## Quick Start

```bash
# Add marketplace
/plugin marketplace add hkarchokov/claude-plugins

# Install orchestration plugin
/plugin install orchestration@hkarchokov-claude-plugins

# Verify
/plugin list
```

**Try your first lookup**:
```bash
/lookup what does getUserById do
```

**Or run a deep investigation**:
```bash
/investigate how does authentication work
```

---

## Available Plugins

| Plugin | Purpose | Commands | Agents | Skills |
|--------|---------|----------|--------|--------|
| **orchestration** | Multi-agent codebase investigation | 3 | 7 | 10 |
| **notification-hooks** | Audio notifications (macOS) | - | - | - |
| **observability-hooks** | Event logging and debugging | - | - | - |

---

## Orchestration Plugin

Multi-agent investigation platform with smart routing, specialized agents, and comprehensive analysis capabilities.

### What It Does

Provides three investigation depths:
- **Fast lookups** (`/lookup`) - 1-2 minutes using Explore agent
- **Smart investigations** (`/investigate`) - 3-8 minutes with multi-agent analysis
- **Requirement clarification** (`/clarify`) - 2-3 minutes for ambiguous requests

### Commands

**`/lookup [query]`** - Fast codebase lookups (NEW)
- Time: 1-2 minutes
- Use for: "What does X do?", "Find Y", "Where is Z?"
- Agent: Explore only
- Example: `/lookup what does getUserById do`

**`/investigate [topic]`** - Deep multi-agent investigation
- Time: 3-8 minutes (smart routing)
- Use for: Architecture analysis, security reviews, pattern discovery
- Agents: 2-5 specialized agents (parallel execution)
- Example: `/investigate how does authentication work`

**`/clarify [request]`** - Extract structured requirements
- Time: 2-3 minutes
- Use for: Ambiguous requests needing clarification
- Agent: Clarifier with systematic questioning
- Example: `/clarify improve the authentication system`

### Agents

**Investigation Agents** (deployed by `/investigate`):
- **clarifier** - Requirement extraction through systematic questioning
- **task-decomposer** - Investigation planning and routing decisions
- **code-investigator** - Deep codebase analysis, file discovery, architecture
- **pattern-analyzer** - Convention and pattern discovery, consistency assessment
- **dependency-mapper** - Relationship and impact zone mapping
- **docs-researcher** - Documentation validation against best practices
- **validator** - Adversarial validation, edge case identification

**Quick Lookup Agent** (deployed by `/lookup`):
- **Explore** - Fast file finding, code search, pattern matching

### Skills

Loaded automatically when needed:
- **investigation-orchestration** - Investigation methodology, complexity assessment, agent selection
- **agent-orchestration** - Agent deployment patterns (parallel/sequential)
- **prompt-engineering** - 5-requirement prompt format (ROLE/CONTEXT/TASK/CONSTRAINTS/OUTPUT)
- **request-clarification** - Systematic ambiguity detection and resolution
- **code-search-techniques** - Effective code search patterns using Read/Grep/Glob
- **investigative-chaining** - Following breadcrumbs, tracing dependencies
- **adversarial-thinking** - Validation framework, edge case identification
- **context-expansion** - Identifying related investigation areas
- **documentation-research** - Documentation search and validation strategies
- **platform-guide** - Platform capabilities reference and workflows

### Architecture

**Fast Lookup Flow** (`/lookup`):
```
Query → Explore Agent → Synthesis → Done (1-2 min)
```

**Investigation Flow** (`/investigate`):
```
Request → Task-Decomposer (routing decision)
              ↓
         ┌────┴─────┐
      SIMPLE      COMPLEX
         │            │
    Direct Answer   Investigators (2-5 agents in parallel)
         │            ├─ code-investigator
         │            ├─ pattern-analyzer
         │            ├─ dependency-mapper
         │            ├─ docs-researcher (conditional)
         │            └─ validator (conditional)
         │            │
         └────┬───────┘
              ↓
         Synthesis → Done (3-8 min)
```

**Key Principles**:
- Smart routing: SIMPLE (direct), COMPLEX (multi-agent)
- Conditional validation: Based on investigation complexity
- Parallel execution: Multiple agents analyze simultaneously
- Agents investigate (read-only), Claude implements

---

## Usage Examples

### Quick Lookups

```bash
# Function lookup
/lookup what does getUserById do
→ 1 min: Function location, code snippet, explanation

# Find pattern
/lookup find all API endpoints
→ 90 sec: List of endpoints with file:line references

# Configuration search
/lookup where is database configured
→ 75 sec: Config files and relevant code sections
```

### Investigations

```bash
# Simple question - auto-routes SIMPLE
/investigate what does the login endpoint do
→ 2 min: Direct answer based on quick analysis

# Architecture question - auto-routes COMPLEX (no validation)
/investigate how does authentication work
→ 5 min: Multi-agent analysis (structure, patterns, dependencies)

# Security review - auto-routes COMPLEX (with validation)
/investigate security review of authentication system
→ 8 min: Full investigation + documentation validation + adversarial review
```

### Clarification

```bash
# Ambiguous request
/clarify improve the auth system
→ 2 min: Asks clarifying questions, produces CONTEXT REPORT with:
  - Structured requirements
  - Scope boundaries
  - Success criteria
  - Investigation dimensions
```

---

## Choosing the Right Command

| Need | Use | Time | Output |
|------|-----|------|--------|
| "What/Where is X?" | `/lookup` | 1-2 min | File:line + snippet |
| "How does X work?" | `/investigate` | 3-8 min | Comprehensive analysis |
| "Unclear requirements" | `/clarify` | 2-3 min | Structured requirements |

**Rule of thumb**:
- `/lookup` - You know what you're looking for
- `/investigate` - You want to understand how something works
- `/clarify` - You're not sure exactly what you need

---

## Installation

### GitHub Installation (Recommended)

```bash
# Add marketplace
/plugin marketplace add hkarchokov/claude-plugins

# Install orchestration plugin
/plugin install orchestration@hkarchokov-claude-plugins

# Optional: utilities
/plugin install notification-hooks@hkarchokov-claude-plugins
/plugin install observability-hooks@hkarchokov-claude-plugins

# Verify
/plugin list
```

### Local Development

For plugin development and customization:

```bash
# Clone repository
git clone https://github.com/hkarchokov/claude-plugins.git
cd claude-plugins

# Add as local marketplace (use absolute path)
/plugin marketplace add directory /absolute/path/to/claude-plugins

# Install plugins
/plugin install orchestration@hkarchokov-claude-plugins

# Changes take effect immediately - no restart needed
```

---

## notification-hooks

Simple audio notification when Claude completes long-running tasks.

### Features

- Plays subtle ping sound when agents finish
- No text-to-speech, no complexity
- macOS only (uses `afplay`)

### Requirements

- macOS only
- System volume set appropriately (plays at 40%)

---

## observability-hooks

Comprehensive event logging for session analysis, debugging, and auditing.

### Features

- Logs all tool usage (before and after execution)
- Tracks session lifecycle (start, end, statistics)
- Records user prompts and compaction events
- Saves structured JSON logs to `logs/` directory

### Logged Events

- `SessionStart`, `SessionEnd` - Lifecycle tracking
- `PreToolUse`, `PostToolUse` - Tool invocation and results
- `UserPromptSubmit` - User input capture
- `PreCompact` - Compaction triggers
- `Stop`, `SubagentStop` - Interruption events

### Requirements

- Python 3.8+ with `uv` package manager
- Writes to `logs/` directory in current working directory

---

## Common Workflows

### Understanding a Codebase

```bash
# Quick overview
/lookup list all API endpoints

# Deep dive
/investigate how is payment processing implemented
```

Multi-agent investigation with 2-5 agents analyzing code in parallel.

### Building a Feature

```bash
# First: understand existing patterns
/investigate existing authentication patterns

# Review findings, then implement directly with Claude
# (Claude uses investigation findings as context)
```

### Code Review

```bash
# Let Claude review with investigation context
"Review my auth changes for security issues"
```

### Impact Analysis

```bash
# Understand dependencies before changes
/investigate dependencies of the auth module
```

Identifies relationships, breaking change risks, test coverage gaps.

---

## Understanding Components

### Commands (Slash Commands)

**What they are**: Workflows you explicitly trigger by typing `/command`

**How to use**: You must manually type the `/` prefix

**Important**: Claude cannot invoke slash commands for you. These give you explicit control.

```bash
# ✅ Correct
/lookup what does getUserById do
/investigate authentication system

# ❌ Wrong - saying this won't trigger the command
"Please investigate the authentication system"
```

### Skills

**What they are**: Specialized knowledge that Claude or agents load on-demand

**How they load**: Automatically when relevant, or explicitly via Skill() tool

**Examples**:
- Commands load orchestration skills (investigation-orchestration, agent-orchestration)
- Agents load domain skills (code-search-techniques, adversarial-thinking)

**You don't invoke skills directly** - they're loaded automatically by the orchestration workflow.

### Agents

**What they are**: Specialized AI workers deployed via Task tool

**How they're deployed**: Commands create deployment plans and launch agents in parallel

**Types**:
- Investigation agents (clarifier, task-decomposer, code-investigator, pattern-analyzer, dependency-mapper)
- Validation agents (docs-researcher, validator)
- Quick lookup agent (Explore)

**You don't deploy agents directly** - commands handle agent orchestration.

### Hooks

**What they are**: Behaviors that react to events automatically

**How they work**: Triggered on session start, tool usage, compaction, etc.

**Examples**:
- notification-hooks plays sound when agents finish
- observability-hooks logs all tool usage to JSON files

**You don't control hooks** - they run automatically based on events.

---

## Troubleshooting

### Plugins Not Loading

```bash
# Verify marketplace
/plugin marketplace list

# Reinstall
/plugin uninstall orchestration@hkarchokov-claude-plugins
/plugin install orchestration@hkarchokov-claude-plugins

# Check enabled status
/plugin list
```

### Commands Not Working

**Symptom**: Typing `/investigate` or `/lookup` doesn't trigger the command

**Solutions**:
1. Verify plugin is installed and enabled: `/plugin list`
2. Remember: You must manually type the `/` prefix
3. Claude cannot invoke slash commands for you
4. Try the explicit command syntax: `/investigate [topic]` or `/lookup [query]`

### Notification Hooks Not Working

**macOS only** - verify:
```bash
# Check macOS
uname -s    # Should output "Darwin"

# Test sound manually
afplay /System/Library/Sounds/Ping.aiff

# Check system volume
```

### Observability Hooks Not Working

```bash
# Check dependencies
uv --version
python3 --version

# Install uv if needed
curl -LsSf https://astral.sh/uv/install.sh | sh

# Verify logs directory
ls -la logs/
# Should see: session_start.json, pre_tool_use.json, etc.
```

---

## Plugin Structure

```
claude-plugins/
├── .claude-plugin/
│   ├── marketplace.json              # Marketplace registry
│   └── plugin.json                   # Marketplace metadata
├── plugins/
│   ├── orchestration/
│   │   ├── .claude-plugin/
│   │   │   └── plugin.json          # Plugin metadata
│   │   ├── agents/                  # 7 specialized agents
│   │   │   ├── clarifier.md
│   │   │   ├── task-decomposer.md
│   │   │   ├── code-investigator.md
│   │   │   ├── pattern-analyzer.md
│   │   │   ├── dependency-mapper.md
│   │   │   ├── docs-researcher.md
│   │   │   └── validator.md
│   │   ├── commands/                # 3 slash commands
│   │   │   ├── lookup.md
│   │   │   ├── investigate.md
│   │   │   └── clarify.md
│   │   └── skills/                  # 10 orchestration skills
│   │       ├── investigation-orchestration/
│   │       ├── agent-orchestration/
│   │       ├── prompt-engineering/
│   │       ├── request-clarification/
│   │       ├── code-search-techniques/
│   │       ├── investigative-chaining/
│   │       ├── adversarial-thinking/
│   │       ├── context-expansion/
│   │       ├── documentation-research/
│   │       └── platform-guide/
│   ├── notification-hooks/
│   │   ├── .claude-plugin/
│   │   │   └── plugin.json
│   │   └── hooks/
│   │       └── hooks.json
│   └── observability-hooks/
│       ├── .claude-plugin/
│       │   └── plugin.json
│       └── hooks/
│           ├── hooks.json
│           └── *.py                  # Hook scripts
└── README.md
```

---

## Contributing

We welcome contributions!

### Development Setup

```bash
# Fork and clone
git clone https://github.com/hkarchokov/claude-plugins.git
cd claude-plugins

# Create feature branch
git checkout -b feature/your-feature-name

# Make changes
# - Agents: plugins/orchestration/agents/your-agent.md
# - Commands: plugins/orchestration/commands/your-command.md
# - Skills: plugins/orchestration/skills/your-skill/SKILL.md
# - Hooks: plugins/{hook-plugin}/hooks/hooks.json

# Test locally
/plugin marketplace add directory /absolute/path/to/claude-plugins
/plugin install orchestration@hkarchokov-claude-plugins

# Test your changes

# Submit pull request
```

### Agent Guidelines

**Investigation agents** (read-only):
- Tools: `Read, Grep, Glob, LS, Skill, mcp__sequential-thinking__sequentialthinking`
- Must be read-only (no Write, Edit, Bash)
- Focus: Analysis and investigation only

**All agents**:
- Follow 5-requirement format (ROLE/CONTEXT/TASK/CONSTRAINTS/OUTPUT)
- Include specific file:line references in outputs
- Provide actionable, evidence-based recommendations

### Skill Guidelines

- Place in `skills/{skill-name}/SKILL.md`
- Include YAML frontmatter with name and description
- Include "When to Load" section
- Provide clear methodology and templates
- Document integration with other skills

### Available Agent Types

When creating deployment plans, only these agent types exist:
- `orchestration:clarifier`
- `orchestration:task-decomposer`
- `orchestration:code-investigator`
- `orchestration:pattern-analyzer`
- `orchestration:dependency-mapper`
- `orchestration:docs-researcher`
- `orchestration:validator`

**Note**: Use `code-investigator` with dimension-specific prompts for all code analysis needs (structure, architecture, etc.). No separate specialized structure or architecture agents exist.

---

## Acknowledgments

Built on modern multi-agent architecture principles:
- Anthropic's prompt engineering best practices
- Planning-execution separation patterns
- Context engineering for high signal-to-noise ratio
- Hybrid execution pattern (agents investigate, Claude implements)
- Smart routing with conditional validation
