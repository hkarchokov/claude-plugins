---
name: task-decomposition
description: Strategic breakdown of complex requests into phased subtasks with dependencies, success criteria, and execution order. Load when analyzing multi-step requests, identifying parallel opportunities, defining phase boundaries, or creating investigation deployment plans.
triggers:
  - decompose
  - breakdown
  - break-down
  - split
  - subtasks
  - phases
  - planning
  - organize
  - dependencies
  - execution-order
  - phase-organization
  - task-analysis
  - investigation-plan
---

# Task Decomposition Skill

## Overview

The task decomposition skill enables the orchestrator to systematically break down complex, ambiguous, or multi-faceted user requests into well-structured, manageable units of work. This skill is fundamental to effective orchestration, as it transforms high-level intentions into concrete action plans that can be delegated to specialized agents or executed in phases.

## When to Use This Skill

Apply task decomposition when:
- The user's request involves multiple distinct objectives or domains
- The request is complex enough to benefit from phased execution
- Dependencies between subtasks need to be identified and ordered
- Parallel execution opportunities should be discovered
- The scope of work needs clarification before agent deployment
- Success criteria must be established for each component
- Risk assessment requires understanding of individual task complexity

## When NOT to Use This Skill

**Do NOT use task decomposition when**:
- User request is a simple, single-step task (e.g., "read this file", "explain this function")
- Task is already clearly scoped with obvious execution path
- User is asking a straightforward question requiring direct answer
- Request is purely informational with no execution component
- Decomposition overhead would exceed task execution time
- You're in the middle of executing a bounded routine (already decomposed)
- Request is for status update, clarification, or conversation

## Decomposition Process

1. **Request Analysis**: Parse the user's request to identify explicit and implicit objectives, constraints, and success criteria
2. **Task Identification**: Extract discrete units of work that can be independently understood and executed
3. **Dependency Mapping**: Determine relationships between tasks including prerequisites, blocking dependencies, and parallel opportunities
4. **Phase Organization**: Group related tasks into logical execution phases with clear handoff points
5. **Scope Refinement**: Define boundaries, inputs, outputs, and acceptance criteria for each task
6. **Validation**: Verify the decomposition covers all aspects of the original request and identifies any ambiguities requiring clarification

## Output Structure

Task decomposition produces:
- **Task List**: Numbered or hierarchical list of subtasks with descriptions
- **Dependency Graph**: Visual or textual representation of task relationships
- **Phase Plan**: Organization of tasks into execution phases with rationale
- **Success Criteria**: Measurable outcomes for each task and overall objective
- **Risk Assessment**: Identification of high-complexity or high-risk tasks
- **Clarification Questions**: Any ambiguities requiring user input before proceeding

## Decision Criteria

**Decomposition Threshold**:
- `subtasks >= 3`: Decomposition justified → PROCEED WITH BREAKDOWN
- `subtasks = 2`: Consider decomposition if tasks are complex → USE JUDGMENT
- `subtasks = 1`: No decomposition needed → EXECUTE DIRECTLY

**Complexity Justification**:
- `estimated_steps_per_task > 5`: Complex enough for decomposition
- `multiple_domains_involved = true`: Decompose by domain (frontend, backend, DB, etc.)
- `parallel_execution_possible = true`: Decompose to enable concurrency
- `sequential_dependencies_exist = true`: Decompose to clarify execution order

**Phase Organization Threshold**:
- `tasks >= 5`: Organize into phases (investigation, planning, execution, verification)
- `tasks < 5`: Flat list acceptable unless natural phases emerge

**Decomposition Depth Limit**:
- `max_depth = 2`: Two-level hierarchy (phases → tasks, or epics → stories)
- `avoid_depth > 2`: Over-decomposition adds overhead without value

**Quality Gates**:
- `all_original_requirements_covered = true`: Decomposition is complete
- `no_orphan_tasks = true`: All tasks connect to original request
- `dependencies_make_sense = true`: Execution order is logical
- `atomic_tasks = true`: Each task is independently executable

## Integration with Other Skills

- **Agent Delegation**: Decomposition output directly informs which agents to deploy for each subtask
- **Request Clarification**: Identifies ambiguities that require user clarification before proceeding
- **Context Synthesis**: Provides structure for aggregating results from multiple subtasks
- **Workflow Management**: Establishes the execution roadmap for complex multi-phase operations

## Best Practices

- **Maintain Atomicity**: Each subtask should represent a single, focused objective
- **Preserve Context**: Include enough context in task descriptions so they're understandable in isolation
- **Be Explicit**: Make implicit assumptions and dependencies explicit
- **Stay Flexible**: Allow for adjustment as new information emerges during execution
- **Document Rationale**: Explain why tasks were grouped or ordered in specific ways
- **Verify Completeness**: Ensure decomposition covers all aspects of original request

## Example Scenarios

**Complex Feature Request**: "Add authentication to the API with JWT tokens, refresh tokens, and role-based access control"
- Decompose into: authentication mechanism, token generation, token refresh logic, RBAC system, integration testing
- Identify phases: investigation (existing auth patterns) → planning (architecture design) → implementation → testing
- Map dependencies: RBAC depends on authentication mechanism, refresh tokens depend on JWT implementation

**Cross-Cutting Investigation**: "Investigate why the application is slow"
- Decompose into: frontend performance, API response times, database query analysis, network latency, resource utilization
- Enable parallel investigation by multiple specialized agents
- Define metrics and thresholds for each area

**Infrastructure Change**: "Migrate from EC2 to ECS"
- Decompose into: containerization, ECS cluster setup, deployment pipeline, migration strategy, rollback plan
- Phase organization: assessment → planning → staging deployment → production migration → verification
- Risk assessment: identify high-risk tasks requiring manual oversight
