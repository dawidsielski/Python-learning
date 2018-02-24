"""
Palindromic Pleasure
A palindromic number is any (real) number that is able to have its digits reversed, and it stay the same number. For example, 11 is a palindrome because if you reverse its digits, it is still 11. 92729 is another example, if you reverse the digits, it is still 92729. Here is the problem:

What is the only (double-digit, or above) Prime number that is palindromic in both base-2 (binary), and base-10 (decimal) instances?

This problem will be very tricky, as it will require the ability to find both palindromes, and prime numbers (don't forget the function we built earlier) at the same time. Don't give up here, you have come so far.
"""
import math


def is_prime(number):
    for i in range(2, int(number / 2) + 1):
        if number % i == 0:
            return False
    return True


def is_palindrome(number):
    return str(number) == str(number)[::-1]


def to_binary(number):
    return bin(number)[2:]


i = 10
while not (is_prime(i) and is_palindrome(i) and is_palindrome(to_binary(i))):
    i += 1
print(i)