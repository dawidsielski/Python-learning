import math

def get_number(text = "Enter your number: "):
    return int(input(text))

def if_prime(number):
    for i in range(2,int(math.sqrt(number)+1)):
        if number % i == 0:
            return False
    return True

print(if_prime(get_number()))


#test
for i in range(1,100):
    print(str(i) + " " + str(if_prime(i)))
