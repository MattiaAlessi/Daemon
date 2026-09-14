import msvcrt #only windows

from .keys import Key


class Input:
    EXTENDED = {
        "H": Key.UP,
        "P": Key.DOWN,
        "K": Key.LEFT,
        "M": Key.RIGHT,
        "G": Key.HOME,
        "O": Key.END,
        "I": Key.PAGE_UP,
        "Q": Key.PAGE_DOWN,
        "R": Key.INSERT,
        "S": Key.DELETE,
        ";": Key.F1,
        "<": Key.F2,
        "=": Key.F3,
        ">": Key.F4,
        "?": Key.F5,
        "@": Key.F6,
        "A": Key.F7,
        "B": Key.F8,
        "C": Key.F9,
        "D": Key.F10,
        "\x85": Key.F11,
        "\x86": Key.F12,
    }
    
    PREFIX = ("\x00", "\xe0")

    SPECIAL = {
        "\r": Key.ENTER,
        "\t": Key.TAB,
        "\x08": Key.BACKSPACE,
        "\x1b": Key.ESC,
        " ": Key.SPACE,
    }
 

    @staticmethod
    def read():
        key = msvcrt.getwch()

        if key in Input.PREFIX:
            code = msvcrt.getwch()
            return Input.EXTENDED.get(code, key + code)
            
        return Input.SPECIAL.get(key, key)
    
    
    