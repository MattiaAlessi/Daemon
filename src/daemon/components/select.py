from daemon.input.keys import Key


class Select:
    def __init__(self, options):
        self.options = options
        self.selected_option = 0

        
    def render(self):
        lines = []
        for i, option in enumerate(self.options):
            lines.append(f"> {option}" if i==self.selected_option else f"  {option}")
            
        return "\n".join(lines)
    
    def handle_key(self, key):
        if key == Key.DOWN and self.selected_option < len(self.options) - 1:
            self.selected_option += 1
        elif key == Key.UP and self.selected_option > 0:
            self.selected_option -= 1
        
        


if __name__ == "__main__":
    from daemon.input.keyboard import Keyboard
    from daemon.terminal.terminal import Terminal

    sel = Select(["Gino caio pino", "Pizza", "Pasta"])
    kb = Keyboard()
    t = Terminal()

    while True:
        t.clear_window()
        t.write(sel.render(), newline=True)

        key = kb.read()

        if key == Key.ESC:
            break

        sel.handle_key(key)