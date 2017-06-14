#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Guess number having three chances"""

import random

number = random.randint(1, 10)
# print("Random number: ", number)
for i in range(3):
    print("Chance number:", i + 1)
    answer = input("What number from 1 to 10  do i have in my mind? ")
    if number == int(answer):
        print("Congratulations! You guessed the right number!")
        break
    elif i == 2:
        print("My number was:", number)
    else:
        print("Try one more time.")