"""Entry point for Sphero RVR MCP Server."""

import asyncio
import signal
import sys

from .server import get_server, _rvr_manager, _sensor_manager


async def cleanup():
    """Clean up on shutdown."""
    global _rvr_manager, _sensor_manager

    if _sensor_manager is not None:
        try:
            await _sensor_manager.stop_streaming()
        except Exception:
            pass

    if _rvr_manager is not None:
        try:
            await _rvr_manager.disconnect()
        except Exception:
            pass


def handle_signal(sig, frame):
    """Handle shutdown signals."""
    print("\nShutting down Sphero RVR MCP server...", file=sys.stderr)
    loop = asyncio.get_event_loop()
    loop.run_until_complete(cleanup())
    sys.exit(0)


def main():
    """Run the MCP server."""
    # Set up signal handlers
    signal.signal(signal.SIGINT, handle_signal)
    signal.signal(signal.SIGTERM, handle_signal)

    # Get and run the server
    server = get_server()
    server.run()


if __name__ == "__main__":
    main()
