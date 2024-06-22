#!/usr/bin/python3
from Model import Realty, Room, Rect
from Persistence import load


if __name__ == '__main__':
    sites = load()

    import sys
    if len(sys.argv) == 1:
        sys.argv.append('')
    match sys.argv[1].lower().strip():
        case '' | 'tui':
            from TUI import run
        case 'gui':
            from GUI import run

    run(sites)
