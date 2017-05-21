"""
In this little assignment you are given a string of space separated numbers, and have to return the highest and lowest number.
"""

def high_and_low(numbers):
    numbers = sorted([int(x) for x in numbers.split()])
    return str(numbers[-1]) + " " + str(numbers[0])


print(high_and_low("4 5 29 54 4 0 -214 542 -64 1 -3 6 -6"))