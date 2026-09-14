import os

class Keyboard:
    def __init__(self):
        if os.name == 'nt': 
            from .input import Input
            self.input = Input()
        else:
            from .unix import UnixInput
            self.input = UnixInput()

    def read(self):
        return self.input.read() 
    