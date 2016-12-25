import random

random_number = random.randint(1,9)

while True:
    your_number = int(input("Enter Your number:"))
    if your_number == random_number:
        print("You got it!")
        break
    elif your_number > random_number:
        print("Try smaller one.")
    else:
        print("Try bigger one.")
