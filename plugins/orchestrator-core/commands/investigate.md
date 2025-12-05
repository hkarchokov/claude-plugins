---
description: Trigger Phase 1 investigation workflow (no code changes)
argument-hint: topic to investigate
skills: [agent-delegation, task-decomposition, context-synthesis, result-aggregation]
---

## Skills Used

This command leverages the following skills:
Investigate: $ARGUMENTS

This is a **Phase 1 investigation only** - no code changes will be made.

Follow these steps:
**Step 0: Load Orchestration Skills**
0. **Invoke all required skills** to load investigation guidance:
   - `Skill("orchestrator-core:agent-delegation")` - Delegation best practices
   - `Skill("orchestrator-core:task-decomposition")` - Investigation planning
   - `Skill("orchestrator-core:context-synthesis")` - Findings synthesis
   - `Skill("orchestrator-core:result-aggregation")` - Report aggregation
**Skill Hint Guidance**
IMPORTANT: When deploying agents, include relevant skill hints in the prompt. Available skills for investigation workflows:
- **agent-delegation**: Frameworks for 5-requirement prompts and prompt validation
- **task-decomposition**: Strategic breakdown methods for complex requests
- **context-synthesis**: Integration techniques for multi-source findings
- **result-aggregation**: Validation protocols for parallel agent outputs
- **project-detection**: Systematic project type detection (suggest to investigation agents when project type unknown)

## DELEGATION STRATEGY

When executing investigation workflows, deciding whether to delegate to specialized agents or handle tasks directly is critical for efficiency and quality.

### When to Delegate to Specialized Agents

**Delegate when**:
- Request involves multiple codebases, files, or systems requiring parallel analysis
- Investigation requires specialized domain knowledge (architecture, patterns, dependencies)
- Task benefits from focused, single-responsibility approach (one agent per concern)
- Comprehensive analysis needed across different dimensions (structure, patterns, relationships)

**Handle directly when**:
- Request is a simple query about a specific file or function
- Answer can be found with 1-2 tool calls (Read, Grep)
- Investigation scope is narrow and well-defined
- Delegation overhead exceeds execution cost

### Agent Selection Guide for Investigation

| Task Type | Recommended Agent | When to Use | Expected Output |
|-----------|------------------|-------------|-----------------|
| Codebase structure analysis | code-investigator | Multi-file exploration, understanding architecture | File inventory, component relationships, entry points |
| Pattern discovery | pattern-analyzer | Identifying conventions, standards, best practices | Pattern catalog, consistency assessment |
| Dependency mapping | dependency-mapper | Understanding module relationships, impact zones | Dependency graph, integration points |
| Quality assessment | quality-analyst | Code quality review, security analysis | Issue inventory, vulnerability report |
| Architecture review | architecture-analyst | Design patterns, system structure | Architecture diagrams, design decisions |

## 3-STAGE WORKFLOW GUIDE

All investigation workflows follow a 3-stage pattern to ensure quality execution and validation.

### Stage 1: Setup & Planning (REQUIRED - Use Sequential Thinking)

**Mandatory Skills** (Step 0):
- Load all skills listed in command metadata before workflow execution
- `Skill("orchestrator-core:agent-delegation")`
- `Skill("orchestrator-core:task-decomposition")`
- `Skill("orchestrator-core:context-synthesis")`
- `Skill("orchestrator-core:result-aggregation")`

**Planning with Sequential Thinking**:
Use `mcp__sequential-thinking__sequentialthinking` to:
- Analyze investigation request complexity
- Determine if delegation is warranted (see DELEGATION STRATEGY)
- If delegating: Identify which specialized agents to deploy
- Plan parallel vs sequential execution
- Define success criteria for investigation

**Pre-Execution Checklist**:
- [ ] All mandatory skills loaded
- [ ] Investigation complexity assessed
- [ ] Delegation decision made (delegate vs handle directly)
- [ ] If delegating: Agent selection completed
- [ ] Agent prompts validated against 5-requirement format

### Stage 2: Investigation Execution

**PARALLEL Execution Pattern**:
- Deploy multiple specialized agents in a **single message** when investigations are independent
- Common pattern: code-investigator + pattern-analyzer + dependency-mapper
- Wait for all agents to complete before synthesis

**Sequential Thinking (OPTIONAL)**:
May be used during execution for adaptive decision-making if investigation reveals unexpected complexity.

### Stage 3: Synthesis & Validation (REQUIRED - Use Sequential Thinking)

**Use Sequential Thinking to**:
- Review all investigation findings for completeness
- Cross-reference findings from multiple agents
- Identify gaps, conflicts, or inconsistencies
- Validate file:line references are specific and accurate
- Ensure all success criteria met

**Output Validation Checklist**:
- [ ] All findings include specific file:line references
- [ ] Key patterns documented with examples
- [ ] Architecture insights supported by evidence
- [ ] Dependencies clearly mapped
- [ ] Recommendations actionable and prioritized
- [ ] Multi-project scope addressed (if applicable)

## AGENT PROMPT TEMPLATES

When delegating to specialized agents, use the **5-requirement format** to ensure clarity and completeness.

**5-Requirement Format**:
1. **ROLE**: Agent's identity and expertise domain
2. **CONTEXT**: Relevant background, project specifics, constraints
3. **TASK**: Single, measurable objective with clear boundaries
4. **CONSTRAINTS**: Scope limits, token budgets, time limits, circuit breakers
5. **OUTPUT**: Exact deliverable format with verification criteria

### Template: code-investigator for Codebase Structure Analysis

```
ROLE:
You are a code-investigator specializing in codebase structure analysis and component identification.

CONTEXT:
- Project: [PROJECT_TYPE - e.g., Node.js, Python, Rust]
- Investigation scope: [DIRECTORIES/FILES to analyze]
- Background: [Why investigation needed - e.g., "Understanding authentication flow"]

TASK:
Analyze the codebase structure and identify:
1. Key components and their responsibilities
2. Entry points and initialization flows
3. Module organization and file structure
4. Integration points between components

CONSTRAINTS:
- Token Budget: [e.g., 15000 tokens]
- Focus on [SPECIFIC_AREA - e.g., "src/ directory only"]
- Do NOT make code changes
- Circuit Breaker: Stop if exceeding token budget or finding no relevant files

OUTPUT:
Provide a structured report with:
1. **Component Inventory**: List of key files/modules with purposes (file:line references)
2. **Entry Points**: Main initialization paths with call flows
3. **Module Relationships**: How components interact
4. **Integration Points**: External dependencies and APIs
5. **Recommendations**: Areas needing attention or further investigation

AVAILABLE SKILLS (contextual suggestions):
- If project type unknown: Consider loading `Skill("orchestrator-core:project-detection")`
- For dependency analysis: Note findings for dependency-mapper agent
```

### Template: pattern-analyzer for Code Convention Discovery

```
ROLE:
You are a pattern-analyzer specializing in discovering coding patterns, conventions, and architectural standards.

CONTEXT:
- Project: [PROJECT_TYPE]
- Analysis scope: [PATTERN_DOMAIN - e.g., "error handling", "API design", "state management"]
- Background: [Investigation context]

TASK:
Identify and document patterns for [PATTERN_DOMAIN]:
1. Common implementations and variations
2. Consistency across codebase
3. Best practices followed/violated
4. Architectural decisions

CONSTRAINTS:
- Token Budget: [e.g., 12000 tokens]
- Focus on [SPECIFIC_PATTERN_TYPE]
- Provide 2-3 concrete examples per pattern
- Circuit Breaker: Stop after analyzing [N] representative files

OUTPUT:
Provide a structured report with:
1. **Pattern Catalog**: Identified patterns with descriptions
2. **Examples**: Code snippets showing pattern usage (file:line references)
3. **Consistency Assessment**: How uniformly patterns are applied
4. **Violations**: Deviations from established patterns
5. **Recommendations**: Pattern improvements or standardization needs

AVAILABLE SKILLS (contextual suggestions):
- No additional skills typically needed for pattern analysis
```

### Template: dependency-mapper for Module Relationship Analysis

```
ROLE:
You are a dependency-mapper specializing in analyzing module relationships, dependencies, and impact zones.

CONTEXT:
- Project: [PROJECT_TYPE]
- Scope: [MODULES/COMPONENTS to analyze]
- Background: [Why dependency mapping needed]

TASK:
Map dependencies and relationships for [SCOPE]:
1. Direct dependencies between modules
2. Transitive dependencies
3. Integration points with external systems
4. Impact zones (what breaks if component changes)

CONSTRAINTS:
- Token Budget: [e.g., 10000 tokens]
- Focus on [SPECIFIC_LAYER - e.g., "service layer", "data layer"]
- Circuit Breaker: Stop if dependency graph exceeds [N] nodes

OUTPUT:
Provide a structured report with:
1. **Dependency Graph**: Module relationships with directions
2. **Integration Points**: External APIs, databases, services (file:line references)
3. **Impact Zones**: Components affected by changes to [SCOPE]
4. **Circular Dependencies**: Any problematic dependency cycles
5. **Recommendations**: Decoupling opportunities, risk areas

AVAILABLE SKILLS (contextual suggestions):
- For cross-project dependencies: Consider broader project context
```

## SKILL MAPPING

Skills provide specialized guidance for specific aspects of investigation workflows.

### Mandatory Skills for Investigation (Step 0)

| Skill | Purpose | When to Load | Expected Benefit |
|-------|---------|--------------|------------------|
| agent-delegation | 5-requirement prompt framework, validation checklist | Always (Step 0) | Well-structured agent prompts, quality delegation |
| task-decomposition | Strategic breakdown for complex investigations | Always (Step 0) | Effective investigation planning, parallel execution |
| context-synthesis | Multi-source findings integration | Always (Step 0) | Unified insights from multiple agents |
| result-aggregation | Parallel agent output validation | Always (Step 0) | Quality control, completeness verification |

**Loading Pattern**:
```
Step 0: Load Orchestration Skills
0. Invoke all required skills:
   - Skill("orchestrator-core:agent-delegation")
   - Skill("orchestrator-core:task-decomposition")
   - Skill("orchestrator-core:context-synthesis")
   - Skill("orchestrator-core:result-aggregation")
```

### Contextual Skills for Investigation Agents

| Skill | Suggest When | Agent Types | Expected Benefit |
|-------|--------------|-------------|------------------|
| project-detection | Project type unknown or needs validation | code-investigator | Accurate project type detection, tailored analysis |
| orchestration-guide | Agent needs workflow command reference | task-decomposer | Understanding of available commands, workflow patterns |

**Contextual Loading Pattern** (in agent prompts):
```
AVAILABLE SKILLS (contextual suggestions):
- If project type unknown: Consider loading Skill("orchestrator-core:project-detection")
- For workflow guidance: Consider loading Skill("orchestrator-core:orchestration-guide")
```

**Phase 0a: Request Validation (OPTIONAL)**
0a. **Deploy request-clarifier** only if user explicitly requests clarification (e.g., "clarify", "I want to clarify")
   - Use when: User mentions "clarify", asks for help clarifying, or request is highly ambiguous
   - Skip when: Request is clear and specific with defined scope
   - Produces CONTEXT REPORT with structured requirements if deployed

**Phase 0: Analysis & Planning (MANDATORY - Use Sequential Thinking)**

0. **Use sequential thinking to analyze the request**:
   ```
   Use mcp__sequential-thinking__sequentialthinking to:
   - Analyze investigation request complexity and scope
   - Determine if delegation is warranted (see DELEGATION STRATEGY)
   - Assess if request is simple/clear (basic query) or complex (multi-agent investigation)
   - If simple: Plan to handle directly without task-decomposer
   - If complex: Prepare context for task-decomposer deployment
   - Define success criteria for investigation
   ```

   **Decision Point**:
   - If `request_complexity = simple` (basic query, 1-2 file reads): Execute directly, skip to results
   - If `request_complexity = complex`: Proceed to Step 1 (task-decomposer deployment)

**Phase 1: Deployment Planning**

**Agent Prompt Validation**: Follow agent-delegation:prompt-validation checklist

1. **Deploy task-decomposer agent**:
   - **Input**: Investigation request + complexity analysis from Step 0
   - **Task**: Create comprehensive investigation deployment plan
   - **Required Output Format**:
     ```
     DEPLOYMENT PLAN:
     1. Investigation Scope: [What needs to be investigated]
     2. Recommended Agents: [List of 2-4 specialized agents]
     3. Execution Pattern: PARALLEL (agents are independent)
     4. Agent Prompts: [Complete 5-requirement prompts for EACH agent]

        Agent 1: [agent-type]
        ROLE: [...]
        CONTEXT: [...]
        TASK: [...]
        CONSTRAINTS: [...]
        OUTPUT: [...]

        Agent 2: [agent-type]
        [Complete 5-requirement prompt]

     5. Success Criteria: [How to validate investigation completeness]
     ```

**Phase 2: Deployment Execution**

**Agent Prompt Validation**: Validate each agent prompt from deployment plan against 5-requirement checklist

2. **Review task-decomposer's deployment plan**:
   - Verify all agent prompts follow 5-requirement format (ROLE/CONTEXT/TASK/CONSTRAINTS/OUTPUT)
   - Confirm execution pattern (PARALLEL for independent investigations)
   - Validate success criteria are measurable

3. **Execute deployment plan - Deploy investigation agents in PARALLEL**:
   - Launch ALL agents in a **single message** using task-decomposer's exact prompts
   - Common agents: code-investigator, pattern-analyzer, dependency-mapper
   - Use prompts exactly as provided by task-decomposer

**Phase 3: Result Collection & Synthesis**

4. **Wait for all agents** to return their structured reports

5. **Synthesize findings** using context-synthesis guidance:
   - Review all investigation reports for completeness
   - Cross-reference findings from multiple agents
   - Extract key insights and patterns
   - Validate file:line references are specific and accurate

6. **Present summary** with:
   - Key findings with file:line references
   - Code patterns discovered
   - Architecture insights
   - Dependencies identified
   - Recommendations (if applicable)

**Success criteria:**
- All findings include specific file:line references
- Multi-project scope addressed if relevant
- No code changes made
- Clear, actionable summary provided

**After completion:**
Suggest next steps (e.g., "Ready to implement? Use `/implement [feature]`")
