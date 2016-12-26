winner_is_2 =   [[2, 2, 0],
                [2, 1, 0],
                [2, 1, 1]]

winner_is_1 =   [[1, 2, 0],
                [2, 1, 0],
                [2, 1, 1]]

winner_is_also_1 =  [[0, 1, 0],
                    [2, 1, 0],
                    [2, 1, 1]]

no_winner = [[1, 2, 0],
            [2, 1, 0],
            [2, 1, 2]]

also_no_winner =    [[1, 2, 0],
                    [2, 1, 0],
                    [2, 1, 0]]


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

print_winner(also_no_winner)
