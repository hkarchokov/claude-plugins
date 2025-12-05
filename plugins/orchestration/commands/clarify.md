---
description: Extract structured requirements from vague or ambiguous requests through interactive clarification
argument-hint: topic or request to clarify
---

Clarify: $ARGUMENTS

**Requirement extraction** - transforms vague requests into structured CONTEXT REPORTS with clear scope, success criteria, and investigation dimensions.

## Workflow

**Step 1: Deploy Clarifier Agent**

Deploy the clarifier agent:

```
Task(subagent_type="orchestration:clarifier",
     prompt="ROLE:
You are a clarifier specializing in extracting structured requirements through systematic questioning.

CONTEXT:
- User request: $ARGUMENTS
- Background: User needs help clarifying their request to prevent scope creep and ensure clear investigation boundaries

TASK:
Extract structured requirements through interactive clarification:
1. Use sequential thinking to identify:
   - Ambiguities in request (multiple interpretations)
   - Missing critical information (scope, success criteria, constraints)
   - Complexity level (simple lookup vs comprehensive investigation)
   - Investigation dimensions needed (structure, patterns, dependencies)
2. Formulate 2-4 targeted clarifying questions prioritized by importance
3. Ask user questions using AskUserQuestion tool
4. Process user responses and extract structured requirements
5. Produce comprehensive CONTEXT REPORT

CONSTRAINTS:
- Question rounds: Maximum 2 rounds
- Questions per round: 2-4 questions
- Focus on: scope, complexity, success criteria, investigation dimensions
- Stop after 2 rounds or if user requests to proceed

OUTPUT:
Provide a comprehensive CONTEXT REPORT with:
1. **Request Analysis**: Original request, ambiguity level, assumptions, validation confidence
2. **Clarification Q&A**: Questions, answers, interpretations
3. **Structured Requirements**: Functional, non-functional, scope boundaries, success criteria with validation needs
4. **Investigation Requirements**: Areas needing deep investigation, documentation research needs
5. **Validation Strategy**: Critical validation points, adversarial questions for validator
6. **Complexity Assessment**: SIMPLE (1-2 files, direct lookup) or COMPLEX (multi-file, patterns, dependencies)
7. **Investigation Dimensions**: Which dimensions needed (code structure, patterns, dependencies, architecture)
8. **Constraints**: Technical, business, preferences
9. **Project Context**: Relevant directories, files, dependencies
10. **Assumptions & Risks**: With confidence levels, likelihood, impact, and mitigation strategies
11. **Recommended Approach**: Investigation strategy, next steps with reasoning
12. **Handoff Summary**: Validation priorities, documentation priorities
")
```

**Step 2: Present Clarified Requirements**

After clarifier completes:
- Review CONTEXT REPORT
- Confirm scope boundaries with user
- Present complexity assessment
- Suggest next steps based on complexity

## Success Criteria

- All ambiguities identified and resolved
- CONTEXT REPORT complete with all sections
- Complexity explicitly determined (SIMPLE or COMPLEX)
- Clear scope boundaries defined (in scope, out of scope, uncertain)
- Success criteria measurable and testable
- Investigation dimensions identified

## Next Steps

After clarification completion:
- **For investigations**: `/investigate [topic]` with clarified requirements
- **For implementation**: `/implement [feature]` with CONTEXT REPORT
- **For manual work**: Use CONTEXT REPORT as specification
