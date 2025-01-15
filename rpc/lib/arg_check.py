import sys
from .commands import supported_commands
from .err import UnknownCommand, InvalidArguments

def check_args():
    if len(sys.argv) < 2:
        raise ValueError("Usage: python -m rpc <command> [...args]")

    command = sys.argv[1]
    args = sys.argv[2:]

    if command in supported_commands:
        return command, args
    else:
        raise UnknownCommand(f"Unknown command: {command}")
