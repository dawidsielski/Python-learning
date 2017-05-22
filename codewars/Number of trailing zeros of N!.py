"""
Write a program that will calculate the number of trailing zeros in a factorial of a given number.

http://mathworld.wolfram.com/Factorial.html

N! = 1 * 2 * 3 * 4 ... N

zeros(12) = 2 # 1 * 2 * 3 .. 12 = 479001600 
that has 2 trailing zeros 4790016(00)
Be careful 1000! has length of 2568 digital numbers.
"""

def zeros(n):
    i = 5
    zeros = 0
    while n >= i:
        zeros += n // i
        i *= 5
        print(i, n, zeros)
    return zeros


print(zeros(12) == 2)
print(zeros(13) == 2)
print(zeros(20) == 4)
print(zeros(25) == 6)
print(zeros(30) == 7)
print(zeros(1000) == 249)   