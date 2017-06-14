def print_board():
    for i in range(3):
        for j in range(3):
            print("---", end = " ")
        print()
        for j in range(6):
            print("|", end=" ")
        print()
    for j in range(3):
        print("---", end = " ")
    print()

print_board()
