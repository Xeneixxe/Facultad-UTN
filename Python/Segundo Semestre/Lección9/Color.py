class Color:
    def __init__(self, color):
        self.color = color
        
        
    @property
    def color(self, color):
        return self._color
    
    @color.setter
    def color(self, color):
        self._color = color
        
        
    def __str__(self) -> str:
        return f'Color [color: {self._color}]'