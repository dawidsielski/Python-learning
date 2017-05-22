"""
Write a program that will calculate the number of trailing zeros in a factorial of a given number.

http://mathworld.wolfram.com/Factorial.html

N! = 1 * 2 * 3 * 4 ... N

zeros(12) = 2 # 1 * 2 * 3 .. 12 = 479001600 
that has 2 trailing zeros 4790016(00)
Be careful 1000! has length of 2568 digital numbers.
"""
def zeros(n):
    result = 1
    for number in range(1,n + 1):
        result *= number
    count = 0
    for element in str(result)[::-1]:
        if element == "0":
            count += 1
        else:
            break
    return count


print(zeros(12) == 2)