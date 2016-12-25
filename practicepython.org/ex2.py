user_number = -1
while user_number != 0:
    user_number = int(input("Enter your number:"))
    if user_number%2 == 0:
        print("Your number is divisible by two.")
    else:
        print("Your number is not divisible by two")
