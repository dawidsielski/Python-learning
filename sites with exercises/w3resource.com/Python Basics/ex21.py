import random
user_number = random.randint(0,1000)

def odd_or_even(number):
    if number % 2 == 0:
        return "even"
    else:
        return "odd"
print(user_number)
print(odd_or_even(user_number))
