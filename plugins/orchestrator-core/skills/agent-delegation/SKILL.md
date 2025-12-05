---
name: agent-delegation
description: Framework for deploying and coordinating specialized agents with 5-requirement prompts (ROLE/CONTEXT/TASK/CONSTRAINTS/OUTPUT). Load when creating agent deployment plans, crafting agent prompts, validating prompt quality, or determining parallel vs sequential execution.
triggers:
  - delegate
  - deploy-agent
  - assign
  - agents
  - deployment
  - parallel
  - subagents
  - orchestrate
  - agent-prompts
  - 5-requirement
  - prompt-validation
  - agent-coordination
  - task-assignment
---

# Agent Delegation Skill

## Overview

The agent delegation skill empowers the orchestrator to deploy, coordinate, and manage specialized agents that execute specific subtasks. This skill transforms task plans into concrete agent deployments, managing the full lifecycle from agent selection through result collection and aggregation. It enables parallel execution, specialization, and efficient resource utilization in complex workflows.

## When to Use This Skill

Apply agent delegation when:
- Multiple independent subtasks can be executed in parallel
- Specialized expertise or domain knowledge is required for specific tasks
- Task complexity warrants focused attention from a dedicated agent
- Investigation requires gathering information from multiple sources simultaneously
- Implementation involves changes across multiple domains or subsystems
- Workload distribution can improve overall execution efficiency
- Result aggregation from multiple sources is needed

## When NOT to Use This Skill

**Do NOT use agent delegation when**:
- Task is simple coordination or status reporting (orchestrator handles directly)
- Immediate user interaction is required (agents can't interact with user mid-task)
- You need to make strategic decisions requiring full context (orchestrator's role)
- Reading a single known file (use Read tool directly)
- Delegation overhead exceeds task complexity (simple grep/glob operations)
- You're already inside an agent (agents don't delegate to other agents)
- Task requires iterative back-and-forth dialogue (agents execute bounded tasks)
- User explicitly requests orchestrator to handle directly

## Delegation Process

1. **Task Analysis**: Review decomposed tasks to identify delegation candidates and dependencies
2. **Agent Matching**: Select appropriate agent types based on task requirements and specializations
3. **Context Packaging**: Prepare focused context for each agent including task description, constraints, and relevant information
4. **Deployment Strategy**: Determine execution order (parallel vs sequential) based on dependencies
5. **Agent Deployment**: Launch agents with prepared context and monitor initialization
6. **Progress Tracking**: Monitor execution status and detect completion or blocking issues
7. **Result Collection**: Gather agent outputs and validate against success criteria
8. **Aggregation**: Synthesize results from multiple agents into coherent overall output

## Delegation Guidance

### When to Delegate vs Execute Directly

**Delegate to specialized agents when**:
- Task requires domain-specific expertise (investigation, planning, code execution, quality review)
- Work involves multiple files or complex dependencies
- Clear boundaries and success criteria can be defined
- Task benefits from focused, single-responsibility approach
- Token budget or context limits are approaching

**Execute directly when**:
- Task is simple coordination or status reporting
- Immediate user interaction is required
- Decision requires orchestrator's full context
- Delegation overhead exceeds execution cost
- Agent preparation would be more complex than direct execution

### Effective Agent Prompt Preparation

Prepare agent prompts using the **5-requirement format**:

1. **ROLE**: Define agent's identity and capabilities (e.g., "You are an investigation specialist")
2. **CONTEXT**: Provide relevant background, constraints, and project information
3. **TASK**: State specific, measurable objective with clear boundaries
4. **CONSTRAINTS**: Define scope limits, token budgets, time limits, circuit breakers
5. **OUTPUT**: Specify exact deliverable format, verification criteria, and success indicators

**Template Structure**:
```
You are a [ROLE] with expertise in [DOMAIN].

CONTEXT:
- [Relevant background]
- [Key constraints]
- [Project specifics]

TASK:
[Single clear objective with measurable outcome]

CONSTRAINTS:
- Scope: [Whitelist/blacklist]
- Budget: [Token/time limits]
- Boundaries: [What to avoid]

OUTPUT:
[Exact format with verification criteria]
```

### Agent Prompt Validation Checklist

Before deploying any agent, validate the prompt meets all 5 requirements:

**Validation Checklist**:
- [ ] ROLE: Agent identity and expertise clearly defined
- [ ] CONTEXT: Background, constraints, and project information provided
- [ ] TASK: Specific, measurable objective stated with clear boundaries
- [ ] CONSTRAINTS: Scope limits, token budgets, time limits, circuit breakers defined
- [ ] OUTPUT: Exact deliverable format and verification criteria specified

**Quality Indicators**:
- Agent requires no clarification to start execution
- Agent produces expected output format without interpretation
- Agent completes within defined constraints
- Output requires no correction or reformatting
- Next workflow step can proceed immediately with agent's output

**Reference**: Commands should include `Follow agent-delegation:prompt-validation checklist` instead of duplicating validation blocks.

### Delegation Pattern Examples

**Good Delegation Pattern**:
```
ROLE: Investigation specialist
CONTEXT: Django project, need to understand auth system before adding OAuth
TASK: Map authentication flow, identify extension points, document dependencies
CONSTRAINTS: Focus on /auth/ directory only, max 10 files, 30-minute limit
OUTPUT: Structured report with FILES FOUND, CODE PATTERNS, RECOMMENDATIONS sections
```
Result: Agent has clear boundaries, measurable deliverables, focused scope.

**Bad Delegation Pattern**:
```
"Investigate the authentication system and maybe look at how we could add OAuth or improve security."
```
Problems: Vague objective, no boundaries, multiple unclear tasks, no output format, no constraints.

**Good Pattern Indicators**:
- Single, testable objective
- Explicit file/directory scope
- Clear success criteria
- Defined output structure
- Stated constraints and limits

**Bad Pattern Indicators**:
- Multiple objectives in one delegation
- Open-ended scope ("look around", "explore")
- Vague deliverables ("tell me what you think")
- No time or token limits
- Missing context or background

### Agent Selection Criteria

**Choose the right agent based on task characteristics**:

| Task Type | Recommended Agent | Key Indicators |
|-----------|------------------|----------------|
| Understanding codebase structure | Investigation Specialist | Need to find files, patterns, dependencies |
| Defining implementation steps | Planning Specialist | Have investigation findings, need bounded routine |
| Making code changes | Code Executor | Have clear plan, need mechanical execution |
| Assessing quality | Quality Reviewer | Code complete, need validation against standards |
| User clarification | Interactive Clarifier | Ambiguous requirements, need structured questions |

**Decision Criteria**:
1. **Primary skill needed**: What's the core capability required?
2. **Input available**: Do you have what the agent needs to start?
3. **Output required**: Does the agent produce what you need next?
4. **Context size**: Can the agent work within token limits?
5. **Dependency chain**: Is this agent's output needed for the next step?

### Handoff Protocols

**Pre-Delegation Checklist**:
- [ ] Agent role and capabilities defined
- [ ] Complete context prepared (no missing information)
- [ ] Single, clear task articulated
- [ ] Constraints and boundaries explicit
- [ ] Output format and verification criteria specified
- [ ] Rollback strategy defined
- [ ] Token budget allocated

**During Delegation**:
- Monitor for scope violations or constraint breaches
- Validate intermediate outputs against success criteria
- Be prepared to halt and redirect if agent diverges
- Track token consumption against budget

**Post-Delegation**:
- Verify deliverable meets all specified criteria
- Validate output format matches requirements
- Check for scope boundary compliance
- Extract learnings for future delegations
- Update coordination state with outcomes

**Handoff Quality Indicators**:
- Agent requires no clarification to start
- Agent produces expected output format
- Agent completes within constraints
- Output requires no interpretation or correction
- Next step can proceed immediately with agent's output

## Agent Types and Specializations

### Investigation Agents
- **Codebase Analyzer**: Examine existing code structure, patterns, and conventions
- **Dependency Mapper**: Trace dependencies and impact across codebase
- **Pattern Finder**: Search for existing solutions and established patterns
- **Documentation Reviewer**: Analyze documentation and architectural decisions

### Planning Agents
- **Architecture Designer**: Create technical designs and system architectures
- **Implementation Planner**: Develop detailed implementation routines
- **Risk Assessor**: Identify risks and mitigation strategies

### Execution Agents
- **Code Executor**: Implement changes following implementation routines
- **Test Generator**: Create test cases and validation scripts
- **Documentation Writer**: Generate or update documentation

### Review Agents
- **Code Reviewer**: Assess code quality, security, and best practices
- **Impact Analyzer**: Evaluate cross-project implications of changes
- **Verification Agent**: Confirm changes meet requirements and pass tests

## Output Structure

Agent delegation produces:
- **Deployment Plan**: List of agents to deploy with execution order and rationale
- **Context Packages**: Prepared context for each agent with task details and constraints
- **Dependency Graph**: Visual representation of agent execution dependencies
- **Progress Report**: Status tracking for all deployed agents
- **Result Summary**: Aggregated outputs from completed agents
- **Issue Log**: Any blockers, failures, or clarifications needed

## Integration with Other Skills

- **Task Decomposition**: Receives structured task plans that inform agent deployment decisions
- **Request Clarification**: Identifies when agent execution is blocked by ambiguities requiring user input
- **Context Synthesis**: Aggregates results from multiple agents into coherent summaries
- **Workflow Management**: Coordinates agent execution within broader multi-phase workflows

## Best Practices

- **Right-Sized Context**: Provide agents with relevant context without information overload
- **Clear Boundaries**: Define explicit scope and constraints for each agent to prevent overlap
- **Explicit Dependencies**: Make agent dependencies clear to avoid race conditions or missing prerequisites
- **Failure Handling**: Plan for agent failures with retry logic and fallback strategies
- **Result Validation**: Verify agent outputs meet success criteria before proceeding
- **Avoid Over-Delegation**: Not every task benefits from agent deployment; use judgment
- **Maintain Coherence**: Ensure multiple agents' outputs can be integrated cohesively

## Coordination Patterns

### Parallel Fan-Out
Deploy multiple independent agents simultaneously for investigation or parallel implementation tasks. Collect and synthesize results once all agents complete.

### Sequential Pipeline
Deploy agents in sequence where each agent's output becomes input for the next. Common in investigation → planning → implementation workflows.

### Hierarchical Delegation
Deploy coordinator agents that themselves deploy and manage sub-agents. Useful for very complex tasks requiring multiple levels of decomposition.

### Conditional Deployment
Deploy agents conditionally based on results from previous agents. Enables adaptive workflows that respond to discovered requirements or constraints.

## Example Scenarios

**Parallel Investigation**: User requests understanding of authentication system
- Deploy: codebase-analyzer (auth module), dependency-mapper (auth usage), pattern-finder (similar auth patterns), documentation-reviewer (auth docs)
- Execute: All agents run in parallel
- Synthesize: Combine findings into comprehensive authentication system overview

**Sequential Implementation**: User requests new feature with full workflow
- Phase 1: Deploy investigation agents in parallel
- Phase 2: Deploy implementation-planner with investigation results
- Phase 3: Deploy code-executor with implementation routine
- Phase 4: Deploy verification-agent to confirm success

**Conditional Workflow**: User requests database optimization
- Deploy: performance-analyzer to identify bottlenecks
- Conditional: Based on findings, deploy query-optimizer OR schema-redesigner OR indexing-specialist
- Validate: Deploy verification-agent to confirm improvements
