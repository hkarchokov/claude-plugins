---
name: project-detection
description: Systematic protocol for detecting project type (Node.js, Python, Rust, Claude plugin, etc.) through marker files and file extensions to guide investigation strategy. Load before codebase analysis when project type is unknown or needs validation.
triggers:
  - project-type
  - detect-project
  - marker-files
  - investigation-strategy
  - project-identification
  - codebase-type
  - language-detection
  - unknown-project
  - identify-framework
  - plugin-json
  - package-json
  - cargo-toml
---

# Project Detection

## Overview

This skill provides a systematic protocol for detecting project type before investigation. Accurate project type detection ensures agents apply appropriate investigation strategies, focus on relevant files, and avoid false patterns.

## When to Use This Skill

**Mandatory for**:
- All investigation agents before analysis begins
- Code analysis tasks requiring project-specific patterns
- Dependency mapping across different project types
- Architecture analysis requiring language-specific conventions

## When NOT to Use This Skill

- Project type explicitly provided in PROJECT_CONTEXT
- Single-file analysis tasks
- Language-agnostic documentation reviews
- User has already specified project type

## Process

### Step 1: Check for Marker Files

Search working directory for these files (priority order):

1. **`plugin.json`** → Claude Code plugin
   - Focus: `.md` agents/commands, `.py` hooks, `skills/` directory

2. **`package.json`** → Node.js/JavaScript project
   - Focus: `src/`, `*.ts`/`*.tsx` files, `tsconfig.json`

3. **`pyproject.toml` or `requirements.txt`** → Python project
   - Focus: `*.py` files, package structure

4. **`Cargo.toml`** → Rust project
   - Focus: `src/`, `*.rs` files

5. **`pom.xml` or `build.gradle`** → Java project
   - Focus: `src/`, `*.java` files

6. **`go.mod`** → Go project
   - Focus: `*.go` files, module structure

### Step 2: Analyze File Extension Distribution

If Step 1 inconclusive, count files by extension in scope directories:

- **Majority `.md` + `.py`** → Claude Code plugin
- **Majority `.ts`/`.tsx`** → TypeScript project
- **Majority `.py`** → Python application
- **Majority `.java`** → Java project
- **Majority `.rs`** → Rust project
- **Majority `.go`** → Go project

### Step 3: Read Prompt for PROJECT_CONTEXT

Check if prompt contains explicit `PROJECT_CONTEXT:` section with project type declaration.

### Step 4: Clarify if Ambiguous

If Steps 1-3 fail to determine project type, use AskUserQuestion:

```
questions: [{
  question: "What type of project is this?",
  header: "Project Type",
  multiSelect: false,
  options: [
    {label: "Claude Code Plugin", description: "Plugin with agents/, commands/, hooks/ directories"},
    {label: "Node.js/TypeScript", description: "JavaScript/TypeScript project with package.json"},
    {label: "Python Application", description: "Python project with requirements.txt or pyproject.toml"},
    {label: "Rust Project", description: "Rust project with Cargo.toml"},
    {label: "Java Project", description: "Java project with pom.xml or build.gradle"},
    {label: "Go Project", description: "Go project with go.mod"},
    {label: "Other", description: "Different project type - I'll provide details"}
  ]
}]
```

**DO NOT proceed until project type is determined.**

## Investigation Strategy by Project Type

Once project type detected, apply these strategies:

### Claude Code Plugin
- **Focus on**: plugin.json, agents/*.md, commands/*.md, hooks/*.py, skills/*.md
- **Search for**: Agent definitions, command workflows, hook lifecycle, skill descriptions
- **Ignore**: node_modules/, package.json, tsconfig.json, build/, dist/
- **Pattern**: Agent references use `plugin-name:agent-name` format

### Node.js/TypeScript Project
- **Focus on**: package.json, tsconfig.json, src/, *.ts/*.tsx files
- **Search for**: Import statements, module exports, TypeScript types, React components
- **Analyze**: Dependencies, build configuration, test files
- **Ignore**: node_modules/, dist/, build/

### Python Application
- **Focus on**: requirements.txt, pyproject.toml, setup.py, *.py files
- **Search for**: Import statements, class definitions, function definitions
- **Analyze**: Package structure, virtual environment setup
- **Ignore**: \_\_pycache\_\_/, .pytest_cache/, venv/, .venv/

### Rust Project
- **Focus on**: Cargo.toml, src/, *.rs files
- **Search for**: Module declarations, use statements, pub items
- **Analyze**: Dependencies in Cargo.toml, build scripts
- **Ignore**: target/, Cargo.lock (for apps)

### Java Project
- **Focus on**: pom.xml, build.gradle, src/, *.java files
- **Search for**: Package declarations, imports, annotations
- **Analyze**: Maven/Gradle dependencies
- **Ignore**: target/, build/, .gradle/

### Go Project
- **Focus on**: go.mod, *.go files
- **Search for**: Package declarations, imports, exported functions
- **Analyze**: Module dependencies
- **Ignore**: vendor/, bin/

## Output Format

Agents using this skill should declare detected project type:

```
## PROJECT TYPE DETECTED
Type: [Claude Code Plugin | Node.js/TypeScript | Python | Rust | Java | Go]
Confidence: [High | Medium | Low]
Evidence: [List of markers found]

Strategy Applied: [Brief description of investigation approach]
```

## Integration

**Investigation agents should**:
1. Execute project-detection as Phase 0 (mandatory first step)
2. Apply strategy selection based on detected type
3. Adjust focus areas and ignore patterns accordingly
4. Document detection in investigation report

**Reference pattern for agents**:
```markdown
## PHASE 0: PROJECT TYPE DETECTION

Execute project-detection skill protocol before proceeding with investigation.
```

## Benefits

- **Accuracy**: Agents focus on relevant files for project type
- **Efficiency**: Ignore patterns reduce noise in investigations
- **Consistency**: Same detection logic across all investigation agents
- **Maintainability**: Single source of truth for project type strategies

## Version

**Created**: 2025-10-24
**Tokens Saved**: ~900 tokens (4 agents × ~225 tokens each)
