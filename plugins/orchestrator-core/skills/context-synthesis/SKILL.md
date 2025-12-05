---
name: context-synthesis
description: High-level integration of findings from multiple sources into unified insights, patterns, and recommendations. Load after collecting agent outputs to extract key insights, reconcile conflicts, identify patterns, and formulate actionable next steps.
triggers:
  - synthesize
  - consolidate
  - integrate-findings
  - findings
  - reports
  - summary
  - combine
  - extract-insights
  - reconcile-conflicts
  - identify-patterns
  - actionable-recommendations
  - executive-summary
---

# Context Synthesis Skill

## Overview

The context synthesis skill enables the orchestrator to collect, analyze, and integrate outputs from multiple agents, investigation phases, and information sources into coherent, actionable summaries. This skill transforms disparate findings into unified insights that inform decision-making and guide subsequent workflow phases.

## When to Use This Skill

Apply context synthesis when:
- Multiple agents have completed parallel investigations requiring integration
- Investigation phase results need consolidation before planning phase
- Diverse information sources must be unified into a single coherent view
- Patterns and insights need extraction from multiple data points
- Recommendations must be formulated based on aggregated findings
- Conflicting information from different sources requires reconciliation
- Executive summaries are needed for complex multi-agent workflows
- Decision points require comprehensive situational awareness

## When NOT to Use This Skill

**Do NOT use context synthesis when**:
- Only a single agent report needs review (read and act on it directly)
- No integration is needed between information sources
- User is asking for raw output from a single source
- Simple forwarding of results without analysis is sufficient
- You have no multiple sources to synthesize (synthesis requires ≥2 sources)
- Task is still in investigation phase (synthesis comes after collection)
- User wants detailed findings, not summary (don't oversimplify prematurely)

## Synthesis Process

1. **Collection**: Gather all relevant outputs from agents, tools, and investigation activities
2. **Organization**: Structure findings by logical categories (topic, phase, source, priority)
3. **Analysis**: Review findings to identify patterns, conflicts, gaps, and key insights
4. **Reconciliation**: Resolve contradictions and validate critical claims
5. **Integration**: Combine related findings into unified themes and narratives
6. **Distillation**: Extract most important insights and actionable recommendations
7. **Presentation**: Format synthesis for appropriate audience and purpose

## Synthesis Dimensions

### Topical Synthesis
Organize findings by subject matter or domain. Aggregate all information related to specific topics regardless of source.

**Example**: Synthesize authentication findings from codebase-analyzer, security-reviewer, and pattern-finder into unified authentication overview.

### Temporal Synthesis
Integrate information across time periods or phases. Track evolution of understanding as investigation progresses.

**Example**: Show how initial hypotheses about performance issues evolved through multi-phase investigation.

### Source Synthesis
Combine information from diverse sources including agents, documentation, codebase analysis, and external references.

**Example**: Integrate insights from code analysis, architectural docs, and team knowledge to understand system design rationale.

### Hierarchical Synthesis
Aggregate detailed findings into progressively higher-level summaries. Enable both executive overview and detailed deep-dives.

**Example**: Top-level: "Three critical security issues found", Mid-level: issue categories, Detail-level: specific vulnerabilities and remediation.

### Comparative Synthesis
Analyze similarities and differences between multiple options, approaches, or alternatives.

**Example**: Compare microservices vs monolith approaches based on findings from architecture analysis.

## Output Structure

Context synthesis produces:
- **Executive Summary**: High-level overview of key findings and recommendations (3-5 bullet points)
- **Detailed Findings**: Organized presentation of all relevant information by category
- **Key Insights**: Critical observations and patterns extracted from findings
- **Recommendations**: Actionable next steps with rationale and priority
- **Open Questions**: Identified gaps or unresolved issues requiring further investigation
- **Supporting Evidence**: References to source materials and agent outputs
- **Confidence Assessment**: Evaluation of certainty for major claims and recommendations

## Decision Criteria

**Synthesis Trigger Threshold**:
- `information_sources >= 2`: Synthesis justified → PROCEED WITH SYNTHESIS
- `information_sources = 1`: No synthesis needed → FORWARD DIRECTLY
- `information_sources = 0`: No data → CANNOT SYNTHESIZE

**Synthesis Completeness**:
- `all_required_sections_present = true`: Synthesis complete → READY FOR HANDOFF
- `executive_summary_concise = true` (3-5 bullets): Top-level view clear
- `key_insights_extracted >= 3`: Meaningful patterns identified
- `recommendations_actionable = true`: Next steps are clear

**Quality Thresholds**:
- `confidence_score >= 0.8`: High confidence → PROCEED WITHOUT CAVEATS
- `confidence_score 0.6-0.8`: Medium confidence → PROCEED WITH NOTED UNCERTAINTIES
- `confidence_score < 0.6`: Low confidence → FLAG AS UNCERTAIN (request more investigation)

**Conflict Resolution Status**:
- `critical_conflicts_resolved = true`: Major contradictions addressed → PROCEED
- `critical_conflicts_unresolved > 0`: Blockers exist → ESCALATE TO USER/ORCHESTRATOR
- `minor_conflicts_documented = true`: Noted but non-blocking → PROCEED WITH NOTES

**Synthesis Depth**:
- `detail_level = executive`: 1-2 paragraphs, 3-5 key bullets
- `detail_level = standard`: Multi-section organized findings (default)
- `detail_level = comprehensive`: Includes all agent outputs + synthesis

**Readiness for Next Phase**:
- `synthesis_complete AND confidence >= 0.7 AND critical_conflicts = 0`: READY FOR PLANNING
- `synthesis_incomplete OR confidence < 0.6`: REQUEST MORE INVESTIGATION
- `critical_conflicts > 0`: REQUIRE USER DECISION before proceeding

## Integration with Other Skills

- **Task Decomposition**: Synthesis results inform refinement of task plans and phase transitions
- **Agent Delegation**: Aggregated findings guide deployment of subsequent agents
- **Request Clarification**: Synthesized information may reveal new ambiguities requiring user input
- **Workflow Management**: Synthesis outputs trigger phase transitions and decision points

## Best Practices

- **Maintain Traceability**: Link synthesized insights back to source findings and agent outputs
- **Acknowledge Uncertainty**: Explicitly note confidence levels and areas of ambiguity
- **Highlight Conflicts**: Surface unresolved contradictions rather than hiding them
- **Prioritize Ruthlessly**: Focus attention on highest-impact findings and insights
- **Provide Context**: Ensure synthesized information includes enough context to be actionable
- **Structure for Scanning**: Use headings, bullets, and formatting to enable quick comprehension
- **Include Recommendations**: Don't just summarize; provide clear next steps
- **Avoid Information Loss**: While distilling, preserve access to detailed findings

## Synthesis Patterns

### Convergent Synthesis
Multiple investigation paths converging on consistent conclusions. High confidence in synthesized findings.

**Indicators**: Agreement across sources, corroborating evidence, clear patterns
**Output Focus**: Confident recommendations with strong supporting evidence

### Divergent Synthesis
Investigation reveals multiple viable approaches or conflicting information requiring trade-off analysis.

**Indicators**: Valid alternatives, conflicting evidence, context-dependent conclusions
**Output Focus**: Comparative analysis with decision criteria and trade-offs

### Exploratory Synthesis
Open-ended investigation yielding diverse findings without clear convergence.

**Indicators**: Broad range of findings, emerging patterns, incomplete picture
**Output Focus**: Organized findings with hypotheses for further investigation

### Gap-Identifying Synthesis
Synthesis reveals missing information or areas requiring deeper investigation.

**Indicators**: Unanswered questions, contradictions, insufficient evidence
**Output Focus**: Structured gap analysis with prioritized investigation recommendations

## Quality Criteria

### Completeness
Synthesis addresses all major findings from contributing sources. No significant findings are omitted without justification.

### Coherence
Synthesized narrative flows logically and findings relate clearly to conclusions and recommendations.

### Accuracy
Synthesis correctly represents source findings without distortion or misinterpretation.

### Actionability
Recommendations are specific, prioritized, and directly actionable by stakeholders.

### Proportionality
Emphasis and detail level match importance of findings. Critical insights receive appropriate focus.

### Accessibility
Synthesis is comprehensible to intended audience with appropriate technical depth and clear language.

## Example Scenarios

**Parallel Investigation Synthesis**: Five agents investigated different aspects of API performance
- Synthesize findings:
  - codebase-analyzer: identified N+1 query patterns
  - database-profiler: confirmed slow queries on user endpoints
  - network-analyzer: ruled out network latency issues
  - cache-analyzer: found cache hit rate below 20%
  - load-tester: demonstrated 5x slowdown under concurrent load
- Synthesis: "Performance bottleneck is database layer due to N+1 queries and insufficient caching. Network is not a factor. Recommend: add query optimization and implement Redis caching."

**Multi-Phase Investigation Synthesis**: Understanding authentication across three investigation phases
- Phase 1: Current implementation uses custom JWT with 1-hour expiry
- Phase 2: Security review found token storage in localStorage (XSS risk)
- Phase 3: Pattern search revealed industry standard uses httpOnly cookies + refresh tokens
- Synthesis: "Current auth has security vulnerability. Recommend migration to httpOnly cookies with refresh token pattern following [specific pattern reference]."

**Conflicting Information Resolution**: Different sources provide contradictory information about database schema
- Code analysis: Shows 'users' table with 'email' column
- Documentation: States 'username' is primary identifier
- Test files: Use both email and username interchangeably
- Synthesis: "Documentation is outdated. Current implementation uses email as primary identifier. Recommend updating docs and standardizing test fixtures."

**Decision Support Synthesis**: Evaluating microservices vs monolith migration
- Team expertise: Strong in monolith, learning microservices
- Current pain points: Deployment coupling, scaling granularity
- Infrastructure: Container-ready but limited orchestration experience
- Timeline: 3-month migration window
- Synthesis: "Recommend modular monolith as intermediate step. Achieves deployment independence without full microservices complexity. Provides migration path while matching team capabilities and timeline."
