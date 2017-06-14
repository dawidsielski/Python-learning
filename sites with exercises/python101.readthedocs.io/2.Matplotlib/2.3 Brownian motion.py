#! /usr/bin/env python
# -*- coding: utf-8 -*-

import matplotlib.pyplot as plt
import numpy as np
import random

r = 1
n = 5 #int(input("How many moves do you want: "))
x = y = 0
pos_x , pos_y = [0], [0]

for i in range(0,n):
    rad = float(random.randint(0,360) * np.pi / 180)
    x = x + r * np.cos(rad)
    y = y + r * np.sin(rad)
    pos_x.append(x)
    pos_y.append(y)


translation = np.sqrt(x**2 + y**2)
translation_vector_x = [0, pos_x[-1]]
translation_vector_y = [0, pos_y[-1]]

plt.plot(pos_x, pos_y, "ro:", color = "green", linewidth = "3", alpha = 0.5)
plt.plot(translation_vector_x, translation_vector_y, "r", color = "blue", linewidth = "3", alpha = 0.5) # displacement
plt.legend(["Values of x, y\nDisplacement: " + str(translation)], loc="upper left")
plt.xlabel("Pos_x")
plt.ylabel("Pos_y")
plt.title("Brownian motion")
plt.grid(True)
fig = plt.gcf()
fig.canvas.set_window_title('Brownian motion generator')
plt.show()