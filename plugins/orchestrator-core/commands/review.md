---
description: Review code quality, security, and best practices
argument-hint: optional scope (defaults to unstaged changes)
skills: [agent-delegation, context-synthesis, result-aggregation]
---

Review: ${ARGUMENTS:-"unstaged changes"}

This triggers **quality analysis** on code changes. No code modifications will be made.

Follow these steps:

**Step 0: Load Orchestration Skills**
0. **Invoke all required skills** to load review guidance:
   - `Skill("orchestrator-core:agent-delegation")` - Delegation best practices
   - `Skill("orchestrator-core:context-synthesis")` - Findings synthesis by severity
   - `Skill("orchestrator-core:result-aggregation")` - Quality report aggregation
**Skill Hint Guidance**
When deploying agents, include relevant skill hints in the prompt. Available skills for review workflows:
- **agent-delegation**: Frameworks for 5-requirement prompts and prompt validation
- **context-synthesis**: Integration techniques for grouping issues by severity
- **result-aggregation**: Validation protocols for quality report aggregation

## DELEGATION STRATEGY

When executing review workflows, deciding whether to delegate to specialized agents or handle tasks directly is critical for comprehensive quality analysis.

### When to Delegate to Specialized Agents

**Delegate when**:
- Reviewing multiple files or complex code changes
- Need comprehensive quality analysis across multiple dimensions (security, patterns, testing)
- Changes span different concerns requiring specialized expertise
- Benefit from parallel analysis for faster results

**Handle directly when**:
- Reviewing single file with trivial changes
- Simple linting or formatting review
- Quick sanity check before full review
- Delegation overhead exceeds review cost

### Agent Selection Guide for Review

| Task Type | Recommended Agent | When to Use | Expected Output |
|-----------|------------------|-------------|-----------------|
| Security & quality analysis | quality-analyst | Always for code changes | Vulnerability report, quality issues, best practice violations |
| Pattern consistency | pattern-analyzer | Multi-file changes or new features | Consistency assessment, pattern violations |
| Test coverage analysis | test-strategist | Changes include tests or testable code | Test coverage gaps, testing recommendations |

## 3-STAGE WORKFLOW GUIDE

All review workflows follow a 3-stage pattern to ensure comprehensive quality analysis.

### Stage 1: Setup & Scope Identification (REQUIRED - Use Sequential Thinking)

**Mandatory Skills** (Step 0):
- Load all skills listed in command metadata before workflow execution
- `Skill("orchestrator-core:agent-delegation")`
- `Skill("orchestrator-core:context-synthesis")`
- `Skill("orchestrator-core:result-aggregation")`

**Planning with Sequential Thinking**:
Use `mcp__sequential-thinking__sequentialthinking` to:
- Identify review scope (from $ARGUMENTS or git changes)
- Assess review complexity and file count
- Determine which quality agents to deploy
- Plan parallel execution for independent analyses
- Define success criteria for review

**Pre-Execution Checklist**:
- [ ] All mandatory skills loaded
- [ ] Review scope identified (files/directories)
- [ ] If no changes found: Inform user and exit
- [ ] Agent selection completed (quality-analyst + pattern-analyzer + test-strategist if applicable)
- [ ] Agent prompts validated against 5-requirement format

### Stage 2: Quality Analysis Execution

**PARALLEL Execution Pattern**:
- Deploy quality agents in a **single message** when analyses are independent
- Common pattern: quality-analyst + pattern-analyzer + test-strategist
- Wait for all agents to complete before synthesis

**Sequential Thinking (OPTIONAL)**:
May be used during analysis if unexpected issues require adaptive investigation.

### Stage 3: Synthesis & Validation (REQUIRED - Use Sequential Thinking)

**Use Sequential Thinking to**:
- Review all quality reports for completeness
- Group issues by severity (Critical → High → Medium → Low)
- Remove duplicate findings across agents
- Prioritize issues by impact and urgency
- Validate file:line references are specific and actionable
- Formulate clear recommendation (ready to commit or fix issues first)

**Output Validation Checklist**:
- [ ] All issues include specific file:line references
- [ ] Fix recommendations provided for each issue
- [ ] Severity ratings assigned (Critical/High/Medium/Low)
- [ ] Pattern consistency assessed
- [ ] Test coverage analysis completed (if applicable)
- [ ] Clear recommendation provided (commit or fix)

## AGENT PROMPT TEMPLATES

When delegating to specialized agents, use the **5-requirement format** to ensure clarity and completeness.

**5-Requirement Format**:
1. **ROLE**: Agent's identity and expertise domain
2. **CONTEXT**: Relevant background, project specifics, constraints
3. **TASK**: Single, measurable objective with clear boundaries
4. **CONSTRAINTS**: Scope limits, token budgets, time limits, circuit breakers
5. **OUTPUT**: Exact deliverable format with verification criteria

### Template: quality-analyst for Security & Code Quality Review

```
ROLE:
You are a quality-analyst specializing in security vulnerability detection, code quality assessment, and best practice verification.

CONTEXT:
- Review scope: [FILES/DIRECTORIES to review]
- Project: [PROJECT_TYPE]
- Change type: [New feature / Bug fix / Refactoring]

TASK:
Analyze code for quality and security issues:
1. Identify security vulnerabilities (injection, auth issues, data exposure, etc.)
2. Detect code quality problems (complexity, duplication, maintainability)
3. Verify adherence to best practices (error handling, logging, validation)
4. Assess performance concerns (inefficient algorithms, resource leaks)

CONSTRAINTS:
- Token Budget: [e.g., 15000 tokens]
- Focus on [SCOPE - e.g., "changed files only" or "specific directory"]
- Severity classification: Critical/High/Medium/Low
- Circuit Breaker: Stop if exceeding token budget

OUTPUT:
Provide a QUALITY REPORT with:
1. **Summary**: Total issues by severity (Critical: X, High: Y, Medium: Z, Low: W)
2. **Critical Issues**: MUST fix before commit (file:line, issue, fix recommendation)
3. **High Priority Issues**: Should fix (file:line, issue, fix recommendation)
4. **Medium/Low Issues**: Nice to fix (file:line, issue, fix recommendation)
5. **Best Practices Assessment**: Adherence to standards
6. **Recommendation**: Ready to commit? Or fix issues first?

AVAILABLE SKILLS (contextual suggestions):
- No additional skills typically needed for quality analysis
```

### Template: pattern-analyzer for Consistency Verification

```
ROLE:
You are a pattern-analyzer specializing in verifying code consistency with established project patterns and conventions.

CONTEXT:
- Review scope: [FILES/DIRECTORIES to review]
- Project: [PROJECT_TYPE]
- Background: [Known patterns or style guides]

TASK:
Verify pattern consistency for [SCOPE]:
1. Identify established patterns in the codebase
2. Compare changes against established patterns
3. Detect violations or deviations from conventions
4. Assess impact of inconsistencies on maintainability

CONSTRAINTS:
- Token Budget: [e.g., 12000 tokens]
- Focus on [PATTERN_TYPES - e.g., "naming conventions", "error handling", "module structure"]
- Circuit Breaker: Stop after analyzing [N] representative files for pattern baseline

OUTPUT:
Provide a PATTERN CONSISTENCY REPORT with:
1. **Summary**: Consistency score (High/Medium/Low)
2. **Established Patterns**: Identified conventions (with examples)
3. **Violations**: Deviations from patterns (file:line, violation, recommended fix)
4. **Impact Assessment**: How inconsistencies affect maintainability
5. **Recommendation**: Accept deviations or enforce consistency?

AVAILABLE SKILLS (contextual suggestions):
- No additional skills typically needed for pattern analysis
```

### Template: test-strategist for Test Coverage Analysis

```
ROLE:
You are a test-strategist specializing in test coverage analysis and testing strategy recommendations.

CONTEXT:
- Review scope: [FILES/DIRECTORIES to review]
- Project: [PROJECT_TYPE]
- Test framework: [FRAMEWORK - e.g., Jest, pytest, etc.]

TASK:
Analyze testing coverage and strategy:
1. Identify test coverage gaps for changed code
2. Assess test quality (assertions, edge cases, mocking)
3. Verify testable code structure
4. Recommend additional tests needed

CONSTRAINTS:
- Token Budget: [e.g., 10000 tokens]
- Focus on [TESTABLE_SCOPE - e.g., "new functions", "modified logic"]
- Circuit Breaker: Stop if no tests found in scope

OUTPUT:
Provide a TEST COVERAGE REPORT with:
1. **Summary**: Coverage assessment (High/Medium/Low)
2. **Coverage Gaps**: Untested code paths (file:line, missing tests)
3. **Test Quality**: Assessment of existing tests
4. **Recommendations**: Specific tests to add (function, test cases, edge cases)
5. **Priority**: Which gaps are critical to fill before commit

AVAILABLE SKILLS (contextual suggestions):
- If working with specific test framework: Note framework-specific patterns
```

## SKILL MAPPING

Skills provide specialized guidance for review workflows.

### Mandatory Skills for Review (Step 0)

| Skill | Purpose | When to Load | Expected Benefit |
|-------|---------|--------------|------------------|
| agent-delegation | 5-requirement prompt framework, validation checklist | Always (Step 0) | Well-structured agent prompts for quality agents |
| context-synthesis | Multi-source findings integration, severity grouping | Always (Step 0) | Unified quality report with prioritized issues |
| result-aggregation | Parallel agent output validation, duplicate detection | Always (Step 0) | Quality control for review reports |

**Loading Pattern**:
```
Step 0: Load Orchestration Skills
0. Invoke all required skills:
   - Skill("orchestrator-core:agent-delegation")
   - Skill("orchestrator-core:context-synthesis")
   - Skill("orchestrator-core:result-aggregation")
```

### Contextual Skills for Review Agents

| Skill | Suggest When | Agent Types | Expected Benefit |
|-------|--------------|-------------|------------------|
| N/A | Review agents typically don't need additional skills | quality-analyst, pattern-analyzer, test-strategist | Standard analysis sufficient |

**Contextual Loading Pattern** (in agent prompts):
```
AVAILABLE SKILLS (contextual suggestions):
- No additional skills typically needed for quality/pattern/test analysis
```

**Step 1: Identify Scope**
1. **Identify scope** to review:
   - If $ARGUMENTS provided: review those specific files/directories
   - If no $ARGUMENTS: run `git diff --name-only` and `git diff --staged --name-only` to find changes
   - If no changes found, inform user and exit

**Agent Prompt Validation**: Follow agent-delegation:prompt-validation checklist

2. **Deploy quality agents in parallel using agent-delegation principles**:
   - Launch in a single message:
     - quality-analyst (security vulnerabilities, code quality, best practices)
     - pattern-analyzer (verify consistency with project patterns)
     - test-strategist (if scope includes tests or testable code)

3. **Wait for all agent reports**

4. **Synthesize findings** using context-synthesis and result-aggregation guidance:
   - Group issues by severity (Critical → High → Medium → Low)
   - Remove duplicates
   - Prioritize by impact

5. **Present review report** with:
   - Summary (files reviewed, issue counts by severity)
   - Critical issues (must fix before commit)
   - High/Medium/Low priority issues with file:line references
   - Pattern consistency assessment
   - Test coverage analysis
   - Clear recommendation (ready to commit? or fix issues first?)

**Success criteria:**
- All issues include specific file:line references and fix recommendations
- Severity ratings provided (Critical/High/Medium/Low)
- Clear actionable next steps

**After completion:**
- If critical issues: recommend fixing and running `/review` again
- If no critical issues: approve for commit
