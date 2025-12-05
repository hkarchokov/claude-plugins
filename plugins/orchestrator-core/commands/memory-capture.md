---
name: memory-capture
description: Capture lessons, patterns, and anti-patterns from current work session
trigger: /memory-capture
skills: [agent-delegation]
---

# Memory Capture Command

## 🚨 IMPORTANT: MANUAL CAPTURE ONLY
**Memory capture is a MANUAL, USER-INITIATED operation. It is NOT automatic.**
- Requires explicit user command: `/memory-capture [type]`
- User controls what gets captured and when
- Quality over quantity - selective capture of valuable patterns
- Separate from automatic memory retrieval during tasks

## Purpose
Extract and store valuable patterns, lessons learned, and anti-patterns from the current work session. This enables continuous learning from real experiences, building a knowledge base from actual successes and failures.

## Usage
```
/memory-capture [type] [description]
```

### Types:
- **`success`** - Capture a successful implementation pattern
- **`failure`** - Record an anti-pattern or mistake to avoid
- **`lesson`** - Store a general lesson learned
- **`pattern`** - Document a reusable pattern discovered
- **`all`** - Analyze entire session for all types

### Examples:
```
/memory-capture success "JWT refresh token rotation"
/memory-capture failure "N+1 query in user listing"
/memory-capture lesson "Always check for symlinks first"
/memory-capture pattern "Flask health check implementation"
/memory-capture all                                    # Comprehensive session analysis
```

## What Happens

**Step 0: Load Orchestration Skills**
0. **Invoke all required skills** to load memory capture guidance:
   - `Skill("orchestrator-core:agent-delegation")` - Delegation best practices for memory-curator deployment

**Skill Hint Guidance**
When deploying memory-curator agent via Task(), include relevant skill hints in the prompt:
- **agent-delegation**: Frameworks for 5-requirement prompts and deploying memory agents

## DELEGATION STRATEGY

Memory capture is a specialized workflow that ALWAYS delegates to the memory-curator agent for quality knowledge base management.

### When to Delegate to memory-curator Agent

**Always delegate when**:
- User explicitly triggers `/memory-capture` command
- Memory creation requires duplicate checking and merge decisions
- Quality knowledge base maintenance needed
- Systematic pattern extraction from work session
- Confidence scoring and relationship management required

**Never handle directly**:
- Memory-curator has exclusive CRUD access to Neo4j knowledge graph
- Direct memory creation bypasses duplicate checking (creates low-quality duplicates)
- Manual memory management lacks systematic quality control

### Agent Selection Guide for Memory Capture

| Task Type | Recommended Agent | When to Use | Expected Output |
|-----------|------------------|-------------|-----------------|
| Memory capture | memory-curator | ALWAYS for /memory-capture command | Memory creation/merge report with confidence scores |

## 3-STAGE WORKFLOW GUIDE

Memory capture workflows follow a 3-stage pattern to ensure quality knowledge base growth.

### Stage 1: Setup & Capture Planning (REQUIRED - Use Sequential Thinking)

**Mandatory Skills** (Step 0):
- Load all skills listed in command metadata before workflow execution
- `Skill("orchestrator-core:agent-delegation")`

**Planning with Sequential Thinking**:
Use `mcp__sequential-thinking__sequentialthinking` to:
- Parse capture type (success/failure/lesson/pattern/all)
- Extract description from user command
- Validate capture type and description
- Prepare context for memory-curator deployment
- Define success criteria for capture

**Pre-Execution Checklist**:
- [ ] All mandatory skills loaded
- [ ] Capture type identified (success/failure/lesson/pattern/all)
- [ ] Description extracted (if provided)
- [ ] Agent prompt validated against 5-requirement format
- [ ] User confirmation received for manual capture

### Stage 2: Memory Capture Execution

**SEQUENTIAL Execution Pattern**:
- Deploy memory-curator agent (single agent, not parallel)
- Agent performs mandatory duplicate check FIRST
- Agent applies merge decision matrix (similarity thresholds)
- Agent creates new memory OR merges with existing
- Agent adds tags and relationships
- Agent produces capture completion report

**Sequential Thinking (REQUIRED in agent)**:
Agent MUST use sequential thinking for:
- Duplicate detection and similarity assessment
- Merge decision matrix evaluation
- Context extraction from work session
- Confidence score calculation

### Stage 3: Validation & Reporting (REQUIRED - Use Sequential Thinking)

**Use Sequential Thinking to**:
- Review capture completion report
- Verify duplicate check was performed
- Validate merge decision was appropriate
- Ensure relationships were created (no isolated memories)
- Confirm confidence scores are within expected ranges
- Assess knowledge base quality impact

**Output Validation Checklist**:
- [ ] Duplicate check performed (mandatory)
- [ ] Merge decision matrix applied correctly
- [ ] Memory created/merged successfully
- [ ] Confidence score assigned (0.6-0.95+ range)
- [ ] Tags added for discovery
- [ ] Relationships created (2-3:1 ratio target)
- [ ] No isolated memories created
- [ ] Quality standards met (real experience, complete context, reusable, actionable)

## AGENT PROMPT TEMPLATES

Memory capture ALWAYS delegates to memory-curator using the **5-requirement format**.

**5-Requirement Format**:
1. **ROLE**: Agent's identity and expertise domain
2. **CONTEXT**: Relevant background, project specifics, constraints
3. **TASK**: Single, measurable objective with clear boundaries
4. **CONSTRAINTS**: Scope limits, token budgets, time limits, circuit breakers
5. **OUTPUT**: Exact deliverable format with verification criteria

### Template: memory-curator for Memory Capture

```
ROLE:
You are a memory-curator specializing in capturing high-quality patterns, lessons, and anti-patterns from work sessions into the Neo4j knowledge graph.

CONTEXT:
- Capture type: [success/failure/lesson/pattern/all]
- Description: [USER_DESCRIPTION if provided]
- Work session context: [Recent files modified, changes made, problems solved]
- Background: [Why capture is needed]

TASK:
Capture valuable knowledge from current work session:
1. **MANDATORY: Check for duplicates FIRST**
   - Search Neo4j for similar patterns using multiple methods
   - Calculate similarity scores (0-1.0)
   - Apply merge decision matrix:
     * Similarity >0.8: Merge with existing memory
     * Similarity 0.5-0.8: Analyze unique value, merge if redundant
     * Similarity <0.5: Create new memory with links to related
2. Extract context from work session (implementation details, failure causes, lessons)
3. Create new memory OR merge with existing based on decision matrix
4. Assign confidence score (0.6-0.95+ based on capture type)
5. Add appropriate tags (success/anti-pattern/lesson/pattern)
6. Create relationships to related patterns (2-3:1 ratio target, NO isolated memories)

CONSTRAINTS:
- Token Budget: [e.g., 15000 tokens]
- MANDATORY duplicate check before creation
- Confidence ranges: success (0.9+), failure (0.85+), pattern (0.7-0.9), observation (0.6-0.8)
- Quality standards: Real experience only, complete context, reusable, actionable
- Circuit Breaker: Stop if duplicate check fails or Neo4j unavailable

OUTPUT:
Provide a CAPTURE COMPLETION REPORT with:
1. **Duplicate Check Results**:
   - Similar memories found (if any)
   - Similarity scores
   - Merge decision (create new OR merge with existing)
2. **Memory Details**:
   - Type (ImplementationPattern/AntiPattern/Lesson)
   - Name and description
   - Confidence score with justification
   - Tags applied
3. **Relationships Created**:
   - Related patterns linked
   - Relationship types (similar_to, extends, contradicts, etc.)
   - No isolated memories confirmed
4. **Quality Assessment**:
   - Real experience? Yes/No
   - Complete context? Yes/No
   - Reusable? Yes/No
   - Actionable? Yes/No
5. **Knowledge Base Impact**:
   - New memory created OR existing memory enhanced
   - Graph health maintained (relationship ratio, no duplicates)

AVAILABLE SKILLS (contextual suggestions):
- Use sequential thinking for duplicate detection and merge decisions
- Use Neo4j CRUD tools for memory creation/merging
```

## SKILL MAPPING

Skills provide specialized guidance for memory capture workflows.

### Mandatory Skills for Memory Capture (Step 0)

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
| N/A | memory-curator has Neo4j CRUD access | memory-curator | Full knowledge base management capabilities |

**Contextual Loading Pattern** (in agent prompts):
```
AVAILABLE SKILLS (contextual suggestions):
- Use sequential thinking for duplicate detection and merge decisions
- Use Neo4j CRUD tools (create_entities, create_relations, add_observations, etc.)
```

### 🚨 MANDATORY: Duplicate Check First
**Before ANY memory creation, the curator MUST:**
1. **Search for existing similar patterns** using multiple search methods
2. **Apply merge decision matrix**:
   - Similarity >0.8: Merge with existing
   - Similarity 0.5-0.8: Analyze unique value
   - Similarity <0.5: Create new with links
3. **Ensure relationship optimization** (2-3:1 ratio target)

### Capture Workflow:
**All capture types follow same protocol**:
1. **CHECK FOR DUPLICATES FIRST** (mandatory - see merge decision matrix above)
2. **Analyze**: Implementation (success), failure cause (failure), or full session (all)
3. **Store**: High confidence if unique (0.85-0.95+), merge if duplicate
4. **Tag**: Appropriate labels for discovery (success/anti-pattern/lesson)
5. **Link**: Connect to related patterns (required - no isolated memories)

## Memory Quality Standards

### High-Value Captures:
- **Real Experience**: Based on actual work, not theory
- **Complete Context**: Includes when/why/how it works
- **Reusable**: Pattern applies beyond single use
- **Actionable**: Clear guidance for future use

### Automatic Confidence Scoring:
- **Success patterns**: 0.9+ (proven to work)
- **Failure lessons**: 0.85+ (important to avoid)
- **General patterns**: 0.7-0.9 (depending on clarity)
- **Observations**: 0.6-0.8 (contextual notes)

## Integration with Workflow

### Proactive Capture Points:
1. **After successful implementation** - Capture what worked
2. **After fixing a bug** - Record the solution pattern
3. **After encountering error** - Document the anti-pattern
4. **After complex task** - Extract multiple patterns
5. **End of session** - Comprehensive capture

### Natural Language Triggers:
The orchestrator recognizes natural language cues:
- "That worked perfectly!" → Suggests success capture
- "This was a mistake" → Suggests failure capture
- "Remember this for next time" → Suggests pattern capture
- "Good lesson learned" → Suggests lesson capture

## Command Chain

### Capture Flow:
```
User: /memory-capture [type] "[description]"
↓
Orchestrator → Deploy memory-curator via agent-delegation
↓
Memory Curator:
  - Checks duplicates (mandatory)
  - Analyzes context (implementation/failure/session)
  - Creates/merges entity (ImplementationPattern/AntiPattern/Lesson)
  - Adds tags + relationships
↓
Report: Memory stored/merged with confidence score
```

**Variations**: `success` captures working patterns (0.9+ confidence), `failure` captures anti-patterns with prevention strategies, `all` analyzes full session for multiple memories.

## Best Practices

**When**: Immediately after success/failure, before ending session, when pattern emerges
**What**: Working solutions, failed approaches, debugging techniques, optimizations, architecture decisions
**Why**: Real experiences create high-confidence memories, mistakes become preventable anti-patterns

## Important Notes

- **Not for regular grooming**: Use `/memory-grooming` for maintenance
- **Quality over quantity**: Better to capture few high-quality patterns
- **Context is king**: Always include why/when/how information
- **Real experience only**: Don't create theoretical patterns

**Success criteria:**
- Memory records created successfully
- Key findings captured accurately
- No scope violations or errors
- Within token/time budget

**After completion:**
Return control to orchestrator with capture completion report.

This command enables continuous learning from every coding session, turning experiences into reusable knowledge.
