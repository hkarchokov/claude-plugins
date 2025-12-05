---
description: Interactive requirement clarification for vague or ambiguous requests
argument-hint: topic or request to clarify
skills: [agent-delegation, request-clarification]
---

Clarify: $ARGUMENTS

This extracts **structured requirements from vague or ambiguous requests** through interactive questioning. No code modifications will be made.

Follow these steps:

**Step 0: Load Orchestration Skills**
0. **Invoke all required skills** to load clarification guidance:
   - `Skill("orchestrator-core:agent-delegation")` - Delegation best practices
   - `Skill("orchestrator-core:request-clarification")` - Clarification techniques
**Skill Hint Guidance**
When deploying agents, include relevant skill hints in the prompt. Available skills for clarification workflows:
- **agent-delegation**: Frameworks for 5-requirement prompts and deploying request-clarifier agents
- **request-clarification**: Ambiguity detection methods and targeted questioning techniques

## DELEGATION STRATEGY

When executing clarification workflows, deciding whether to delegate to a specialized agent or handle clarification directly is critical for extracting structured requirements.

### When to Delegate to request-clarifier Agent

**Delegate when**:
- User explicitly requests clarification (mentions "clarify", asks for help clarifying)
- Request is highly ambiguous with multiple valid interpretations
- Scope boundaries are undefined (unclear what's in/out of scope)
- Missing critical information (success criteria, constraints, technical requirements)
- Systematic questioning process would benefit from specialized expertise

**Handle directly when**:
- Request is already clear and specific with defined scope
- Simple confirmation needed (1-2 yes/no questions)
- User provided detailed requirements upfront
- Clarification overhead exceeds value added

### Agent Selection Guide for Clarification

| Task Type | Recommended Agent | When to Use | Expected Output |
|-----------|------------------|-------------|-----------------|
| Requirement extraction | request-clarifier | Vague/ambiguous requests, missing information | CONTEXT REPORT with structured requirements |

## 3-STAGE WORKFLOW GUIDE

All clarification workflows follow a 3-stage pattern to ensure comprehensive requirement extraction.

### Stage 1: Setup & Ambiguity Detection (REQUIRED - Use Sequential Thinking)

**Mandatory Skills** (Step 0):
- Load all skills listed in command metadata before workflow execution
- `Skill("orchestrator-core:agent-delegation")`
- `Skill("orchestrator-core:request-clarification")`

**Planning with Sequential Thinking**:
Use `mcp__sequential-thinking__sequentialthinking` to:
- Analyze user request for ambiguities and missing information
- Determine if clarification is warranted (see DELEGATION STRATEGY)
- If delegating: Plan question formulation strategy
- Define success criteria for clarification

**Pre-Execution Checklist**:
- [ ] All mandatory skills loaded
- [ ] Ambiguity assessment completed
- [ ] Delegation decision made (delegate vs handle directly)
- [ ] If delegating: Agent prompt validated against 5-requirement format

### Stage 2: Interactive Clarification Execution

**SEQUENTIAL Execution Pattern**:
- Deploy request-clarifier agent
- Agent uses sequential thinking to identify ambiguities
- Agent formulates targeted questions
- Agent asks user questions using AskUserQuestion tool
- Agent processes responses iteratively (may ask 1-4 questions per round, max 2 rounds)
- Agent produces CONTEXT REPORT

**Sequential Thinking (REQUIRED in agent)**:
Agent MUST use sequential thinking for:
- Ambiguity detection and analysis
- Question formulation and prioritization
- Response interpretation and requirement extraction

### Stage 3: Validation & Presentation (REQUIRED - Use Sequential Thinking)

**Use Sequential Thinking to**:
- Review CONTEXT REPORT for completeness
- Validate structured requirements are clear and measurable
- Verify scope boundaries are well-defined (in scope, out of scope, uncertain)
- Ensure success criteria are testable
- Confirm assumptions and risks are documented
- Verify user understands and confirms requirements

**Output Validation Checklist**:
- [ ] CONTEXT REPORT complete with all required sections
- [ ] All ambiguities identified and resolved through questions
- [ ] Structured requirements (functional, non-functional) documented
- [ ] Scope boundaries clearly defined
- [ ] Success criteria measurable and testable
- [ ] Constraints (technical, business, preferences) captured
- [ ] Assumptions and risks with mitigation strategies
- [ ] Recommended next steps provided

## AGENT PROMPT TEMPLATES

When delegating to the request-clarifier agent, use the **5-requirement format** to ensure clarity and completeness.

**5-Requirement Format**:
1. **ROLE**: Agent's identity and expertise domain
2. **CONTEXT**: Relevant background, project specifics, constraints
3. **TASK**: Single, measurable objective with clear boundaries
4. **CONSTRAINTS**: Scope limits, token budgets, time limits, circuit breakers
5. **OUTPUT**: Exact deliverable format with verification criteria

### Template: request-clarifier for Requirement Extraction

```
ROLE:
You are a request-clarifier specializing in extracting structured requirements from vague or ambiguous user requests through systematic questioning.

CONTEXT:
- User request: [USER_REQUEST]
- Ambiguity level: [High/Medium based on initial analysis]
- Project context: [PROJECT_TYPE, existing files/directories if known]
- Background: [Why clarification is needed]

TASK:
Extract structured requirements through interactive clarification:
1. Use sequential thinking to identify:
   - Ambiguities in request (multiple interpretations)
   - Missing critical information (scope, success criteria, constraints)
   - Unclear boundaries (what's in scope vs out of scope)
2. Formulate targeted clarifying questions prioritized by importance
3. Ask user questions using AskUserQuestion tool (1-4 questions per round)
4. Process user responses and extract structured requirements
5. Produce comprehensive CONTEXT REPORT

CONSTRAINTS:
- Token Budget: [e.g., 10000 tokens]
- Question rounds: Maximum 2 rounds of questions
- Questions per round: 1-4 questions
- Focus on critical unknowns (scope, success criteria, constraints, technical requirements)
- Circuit Breaker: Stop after 2 rounds or if user requests to proceed

OUTPUT:
Provide a comprehensive CONTEXT REPORT with:
1. **Request Analysis**:
   - Original request interpretation
   - Ambiguity level (High/Medium/Low)
   - Questions asked and reasoning
   - Assumptions made during analysis
2. **Clarification Q&A**:
   - Each question with user's answer
   - Interpretation of responses
   - How answers resolved ambiguities
3. **Structured Requirements**:
   - Functional requirements (what system must do)
   - Non-functional requirements (performance, security, usability)
   - Scope boundaries (in scope, out of scope, uncertain)
   - Success criteria (measurable, testable)
4. **Constraints**:
   - Technical constraints (frameworks, APIs, compatibility)
   - Business constraints (deadlines, resources, priorities)
   - User preferences (style, approach, tools)
5. **Project Context**:
   - Relevant directories and files
   - Dependencies and integrations
   - Existing patterns to follow
6. **Assumptions & Risks**:
   - Assumptions made with confidence levels
   - Identified risks with severity
   - Mitigation strategies for each risk
7. **Recommended Approach**:
   - Suggested next steps (/implement, /investigate, or manual work)
   - Reasoning for recommendation
   - Alternative approaches considered

AVAILABLE SKILLS (contextual suggestions):
- REQUIRED: Use sequential thinking tool throughout for ambiguity detection, question formulation, and response analysis
- Load `Skill("orchestrator-core:request-clarification")` for systematic clarification guidance
```

## SKILL MAPPING

Skills provide specialized guidance for clarification workflows.

### Mandatory Skills for Clarification (Step 0)

| Skill | Purpose | When to Load | Expected Benefit |
|-------|---------|--------------|------------------|
| agent-delegation | 5-requirement prompt framework, validation checklist | Always (Step 0) | Well-structured prompt for request-clarifier agent |
| request-clarification | Ambiguity detection methods, targeted questioning techniques | Always (Step 0) | Systematic clarification process, comprehensive CONTEXT REPORT |

**Loading Pattern**:
```
Step 0: Load Orchestration Skills
0. Invoke all required skills:
   - Skill("orchestrator-core:agent-delegation")
   - Skill("orchestrator-core:request-clarification")
```

### Contextual Skills for request-clarifier Agent

| Skill | Suggest When | Agent Types | Expected Benefit |
|-------|--------------|-------------|------------------|
| request-clarification | Always for clarification workflows | request-clarifier | Systematic ambiguity detection, question formulation strategies |

**Contextual Loading Pattern** (in agent prompts):
```
AVAILABLE SKILLS (contextual suggestions):
- REQUIRED: Use sequential thinking tool throughout
- Load Skill("orchestrator-core:request-clarification") for systematic clarification guidance
```

**Step 1: Deploy Clarifier**

**Agent Prompt Validation**: Follow agent-delegation:prompt-validation checklist

1. **Deploy request-clarifier agent using agent-delegation principles**:
   - Agent tasks:
     - Use sequential thinking to identify ambiguities, missing information, and unclear scope
     - Formulate targeted clarifying questions based on analysis
     - Ask user questions interactively using AskUserQuestion tool
     - Process responses and extract structured requirements
     - Produce comprehensive CONTEXT REPORT

2. **Wait for CONTEXT REPORT** with:
   - Request analysis (ambiguity level, questions asked, assumptions)
   - Clarification Q&A (questions, answers, interpretations)
   - Structured requirements (functional, non-functional, scope boundaries, success criteria)
   - Constraints (technical, business, preferences)
   - Project context (directories, files, dependencies)
   - Assumptions & risks with mitigation strategies
   - Recommended approach for next steps

3. **Present clarified requirements** to user:
   - Summary of structured requirements
   - Clear scope boundaries (in scope, out of scope, uncertain)
   - Success criteria for validation
   - Recommended next steps (/implement, /investigate, or manual work)

**When to use:**
- Request is vague ("make it better", "improve X")
- Scope is unclear or ambiguous
- Multiple valid interpretations exist
- Missing critical information (timeline, constraints, success criteria)
- Before starting /implement to reduce rework

**Success criteria:**
- All ambiguities identified and resolved through questions
- CONTEXT REPORT complete with structured requirements
- Clear scope boundaries defined
- Success criteria measurable and testable
- User confirms understanding

**After completion:**
Suggest next steps:
- "Run `/implement [feature]` with clarified requirements"
- "Run `/investigate [scope]` to research approach"
- "Proceed with manual implementation using CONTEXT REPORT"
