user_number = int(input("Enter your number: "))

while user_number != 1:
    print(user_number)
    if user_number % 2 == 0:
        user_number /= 2
    else:
        user_number = 3*user_number + 1