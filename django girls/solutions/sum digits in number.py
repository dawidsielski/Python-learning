"""
Your task is to sum digits in a given number
FOr example:
sum_digits(1234) should return 10
sum_digits(8000) should return 8
Consicer only postive numbers
"""


def sum_digits(number):
    number_str = str(number)
    result = 0
    for digit in number_str:
        result += int(digit)
    return result


print(sum_digits(1234) == 10)
print(sum_digits(8000) == 8)
print(sum_digits(53475) == 24)
print(sum_digits(98436723) == 42)