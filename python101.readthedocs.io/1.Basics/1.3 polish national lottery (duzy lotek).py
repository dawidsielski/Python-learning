#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Polish National Lottery calles "Duży lotek."""

import random

try:
    how_many_numbers = int(input("Enter how many numbers do you want to enter: "))
    max_number = int(input("Enter maximum number: "))

    if how_many_numbers > max_number:
        print("You cannot have more numbers in given interval.")
        exit()
except:
    print("Wrong input.")
    exit()

print("Enter {0} numbers from 1 to {1}".format(how_many_numbers, max_number))

random_numbers = []
while len(random_numbers) < how_many_numbers:
    number = random.randint(1, max_number)
    if random_numbers.count(number) == 0:
        random_numbers.append(number)
print("Random numbers ", random_numbers)

your_numbers = []

while len(your_numbers) < how_many_numbers:
    user_number = int(input("Enter your {0} number:".format(len(your_numbers) + 1)))
    if user_number in your_numbers:
        print("Please enter different number:")
    elif user_number > max_number:
        print("Your number is too big!")
    elif user_number < 1:
        print("Ypur number is too small!")
    else:
        your_numbers.append(user_number)


random_numbers_set = set(random_numbers)
your_numbers_set = set(your_numbers)

guessed_numbers = random_numbers_set & your_numbers_set

if len(guessed_numbers) == 0:
    print("Your numbers are all different.")
else:
    print("Congratulations! Your guessed numbera:", list(guessed_numbers))