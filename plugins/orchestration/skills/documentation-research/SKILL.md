---
name: documentation-research
description: Methodology for fetching and extracting relevant documentation from official sources. This skill teaches agents to identify technologies, locate authoritative documentation, extract best practices, and validate code patterns against official guidelines.
---

# Documentation Research

## Purpose

Enable agents to dynamically fetch current, authoritative documentation for detected technologies, eliminating reliance on potentially outdated training data. This skill provides systematic approaches for finding, fetching, and extracting relevant information from official documentation sources.

## Core Principle

**"Trust but verify - validate patterns against official documentation"**

Always prefer current official documentation over assumptions. What was best practice yesterday might be deprecated today.

## When to Use This Skill

Load this skill when:
- Validating code patterns against best practices
- Checking for deprecated features or patterns
- Understanding security guidelines for specific technologies
- Verifying version-specific behavior
- Resolving uncertainty about technology constraints

## Technology Detection Methods

### Method 1: Package File Analysis

**Package.json (Node.js/JavaScript)**:
```json
{
  "dependencies": {
    "next": "14.0.3",      // Next.js version 14.0.3
    "prisma": "^5.2.0",    // Prisma version 5.2.x
    "express": "~4.18.0"   // Express version 4.18.x
  }
}
```

**Detection Pattern**:
- Extract package name and version
- Note version constraints (^, ~, exact)
- Identify framework vs library vs tool

**Other Package Files**:
- `requirements.txt` / `Pipfile` (Python)
- `go.mod` (Go)
- `Cargo.toml` (Rust)
- `pom.xml` / `build.gradle` (Java)
- `composer.json` (PHP)
- `Gemfile` (Ruby)

### Method 2: Import Statement Analysis

**JavaScript/TypeScript**:
```typescript
import { useState } from 'react';        // React
import jwt from 'jsonwebtoken';          // JWT library
import { PrismaClient } from '@prisma/client';  // Prisma
```

**Python**:
```python
from fastapi import FastAPI  # FastAPI framework
import boto3                 # AWS SDK
from django.db import models # Django ORM
```

**Detection Pattern**:
- Map import sources to technologies
- Note specific modules imported (hints at features used)
- Identify first-party vs third-party

### Method 3: Pattern Recognition

**File Structure Patterns**:
```
app/api/route.ts         → Next.js 13+ App Router
pages/api/               → Next.js Pages Router
src/controllers/         → MVC pattern (Express, NestJS)
app/models/              → Rails or Django
```

**Code Patterns**:
```typescript
@Controller('users')     → NestJS decorators
app.get('/users', ...)   → Express routing
const [state, setState]  → React hooks
```

**Configuration Files**:
```
next.config.js           → Next.js
tsconfig.json            → TypeScript
.eslintrc.js             → ESLint
jest.config.js           → Jest testing
docker-compose.yml       → Docker
```

### Method 4: Version Detection

**Direct Version Checks**:
```javascript
// In code comments or constants
const NEXT_VERSION = '14.0.3';

// In configuration
module.exports = {
  reactStrictMode: true,  // React 18+ feature
  appDir: true            // Next.js 13+ feature
};
```

**Feature-Based Detection**:
- Use of specific APIs indicates minimum version
- Deprecated warnings suggest version mismatch
- Build errors often reveal version requirements

## Documentation Source Priority

### Priority 1: Official Documentation (Highest)

**Identification Patterns**:
- Domain matches technology name (nextjs.org, reactjs.org)
- GitHub repo from official organization
- Docs subdomain (docs.example.com)

**Examples**:
```
Framework/Library    →  Official Docs URL
Next.js              →  https://nextjs.org/docs
React                →  https://react.dev/
Prisma               →  https://www.prisma.io/docs
Express              →  https://expressjs.com/
Django               →  https://docs.djangoproject.com/
FastAPI              →  https://fastapi.tiangolo.com/
AWS SDK              →  https://docs.aws.amazon.com/
```

### Priority 2: Official GitHub Repositories

**Value**: README files, SECURITY.md, CONTRIBUTING.md, release notes

**URL Pattern**: `https://github.com/[org]/[repo]`

**Key Files**:
- `README.md` - Quick start, basic patterns
- `SECURITY.md` - Security best practices
- `CHANGELOG.md` - Version changes, deprecations
- `docs/` folder - Extended documentation

### Priority 3: MDN Web Docs

**For**: Web APIs, JavaScript features, CSS, HTML

**URL**: `https://developer.mozilla.org/`

**Particularly Valuable For**:
- Browser compatibility
- Web security best practices
- JavaScript language features
- Web API specifications

### Priority 4: Official Blogs and Updates

**Value**: Migration guides, deprecation notices, security advisories

**Examples**:
- Next.js Blog (nextjs.org/blog)
- React Blog (react.dev/blog)
- Security advisories (GitHub Security)

### Priority 5: Standards Organizations

**For**: Specifications, protocols, standards

**Examples**:
- JWT.io for JWT specifications
- OWASP.org for security guidelines
- W3C for web standards
- RFC documents for protocols

## Search Strategy Templates

### Strategy 1: Best Practices Search

**Search Queries**:
```
"[Technology] [Version] best practices"
"[Technology] [Version] security guidelines"
"[Technology] [Version] production checklist"
"[Technology] [Version] performance optimization"
```

**Example**:
```
"Next.js 14 best practices"
"Prisma 5 connection pooling"
"Express.js security headers"
```

### Strategy 2: Specific Feature Documentation

**Search Queries**:
```
"[Technology] [Feature] documentation"
"[Technology] [API method] example"
"[Technology] [Error message]"
```

**Example**:
```
"Next.js middleware documentation"
"Prisma transaction isolation levels"
"React useEffect cleanup"
```

### Strategy 3: Migration and Deprecation

**Search Queries**:
```
"[Technology] [Version] migration guide"
"[Technology] [Version] breaking changes"
"[Technology] deprecated [Feature]"
"[Technology] [OldVersion] to [NewVersion]"
```

**Example**:
```
"Next.js 13 to 14 migration"
"React deprecated componentWillMount"
"Node.js 16 to 20 breaking changes"
```

### Strategy 4: Security and Vulnerabilities

**Search Queries**:
```
"[Technology] security best practices"
"[Technology] CVE vulnerabilities"
"[Technology] [Version] security patches"
"[Technology] OWASP guidelines"
```

## Information Extraction Patterns

### Best Practices Extraction

**Look For**:
- "Recommended approach"
- "Best practice"
- "Do/Don't" sections
- Code examples marked as "Good" vs "Bad"
- Performance tips
- Security considerations

**Example Extraction**:
```
From Next.js docs on data fetching:
✅ GOOD: Use server components for data fetching
❌ BAD: Client-side fetching for initial page data
```

### Security Guidelines Extraction

**Look For**:
- Security headers configuration
- Authentication/authorization patterns
- Input validation requirements
- CORS configuration
- Rate limiting recommendations
- Encryption requirements

**Red Flag Keywords**:
- "Deprecated"
- "Security vulnerability"
- "Do not use"
- "Unsafe"
- "Legacy"

### Anti-Pattern Identification

**Look For**:
- "Common mistakes"
- "Anti-patterns"
- "What not to do"
- "Pitfalls"
- "Known issues"

**Example**:
```
From React docs:
Anti-pattern: Directly mutating state
Correct pattern: Use setState or state update function
```

### Version-Specific Changes

**Look For**:
- "New in version X"
- "Changed in version X"
- "Removed in version X"
- "Breaking changes"
- Migration guides

**Example**:
```
Next.js 13 → 14:
- App Router stable
- Turbopack improvements
- Server Actions stable
```

## Cross-Reference Methodology

### Step 1: Identify Pattern in Code

```typescript
// Found in code:
export default function middleware(req) {
  // Custom logic
  return;  // Returns undefined
}
```

### Step 2: Find Documentation Section

Search: "Next.js middleware return value"

Find: Middleware must return NextResponse

### Step 3: Compare Pattern vs Documentation

```
Code Pattern: Returns undefined
Doc Requirement: Must return NextResponse
Status: ❌ MISMATCH - Deprecated pattern
```

### Step 4: Extract Correction

```
Documentation says:
✅ return NextResponse.next()
❌ return; // undefined

Severity: HIGH - Middleware won't work in Next.js 14
```

### Step 5: Find Migration Path

Look for:
- Migration guides
- Codemods available
- Step-by-step instructions
- Breaking change notices

## Handling Missing Documentation

### Fallback Strategy

```
if official_docs_not_found:
    try github_repository_readme
    try github_issues_for_pattern
    try package_registry_page (npm, pypi)
    check_for_community_docs
    note_documentation_gap
```

### Documentation Gap Reporting

```
## 📚 DOCUMENTATION GAPS

**Technology**: [Name and version]
**Searched Sources**:
- ❌ Official docs (not found/outdated)
- ❌ GitHub repo (no relevant info)
- ⚠️ Found community resource: [URL]

**Limitation**: Cannot validate pattern without official source
**Risk Level**: [HIGH/MEDIUM/LOW]
**Recommendation**: Proceed with caution, verify with testing
```

### Best Effort Analysis

When documentation is unavailable:
1. Note the limitation clearly
2. Use available community resources cautiously
3. Flag patterns that cannot be validated
4. Recommend additional validation methods
5. Suggest contacting maintainers

## Output Format for Documentation Research

Structure documentation findings clearly:

```
## 📚 DOCUMENTATION RESEARCH REPORT

**Technologies Identified**: [count]
- [Technology 1]: v[X.Y.Z] (detected in: file:line)
- [Technology 2]: v[X.Y.Z] (detected in: file:line)

### [Technology 1] - [Version]

**Documentation Sources**:
- Official: [URL]
- GitHub: [URL]
- Security: [URL if applicable]

**Best Practices Found**:
✅ [Best practice with source link]
✅ [Best practice with source link]

**Anti-Patterns Identified**:
❌ [Anti-pattern found in code]
   - Location: file:line
   - Documentation: [URL]
   - Correct pattern: [What to do instead]

**Security Guidelines**:
🔒 [Security requirement from docs]
🔒 [Security requirement from docs]

**Version-Specific Notes**:
- [Feature] requires v[X.Y.Z]+
- [Pattern] deprecated in v[X.Y.Z]

### Pattern Validation Results

**✅ VALIDATED PATTERNS**:
- Pattern at file:line matches [Technology] docs ✓
- Security configuration follows guidelines ✓

**❌ PATTERN MISMATCHES**:
Pattern: [What's in code]
- Location: file:line
- Documentation says: [Correct pattern]
- Severity: [CRITICAL/HIGH/MEDIUM/LOW]
- Fix: [Specific correction needed]

**⚠️ DEPRECATED PATTERNS**:
Pattern: [Deprecated usage]
- Location: file:line
- Deprecated since: v[X.Y.Z]
- Alternative: [Modern approach]
- Migration guide: [URL]

## 💡 RECOMMENDATIONS

1. **Immediate Actions**:
   - Fix deprecated pattern at file:line
   - Update to secure configuration per [docs URL]

2. **Best Practice Adoption**:
   - Implement [pattern] as shown in [docs URL]
   - Follow [guideline] for better [benefit]

3. **Version Considerations**:
   - Consider upgrading to v[X.Y.Z] for [feature]
   - Review migration guide: [URL]

## 📊 CONFIDENCE LEVEL

Documentation Coverage: [HIGH/MEDIUM/LOW]
- [Technology 1]: ✅ Full docs available
- [Technology 2]: ⚠️ Partial docs
- [Technology 3]: ❌ No official docs found

Pattern Validation Confidence: [HIGH/MEDIUM/LOW]
- Reasoning: [Why this confidence level]
```

## Integration with docs-researcher Agent

### Workflow Integration

```
1. Receive investigation reports
2. Load Skill('documentation-research')
3. Extract technologies from reports
4. For each technology:
   a. Determine version
   b. Search for official docs
   c. Fetch relevant sections
   d. Extract guidelines
   e. Cross-reference with code patterns
5. Compile research report
6. Pass to validator for assessment
```

### Tool Usage

```
# Search for documentation
WebSearch("[technology] [version] best practices")

# Fetch documentation
WebFetch("https://official-docs-url.com/path")

# Extract from fetched content
Parse HTML/Markdown for:
- Best practices
- Anti-patterns
- Security guidelines
- Version-specific info
```

## Success Metrics

Effective documentation research achieves:
- 90%+ of technologies have documentation found
- All CRITICAL security guidelines extracted
- Deprecated patterns identified before production
- Version mismatches caught
- Clear citations for all recommendations

Remember: The goal is to ground all recommendations in authoritative sources - be a fact-checker who validates everything against official documentation rather than relying on assumptions or outdated knowledge.
