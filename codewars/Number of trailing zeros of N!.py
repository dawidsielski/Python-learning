"""
Write a program that will calculate the number of trailing zeros in a factorial of a given number.

http://mathworld.wolfram.com/Factorial.html

N! = 1 * 2 * 3 * 4 ... N

zeros(12) = 2 # 1 * 2 * 3 .. 12 = 479001600 
that has 2 trailing zeros 4790016(00)
Be careful 1000! has length of 2568 digital numbers.
"""


def Trailing_Zeroes(x):
    fives = 0
    for number in range(2, x+1):          
        while number > 0:
            if number % 5 == 0:
                fives += 1
                number = number/5
            else:
                break
    return fives


def zeros(n):
    count_2, count_5 = 0, 0
    for element in range(1, n + 1):
        # if element % 2 == 0:
        #     number = element
        #     while number % 2 == 0 and number != 0:
        #         number = number / 2
        #         count_2 += 1
        if element % 5 == 0:
            number = element
            while number % 5 == 0 and number != 0:
                number = number / 5
                count_5 += 1
    return min(count_2,count_5)


print(zeros(12) == 2)
print(zeros(13) == 2)
print(zeros(20) == 4)
print(zeros(25) == 6)
print(zeros(30) == 7)
print(zeros(1000) == 249)