#! /usr/bin/env python
# -*- coding: utf-8 -*-

import pylab
import numpy as np


a = int(input("Enter a coefficient: "))
b = int(input("Enter b coefficient: "))
c = int(input("Enter c coefficient: "))



x_values = np.arange(-10,10,0.1)
y_values = []
for element in x_values:
    y = a * element**2 + b * element  + c
    y_values.append(y)

pylab.plot(x_values,y_values)
pylab.grid(True)
pylab.show()