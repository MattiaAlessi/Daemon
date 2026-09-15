

class Text:
    def __init__(self, text):
        self._text = text
        
    def render(self):
        return self._text
        
        
    def set_text(self, new_text):
        if new_text:
            self._text = new_text
        else:
            raise ValueError("new_text is empty")
            