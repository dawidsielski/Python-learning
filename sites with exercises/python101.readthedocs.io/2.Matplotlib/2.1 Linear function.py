#! /usr/bin/env python
# -*- coding: utf-8 -*-

import pylab

a = float(input("Enter a value: "))
b = float(input("Enter b value: "))
x = range(-10, 11) 

y = []
for i in x:
    y.append(a * i + b)

pylab.plot(x, y)
pylab.title('Plot f(x) = a*x - b')
pylab.grid(True)
pylab.show()