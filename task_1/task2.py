import math

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    def coordinates(self):
        print(f"координаты точки:({self.x},{self.y})")
    def other_point(self,x1,y1):
        q = math.sqrt((x1 - self.x)**2 + (y1 - self.y)**2)
        print(q)
    def sqr_coordinates(self,x2,y2):
        w = math.fabs(self.x - x2) * math.fabs(self.y - y2)
        print(w)
point = Point(2,5)
point.coordinates()
point.other_point(7,9)
point.sqr_coordinates(10,10)
