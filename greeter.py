# print some sort of welcome screen
# give option to start new study session
# give option to set new goal

import sys
import shutil

"""
this function gets a key press from the user, and not showing it on the screen
other then input.
"""
def getKey():
    if sys.platform == "win32":
        import msvcrt
        return msvcrt.getch().decode()  # Windows single key press
    else:
        import tty
        import termios
        fd = sys.stdin.fileno()
        old_settings = termios.tcgetattr(fd)
        try:
            tty.setraw(fd)
            ch = sys.stdin.read(1)  # Read a single key
        finally:
            termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)  # Restore settings
        return ch


def clear():
    # Get terminal size
    size = shutil.get_terminal_size()

    # Print enough newlines to clear the screen
    sys.stderr.write("\n" * size.lines)

    # Move cursor to the top-left corner
    sys.stderr.write("\033[0;0H")

    sys.stderr.flush()


def greeter():
    normalGreetScreen = """
\t┌──────────────────────────────────────────────────────────────────┐
\t│   ___ _____ _   _ _____   __  _____ ___    _   ___ _  _____ ___  │
\t│  / __|_   _| | | |   \\ \\ / / |_   _| _ \\  /_\\ / __| |/ / __| _ \\ │
\t│  \\__ \\ | | | |_| | |) \\ V /    | | |   / / _ \\ (__| ' <| _||   / │
\t│  |___/ |_|  \\___/|___/ |_|     |_| |_|_\\/_/ \\_\\___|_|\\_\\___|_|_\\ │
\t│                                                                  │
\t└──────────────────────────────────────────────────────────────────┘

\t \tTrack Your Studies, Track Your Success! 📖⏳
"""

    smallerGreetScreen = """
┌────────────────────────────────────────────┐
│ ____ _____ _   _ ______   __               │
│/ ___|_   _| | | |  _ \\ \\ / /               │
│\\___ \\ | | | | | | | | \\ V /                │
│ ___) || | | |_| | |_| || |                 │
│|____/ |_|_ \\___/|____/_|_|_  _______ ____  │
│|_   _|  _ \\    / \\  / ___| |/ / ____|  _ \\ │
│  | | | |_) |  / _ \\| |   | ' /|  _| | |_) |│
│  | | |  _ <  / ___ \\ |___| . \\| |___|  _ < │
│  |_| |_| \\_\\/_/   \\_\\____|_|\\_\\_____|_| \\_\\│
└────────────────────────────────────────────┘
    Your Studies, Track Your Success! 📖⏳
"""


    # gets the width of the ascii art
    ascii_width = max(len(line) for line in normalGreetScreen.splitlines())
    # gets the width of the terminal
    terminal_width = shutil.get_terminal_size().columns

    if terminal_width < ascii_width:
        print(smallerGreetScreen)
    else:
        print(normalGreetScreen)

    print("[c] continue session ")
    print("[s] start new session")
    print("[e] exit")

    print("choose an option... ", end="", flush=True)
    key = getKey()
    print("\n")

    if key == "c":
        print("Continuing study session... 📖\n")
        return 1
    elif key == "s":
        print("Starting a new session... 📖\n")
        return 2
    elif key == "e":
        print("Exiting... 👋") 
        return 3
    else:
        print("Invalid choice! ❌")
        return -1
