from math import sqrt

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def distance_from(self, p2):
        val = sqrt(pow((p2.x - self.x), 2) + pow((p2.y - self.y), 2))
        return val

class Circle:
    def __init__(self, p, radius):
        self.center = p
        self.radius = radius

    def is_inside(self, p):
        val = pow((p.x - self.center.x), 2) + pow((p.y - self.center.y), 2)
        if val < pow(self.radius, 2):
            return True
        else:
            return False
