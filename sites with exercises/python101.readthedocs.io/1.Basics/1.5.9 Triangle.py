#! /usr/bin/env python
# -*- coding: utf-8 -*-

import math

def checkIfPossible(a,b,c):
    if a + b > c and a + c > b and b + c > a:
        return True
    return False

def checkIfRightTriangle(a,b,c):
    if a**2 + b**2 == c**2 or b**2 + c**2 == a**2 or c**2 + a**2 == b**2:
        return True
    return False

def area(a,b,c):
    p = circumference(a, b, c) * 0.5
    area = math.sqrt(p * (p - a) * (p - b) * (p - c))
    return area

def circumference(a,b,c):
    return a + b + c


triangle = []

while len(triangle) < 3:
    side = int(input("Enter {0} side: ".format(len(triangle) + 1)))
    if side > 0:
        triangle.append(side)
    else:
        print("Side must have positive value.")

print(checkIfPossible(*triangle))

if checkIfPossible(*triangle):
    print("Your triangle is possible to make!")
    if checkIfRightTriangle(*triangle):
        print("Your triangle is also the right one.")
    print("THe circumference of your triangle is {0} and the area is {1}".format(circumference(*triangle), area(*triangle)))
else:
    print("Your triangle is not possible to make!")