import sys
import tty
import termios

from .keys import Key


class UnixInput:

    EXTENDED = {
        "[A": Key.UP,
        "[B": Key.DOWN,
        "[C": Key.RIGHT,
        "[D": Key.LEFT,

        "[H": Key.HOME,
        "[F": Key.END,

        "[2~": Key.INSERT,
        "[3~": Key.DELETE,
        "[5~": Key.PAGE_UP,
        "[6~": Key.PAGE_DOWN,

        "OP": Key.F1,
        "OQ": Key.F2,
        "OR": Key.F3,
        "OS": Key.F4,
        "[15~": Key.F5,
        "[17~": Key.F6,
        "[18~": Key.F7,
        "[19~": Key.F8,
        "[20~": Key.F9,
        "[21~": Key.F10,
        "[23~": Key.F11,
        "[24~": Key.F12,
    }

    SPECIAL = {
        "\r": Key.ENTER,
        "\n": Key.ENTER,
        "\t": Key.TAB,
        "\x7f": Key.BACKSPACE,
        "\x08": Key.BACKSPACE,
        "\x1b": Key.ESC,
        " ": Key.SPACE,
        "\x03":Key.CTRL_C,
        "\x04": Key.CTRL_D
    }

    @staticmethod
    def read():
        old_settings = termios.tcgetattr(sys.stdin)

        try:
            tty.setraw(sys.stdin)

            key = sys.stdin.read(1)

            if key == "\x1b":
                key += sys.stdin.read(2)

                if key[1:] in UnixInput.EXTENDED:
                    key = UnixInput.EXTENDED[key[1:]]

            return UnixInput.SPECIAL.get(key, key)

        finally:
            termios.tcsetattr(
                sys.stdin,
                termios.TCSADRAIN,
                old_settings
            )