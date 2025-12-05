---
description: Search for existing patterns and solutions in memory and codebase
argument-hint: topic or problem to find patterns for
skills: [agent-delegation, context-synthesis, result-aggregation]
---

## Skills Used

This command leverages the following skills:
- **agent-delegation**: Delegates pattern discovery to memory and codebase search agents
- **context-synthesis**: Combines memory patterns with codebase patterns
- **result-aggregation**: Aggregates pattern findings from multiple sources

Find patterns for: $ARGUMENTS

This searches for **existing patterns, solutions, and past learnings** in memory and codebase. No code modifications will be made.

Follow these steps:

**Step 0: Load Orchestration Skills**
0. **Invoke all required skills** to load pattern search guidance:
   - `Skill("orchestrator-core:agent-delegation")` - Delegation best practices
   - `Skill("orchestrator-core:context-synthesis")` - Pattern synthesis
   - `Skill("orchestrator-core:result-aggregation")` - Pattern aggregation

**Skill Hint Guidance**
When deploying agents, include relevant skill hints in the prompt. Available skills for pattern search workflows:
- **agent-delegation**: Frameworks for 5-requirement prompts and prompt validation
- **context-synthesis**: Pattern synthesis and integration techniques
- **result-aggregation**: Pattern aggregation protocols from multiple sources

## DELEGATION STRATEGY

When executing pattern search workflows, deciding whether to delegate to specialized agents or handle searches directly is critical for comprehensive pattern discovery.

### When to Delegate to Specialized Agents

**Delegate when**:
- Need to search both memory (past learnings) AND codebase (current patterns)
- Pattern discovery requires analyzing multiple projects or large codebase
- Benefit from parallel search across memory and code
- Complex pattern with variations across projects
- Historical context important (what was tried before, lessons learned)

**Handle directly when**:
- Simple keyword search in specific file
- Pattern is well-known and documented
- Quick lookup of specific function/class
- Delegation overhead exceeds search cost

### Agent Selection Guide for Pattern Search

| Task Type | Recommended Agent | When to Use | Expected Output |
|-----------|------------------|-------------|-----------------|
| Memory pattern search | memory-assistant | Search for past solutions, lessons learned, established conventions | Memory patterns, historical insights, past approaches |
| Codebase pattern search | pattern-analyzer | Discover patterns in current code across projects | Code examples, consistency analysis, project variations |

## 3-STAGE WORKFLOW GUIDE

All pattern search workflows follow a 3-stage pattern to ensure comprehensive discovery from both memory and codebase.

### Stage 1: Setup & Search Planning (REQUIRED - Use Sequential Thinking)

**Mandatory Skills** (Step 0):
- Load all skills listed in command metadata before workflow execution
- `Skill("orchestrator-core:agent-delegation")`
- `Skill("orchestrator-core:context-synthesis")`
- `Skill("orchestrator-core:result-aggregation")`

**Planning with Sequential Thinking**:
Use `mcp__sequential-thinking__sequentialthinking` to:
- Analyze pattern search topic/problem
- Determine search strategy (memory + codebase vs one source)
- Plan parallel deployment of memory-assistant and pattern-analyzer
- Define success criteria for pattern discovery

**Pre-Execution Checklist**:
- [ ] All mandatory skills loaded
- [ ] Pattern search topic clarified
- [ ] Search strategy determined (both sources or single source)
- [ ] Agent prompts validated against 5-requirement format

### Stage 2: Parallel Pattern Search Execution

**PARALLEL Execution Pattern**:
- Deploy memory-assistant and pattern-analyzer in a **single message**
- Both searches are independent and can run concurrently
- Memory-assistant searches Neo4j knowledge graph
- pattern-analyzer searches current codebase across all projects
- Wait for both agents to complete before synthesis

**Sequential Thinking (OPTIONAL)**:
May be used during search if unexpected patterns require adaptive investigation.

### Stage 3: Pattern Synthesis & Validation (REQUIRED - Use Sequential Thinking)

**Use Sequential Thinking to**:
- Review both search reports for completeness
- Combine memory patterns with codebase patterns
- Identify most relevant and applicable patterns
- Remove duplicates and contradictions
- Prioritize patterns by confidence and applicability
- Assess consistency across projects
- Formulate implementation guidance

**Output Validation Checklist**:
- [ ] Recommended pattern identified with high confidence
- [ ] Real code examples provided with file:line references
- [ ] Memory insights integrated (past solutions, lessons learned)
- [ ] Alternative patterns documented with trade-offs
- [ ] Anti-patterns identified and explained
- [ ] Consistency analysis shows project variations
- [ ] Actionable implementation checklist provided
- [ ] Confidence scores assigned (High/Medium/Low)

## AGENT PROMPT TEMPLATES

When delegating to specialized agents, use the **5-requirement format** to ensure clarity and completeness.

**5-Requirement Format**:
1. **ROLE**: Agent's identity and expertise domain
2. **CONTEXT**: Relevant background, project specifics, constraints
3. **TASK**: Single, measurable objective with clear boundaries
4. **CONSTRAINTS**: Scope limits, token budgets, time limits, circuit breakers
5. **OUTPUT**: Exact deliverable format with verification criteria

### Template: memory-assistant for Memory Pattern Search

```
ROLE:
You are a memory-assistant specializing in searching the Neo4j knowledge graph for past solutions, lessons learned, and established patterns.

CONTEXT:
- Pattern topic: [TOPIC/PROBLEM to search for]
- Search domain: [PATTERN_TYPE - e.g., "error handling", "authentication", "state management"]
- Background: [Why pattern is needed]

TASK:
Search memory for relevant patterns and insights:
1. Query Neo4j knowledge graph for similar problems/solutions
2. Identify past approaches and their outcomes (success/failure)
3. Extract lessons learned and established conventions
4. Find anti-patterns and what to avoid
5. Retrieve confidence scores for past solutions

CONSTRAINTS:
- Token Budget: [e.g., 10000 tokens]
- Focus on [SPECIFIC_DOMAIN]
- Prioritize recent and high-confidence memories
- Circuit Breaker: Stop if no relevant memories found after initial search

OUTPUT:
Provide a MEMORY PATTERN REPORT with:
1. **Summary**: Number of relevant memories found, confidence level
2. **Past Solutions**: Approaches tried previously with outcomes
3. **Lessons Learned**: Key insights from past implementations
4. **Established Conventions**: Team/project standards and patterns
5. **Anti-Patterns**: What to avoid based on past failures
6. **Confidence Assessment**: How reliable each memory pattern is
7. **Recommendations**: Which past approach to follow

AVAILABLE SKILLS (contextual suggestions):
- Use Neo4j memory search tools to query knowledge graph
```

### Template: pattern-analyzer for Codebase Pattern Search

```
ROLE:
You are a pattern-analyzer specializing in discovering patterns in current codebase across all projects.

CONTEXT:
- Pattern topic: [TOPIC/PROBLEM to find patterns for]
- Codebase scope: [ALL projects OR specific projects]
- Background: [Why pattern discovery needed]

TASK:
Discover patterns in current codebase:
1. Search codebase for implementations related to [TOPIC]
2. Identify common patterns and variations across projects
3. Extract representative code examples with file:line references
4. Assess consistency of pattern usage
5. Detect project-specific adaptations
6. Find edge cases and special handling

CONSTRAINTS:
- Token Budget: [e.g., 15000 tokens]
- Scope: ALL projects in workspace
- Provide 2-3 concrete code examples per pattern
- Circuit Breaker: Stop after finding 5+ representative examples

OUTPUT:
Provide a CODEBASE PATTERN REPORT with:
1. **Summary**: Patterns found, consistency level (High/Medium/Low)
2. **Primary Pattern**: Most common approach with code examples (file:line)
3. **Pattern Variations**: Project-specific adaptations with examples
4. **Code Examples by Use Case**: Categorized implementations
5. **Consistency Analysis**: How uniformly pattern is applied across projects
6. **Edge Cases**: Special handling found in codebase
7. **Recommendations**: Which variation to use when

AVAILABLE SKILLS (contextual suggestions):
- No additional skills typically needed for codebase pattern analysis
```

## SKILL MAPPING

Skills provide specialized guidance for pattern search workflows.

### Mandatory Skills for Pattern Search (Step 0)

| Skill | Purpose | When to Load | Expected Benefit |
|-------|---------|--------------|------------------|
| agent-delegation | 5-requirement prompt framework, validation checklist | Always (Step 0) | Well-structured prompts for memory-assistant and pattern-analyzer |
| context-synthesis | Multi-source pattern integration, priority ranking | Always (Step 0) | Unified pattern guide combining memory and codebase insights |
| result-aggregation | Parallel search output validation, duplicate detection | Always (Step 0) | Quality control for pattern reports |

**Loading Pattern**:
```
Step 0: Load Orchestration Skills
0. Invoke all required skills:
   - Skill("orchestrator-core:agent-delegation")
   - Skill("orchestrator-core:context-synthesis")
   - Skill("orchestrator-core:result-aggregation")
```

### Contextual Skills for Pattern Search Agents

| Skill | Suggest When | Agent Types | Expected Benefit |
|-------|--------------|-------------|------------------|
| N/A | Pattern search agents use Neo4j and codebase tools | memory-assistant, pattern-analyzer | Standard search tools sufficient |

**Contextual Loading Pattern** (in agent prompts):
```
AVAILABLE SKILLS (contextual suggestions):
- memory-assistant: Use Neo4j memory search tools
- pattern-analyzer: Use standard codebase search tools (Grep, Glob, Read)
```

**Step 1: Deploy Pattern Search**
1. **Deploy pattern search agents in parallel using agent-delegation principles**:
   - Launch in a single message:
     - memory-assistant (search Neo4j knowledge graph for similar problems, past solutions, lessons learned)
     - pattern-analyzer (discover patterns in current codebase across ALL projects)

2. **Wait for both agent reports**

3. **Synthesize pattern findings** using context-synthesis and result-aggregation guidance:
   - Combine memory patterns with codebase patterns
   - Identify most relevant and applicable patterns
   - Remove duplicates and contradictions
   - Prioritize by confidence and applicability

4. **Present pattern discovery guide** with:
   - Recommended pattern (highest confidence) with description and code example
   - Alternative patterns with trade-offs
   - Memory insights (past solutions, lessons learned, established conventions)
   - Project-specific variations with file:line references
   - Anti-patterns to avoid
   - Code examples by use case
   - Consistency analysis across projects
   - Implementation checklist

**Success criteria:**
- Clear recommended pattern with real code examples from codebase
- All examples include file:line references
- Confidence scores provided (High/Medium/Low)
- Consistency analysis shows project variations
- Actionable implementation guidance

**After completion:**
Suggest next steps:
- "Run `/investigate [file:line]` to understand implementation details"
- "Run `/implement [feature] following [pattern] from [file:line]`"
