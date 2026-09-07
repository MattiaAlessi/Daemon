import os #import necessary to retrieve terminal dimensions
import sys #necessary to use the ansi escape code for terminal
import time


class Terminal:
    """Class Terminal"""
    def __init__(self):
        pass
    
    
    def write(self, text="", newline=False, flush=True):
        print(text, end="\n" if newline else "", flush=flush)
    
    def clear_window(self):
        """This class use the ANSI code sequence Esc[2J Esc[H to clear the entire screen"""
        #Esc[2J clear and cursor to home position
        #Esc[H send cursor to cursor home position
        #Esc = x1b in byte
        sys.stdout.write('\x1b[2J\x1b[H') 
        sys.stdout.flush()
        
    def clear_current_line(self):
        """This class use the ANSI code sequence Esc[2K \\r to clear the curent screen"""
        # ESC[2K clears the entire line; '\r' returns cursor to column 0
        sys.stdout.write('\x1b[2K\r')
        sys.stdout.flush()
    
    @property
    def terminal_width(self):
        self.size = os.get_terminal_size() #recall in case the terminal dimensions have been changed
        return self.size[0]
    
    @property
    def terminal_height(self):
        self.size = os.get_terminal_size() #recall in case the terminal dimensions have been changed
        return self.size[1]
    
    

#use @property @funct.setter @func.deleter

#example of stackoverflow: for update bar  
"""for i in range(5):
    sys.stdout.write(f'Processing {i}')
    sys.stdout.write('\x1b[K')  # clear from cursor to end of line
    sys.stdout.flush()
    time.sleep(0.5)
    sys.stdout.write('\r')     # return to start for next update"""