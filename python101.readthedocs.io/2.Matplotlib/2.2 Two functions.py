#! /usr/bin/env python
# -*- coding: utf-8 -*-

#! /usr/bin/env python
# -*- coding: utf-8 -*-

import pylab
import numpy as np

a = float(input("Enter a argument: "))
b = float(input("Enter b argument: "))

x1 = np.arange(-10.,0.1,0.5)
x2 = np.arange(0.,10.1,0.5)

f1 , f2 = [], []

for i in x1:
    f1.append(i/(-3))

for i in x2:
    f2.append((i**2)/3)

pylab.plot(x1,f1)
pylab.plot(x2,f2)
pylab.grid(True)
pylab.show()