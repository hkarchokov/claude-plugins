---
description: Trigger full Phase 0-3 workflow (investigation + planning + execution)
argument-hint: feature to implement
skills: [agent-delegation, task-decomposition, context-synthesis, result-aggregation, workflow-management]
---

Implement: $ARGUMENTS

This is the **full Phase 0-3 workflow** - investigation, planning, and code execution.

This command orchestrates specialized agents through multiple phases using agent-delegation principles.

Follow these steps:

**Step 0: Load Orchestration Skills**
0. **Invoke all required skills** to load orchestration guidance:
   - `Skill("orchestrator-core:agent-delegation")` - Delegation best practices
   - `Skill("orchestrator-core:task-decomposition")` - Task breakdown guidance
   - `Skill("orchestrator-core:context-synthesis")` - Synthesis techniques
   - `Skill("orchestrator-core:result-aggregation")` - Result aggregation patterns
   - `Skill("orchestrator-core:workflow-management")` - Progress tracking methods

**Skill Hint Guidance**
When deploying agents, include relevant skill hints in the prompt. Available skills for implementation workflows:
- **agent-delegation**: Frameworks for 5-requirement prompts and prompt validation
- **task-decomposition**: Strategic breakdown methods for complex requests
- **context-synthesis**: Integration techniques for multi-source findings
- **result-aggregation**: Validation protocols for parallel agent outputs
- **workflow-management**: State machine for tracking multi-phase progress

## DELEGATION STRATEGY

The implement workflow is the most complex orchestration command, requiring careful delegation decisions across multiple phases (0a → 0 → 1 → 2 → 3 → 4).

### When to Delegate to Specialized Agents

**Delegate when**:
- Feature requires understanding existing codebase patterns (use Phase 1 investigation)
- Implementation involves multiple files or complex refactoring
- Changes need careful planning to avoid breaking existing functionality
- Task benefits from separation of concerns (investigation → planning → execution)

**Handle directly when**:
- Simple file operations (creating single files, trivial edits)
- Request is clarification-only with no code changes
- Delegation overhead (6+ phases) exceeds implementation cost
- User explicitly requests direct implementation

### Phase-Specific Agent Selection

| Phase | Agent Type | When to Use | Expected Output |
|-------|------------|-------------|-----------------|
| 0a (Optional) | request-clarifier | User explicitly requests clarification or request is highly ambiguous | CONTEXT REPORT with structured requirements |
| 0 | task-decomposer | Always (unless trivial) | Investigation deployment plan with agent prompts |
| 1 | code-investigator, pattern-analyzer, etc. | Multi-file features, pattern matching needed | Investigation reports with file:line references |
| 2 | implementation-planner | After Phase 1 investigation | Bounded routine with step-by-step plan |
| 3 | code-executor | After Phase 2 planning | Execution report with changes made |

### Phase Skip Assessment

**Skip Phase 1 (Investigation) when**:
- Request is trivial/clear (simple file operations, no complexity analysis needed)
- User provides explicit implementation instructions
- No existing patterns need to be discovered

**Skip Phase 0a (Clarification) unless**:
- User explicitly requests clarification ("clarify", "I want to clarify")
- Request is highly ambiguous with multiple valid interpretations

## 3-STAGE WORKFLOW GUIDE

The implement workflow operates across multiple phases, with each phase following the 3-stage pattern internally.

### Stage 1: Setup & Multi-Phase Planning (REQUIRED - Use Sequential Thinking)

**Mandatory Skills** (Step 0):
- Load all skills listed in command metadata before workflow execution
- `Skill("orchestrator-core:agent-delegation")`
- `Skill("orchestrator-core:task-decomposition")`
- `Skill("orchestrator-core:context-synthesis")`
- `Skill("orchestrator-core:result-aggregation")`
- `Skill("orchestrator-core:workflow-management")`

**Planning with Sequential Thinking**:
Use `mcp__sequential-thinking__sequentialthinking` to:
- Analyze implementation request complexity
- Determine which phases to execute (0a? 1? or skip to 2/3?)
- Plan agent deployment for each active phase
- Define success criteria for entire workflow
- Estimate total workflow complexity (token budget, time)

**Pre-Execution Checklist**:
- [ ] All mandatory skills loaded
- [ ] Phase execution plan determined (which phases to run)
- [ ] Phase 0a decision made (clarify or skip)
- [ ] Phase 1 decision made (investigate or skip to planning)
- [ ] Overall success criteria defined

### Stage 2: Multi-Phase Execution

**Phase 0a - Request Clarification (OPTIONAL)**:
- Deploy request-clarifier only if user explicitly requests
- Output: CONTEXT REPORT with structured requirements

**Phase 0 - Prompt Engineering**:
- Deploy task-decomposer with CONTEXT REPORT
- Output: Investigation deployment plan
- Skip Phase 1 if request is trivial/clear

**Phase 1 - Investigation (CONDITIONAL)**:
- Deploy investigation agents in **parallel** (single message)
- Output: Investigation reports with patterns, architecture, dependencies
- Synthesize findings using context-synthesis

**Phase 2 - Planning**:
- Deploy implementation-planner with synthesized findings
- Output: Bounded routine with step-by-step plan, circuit breakers, verification criteria

**Phase 3 - Execution**:
- Deploy code-executor with complete routine
- Output: Execution report with changes made, verification results

**Sequential Thinking (OPTIONAL)**:
May be used between phases for adaptive decision-making if workflow reveals unexpected complexity.

### Stage 3: Verification & Validation (REQUIRED - Use Sequential Thinking)

**Use Sequential Thinking to**:
- Review execution report for completeness
- Verify all planned changes were made
- Check circuit breakers were not triggered
- Validate changes follow discovered patterns
- Ensure all success criteria met
- Assess code quality before suggesting review

**Output Validation Checklist**:
- [ ] All phases completed successfully
- [ ] Execution report shows successful verification
- [ ] Changes made match planned steps
- [ ] Circuit breakers not triggered
- [ ] Code follows patterns discovered in Phase 1
- [ ] Files modified documented with descriptions

### Phase 4: Review & Present

**Final Steps**:
- Review execution report and verify changes
- Present summary with changes made, verification results, files modified
- Strongly recommend: "Run `/review` to validate code quality before committing"

## AGENT PROMPT TEMPLATES

The implement workflow requires phase-specific agent prompts using the **5-requirement format**.

**5-Requirement Format**:
1. **ROLE**: Agent's identity and expertise domain
2. **CONTEXT**: Relevant background, project specifics, constraints
3. **TASK**: Single, measurable objective with clear boundaries
4. **CONSTRAINTS**: Scope limits, token budgets, time limits, circuit breakers
5. **OUTPUT**: Exact deliverable format with verification criteria

### Template: request-clarifier for Phase 0a

```
ROLE:
You are a request-clarifier specializing in extracting structured requirements from vague or ambiguous implementation requests.

CONTEXT:
- User request: [USER_REQUEST]
- Ambiguity level: [High/Medium based on analysis]
- Project context: [PROJECT_TYPE, existing files]

TASK:
Extract structured requirements through interactive questioning:
1. Use sequential thinking to identify ambiguities and missing information
2. Formulate targeted clarifying questions
3. Ask user questions using AskUserQuestion tool
4. Process user responses and extract requirements
5. Produce comprehensive CONTEXT REPORT

CONSTRAINTS:
- Token Budget: [e.g., 10000 tokens]
- Ask 1-4 questions maximum per round
- Focus on critical unknowns (scope, success criteria, constraints)
- Circuit Breaker: Stop after 2 rounds of questions

OUTPUT:
Provide a CONTEXT REPORT with:
1. **Request Analysis**: Ambiguity level, questions asked, assumptions
2. **Clarification Q&A**: Questions, answers, interpretations
3. **Structured Requirements**: Functional, non-functional, scope boundaries, success criteria
4. **Constraints**: Technical, business, user preferences
5. **Project Context**: Directories, files, dependencies
6. **Assumptions & Risks**: With mitigation strategies
7. **Recommended Approach**: Next steps for implementation

AVAILABLE SKILLS (contextual suggestions):
- Use sequential thinking tool throughout for analysis and question formulation
```

### Template: task-decomposer for Phase 0

```
ROLE:
You are a task-decomposer specializing in creating comprehensive investigation deployment plans for implementation workflows.

CONTEXT:
- Implementation request: [USER_REQUEST or CONTEXT_REPORT from Phase 0a]
- Project: [PROJECT_TYPE]
- Complexity assessment: [HIGH/MEDIUM/LOW]

TASK:
Create investigation deployment plan:
1. Analyze request complexity and scope
2. Recommend Phase 1 skip or execution (with justification)
3. If executing Phase 1: Identify which investigation agents to deploy
4. For each agent: Write complete 5-requirement prompt
5. Define success criteria for investigation phase
6. Specify parallel vs sequential execution pattern

CONSTRAINTS:
- Token Budget: [e.g., 15000 tokens]
- Agent selection: Choose 2-4 investigation agents maximum
- Each agent prompt must follow 5-requirement format
- Circuit Breaker: Recommend skipping Phase 1 if request is trivial

OUTPUT:
Provide a DEPLOYMENT PLAN with:
1. **Phase 1 Assessment**: SKIP or EXECUTE with justification
2. **Agent Selection**: List of agents to deploy with rationale
3. **Agent Prompts**: Complete 5-requirement prompts for each agent
4. **Execution Pattern**: PARALLEL or SEQUENTIAL with reasoning
5. **Success Criteria**: What investigation must accomplish
6. **Estimated Complexity**: Token budget, time estimate

AVAILABLE SKILLS (contextual suggestions):
- Load `Skill("orchestrator-core:task-decomposition")` for breakdown guidance
- Use sequential thinking for complexity analysis
```

### Template: implementation-planner for Phase 2

```
ROLE:
You are an implementation-planner specializing in creating bounded implementation routines from investigation findings.

CONTEXT:
- Investigation findings: [SYNTHESIZED_REPORTS from Phase 1]
- Implementation request: [USER_REQUEST]
- Project: [PROJECT_TYPE]
- Patterns discovered: [KEY_PATTERNS from investigation]

TASK:
Create bounded implementation routine:
1. Analyze investigation findings and extract actionable insights
2. Design step-by-step implementation plan
3. Define scope boundaries (files to modify, files to preserve)
4. Set circuit breakers (token budget, step count, time limit)
5. Specify verification criteria for each step
6. Include pattern adherence requirements

CONSTRAINTS:
- Token Budget: [e.g., 20000 tokens for execution phase]
- Step count: [e.g., 10-15 steps maximum]
- File scope: [e.g., "Only modify files in src/ directory"]
- Circuit Breaker: Executor must stop if exceeding budget or step count

OUTPUT:
Provide a BOUNDED ROUTINE with:
1. **Implementation Plan**: Step-by-step instructions (numbered, sequential)
2. **Scope Boundaries**:
   - Whitelist: Files/directories that MAY be modified
   - Blacklist: Files/directories that MUST NOT be modified
3. **Circuit Breakers**:
   - Token budget limit
   - Maximum step count
   - Time limit (if applicable)
   - Failure conditions requiring immediate stop
4. **Verification Criteria**: Per-step validation requirements
5. **Pattern Adherence**: Requirements from investigation
6. **Success Criteria**: Overall completion definition

AVAILABLE SKILLS (contextual suggestions):
- Use sequential thinking for plan design and validation
```

### Template: code-executor for Phase 3

```
ROLE:
You are a code-executor specializing in following bounded implementation routines with strict adherence to constraints.

CONTEXT:
- Bounded routine: [COMPLETE_ROUTINE from Phase 2]
- Project: [PROJECT_TYPE]
- Scope boundaries: [WHITELIST/BLACKLIST from routine]
- Circuit breakers: [TOKEN_BUDGET, STEP_COUNT, TIME_LIMIT]

TASK:
Execute the bounded routine:
1. Follow each step in exact sequence
2. Verify each step before proceeding to next
3. Monitor circuit breakers continuously
4. Report any violations or blockers immediately
5. Complete all verification criteria
6. Produce execution report

CONSTRAINTS:
- STRICT adherence to routine steps (no deviations)
- STOP immediately if circuit breaker triggered
- STOP if step verification fails
- Token Budget: [FROM_ROUTINE]
- Maximum Steps: [FROM_ROUTINE]
- Scope: Only modify whitelisted files

OUTPUT:
Provide an EXECUTION REPORT with:
1. **Steps Completed**: List of completed steps with results
2. **Changes Made**: Files modified with descriptions
3. **Verification Results**: Per-step validation outcomes
4. **Circuit Breaker Status**: Budget remaining, steps used
5. **Blockers Encountered**: Any issues or violations
6. **Success Assessment**: Overall completion status

AVAILABLE SKILLS (contextual suggestions):
- Use sequential thinking for step verification
- If working with specific file types: Load appropriate skills (e.g., document-skills)
```

## SKILL MAPPING

Skills provide specialized guidance for the multi-phase implementation workflow.

### Mandatory Skills for Implementation (Step 0)

| Skill | Purpose | When to Load | Expected Benefit |
|-------|---------|--------------|------------------|
| agent-delegation | 5-requirement prompt framework, validation checklist | Always (Step 0) | Well-structured agent prompts across all phases |
| task-decomposition | Strategic breakdown for complex implementations | Always (Step 0) | Effective Phase 0 planning, phase skip assessment |
| context-synthesis | Multi-source findings integration | Always (Step 0) | Unified insights from Phase 1 investigation |
| result-aggregation | Parallel agent output validation | Always (Step 0) | Quality control for Phase 1 reports |
| workflow-management | Multi-phase state tracking, progress monitoring | Always (Step 0) | Phase transition management, stall detection |

**Loading Pattern**:
```
Step 0: Load Orchestration Skills
0. Invoke all required skills:
   - Skill("orchestrator-core:agent-delegation")
   - Skill("orchestrator-core:task-decomposition")
   - Skill("orchestrator-core:context-synthesis")
   - Skill("orchestrator-core:result-aggregation")
   - Skill("orchestrator-core:workflow-management")
```

### Contextual Skills for Implementation Agents

| Skill | Suggest When | Agent Types | Expected Benefit |
|-------|--------------|-------------|------------------|
| request-clarification | Phase 0a executing | request-clarifier | Ambiguity detection, targeted questioning |
| project-detection | Project type unknown | code-investigator | Accurate project type detection |
| document-skills:* | Working with docs/spreadsheets/PDFs | code-executor | Proper document manipulation |

**Contextual Loading Pattern** (in agent prompts):
```
AVAILABLE SKILLS (contextual suggestions):
- For Phase 0a: Load Skill("orchestrator-core:request-clarification")
- If project type unknown: Consider loading Skill("orchestrator-core:project-detection")
- For document work: Load appropriate Skill("document-skills:pdf|docx|xlsx|pptx")
```

**Phase 0a: Request Validation (OPTIONAL)**
0. **Deploy request-clarifier** only if user explicitly requests clarification (e.g., "clarify", "I want to clarify")
   - Use when: User mentions "clarify", asks for help clarifying, or request is highly ambiguous
   - Skip when: Request is clear and specific with defined scope
   - Produces CONTEXT REPORT with structured requirements if deployed

**Phase 0: Prompt Engineering**

**Agent Prompt Validation**: Follow agent-delegation:prompt-validation checklist

1. **Deploy task-decomposer** with CONTEXT REPORT from Phase 0a:
   - Create comprehensive deployment plan including investigation agents, scope, and success criteria

**Phase 1 Skip Assessment**: Skip investigation if request is trivial/clear (simple file operations, clarification only, no complexity). Otherwise proceed to deployment.

**Phase 1: Investigation**

**Agent Prompt Validation**: Follow agent-delegation:prompt-validation checklist

2. **Deploy investigation agents in parallel** based on the deployment plan:
   - Launch all agents in a single message
3. **Wait for all investigation reports** and synthesize findings using context-synthesis guidance

**Phase 2: Planning**

**Agent Prompt Validation**: Follow agent-delegation:prompt-validation checklist

4. **Deploy implementation-planner** with synthesized investigation findings:
   - Create bounded routine with:
     - Step-by-step implementation plan
     - Scope boundaries (whitelist/blacklist)
     - Circuit breakers (token budget, step count, time limit)
     - Verification criteria

**Phase 3: Execution**

**Agent Prompt Validation**: Follow agent-delegation:prompt-validation checklist

5. **Deploy code-executor** with the complete routine from Phase 2
6. **Wait for execution report** with changes made and verification results

**Phase 4: Review & Present**
7. **Review execution report** and verify changes
8. **Present summary** with:
   - Changes made (files modified)
   - Verification results
   - Files modified with descriptions

**Success criteria:**
- All phases completed in sequence
- Execution report shows successful verification
- Changes follow patterns discovered in investigation
- Circuit breakers not triggered

**After completion:**
Strongly recommend: "Run `/review` to validate code quality before committing"
