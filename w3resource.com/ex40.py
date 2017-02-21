"""
Write a Python program to compute the distance between the points (x1, y1) and (x2, y2).
"""

import math

def distance(a_x, a_y, b_x, b_y):
    """Evaluate distance between two points."""
    return math.sqrt((b_y - a_y)**2 + (b_x - a_x)**2)

print(distance(0, 0, 3, 4))
print(distance.__doc__ + "\n")