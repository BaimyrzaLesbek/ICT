class Shape:
    def __init__(self, area = 0):
        self.area = area
    
    def returnArea(self):
        return self.area

class Rect(Shape):
    def __init__(self, len = 0, wid = 0):
        super().__init__()
        self.len = len
        self.wid = wid

    def returnArea(self):
        return self.len * self.wid