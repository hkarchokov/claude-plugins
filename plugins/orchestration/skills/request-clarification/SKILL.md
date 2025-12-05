---
name: request-clarification
description: Provides systematic methodology for detecting ambiguities in user requests and resolving them through targeted questioning to produce CONTEXT REPORTS with structured requirements. This skill should be used when requests are vague or missing critical information. Use when users make ambiguous requests like "add authentication" (which method?), "make it faster" (what specifically?), "improve the API" (how?), or when scope boundaries are undefined, multiple interpretations exist, or assumptions need validation before proceeding. Do NOT use when requirements are already clear and specific, user provided explicit instructions, or user explicitly states "you decide" or "use best judgment".
---

# Request Clarification

## Purpose

Provides systematic methodology for identifying ambiguities, missing information, and implicit assumptions in user requests, then formulating precise questions to resolve uncertainties before execution. Prevents wasted effort from misunderstood requirements and ensures alignment between user intent and orchestrator actions.

## When to Use This Skill

Apply request clarification when:
- User requests contain vague or ambiguous terms requiring interpretation
- Critical implementation details are missing or underspecified
- Multiple valid interpretations of the request exist
- Assumptions need validation before making significant changes
- Scope boundaries are unclear and need definition
- Technical approach options require user preference input
- Risk of misalignment between user intent and planned execution exists
- Requirements conflict or have implicit contradictions

## When NOT to Use This Skill

**Do NOT use request clarification when**:
- User request is clear, specific, and actionable as stated
- All necessary information is already provided
- Ambiguities are minor and reasonable defaults exist
- Over-clarification would frustrate user ("just do the obvious thing")
- User explicitly states "you decide" or "use best judgment"
- Clarification questions would outnumber actual execution steps
- Request is conversational/exploratory rather than execution-focused
- User is responding to previous clarification (don't loop indefinitely)

## Clarification Process

1. **Request Parsing**: Analyze user request to extract explicit requirements and identify implicit elements
2. **Ambiguity Scanning**: Identify vague terms, underspecified requirements, and areas requiring interpretation
3. **Impact Assessment**: Evaluate which ambiguities have highest impact on execution outcome
4. **Question Generation**: Formulate specific, actionable questions with clear options or examples
5. **Priority Ordering**: Organize questions by criticality and logical flow
6. **Context Addition**: Include rationale explaining why each clarification matters
7. **User Presentation**: Present questions in digestible format with suggested defaults when appropriate

## Types of Clarifications

### Scope Clarifications
Questions about what is included or excluded from the request scope. Define boundaries of the work to prevent scope creep or missed requirements.

**Example**: "Should the authentication system include password reset functionality, or only login/logout?"

### Technical Approach Clarifications
Questions about preferred technical implementation when multiple valid approaches exist. Gather user preferences on technology choices, architectural patterns, or design decisions.

**Example**: "For session management, would you prefer JWT tokens (stateless) or server-side sessions (stateful)?"

### Constraint Clarifications
Questions about requirements, limitations, or constraints not explicitly stated. Identify performance requirements, compatibility needs, security constraints, or resource limitations.

**Example**: "Are there specific performance requirements for API response times (e.g., < 200ms)?"

### Priority Clarifications
Questions about relative importance when multiple objectives may conflict. Determine which requirements take precedence when tradeoffs are necessary.

**Example**: "If we need to choose, is faster development or more comprehensive testing the higher priority?"

### Assumption Validations
Questions that validate implicit assumptions before proceeding. Confirm understanding of existing systems, user workflows, or business logic.

**Example**: "I'm assuming all users authenticate via email/password. Should we also support social login (Google, GitHub)?"

### Dependency Clarifications
Questions about relationships to other systems or features. Identify integration requirements, data dependencies, or cross-system constraints.

**Example**: "Will this feature need to integrate with the existing notification system, or operate independently?"

## Output Structure

Request clarification produces:
- **Clarification Questions**: Numbered list of specific questions with context
- **Priority Indicators**: Marking of critical vs optional clarifications
- **Suggested Defaults**: Reasonable default assumptions if user prefers to proceed without answering
- **Impact Explanations**: Description of how different answers affect execution
- **Question Categories**: Grouping of related questions for easier comprehension
- **Deferral Options**: Identification of clarifications that can be addressed later if needed

## Integration with Other Skills

- **Task Decomposition**: Identifies ambiguities during breakdown that require clarification before proceeding
- **Agent Delegation**: Prevents deploying agents with insufficient or ambiguous requirements
- **Context Synthesis**: Ensures synthesized information aligns with validated user intent
- **Workflow Management**: Pauses workflow at appropriate checkpoints to gather needed clarifications

## Best Practices

- **Be Specific**: Ask precise questions with clear options rather than open-ended queries
- **Provide Context**: Explain why the clarification matters and how it affects execution
- **Suggest Defaults**: Offer reasonable default answers to help users understand the question
- **Group Logically**: Organize related questions together for coherent user experience
- **Prioritize Ruthlessly**: Only ask questions that meaningfully impact execution
- **Show Examples**: Use concrete examples to illustrate what you're asking about
- **Allow Deferral**: Identify which clarifications can be answered later without blocking progress
- **Validate Understanding**: Rephrase user's request to confirm shared understanding

## Clarification Timing

### Pre-Execution Clarifications
Critical questions that must be answered before any work begins. These typically involve scope, approach, or constraints that fundamentally shape the execution plan.

### Checkpoint Clarifications
Questions that arise at phase boundaries after initial investigation reveals new information. These refine understanding based on discovered context.

### Just-In-Time Clarifications
Questions that can be deferred until they become immediately relevant. These avoid overwhelming users with too many questions upfront.

### Post-Execution Validations
Confirmations after work is complete to validate the output matches user intent. These catch any residual misalignments.

## Example Scenarios

**Vague Feature Request**: "Make the app faster"
- Clarifications needed:
  - Which aspects feel slow? (page load, API responses, database queries, UI interactions)
  - What are acceptable performance targets? (specific metrics)
  - Are there particular user flows or features that need optimization?
  - Any constraints on approach? (budget, timeline, can't change database)

**Ambiguous Integration Request**: "Connect to the payment system"
- Clarifications needed:
  - Which payment system? (Stripe, PayPal, custom system)
  - What operations? (process payments, refunds, subscriptions, webhooks)
  - Real transactions or test mode initially?
  - Where should payment data be stored?
  - Error handling and retry requirements?

**Underspecified Architecture Change**: "Add caching"
- Clarifications needed:
  - What should be cached? (API responses, database queries, computed results)
  - Cache invalidation strategy? (TTL, manual, event-based)
  - Cache storage? (memory, Redis, CDN)
  - Caching for all users or specific segments?
  - Performance goals that would indicate success?

**Conflicting Requirements**: "Add comprehensive logging but keep the app lightweight"
- Clarifications needed:
  - Definition of "lightweight"? (file size, memory usage, dependencies)
  - Logging scope? (errors only, all requests, debug info)
  - Can logs be async/deferred to reduce performance impact?
  - Priority when tradeoffs necessary? (completeness vs performance)
