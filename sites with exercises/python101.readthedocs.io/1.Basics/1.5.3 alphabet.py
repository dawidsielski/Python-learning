#! /usr/bin/env python
# -*- coding: utf-8 -*-
"""Print alphabet"""

def printAlphabet(lowercase = False):
    if lowercase:
        shift = 32
    else:
        shift = 0
    for i in range(65,91,1):
        letter = chr(i + shift)
        print(letter, end = ", ")
    print("\n")

printAlphabet()
printAlphabet(True)