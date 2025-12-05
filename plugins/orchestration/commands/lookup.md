---
description: Fast codebase lookups using Explore agent. For quick questions like "what does X do", "find Y", "where is Z". Use /investigate for thorough analysis.
argument-hint: topic to lookup
---

# Quick Lookup Command

**Purpose**: Rapid codebase exploration for simple questions using the Explore agent.

**When to use**:
- Quick function/component lookups ("what does getUserById do?")
- File finding ("where is authentication implemented?")
- Configuration searches ("list all API endpoints")
- Code location queries ("find error handling patterns")

**When NOT to use** (use `/investigate` instead):
- Architecture analysis
- Security reviews
- Pattern consistency assessment
- Production readiness evaluation

---

## Workflow

Deploy Explore agent with focused query and synthesize results.

---

## Deploy Explore Agent & Synthesize

Deploy the Explore agent with the user's query:

```
Task(subagent_type="Explore",
     description="Quick codebase lookup",
     prompt="""$ARGUMENTS - Perform focused codebase lookup.

LOOKUP REQUEST: $ARGUMENTS

APPROACH:
1. Use Glob to find relevant files
2. Use Grep to search for specific patterns/functions/components
3. Use Read to examine key files and extract relevant sections
4. Provide file:line references for all findings
5. Include code snippets with context where helpful

CONSTRAINTS:
- Focus on answering the specific question
- Limit scope to directly relevant files (maximum 10-15 files)
- Prioritize accuracy over exhaustive coverage

OUTPUT FORMAT:
## Findings

**Query**: [what was requested]

**Results**: ([count] items found)
1. file:line - [description]
   ```language
   [code snippet if relevant]
   ```

2. file:line - [description]
   ...

**Summary**: [2-3 sentence answer]
""",
     model="haiku")
```

**After Explore completes**, present the findings to the user:

```markdown
## Lookup Results

[Explore agent's findings]

**Lookup complete** ✅

Need deeper analysis? Use `/investigate "$ARGUMENTS"` for thorough multi-agent investigation.
```

---

## Example Usage

**Quick function lookup**:
```
/lookup what does getUserById do
```
→ ~1 minute, returns function location, code snippet, explanation

**Find pattern**:
```
/lookup find all API endpoints
```
→ ~90 seconds, returns list of endpoints with file:line references

**Configuration search**:
```
/lookup where is database configured
```
→ ~75 seconds, returns config files and relevant code

---

## Comparison: /lookup vs /investigate

| Aspect | /lookup | /investigate |
|--------|---------|--------------|
| **Time** | 1-2 min | 5-10 min |
| **Agents** | 1 (Explore) | 4-7 (multi-agent) |
| **Depth** | Quick findings | Comprehensive analysis |
| **Validation** | None | Full validation |
| **Use for** | "Where/What is X?" | "How does X work?" |

---

## Success Criteria

A successful lookup provides:
- ✅ Direct answer to the question
- ✅ Specific file:line references
- ✅ Code snippets with context
- ✅ Completion under 2 minutes

---

## Tips

**Be specific**:
- ✅ "find the JWT token validation function"
- ❌ "find auth stuff" (too vague)

**Use for focused questions**:
- ✅ "where is password hashing implemented"
- ❌ "how does authentication work" (use `/investigate`)

**Upgrade to /investigate when**:
- You need to understand "how" not just "where"
- You need pattern analysis
- You need security validation
- The lookup reveals unexpected complexity
