#!/ust/bin/env python
# -*- coding: utf-8 -*-

import random

number = random.randint(1, 10)
print("Random number: ", number)

answer = input("What number from 1 to 10  do i have in my mind?")

if number == int(answer):
    print("Congratulations! You guessed the right number!")
else:
    print("Try one more time.")