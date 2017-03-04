"""line 1297"""

class Rectangle(object):

    def __init__(self, w, l):
        self.width = w
        self. length = l
    
    def area(self):
        return self.width * self.length

rec = Rectangle(2,5)
print(rec.area())