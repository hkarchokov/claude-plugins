---
name: workflow-management
description: State machine for tracking multi-phase workflow progress (Phase 0-4), detecting stalls, and reporting completion status. Load when initializing workflows, transitioning between phases, detecting blocked tasks, or generating progress reports.
triggers:
  - track-progress
  - workflow-status
  - phase-tracking
  - phase-transition
  - completion-estimate
  - detect-stalls
  - workflow-state
  - progress-report
  - stalled-workflow
  - initialize-workflow
  - update-progress
---

# Progress Tracking

## Overview

Progress tracking provides centralized workflow state management across all orchestration phases (Phase 0-4). This skill maintains the state machine for multi-phase workflows, tracks task completion, detects stalls, estimates time to completion, and reports progress to users and the orchestrator.

**Key Role**: Every other skill references "Workflow Management" as an integration point, but NO skill owns state tracking - that's this skill's responsibility.

## When to Use This Skill

Apply progress tracking when:
- Multi-phase workflow begins (initialize tracking from task plan)
- Phase transitions occur (update state machine)
- Tasks/agents start or complete (update progress counters)
- Workflow appears stalled (no progress for X minutes)
- User requests status update (generate progress report)
- Orchestrator needs to validate phase transition readiness

## When NOT to Use This Skill

**Do NOT use progress tracking when**:
- Single-step, simple tasks with no workflow (no phases to track)
- User is asking conversational questions (not executing workflow)
- You're inside an agent executing bounded task (agents don't track orchestrator state)
- TodoWrite tool is sufficient for task tracking (for simple linear task lists)
- Workflow hasn't started yet (nothing to track)
- Real-time progress is unnecessary (post-execution summary sufficient)
- Over-engineering progress tracking for trivial operations

## Process

1. **Initialize Tracking**: Accept workflow plan from task-decomposition, create state structure
2. **Start Monitoring**: Begin tracking time, set stall detection thresholds
3. **Listen for Events**: Receive notifications from all skills (task start, complete, fail, block)
4. **Update State**: Modify state machine based on events (phase transitions, task status changes)
5. **Detect Anomalies**: Check for stalls, bottlenecks, or unexpected failures
6. **Calculate Metrics**: Update progress percentage, ETA, active task count
7. **Report Status**: Provide reports on demand or at regular intervals
8. **Validate Transitions**: Check if phase completion criteria met before allowing transition

## State Structure

Progress tracking maintains a **Workflow State** object:

```json
{
  "workflow_id": "unique-id",
  "started_at": "ISO-8601",
  "updated_at": "ISO-8601",
  "current_phase": "Phase 1: Investigation",
  "phases": {
    "Phase 0: Prompt Engineering": {
      "status": "completed",
      "started_at": "ISO-8601",
      "completed_at": "ISO-8601",
      "duration_ms": 45000,
      "tasks_completed": 1,
      "tasks_total": 1
    },
    "Phase 1: Investigation": {
      "status": "in-progress",
      "started_at": "ISO-8601",
      "progress_percent": 60,
      "tasks_completed": 3,
      "tasks_total": 5,
      "tasks": [
        {
          "task_id": "investigate-auth",
          "agent": "code-investigator",
          "status": "completed",
          "started_at": "ISO-8601",
          "completed_at": "ISO-8601",
          "duration_ms": 12500
        },
        {
          "task_id": "analyze-patterns",
          "agent": "pattern-analyzer",
          "status": "in-progress",
          "started_at": "ISO-8601",
          "elapsed_ms": 8000,
          "stall_detected": false
        },
        {
          "task_id": "map-dependencies",
          "agent": "dependency-mapper",
          "status": "pending",
          "blocked_by": ["analyze-patterns"]
        }
      ]
    },
    "Phase 2: Planning": {"status": "pending"},
    "Phase 3: Execution": {"status": "pending"},
    "Phase 4": Review": {"status": "pending"}
  },
  "overall_progress": {
    "percent_complete": 35,
    "estimated_completion_time": "ISO-8601",
    "time_remaining_ms": 180000
  },
  "alerts": [
    {
      "severity": "warning",
      "message": "Task 'analyze-patterns' running longer than expected (8s > 5s threshold)",
      "timestamp": "ISO-8601"
    }
  ]
}
```

## Decision Criteria

**Stall Detection Thresholds**:
- `task_duration > 2x_expected_duration`: FLAG as slow (warning)
- `task_duration > 5x_expected_duration`: ALERT as stalled (requires attention)
- `no_state_change_for_5_minutes`: ESCALATE to orchestrator

**Phase Transition Readiness**:
- `all_tasks_completed = true AND all_tasks_succeeded = true`: READY TO TRANSITION
- `critical_tasks_completed = true AND non_critical_failures_acceptable = true`: READY WITH WARNINGS
- `any_critical_task_failed = true`: BLOCKED (cannot transition)
- `tasks_still_in_progress = true`: NOT READY (wait for completion)

**Progress Percentage Calculation**:
- `Simple: completed_tasks / total_tasks * 100`
- `Weighted: sum(task_weight * task_completion) / sum(all_task_weights) * 100`
- Use weighted when tasks have varying complexity/duration

**ETA Calculation**:
- `elapsed_time / progress_percent * (100 - progress_percent)`
- Adjust for historical phase durations if available
- Add buffer for uncertainty (20% padding)

## Failure Handling

**Scenario 1: Workflow Stalled (No Progress)**
- **Condition**: No state changes for 5+ minutes, tasks remain in-progress
- **Recovery**:
  1. Identify which specific task/agent is stuck
  2. Check if agent is still running (timeout vs. hang)
  3. Alert orchestrator with task details and elapsed time
  4. Recommend action: extend timeout, terminate and retry, or escalate to user
  5. Do NOT auto-terminate - defer decision to orchestrator

**Scenario 2: Critical Task Failed**
- **Condition**: Task marked as critical in plan fails with error
- **Recovery**:
  1. Mark phase as blocked (cannot proceed)
  2. Capture failure reason and task details
  3. Alert orchestrator immediately
  4. Recommend: retry task, deploy alternative agent, or request user intervention
  5. Prevent phase transition until resolved

**Scenario 3: Phase Transition Requested Prematurely**
- **Condition**: Orchestrator requests transition but tasks still in-progress
- **Recovery**:
  1. Validate transition criteria (all critical tasks complete?)
  2. If not ready: DENY transition request with specific blockers
  3. List incomplete tasks preventing transition
  4. Provide completion percentage and ETA
  5. Allow orchestrator to force transition (with warnings) or wait

**Scenario 4: Dependency Deadlock**
- **Condition**: Task A blocked by Task B, Task B blocked by Task A (circular dependency)
- **Recovery**:
  1. Detect cycle in dependency graph
  2. Mark workflow as DEADLOCKED
  3. Alert orchestrator with cycle details (A → B → A)
  4. Recommend: break dependency (manual intervention), revise task plan, or abort workflow
  5. Prevent any progress until cycle resolved

## Integration with Other Skills

**Receives From (Passive Monitoring)**:
- **ALL SKILLS**: Emit events when tasks start, complete, fail, or block
- **task-decomposition**: Initial workflow plan with phases, tasks, dependencies, expected durations
- **agent-delegation**: Agent deployment and completion notifications
- **orchestrator**: Status queries, transition requests, configuration updates

**Provides To**:
- **orchestration-guide**: Current workflow state for displaying to users
- **orchestrator**: State machine for decision making, transition validation
- **User Interface**: Human-readable progress reports, ETAs, active task lists
- **ALL SKILLS**: Context about current phase, workflow state (on request)

**Event Schema**:
Skills emit events to workflow-management:
```json
{
  "event_type": "task_started|task_completed|task_failed|task_blocked|phase_started|phase_completed",
  "workflow_id": "unique-id",
  "timestamp": "ISO-8601",
  "task_id": "optional",
  "agent": "optional",
  "phase": "Phase 1: Investigation",
  "details": { /* event-specific data */ }
}
```

**Query Interface**:
Progress-tracking responds to queries:
```json
{
  "query_type": "get_current_state|get_phase_progress|validate_transition|get_eta",
  "workflow_id": "unique-id",
  "parameters": { /* query-specific params */ }
}
```

## Best Practices

**Track Everything**: Don't assume "minor" tasks don't matter - visibility into all work prevents blind spots

**Use Quantitative Thresholds**: Never use subjective assessments like "seems slow" - define numeric thresholds (2x expected, 5 minutes no progress)

**Passive Observation**: Don't interfere with agents or workflows - only observe, track, and report

**Fast Alerts**: When stalls or failures detected, alert immediately (don't wait for next polling interval)

**Preserve History**: Keep completed task data for analytics and ETA calculation improvements

**Machine & Human Readable**: Support both structured queries (orchestrator) and formatted reports (users)

**Handle State Loss**: If tracking state is lost (crash, restart), gracefully degrade (conservative estimates, warn about gaps)

## Example Scenarios

**Scenario 1: Normal Workflow Progress**
- Initialize from task plan: 3 phases, 12 total tasks
- Phase 1 starts: 5 investigation tasks pending
- Tasks complete one by one: progress updates from 0% → 20% → 40% → 60% → 80% → 100%
- Phase 1 complete: transition to Phase 2
- **Tracking Actions**: Update state after each event, calculate progress percentage, provide ETA updates
- **Output**: Regular progress reports showing "Phase 1: 80% complete, ETA 2 minutes"

**Scenario 2: Stalled Agent Detection**
- Phase 1 in-progress: agent "dependency-mapper" started 10 minutes ago
- Expected duration: 2 minutes, threshold: 10 minutes (5x)
- No progress events from agent in last 8 minutes
- **Tracking Actions**:
  1. Detect stall at 10 minute mark
  2. Alert orchestrator: "Agent 'dependency-mapper' stalled (10m > 2m expected)"
  3. Recommend action: "Check agent health, consider termination and retry"
- **Output**: Stall alert with details and recommended actions

**Scenario 3: Premature Transition Blocked**
- Phase 1 in-progress: 4 of 5 tasks complete, 1 critical task still running
- Orchestrator requests transition to Phase 2
- **Tracking Actions**:
  1. Validate transition criteria
  2. Detect incomplete critical task: "pattern-analysis" at 75% complete
  3. DENY transition request
  4. Respond: "Cannot transition - critical task 'pattern-analysis' incomplete (75%, ETA 30s)"
- **Output**: Transition blocked with specific reason and ETA for readiness

**Scenario 4: Workflow Health Report**
- User requests status update mid-execution
- Current state: Phase 2 in-progress, 2 of 3 planning tasks complete
- Overall workflow: 65% complete
- **Tracking Actions**:
  1. Query current state
  2. Calculate metrics (progress %, ETA, active tasks)
  3. Format human-readable report
- **Output**:
```
Workflow Status Report
======================
Current Phase: Phase 2 (Planning)
Phase Progress: 67% (2 of 3 tasks complete)
Overall Progress: 65% complete
Active Tasks:
  - implementation-planner: In Progress (started 2m ago, expected completion in 1m)
Completed: 8 tasks
Failed: 0 tasks
ETA: 3 minutes
```

## Integration Architecture

Progress tracking operates as a **cross-cutting observability layer**:

```
┌──────────────────────────────────────────────────────────────┐
│                      Progress Tracking                       │
│                  (Centralized State Manager)                 │
└────────────────────────┬─────────────────────────────────────┘
                         │
            ┌────────────┼────────────┐
            │ OBSERVES   │ REPORTS TO │
            ▼            ▼            ▼
     ┌──────────┐  ┌──────────┐  ┌───────┐
     │  All     │  │Orchestr- │  │ User  │
     │ Skills   │  │  ator    │  │  UI   │
     └──────────┘  └──────────┘  └───────┘
            │            │            │
            └────── EMIT EVENTS ──────┘
                (task start/complete/fail)
```

**Event Flow**:
1. Skills emit lifecycle events (task start, complete, fail)
2. Progress-tracking receives events, updates state
3. Orchestrator queries state for decisions
4. User UI displays formatted progress reports
5. Phase transitions validated before proceeding

**No Direct Control**: Progress-tracking never controls workflows - only observes and reports.
