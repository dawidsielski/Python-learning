"""
Get the digits sum of nth number from the Look-and-Say sequence(1-based).

1, 11, 21, 1211, 111221, 312211, 13112221, 1113213211, ...

Input/Output

[input] integer n

nth number in the sequence to get where 1 <= n <= 55 and n=1 is "1".

[output] an integer

The sum of digits in nth number from the Look-and-Say sequence.

Example

For n = 2, the output shoule be 2.

"11" --> 1 + 1 --> 2

For n = 3, the output shoule be 3.

"21" --> 2 + 1 --> 3

For n = 4, the output shoule be 5.

"1211" --> 1 + 2 + 1 + 1 --> 5
"""

def look_and_say_and_sum(n):
    pass



print(look_and_say_and_sum(1) == 1)
print(look_and_say_and_sum(2) == 2)
print(look_and_say_and_sum(3) == 3)
print(look_and_say_and_sum(4) == 5)
print(look_and_say_and_sum(5) == 8)
