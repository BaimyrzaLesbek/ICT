import math
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def showCoord(self):
        return (self.x, self.y)
    
    def movePoint(self, dx, dy):
        self.x += dx
        self.y += dy
    
    def dist(self, x1 , y1):
        return math.sqrt( (x1-self.x) * (x1-self.x) + (y1 - self.y) * (y1 - self.y) )