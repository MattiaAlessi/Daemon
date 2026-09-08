
class Color:    
    BLACK = "\033[0;30m"
    RED = "\033[0;31m"
    GREEN = "\033[0;32m"
    YELLOW = "\033[0;33m"
    BLUE = "\033[0;34m"
    MAGENTA = "\033[0;35m"
    CYAN = "\033[0;36m"
    WHITE = "\033[0;37m"
    DARK_GRAY = "\033[1;30m"
    LIGHT_RED = "\033[1;31m"
    LIGHT_GREEN = "\033[1;32m"
    LIGHT_YELLOW = "\033[1;33m"
    LIGHT_BLUE = "\033[1;34m"
    LIGHT_MAGENTA = "\033[1;35m"
    LIGHT_CYAN = "\033[1;36m"
    LIGHT_WHITE = "\033[1;37m"
    BOLD = "\033[1m"
    FAINT = "\033[2m"
    ITALIC = "\033[3m"
    UNDERLINE = "\033[4m"
    BLINK = "\033[5m"
    NEGATIVE = "\033[7m"
    CROSSED = "\033[9m"
    END = "\033[0m"
    
    

    
    @staticmethod
    def apply(testo, color, *styles):
        colorful_text = color
        for style in styles:
            colorful_text += style
        colorful_text += testo + Color.END
        return colorful_text
    

    
    @staticmethod
    def _apply_color(testo, color, *styles, printable=True):
        if printable:
            print(Color.apply(testo, color, *styles))
            return True
        return Color.apply(testo, color, *styles)
        





def make_color_method(color):
    def color_method(testo, *styles, printable=True):
        return Color._apply_color(
            testo,
            color,
            *styles,
            printable=printable
        )

    return color_method
    
for name, code in list(vars(Color).items()):
    if isinstance(code, str) and (code.startswith("\033[0;") or code.startswith("\033[1;")) :
        method_name = name.lower()
        setattr(Color, method_name, make_color_method(code))