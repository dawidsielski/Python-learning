#! /usr/bin/env python
# -*- coding: utf-8 -*-

def fibonacc(n):
    """Returns list of fibonacci numbers"""
    fibbonaci = [1,1]
    for i in range(2,n):
        fibbonaci.append(fibbonaci[i-1] + fibbonaci[i - 2])
    return fibbonaci


result = fibonacciUpToSpecificIndexNumber(10000)
print(result)
print(len(str(result[-1])))