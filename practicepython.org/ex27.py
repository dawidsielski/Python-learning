def print_board(board):
    for i in range(3):
        for j in range(3):
            print("---", end = " ")
        print()
        for j in range(3):
            print("|%d|" %(board[i][j]), end=" ")
        print()
    for j in range(3):
        print("---", end = " ")
    print()

def shoot(row, col, player):
        game[row][col] = player

def if_place_to_shoot(board):
    for i in range(3):
        for j in range(3):
            if board[i][j] == 0:
                return True
    return False


def check_board(board):
    for i in range(3):
        check_vertical = board[i]
        if ((check_vertical[0] == check_vertical[1]) and check_vertical[0] == check_vertical[2]):
            return check_vertical[0] #because he is a winner
        if ((board[0][i] == board[1][i]) and board[0][i] == board[2][i]): #check columns
            return board[0][i]
    if board[0][0] == board[1][1] and board[0][0] == board[2][2]:
        return board[0][0]
    if board[0][2] == board[1][1] and board[0][0] == board[2][0]:
        return board[0][2]
    return 0

def print_winner(board):
    winner = check_board(board)
    if winner == 0:
        print("There are no winners!")
    elif winner == 1:
        print("Player one is the winner. Congratulations!")
    elif winner == 2:
        print("Player two is the winner. Congratulations!")
    else:
        print("Something went wrong :\(")


game = [[0,0,0],
        [0,0,0],
        [0,0,0]]

player = 0
while if_place_to_shoot(game):
    row, col = int(input("Enter row coordinate: ")), int(input("Enter col coordinate: "))
    shoot(row - 1, col - 1, player % 2 + 1)
    player += 1
    print_board(game)
print_winner(game)
