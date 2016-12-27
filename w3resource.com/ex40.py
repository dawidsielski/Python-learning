import math

def distance(a_x, a_y, b_x, b_y):
    return math.sqrt((b_y - a_y)**2 + (b_x - a_x)**2)

print(distance(0,0,3,4))
