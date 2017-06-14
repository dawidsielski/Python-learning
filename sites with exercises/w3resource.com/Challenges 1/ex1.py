n = int(input("Enter your number:"))

if n % 2 == 1:
    print("Number is not a power of 2")
else:
    while n % 2 == 0:
        n = n / 2
        if n == 1:
            print("Number is a power of two.")
            break
        if n % 2 == 1:
            print("Number is not a power of two.")
            break
