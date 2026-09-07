import sys


class Cursor:
    def __init__(self):
        pass
    
    
    def hide(self):
        """Hide the cursor thanks to Esc[?25l"""
        sys.stdout.write("\x1b[?25l")
        sys.stdout.flush()
        
    def show(self):
        """Show the cursor thanks to Esc[?25h"""
        sys.stdout.write("\x1b[?25h")
        sys.stdout.flush()   

    def move(self, row, column):
        """Move to row x, column y"""
        sys.stdout.write(f"\x1b[{row};{column}H")
        sys.stdout.flush()   
        
    def move_up(self, n=1):
        """move the cursor up N lines"""
        sys.stdout.write(f"\x1b[{n}A")
        sys.stdout.flush()   
        
    def move_down(self, n=1):
        """move the cursor down N lines"""
        sys.stdout.write(f"\x1b[{n}B")
        sys.stdout.flush()   
            
    def move_left(self, n=1):
        """move the cursor left N lines"""
        sys.stdout.write(f"\x1b[{n}D")
        sys.stdout.flush()   
        
    def move_right(self, n=1):
        """move the cursor right N lines"""
        sys.stdout.write(f"\x1b[{n}C")
        sys.stdout.flush()   
    
    def save(self):
        """save cursor"""
        sys.stdout.write("\x1b[s")
        sys.stdout.flush()   
        
    def restore(self):
        """restore cursor"""
        sys.stdout.write("\x1b[u")
        sys.stdout.flush()   
    