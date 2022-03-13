class Shape:
    def __init__(self, area = 0):
        self.area = area
    
    def returnArea(self):
        return self.area

class Square(Shape):
    def __init__(self, len = 0):
        super().__init__()
        self.len = len
    
    def returnArea(self):
        return self.len * self.len
