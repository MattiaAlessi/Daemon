from daemon.terminal.input import Input

class Keyboard:
    def __init__(self):
        self.input = Input()

    def read(self):
        return self.input.read()