import math

print("Rock paper scissors game")
print("Rock is 1 \nPaper is 2 \nScissors are 3")


while True:
    user_one_move = int(input("User one move: "))
    user_two_move = int(input("User two move: "))

    if (user_one_move - user_two_move) == 1:
        print("User one wins")
    elif (user_one_move - user_two_move) == -1:
        print("User two wins")
    elif (user_one_move - user_two_move) == 2:
        print("User two wins")
    elif (user_one_move - user_two_move) == -2:
        print("User one wins")
    else:
        break
