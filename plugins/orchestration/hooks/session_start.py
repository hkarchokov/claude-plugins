#!/usr/bin/env -S uv run --script
# /// script
# requires-python = ">=3.11"
# dependencies = []
# ///
"""SessionStart Hook - Initializes orchestration context"""

import sys
import json

# Read stdin (hook receives session data)
try:
    input_data = json.loads(sys.stdin.read())
except (json.JSONDecodeError, ValueError) as e:
    input_data = {}

# Build context message with instructions
context = """<ORCHESTRATION>
🚀 MULTI-AGENT ORCHESTRATION SYSTEM AVAILABLE

This environment includes the orchestration plugin for codebase investigation and requirement clarification.

SLASH COMMANDS (User-Triggered):

Users can trigger these workflows by typing:
- /orchestration:investigate [topic] - Multi-agent code investigation
- /orchestration:clarify [topic] - Requirement extraction
- /orchestration:lookup [topic] - Quick codebase lookup

INVESTIGATION PATTERN (Scout → Investigate → Validate):

When /orchestration:investigate is triggered:
1. Scout (haiku) - Quick structure scan to understand the codebase
2. Investigate (sonnet, parallel) - Multiple focused Explore agents on different angles
3. Validate (sonnet, optional) - Adversarial review of findings
4. Synthesize - Combine into structured report

Deploy Explore agents with Task(subagent_type="Explore", model="haiku/sonnet", ...).
Phase 2 agents must all deploy in a SINGLE message for parallel execution.

CLARIFICATION:

For ambiguous requests, use:
- Task(subagent_type='orchestration:clarifier', ...) for requirement extraction

Load Skill('orchestration:investigation-pattern') for methodology details.
</ORCHESTRATION>"""

# Output JSON format for context injection
output = {
    "hookSpecificOutput": {
        "hookEventName": "SessionStart",
        "additionalContext": context
    }
}

print(json.dumps(output))
sys.exit(0)
