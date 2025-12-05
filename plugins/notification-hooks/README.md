# notification-hooks

Simple audio notification when Claude needs your attention.

## Installation

```bash
/plugin install notification-hooks@hkarchokov
```

## What It Does

Plays a simple sound (ding) when Claude Code:
- Requests user input
- Needs permission for an operation
- Waits for your response

## Platform Support

- **macOS**: Plays system sound (Ping.aiff) at 40% volume
- **Linux**: Plays freedesktop notification sound via PulseAudio, falls back to ALSA

## Configuration

### Disable Sounds (Optional)

If you want to disable the notification sound:

```bash
export CLAUDE_ENABLE_SOUNDS=false
```

Then restart Claude Code.

## Uninstall

```bash
/plugin uninstall notification-hooks@hkarchokov
```

Notifications will stop immediately.

## Technical Details

- **Hook Type**: Notification
- **Timeout**: 2 seconds

### macOS
- **Command**: `afplay -v 0.4 /System/Library/Sounds/Ping.aiff`

### Linux
- **Command**: `paplay` (PulseAudio) with fallback to `aplay` (ALSA)
- **Sound**: `/usr/share/sounds/freedesktop/stereo/complete.oga`

## License

MIT
