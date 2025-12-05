---
name: result-aggregation
description: Operational validation and collection of parallel agent outputs, checking completeness, format compliance, and conflict detection before synthesis. Load after multiple agents complete to validate schemas, assess quality, and prepare structured handoff packages.
triggers:
  - aggregate
  - collect-results
  - validate-outputs
  - prepare-synthesis
  - agent-completion
  - schema-validation
  - completeness-check
  - agent-outputs
  - parallel-completion
  - validation-errors
  - conflict-detection
---

# Result Aggregation

## Overview

Result aggregation is the systematic collection and validation of outputs from parallel agent execution. This skill bridges the gap between raw agent outputs and context synthesis by ensuring completeness, validating formats, detecting conflicts, and preparing structured handoff packages.

**Distinction from context-synthesis**: This is LOW-LEVEL operational work (checking completeness, validating schemas) while context-synthesis performs HIGH-LEVEL conceptual work (extracting insights, identifying patterns).

## When to Use This Skill

Apply result aggregation when:
- Multiple agents have completed parallel execution and outputs need collection
- Agent outputs must be validated against expected schemas before synthesis
- Completeness verification is required (all expected agents reported?)
- Format compliance checking is needed (outputs match specifications?)
- Conflict detection between agent results is necessary
- Preparing structured handoff package for context-synthesis

## When NOT to Use This Skill

**Do NOT use result aggregation when**:
- Only a single agent has completed (no aggregation needed, read directly)
- Agents are still running (premature, wait for completion first)
- No validation is required (simple pass-through to next phase)
- Outputs are informal/unstructured (this skill requires structured agent reports)
- You're doing high-level synthesis (that's context-synthesis, not aggregation)
- Agents executed sequentially with dependencies (each output consumed immediately)

## Process

1. **Initialize Collection**: Accept agent completion signals and expected agent list
2. **Gather Outputs**: Collect reports from all completed agents
3. **Validate Completeness**: Check all expected agents reported (or timed out/failed)
4. **Validate Formats**: Verify each output matches expected schema
5. **Detect Conflicts**: Compare findings for contradictions or inconsistencies
6. **Assess Quality**: Calculate completeness score, confidence aggregate, validation status
7. **Prepare Handoff**: Structure results with metadata for synthesis
8. **Report Status**: Notify orchestrator of collection status (complete/partial/failed)

## Output Structure

Result aggregation produces a **Result Package** with:

```json
{
  "collection_id": "unique-id",
  "timestamp": "ISO-8601",
  "completeness": {
    "expected_agents": 5,
    "completed": 4,
    "failed": 1,
    "score": 0.8
  },
  "validation_status": {
    "all_valid": false,
    "schema_violations": 1,
    "format_warnings": 2
  },
  "agent_outputs": [
    {
      "agent_id": "code-investigator-1",
      "status": "completed",
      "execution_time_ms": 12500,
      "confidence": 0.85,
      "output": { /* validated agent output */ },
      "schema_valid": true,
      "warnings": []
    }
  ],
  "conflicts": [
    {
      "severity": "important",
      "agents": ["agent-1", "agent-2"],
      "description": "Contradictory findings on authentication method",
      "details": "agent-1 reports JWT, agent-2 reports session-based"
    }
  ],
  "quality_assessment": {
    "overall_score": 0.75,
    "readiness_for_synthesis": "proceed-with-caution",
    "recommended_actions": ["resolve conflicts", "request clarification on missing agent"]
  }
}
```

## Decision Criteria

**Completeness Thresholds**:
- `completeness_score >= 1.0`: All expected agents reported → PROCEED
- `completeness_score >= 0.8`: Most agents reported → PROCEED WITH CAUTION
- `completeness_score >= 0.6`: Majority reported → REQUEST DECISION (user/orchestrator)
- `completeness_score < 0.6`: Insufficient data → FAIL (request re-execution)

**Validation Thresholds**:
- `schema_violations = 0`: All outputs valid → PROCEED
- `schema_violations <= 2`: Minor issues → PROCEED WITH WARNINGS
- `schema_violations > 2`: Major issues → FAIL (request agent fixes)

**Conflict Severity**:
- `critical`: Contradictions on core findings → BLOCK until resolved
- `important`: Significant inconsistencies → FLAG for synthesis attention
- `minor`: Minor discrepancies → DOCUMENT but proceed

**Synthesis Readiness**:
- `completeness >= 0.8 AND schema_violations <= 2 AND critical_conflicts = 0` → READY
- Otherwise → NOT READY (specify blockers)

## Failure Handling

**Scenario 1: Missing Agent Outputs**
- **Condition**: Expected agent didn't report (timeout, crash, or skipped)
- **Recovery**:
  1. Check if missing agent is critical (marked high-priority in task plan)
  2. If critical: request agent re-execution with extended timeout
  3. If non-critical: proceed with partial results, document gap
  4. Set completeness flag to indicate partial results

**Scenario 2: Schema Validation Failures**
- **Condition**: Agent output doesn't match expected schema
- **Recovery**:
  1. Attempt auto-correction for common issues (missing optional fields, type coercion)
  2. If auto-correction fails: mark output as invalid, proceed with other outputs
  3. If too many failures: abort and request schema review
  4. Log all validation errors for debugging

**Scenario 3: Critical Conflicts**
- **Condition**: Agents report contradictory findings on core issues
- **Recovery**:
  1. Do NOT attempt to resolve conflicts (not this skill's role)
  2. Document conflicts with severity and details
  3. Block synthesis until conflicts resolved (return to request-clarification or deploy arbiter agent)
  4. Provide conflict summary to orchestrator for decision

**Scenario 4: All Agents Failed**
- **Condition**: No agents completed successfully
- **Recovery**:
  1. Collect failure reasons from all agents
  2. Categorize failures (common root cause?)
  3. Abort result aggregation
  4. Return failure report to orchestrator with recommended fixes

## Integration with Other Skills

**Receives From**:
- **agent-delegation**: Agent completion signals, expected agent list, agent metadata
- **task-decomposition**: Original task plan with agent requirements, success criteria

**Provides To**:
- **context-synthesis**: Validated result package with all agent outputs and quality metadata
- **workflow-management**: Collection status updates (started, in-progress, complete/failed)
- **orchestrator**: Readiness assessment, blocker notifications, quality warnings

**Invocation Pattern**:
```
agent-delegation (deploys parallel agents)
    ↓
[agents execute in parallel]
    ↓
agent-delegation (signals completion)
    ↓
result-aggregation (THIS SKILL - collects, validates, prepares)
    ↓
context-synthesis (synthesizes insights from validated results)
```

## Best Practices

**Maintain Strict Validation**: Always validate against schemas - don't accept malformed outputs even if "good enough"

**Preserve All Metadata**: Keep execution times, confidence scores, warnings - context-synthesis needs this for quality assessment

**Don't Interpret Results**: This is not synthesis - just collect, validate, and organize. Leave interpretation to context-synthesis

**Handle Partial Results Gracefully**: Not every agent succeeds - design for resilience with partial data

**Use Quantitative Criteria**: Never guess if results are "sufficient" - use defined thresholds (completeness score, schema violations)

**Document All Conflicts**: Even minor inconsistencies should be recorded - context-synthesis decides if they matter

**Fast Failure on Critical Issues**: If critical agents missing or critical conflicts detected, fail fast rather than proceeding with bad data

## Example Scenarios

**Scenario 1: Clean Parallel Investigation**
- 5 investigation agents deployed in parallel
- All 5 complete successfully within 2 minutes
- All outputs pass schema validation
- No conflicts detected
- **Result**: completeness=1.0, validation=pass, conflicts=0 → READY for synthesis
- **Action**: Pass complete result package to context-synthesis

**Scenario 2: Partial Success with Minor Issues**
- 5 agents deployed, 4 complete, 1 times out
- 3 outputs pass validation, 1 has missing optional field (auto-corrected)
- Minor conflict: two agents disagree on performance metric
- **Result**: completeness=0.8, validation=pass-with-warnings, conflicts=1(minor) → PROCEED WITH CAUTION
- **Action**: Pass partial result package with warnings to context-synthesis

**Scenario 3: Critical Conflict Blocks Synthesis**
- 3 agents deployed, all complete successfully
- All outputs pass schema validation
- Critical conflict: agent-1 says "authentication is JWT", agent-2 says "authentication is OAuth", agent-3 says "authentication is session-based"
- **Result**: completeness=1.0, validation=pass, conflicts=1(critical) → NOT READY
- **Action**: Block synthesis, return conflict report to orchestrator, recommend deploying authentication-specialist agent or requesting user clarification

**Scenario 4: Catastrophic Failure**
- 4 agents deployed, all 4 fail with same error: "database connection timeout"
- No outputs to collect
- **Result**: completeness=0.0, validation=N/A, conflicts=N/A → FAILED
- **Action**: Abort aggregation, return failure report with root cause analysis ("common failure: database unavailable"), recommend infrastructure check before retry
