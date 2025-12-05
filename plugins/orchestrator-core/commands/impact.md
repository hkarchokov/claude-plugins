---
description: Analyze cross-project dependencies and impact of proposed changes
argument-hint: description of change to analyze
skills: [agent-delegation, context-synthesis, result-aggregation]
---

Analyze impact of: $ARGUMENTS

This triggers **cross-project dependency and impact analysis**. No code modifications will be made.

Follow these steps:

**Step 0: Load Orchestration Skills**
0. **Invoke all required skills** to load impact analysis guidance:
   - `Skill("orchestrator-core:agent-delegation")` - Delegation best practices
   - `Skill("orchestrator-core:context-synthesis")` - Impact synthesis
   - `Skill("orchestrator-core:result-aggregation")` - Report aggregation
**Skill Hint Guidance**
When deploying agents, include relevant skill hints in the prompt. Available skills for impact analysis workflows:
- **agent-delegation**: Frameworks for 5-requirement prompts and prompt validation
- **context-synthesis**: Integration techniques for combining dependency maps with risk assessments
- **result-aggregation**: Validation protocols for parallel agent outputs

## DELEGATION STRATEGY

When executing impact analysis workflows, deciding whether to delegate to specialized agents or handle tasks directly is critical for comprehensive dependency and risk assessment.

### When to Delegate to Specialized Agents

**Delegate when**:
- Proposed change affects shared libraries or cross-project dependencies
- Change involves core modules with wide usage
- Need comprehensive risk analysis across multiple dimensions
- Multi-project workspace requires dependency mapping
- Breaking change assessment needed

**Handle directly when**:
- Change is isolated to single file with no external dependencies
- Simple refactoring within module boundaries
- Quick dependency check on specific function
- Delegation overhead exceeds analysis cost

### Agent Selection Guide for Impact Analysis

| Task Type | Recommended Agent | When to Use | Expected Output |
|-----------|------------------|-------------|-----------------|
| Dependency mapping | dependency-mapper | Always for cross-project changes | Dependency graph, direct and transitive dependencies |
| Risk assessment | impact-analyzer | Always for significant changes | Risk categorization, breaking changes, mitigation strategies |

## 3-STAGE WORKFLOW GUIDE

All impact analysis workflows follow a 3-stage pattern to ensure comprehensive dependency and risk assessment.

### Stage 1: Setup & Change Clarification (REQUIRED - Use Sequential Thinking)

**Mandatory Skills** (Step 0):
- Load all skills listed in command metadata before workflow execution
- `Skill("orchestrator-core:agent-delegation")`
- `Skill("orchestrator-core:context-synthesis")`
- `Skill("orchestrator-core:result-aggregation")`

**Planning with Sequential Thinking**:
Use `mcp__sequential-thinking__sequentialthinking` to:
- Analyze proposed change description
- Identify affected code/modules/libraries
- Determine scope of impact analysis (single project vs multi-project)
- Plan parallel deployment of dependency-mapper and impact-analyzer
- Define success criteria for analysis

**Pre-Execution Checklist**:
- [ ] All mandatory skills loaded
- [ ] Proposed change understood (what/where/why)
- [ ] Scope identified (affected modules, projects)
- [ ] Agent prompts validated against 5-requirement format
- [ ] Multi-project workspace scope confirmed

### Stage 2: Parallel Analysis Execution

**PARALLEL Execution Pattern**:
- Deploy dependency-mapper and impact-analyzer in a **single message**
- Both analyses are independent and can run concurrently
- Wait for both agents to complete before synthesis

**Sequential Thinking (OPTIONAL)**:
May be used during analysis if unexpected dependencies require adaptive investigation.

### Stage 3: Synthesis & Validation (REQUIRED - Use Sequential Thinking)

**Use Sequential Thinking to**:
- Review both analysis reports for completeness
- Combine dependency map with risk assessment
- Identify all affected projects across workspace
- Categorize risks by severity (High/Medium/Low)
- Detect breaking changes with project-level impact
- Formulate update strategy and rollback plan
- Provide clear go/no-go recommendation

**Output Validation Checklist**:
- [ ] All dependencies mapped with file:line references
- [ ] Direct and transitive dependencies identified
- [ ] Risks categorized by severity with mitigation strategies
- [ ] Breaking changes explicitly identified with affected projects
- [ ] Update sequence provided (which projects, in what order)
- [ ] Rollback plan included
- [ ] Testing checklist provided
- [ ] Clear go/no-go recommendation

## AGENT PROMPT TEMPLATES

When delegating to specialized agents, use the **5-requirement format** to ensure clarity and completeness.

**5-Requirement Format**:
1. **ROLE**: Agent's identity and expertise domain
2. **CONTEXT**: Relevant background, project specifics, constraints
3. **TASK**: Single, measurable objective with clear boundaries
4. **CONSTRAINTS**: Scope limits, token budgets, time limits, circuit breakers
5. **OUTPUT**: Exact deliverable format with verification criteria

### Template: dependency-mapper for Cross-Project Dependency Analysis

```
ROLE:
You are a dependency-mapper specializing in mapping dependencies across multi-project workspaces and identifying impact zones.

CONTEXT:
- Proposed change: [CHANGE_DESCRIPTION]
- Affected module/library: [MODULE_NAME]
- Workspace projects: [PROJECT_LIST - e.g., email-service, github-runners, insights-service, etc.]
- Background: [Why change is needed]

TASK:
Map dependencies across ALL projects in workspace:
1. Identify direct dependencies on [AFFECTED_MODULE]
2. Map transitive dependencies (who depends on dependents)
3. Locate all import/usage sites with file:line references
4. Identify integration points with external systems
5. Build complete dependency graph

CONSTRAINTS:
- Token Budget: [e.g., 20000 tokens]
- Scope: ALL projects in workspace (not just single project)
- Must include file:line references for every dependency
- Circuit Breaker: Stop if exceeding token budget

OUTPUT:
Provide a DEPENDENCY MAP with:
1. **Summary**: Total projects affected, total dependency sites
2. **Direct Dependencies**: Projects directly using [AFFECTED_MODULE] (file:line references)
3. **Transitive Dependencies**: Projects indirectly affected through dependents
4. **Dependency Graph**: Visual representation of dependency chains
5. **Integration Points**: External APIs, databases, services affected
6. **Impact Zones**: Components that will break if [AFFECTED_MODULE] changes

AVAILABLE SKILLS (contextual suggestions):
- No additional skills typically needed for dependency mapping
```

### Template: impact-analyzer for Risk and Breaking Change Assessment

```
ROLE:
You are an impact-analyzer specializing in assessing risks, breaking changes, and backward compatibility for proposed code changes.

CONTEXT:
- Proposed change: [CHANGE_DESCRIPTION]
- Affected module/library: [MODULE_NAME]
- Dependency map: [DEPENDENCY_SITES from dependency-mapper]
- Background: [Change motivation]

TASK:
Assess risks and breaking changes for [PROPOSED_CHANGE]:
1. Identify breaking changes (API changes, signature modifications, behavior changes)
2. Assess backward compatibility impact
3. Categorize risks by severity (High/Medium/Low)
4. Develop mitigation strategies for each risk
5. Create update strategy (which projects need changes, in what order)
6. Design rollback plan

CONSTRAINTS:
- Token Budget: [e.g., 15000 tokens]
- Focus on [SCOPE - e.g., "cross-project impacts"]
- Risk categories: High (critical failure), Medium (degraded functionality), Low (minor issues)
- Circuit Breaker: Stop if exceeding token budget

OUTPUT:
Provide an IMPACT ASSESSMENT with:
1. **Summary**: Risk level (High/Medium/Low), breaking changes Y/N
2. **Breaking Changes**: Specific API/behavior changes with affected projects
3. **Risk Assessment by Severity**:
   - High: Critical risks requiring immediate mitigation
   - Medium: Moderate risks with workarounds
   - Low: Minor issues with minimal impact
4. **Mitigation Strategies**: How to address each risk category
5. **Update Strategy**: Which projects to update, in what sequence, why
6. **Rollback Plan**: Steps to revert if deployment fails
7. **Testing Checklist**: Critical tests to run before deployment
8. **Recommendation**: GO or NO-GO with justification

AVAILABLE SKILLS (contextual suggestions):
- No additional skills typically needed for impact analysis
```

## SKILL MAPPING

Skills provide specialized guidance for impact analysis workflows.

### Mandatory Skills for Impact Analysis (Step 0)

| Skill | Purpose | When to Load | Expected Benefit |
|-------|---------|--------------|------------------|
| agent-delegation | 5-requirement prompt framework, validation checklist | Always (Step 0) | Well-structured prompts for dependency-mapper and impact-analyzer |
| context-synthesis | Multi-source findings integration, risk categorization | Always (Step 0) | Unified impact report combining dependencies and risks |
| result-aggregation | Parallel agent output validation | Always (Step 0) | Quality control for analysis reports |

**Loading Pattern**:
```
Step 0: Load Orchestration Skills
0. Invoke all required skills:
   - Skill("orchestrator-core:agent-delegation")
   - Skill("orchestrator-core:context-synthesis")
   - Skill("orchestrator-core:result-aggregation")
```

### Contextual Skills for Impact Analysis Agents

| Skill | Suggest When | Agent Types | Expected Benefit |
|-------|--------------|-------------|------------------|
| N/A | Impact analysis agents typically don't need additional skills | dependency-mapper, impact-analyzer | Standard analysis sufficient |

**Contextual Loading Pattern** (in agent prompts):
```
AVAILABLE SKILLS (contextual suggestions):
- No additional skills typically needed for dependency/impact analysis
```

**Step 1: Clarify Change**
1. **Clarify the proposed change** - understand what code/module/library will be modified and scope of changes

**Agent Prompt Validation**: Follow agent-delegation:prompt-validation checklist

2. **Deploy analysis agents in parallel using agent-delegation principles**:
   - Launch in a single message:
     - dependency-mapper (map dependencies across ALL projects in workspace)
     - impact-analyzer (assess risks, breaking changes, backward compatibility)

3. **Wait for both agent reports**

4. **Synthesize impact assessment** using context-synthesis guidance:
   - Combine dependency map with risk assessment
   - Identify all affected projects (email-service, github-runners, insights-service, terraform-services, terraform-s3-buckets, braze-content-service, github-workflows)
   - Categorize risks by severity (High/Medium/Low)
   - Detect breaking changes

5. **Present comprehensive impact report** with:
   - Summary (projects affected, critical risks, breaking changes Y/N)
   - Dependency map (direct and transitive dependencies with file:line)
   - Risk assessment by severity with mitigation strategies
   - Breaking changes identified with affected projects
   - Update strategy (which projects need changes, in what order)
   - Rollback plan
   - Testing checklist
   - Clear go/no-go recommendation

**Success criteria:**
- All dependencies mapped across projects with file:line references
- Risks categorized by severity with mitigation plans
- Breaking changes explicitly identified
- Update sequence provided
- Rollback plan included

**After completion:**
- If critical risks: recommend addressing before implementation
- If safe: approve proceeding with `/implement`
