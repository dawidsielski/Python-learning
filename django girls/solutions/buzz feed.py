"""
Your task is to prepare program which will take number as an argument. 
Print "Buzz" if number is divisible by 3. 
If the number is divisible by 5 print "Feed"
If number is divisible by 3 and 5 print "Buzz Feed"
Else print number itself
"""

def buzz_feed(number):
    # Insert your code below
    if number % 3 == 0 and number % 5 == 0:
        return "Buzz Feed"
    elif number % 3 == 0:
        return "Buzz"
    elif number % 5 == 0:
        return "Feed"
    else:
        return number


# test code
print(buzz_feed(1) == 1)
print(buzz_feed(3) == "Buzz")
print(buzz_feed(15) == "Buzz Feed")
print(buzz_feed(14) == 14)
print(buzz_feed(30) == "Buzz Feed")