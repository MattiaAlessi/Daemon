import msvcrt #only windows

from .keys import Key


class Input:
    EXTENDED = {"H":Key.UP,
                        "P":Key.DOWN,
                        "K":Key.LEFT,
                        "M":Key.RIGHT
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

        #if key == 'à':
        if key in Input.PREFIX and (key != "\x00" or key == "\xe0"):
            code = msvcrt.getwch()
            return Input.EXTENDED.get(code, key + code)
            
        return Input.SPECIAL.get(key, key)
    
    
    