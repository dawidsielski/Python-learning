#! /usr/bin/env python
# -*- coding: utf-8 -*-

current_year = int(input("Enter current year: "))
python_year = 1989

age_of_python = current_year - python_year

your_name = input("Enter your name: ")
your_age = input("Enter your age: ")

print("Hello {0} :)".format(your_name))
print("My name is Python and i am {0} years old.".format(age_of_python))

if int(your_age) < age_of_python:
    print("You are younger than python.")
else:
    print("You are not younger than python.")