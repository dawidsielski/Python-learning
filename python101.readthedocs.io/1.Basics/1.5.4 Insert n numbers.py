#! /usr/bin/env python
# -*- coding: utf-8 -*-

# ~/python/04_1_listy.py

input_tuple = input("Podaj liczby oddzielone przecinkami: ")
input_list = input_tuple.split(",")

print(input_tuple)
print(input_list)

for i in range(len(input_tuple)):
    print(input_tuple[i], end = " ")

print("\n")

for index, value in enumerate(input_list):
    print("{0} : {1}".format(index, value))


print("Reversed list:")
for element in reversed(input_list):
    print(element, end = " ")

print("Sorted list:")
for element in sorted(input_list):
    print(element, end = " ") 