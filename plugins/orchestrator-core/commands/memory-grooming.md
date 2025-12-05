---
name: memory-grooming
description: Trigger comprehensive knowledge base maintenance and grooming operations
trigger: /memory-grooming
skills: [agent-delegation]
---

# Memory Grooming Command

## 🚨 IMPORTANT: MANUAL OPERATION ONLY
**Memory grooming is a MANUAL, USER-TRIGGERED operation. It is NOT automatic.**
- Requires explicit user command: `/memory-grooming` or `/memory-capture`
- Does NOT run automatically during tasks
- User decides when maintenance is needed
- Separate from automatic memory retrieval by memory-assistant

## Purpose
Initiates a comprehensive knowledge base maintenance session using the memory-curator agent to ensure the Neo4j knowledge graph remains healthy, well-organized, and valuable.

## Usage
```
/memory-grooming [mode] [context]
```

### Modes:
- **`/memory-grooming`** - Standard full grooming (default)
- **`/memory-grooming session`** - Analyze current conversation for patterns
- **`/memory-grooming success [description]`** - Capture successful pattern
- **`/memory-grooming failure [description]`** - Record anti-pattern or lesson
- **`/memory-grooming review`** - Quality check recent memory additions

### Examples:
```
/memory-grooming                              # Full maintenance
/memory-grooming session                      # Extract patterns from this conversation
/memory-grooming success "JWT implementation" # Store successful JWT pattern
/memory-grooming failure "N+1 query issue"    # Record performance anti-pattern
/memory-grooming review                       # Review recent memories for quality
```

## What Happens
When you invoke `/memory-grooming [mode]`, the system will:

**Step 0: Load Orchestration Skills**
0. **Invoke all required skills** to load memory grooming guidance:
   - `Skill("orchestrator-core:agent-delegation")` - Delegation best practices for memory-curator deployment

**Skill Hint Guidance**
When deploying memory-curator agent via Task(), include relevant skill hints in the prompt:
- **agent-delegation**: Frameworks for 5-requirement prompts and deploying memory agents

## DELEGATION STRATEGY

Memory grooming is a specialized maintenance workflow that ALWAYS delegates to the memory-curator agent for comprehensive knowledge base operations.

### When to Delegate to memory-curator Agent

**Always delegate when**:
- User explicitly triggers `/memory-grooming` command (any mode)
- Comprehensive knowledge base maintenance needed
- Duplicate detection and merging required
- Quality assessment and enhancement operations
- Relationship maintenance and graph health optimization
- Obsolete pattern removal or knowledge base reorganization

**Never handle directly**:
- Memory-curator has exclusive CRUD access to Neo4j knowledge graph
- Direct grooming bypasses systematic quality control
- Manual operations lack comprehensive graph audit capabilities

### Agent Selection Guide for Memory Grooming

| Task Type | Recommended Agent | When to Use | Expected Output |
|-----------|------------------|-------------|-----------------|
| Knowledge base grooming | memory-curator | ALWAYS for /memory-grooming command | Grooming report with statistics, health status, recommendations |

### Grooming Modes

| Mode | Purpose | Agent Focus |
|------|---------|-------------|
| Default | Full maintenance | All 6 grooming operations |
| session | Conversation analysis | Pattern extraction from current session |
| success | Pattern capture | Store successful implementation |
| failure | Anti-pattern capture | Record lesson with prevention strategies |
| review | Quality check | Assess recent memory additions |

## 3-STAGE WORKFLOW GUIDE

Memory grooming workflows follow a 3-stage pattern to ensure comprehensive knowledge base maintenance.

### Stage 1: Setup & Grooming Planning (REQUIRED - Use Sequential Thinking)

**Mandatory Skills** (Step 0):
- Load all skills listed in command metadata before workflow execution
- `Skill("orchestrator-core:agent-delegation")`

**Planning with Sequential Thinking**:
Use `mcp__sequential-thinking__sequentialthinking` to:
- Parse grooming mode (default/session/success/failure/review)
- Extract context or description (if provided)
- Validate mode and prepare grooming scope
- Prepare context for memory-curator deployment
- Define success criteria for grooming operation

**Pre-Execution Checklist**:
- [ ] All mandatory skills loaded
- [ ] Grooming mode identified
- [ ] Context/description extracted (if applicable)
- [ ] Agent prompt validated against 5-requirement format
- [ ] User confirmation received for manual grooming

### Stage 2: Grooming Execution

**SEQUENTIAL Execution Pattern**:
- Deploy memory-curator agent (single agent, complex maintenance workflow)
- Agent performs mode-specific operations:
  - **Default**: Full graph audit → 6 grooming operations → health report
  - **Session**: Conversation analysis → pattern extraction → memory creation
  - **Success**: Implementation analysis → success pattern creation
  - **Failure**: Failure analysis → anti-pattern creation with prevention
  - **Review**: Recent memories audit → quality enhancement

**Sequential Thinking (REQUIRED in agent)**:
Agent MUST use sequential thinking for:
- Graph health assessment and operation planning
- Duplicate detection with merge decision matrix
- Quality gate evaluation (confidence, evidence, completeness, relationships)
- Systematic execution of 6 grooming operations

### Stage 3: Validation & Reporting (REQUIRED - Use Sequential Thinking)

**Use Sequential Thinking to**:
- Review grooming completion report
- Verify all operations completed successfully
- Validate graph health improvements
- Ensure duplicate-first workflow was followed
- Assess knowledge base quality impact
- Confirm quality gates passed

**Output Validation Checklist**:
- [ ] Mode-specific operations completed
- [ ] Duplicate-first workflow followed (for create operations)
- [ ] Statistics provided (memories processed, duplicates merged, enhancements)
- [ ] Health status assessed (High/Medium/Low)
- [ ] Quality gates passed (confidence ≥0.7, evidence present, complete context)
- [ ] Relationship ratio maintained (2-3:1 target)
- [ ] Recommendations provided for future grooming
- [ ] No scope violations or errors

## AGENT PROMPT TEMPLATES

Memory grooming ALWAYS delegates to memory-curator using the **5-requirement format**.

**5-Requirement Format**:
1. **ROLE**: Agent's identity and expertise domain
2. **CONTEXT**: Relevant background, project specifics, constraints
3. **TASK**: Single, measurable objective with clear boundaries
4. **CONSTRAINTS**: Scope limits, token budgets, time limits, circuit breakers
5. **OUTPUT**: Exact deliverable format with verification criteria

### Template: memory-curator for Full Grooming (Default Mode)

```
ROLE:
You are a memory-curator specializing in comprehensive knowledge base maintenance and health optimization for the Neo4j knowledge graph.

CONTEXT:
- Grooming mode: Default (full maintenance)
- Last grooming: [DATE or "Unknown"]
- Graph size: [NUMBER of memories]
- Background: [Why grooming is needed]

TASK:
Perform comprehensive knowledge base grooming:
1. **Graph Audit**: Assess current state (total memories, relationship ratio, isolated nodes, quality distribution)
2. **Duplicate Detection & Merging**: Find similar memories (>0.8 similarity), merge with decision matrix
3. **Quality Enhancement**: Review low-confidence memories (<0.7), add missing context, improve clarity
4. **Relationship Maintenance**: Connect isolated memories, fix broken links, optimize ratio (2-3:1 target)
5. **Obsolescence Management**: Identify outdated patterns, remove or update with modern alternatives
6. **Organization & Optimization**: Group related memories, improve keywords, enhance descriptions

CONSTRAINTS:
- Token Budget: [e.g., 30000 tokens for comprehensive grooming]
- Time Limit: [e.g., "Complete within reasonable time"]
- Quality Gates: Confidence ≥0.7, evidence required, complete context, relationship ratio 2-3:1
- Circuit Breaker: Stop if Neo4j unavailable or critical errors

OUTPUT:
Provide a GROOMING COMPLETION REPORT with:
1. **Statistics**:
   - Total memories before/after
   - Duplicates merged (count, examples)
   - Quality enhancements (count, examples)
   - Relationships added/removed
   - Obsolete patterns removed
2. **Health Status**:
   - Overall quality (High/Medium/Low)
   - Organization level (Well-organized/Needs improvement)
   - Coverage assessment (Comprehensive/Gaps identified)
   - Relationship ratio achieved
3. **Operations Summary**:
   - Duplicate detection results
   - Quality enhancements made
   - Relationship maintenance actions
   - Obsolescence removals
   - Organization improvements
4. **Recommendations**:
   - Future grooming schedule (Weekly/Monthly/Quarterly)
   - Knowledge gaps to address
   - Quality improvements needed

AVAILABLE SKILLS (contextual suggestions):
- Use sequential thinking for graph health assessment and operation planning
- Use Neo4j CRUD tools for comprehensive maintenance operations
```

### Template: memory-curator for Session Analysis Mode

```
ROLE:
You are a memory-curator specializing in extracting patterns, lessons, and anti-patterns from work sessions.

CONTEXT:
- Grooming mode: Session analysis
- Conversation context: [Recent messages, files modified, changes made]
- Background: [Why session analysis requested]

TASK:
Analyze current conversation and extract valuable knowledge:
1. Review conversation for successful patterns, failures, and lessons
2. For each identified pattern:
   - **MANDATORY: Check for duplicates** (search similar memories)
   - Apply merge decision matrix (>0.8 merge, 0.5-0.8 analyze, <0.5 create)
   - Extract complete context (what/why/how)
   - Assign confidence score
   - Create relationships
3. Categorize findings (ImplementationPattern/AntiPattern/Lesson)
4. Store high-quality memories only

CONSTRAINTS:
- Token Budget: [e.g., 15000 tokens]
- Focus on: Patterns with reusable value (not one-off solutions)
- Quality Gates: Real experience, complete context, reusable, actionable
- Circuit Breaker: Stop if no valuable patterns found

OUTPUT:
Provide a SESSION ANALYSIS REPORT with:
1. **Patterns Extracted**: Count and types (success/failure/lesson)
2. **Memory Details**: For each memory created/merged
   - Name and description
   - Type and confidence score
   - Duplicate check results
   - Relationships created
3. **Quality Assessment**: All quality gates passed
4. **Knowledge Base Impact**: New insights added to graph

AVAILABLE SKILLS (contextual suggestions):
- Use sequential thinking for pattern identification and duplicate detection
- Use Neo4j CRUD tools for memory creation/merging
```

### Template: memory-curator for Success/Failure Capture

```
ROLE:
You are a memory-curator specializing in capturing specific success patterns or failure lessons.

CONTEXT:
- Grooming mode: [Success OR Failure] capture
- Description: [USER_DESCRIPTION]
- Work context: [Recent implementation or failure details]

TASK:
Capture specific pattern or lesson:
1. **MANDATORY: Check for duplicates** (search for similar patterns)
2. Apply merge decision matrix (>0.8 similarity requires merge)
3. Extract complete context:
   - **Success**: Implementation details, why it worked, when to use
   - **Failure**: What failed, root cause, prevention strategies
4. Assign confidence score:
   - Success: 0.9+ (proven to work)
   - Failure: 0.85+ (important to avoid)
5. Create relationships to related patterns
6. Store as ImplementationPattern (success) or AntiPattern (failure)

CONSTRAINTS:
- Token Budget: [e.g., 10000 tokens]
- Quality Gates: Real experience, complete context, actionable guidance
- Circuit Breaker: Stop if duplicate check fails

OUTPUT:
Provide a CAPTURE REPORT with:
1. **Duplicate Check**: Similar memories found, merge decision
2. **Memory Created/Merged**:
   - Name and description
   - Type (ImplementationPattern/AntiPattern)
   - Confidence score with justification
   - Context completeness
3. **Relationships**: Links to related patterns
4. **Quality Confirmation**: All gates passed

AVAILABLE SKILLS (contextual suggestions):
- Use sequential thinking for duplicate detection and context extraction
- Use Neo4j CRUD tools for pattern storage
```

### Template: memory-curator for Review Mode

```
ROLE:
You are a memory-curator specializing in quality assessment and enhancement of recent memory additions.

CONTEXT:
- Grooming mode: Review
- Review scope: Recent memories (last N days/additions)
- Background: [Why review requested]

TASK:
Review recent memory additions for quality:
1. Identify recent memories (by timestamp or creation date)
2. For each memory, assess:
   - Confidence score appropriateness
   - Evidence and context completeness
   - Relationship health (isolated? proper ratio?)
   - Description clarity and keyword effectiveness
3. Enhance low-quality memories:
   - Add missing context
   - Improve descriptions
   - Create relationships if isolated
   - Adjust confidence scores if needed
4. Identify duplicates that were missed in initial creation

CONSTRAINTS:
- Token Budget: [e.g., 12000 tokens]
- Review scope: [Last N memories OR last N days]
- Quality Gates: Confidence ≥0.7, complete context, relationship ratio 2-3:1
- Circuit Breaker: Stop after reviewing [N] memories

OUTPUT:
Provide a REVIEW REPORT with:
1. **Summary**: Memories reviewed, enhancements made
2. **Quality Issues Found**:
   - Low-confidence memories improved
   - Missing context added
   - Isolated memories connected
   - Duplicates detected and merged
3. **Health Assessment**: Overall quality of recent additions
4. **Recommendations**: Quality control improvements

AVAILABLE SKILLS (contextual suggestions):
- Use sequential thinking for systematic quality assessment
- Use Neo4j CRUD tools for enhancement operations
```

## SKILL MAPPING

Skills provide specialized guidance for memory grooming workflows.

### Mandatory Skills for Memory Grooming (Step 0)

| Skill | Purpose | When to Load | Expected Benefit |
|-------|---------|--------------|------------------|
| agent-delegation | 5-requirement prompt framework, validation checklist | Always (Step 0) | Well-structured prompt for memory-curator agent |

**Loading Pattern**:
```
Step 0: Load Orchestration Skills
0. Invoke all required skills:
   - Skill("orchestrator-core:agent-delegation")
```

### Contextual Skills for memory-curator Agent

| Skill | Suggest When | Agent Types | Expected Benefit |
|-------|--------------|-------------|------------------|
| N/A | memory-curator has full Neo4j CRUD access | memory-curator | Comprehensive knowledge base maintenance capabilities |

**Contextual Loading Pattern** (in agent prompts):
```
AVAILABLE SKILLS (contextual suggestions):
- Use sequential thinking for graph health assessment, duplicate detection, quality evaluation
- Use Neo4j CRUD tools for comprehensive maintenance (create, read, update, delete)
```

**Step 1: Deploy Memory Curator**
1. **Delegate to memory-curator using agent-delegation principles** for comprehensive maintenance
2. **Perform full graph audit** to assess current state
3. **Execute grooming operations** including:
   - Duplicate detection and merging
   - Quality assessment and enhancement
   - Relationship maintenance
   - Obsolete pattern removal
   - Graph reorganization
   - Keyword optimization

## 🚨 CRITICAL: Duplicate-First Workflow

**Every grooming operation MUST follow this mandatory workflow:**

### Duplicate Detection FIRST (Non-Negotiable)
Before creating ANY new memory, the curator MUST:
1. **Search exact matches**: `mcp__neo4j__find_memories_by_name()`
2. **Search semantic similarity**: `mcp__neo4j__search_memories()`
3. **Check domain patterns**: Search for domain-specific variations
4. **Decision matrix**:
   - Similarity >0.8: MERGE (required)
   - Similarity 0.5-0.8: Analyze & decide
   - Similarity <0.5: Create with relationships

### Quality Gates (All Must Pass)
- **Confidence**: Minimum 0.7 threshold
- **Evidence**: Concrete implementation required
- **Completeness**: Context + Solution + Outcome
- **Relationships**: Target 2-3:1 ratio

## Grooming Operations

**Six core operations**:
1. **Duplicate Detection**: Merge similar memories (>0.8 similarity mandatory)
2. **Quality Enhancement**: Review low-confidence memories, add missing context
3. **Relationship Maintenance**: Connect isolated memories, fix broken links
4. **Obsolescence Management**: Remove outdated patterns, update with modern alternatives
5. **Organization**: Group related memories, create logical hierarchies
6. **Search Optimization**: Update keywords, improve descriptions for better discovery

## When to Use

**Regular**: Weekly (light), Monthly (comprehensive), Quarterly (deep reorganization)
**Triggered**: After major projects, when duplicates noticed, before new initiatives, when search inconsistent

## Expected Output

Memory-curator provides grooming report with:
- **Statistics**: Total memories, duplicates merged, enhancements, relationships added/removed
- **Health Status**: Overall quality (High/Medium/Low), organization, coverage assessment
- **Recommendations**: Future grooming needs, knowledge gaps to address

## Important Notes

- **Not for regular tasks**: This command is for maintenance only
- **Memory retrieval**: For task context, memory-assistant handles retrieval automatically
- **Time investment**: Grooming can take time depending on graph size
- **Quality over quantity**: Focus on valuable, reusable knowledge

## Integration with Task Flow

The memory system now has clear separation:

1. **During Tasks**: `memory-assistant` automatically retrieves relevant context
2. **For Maintenance**: `/memory-grooming` triggers curator for quality control
3. **Result**: Clean, organized knowledge that enhances all agent performance

## Command Chain

### Standard Grooming:
```
User: /memory-grooming
↓
Orchestrator: Recognizes command
↓
Task(subagent_type="memory-curator",
     prompt="Perform comprehensive knowledge base grooming...")
↓
Memory Curator: Executes full maintenance
↓
Report: Detailed grooming results
```

### Session Analysis:
```
User: /memory-grooming session
↓
Orchestrator: Recognizes command with mode
↓
Task(subagent_type="memory-curator",
     prompt="Analyze current conversation and extract patterns, lessons, and anti-patterns...")
↓
Memory Curator: Reviews conversation, creates memories
↓
Report: Patterns captured, lessons learned
```

### Success Capture:
```
User: /memory-grooming success "JWT implementation worked"
↓
Orchestrator: Recognizes success pattern
↓
Task(subagent_type="memory-curator",
     prompt="Capture successful pattern: JWT implementation. Extract and store with high confidence...")
↓
Memory Curator: Analyzes success, stores pattern
↓
Report: Pattern stored for future reference
```

### Failure Learning:
```
User: /memory-grooming failure "N+1 query problem"
↓
Orchestrator: Recognizes failure/anti-pattern
↓
Task(subagent_type="memory-curator",
     prompt="Capture anti-pattern: N+1 query problem. Store lesson with prevention strategies...")
↓
Memory Curator: Analyzes failure, stores lesson
↓
Report: Anti-pattern recorded, prevention noted
```

**Success criteria:**
- Memory records updated/consolidated successfully
- No scope violations or errors
- Within token/time budget
- Memory quality improved (redundancy reduced, clarity enhanced)

**After completion:**
Return control to orchestrator with grooming completion report.

This separation ensures the knowledge base receives proper maintenance without interfering with active development work.
