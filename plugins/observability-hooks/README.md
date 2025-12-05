# observability-hooks

Optional tool usage tracking, event logging, and session telemetry for Claude Code.

## Installation

```bash
/plugin install observability-hooks@hkarchokov
```

## What It Does

Tracks and logs all Claude Code activity:
- **Tool Usage**: Every tool call (Read, Write, Edit, Bash, etc.)
- **Session Events**: Session start/end, stop signals
- **Subagent Activity**: Subagent execution and metrics
- **User Prompts**: Prompt submissions and preprocessing
- **Compaction Events**: Memory compaction triggers

## Features

### Tool Tracking (PreToolUse & PostToolUse)

Logs every tool call with:
- Tool name and parameters
- Execution time
- Success/failure status
- Output summary

### Session Lifecycle

- **SessionStart**: Logs session initialization, loads git context
- **SessionEnd**: Logs session termination and cleanup
- **Stop**: Captures stop events and shutdown reason

### Subagent Monitoring

- **SubagentStop**: Tracks subagent completion, duration, token usage

### Prompt Tracking

- **UserPromptSubmit**: Logs user prompts before processing

### Memory Management

- **PreCompact**: Logs conversation compaction events

## Log Storage

All events are logged to:
```
logs/
├── session_start.json
├── session_end.json
├── stop_events.json
├── subagent_metrics.json
├── tool_usage.json
└── prompts.json
```

## Event Logging Server

Sends events to optional observability server (if configured):
- Tool usage analytics
- Performance metrics
- Error tracking

Configure server URL via environment variable:
```bash
export OBSERVABILITY_SERVER_URL=https://your-server.com/events
```

## Privacy & Security

- All logs stored locally in `logs/` directory
- No data sent externally unless `OBSERVABILITY_SERVER_URL` is configured
- Sensitive data (API keys, passwords) filtered from logs
- `.env` file access blocked by PreToolUse validation

## Disable Observability

To temporarily disable all tracking:

```bash
/plugin uninstall observability-hooks@hkarchokov
```

Logs will stop immediately, but existing log files remain.

## Use Cases

1. **Debugging**: Track exactly what tools were called and when
2. **Performance Analysis**: Measure tool execution times
3. **Usage Patterns**: Understand which agents/commands you use most
4. **Audit Trail**: Complete history of all Claude Code activity
5. **Subagent Metrics**: Optimize subagent usage based on performance data

## Technical Details

### Hooks Registered
- PreToolUse - Before every tool call
- PostToolUse - After every tool call
- SessionStart - On session initialization
- SessionEnd - On session termination
- Stop - On stop events
- SubagentStop - When subagents complete
- UserPromptSubmit - On user input
- PreCompact - Before memory compaction

### Dependencies
- `python-dotenv` (environment variable management)
- Standard library (json, pathlib, subprocess)

## License

MIT
