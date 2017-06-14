"""line 1270"""
import math
class Circle(object):

    def __init__(self, r):
        self.radius = r

    def area(self):
        return math.pi * self.radius ** 2


cir = Circle(2)
print(cir.area())
