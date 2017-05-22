"""
###Sudoku Background Sudoku is a game played on a 9x9 grid. The goal of the game is to fill all cells of the grid with digits from 1 to 9, so that each column, each row, and each of the nine 3x3 sub-grids (also known as blocks) contain all of the digits from 1 to 9. 
(More info at: http://en.wikipedia.org/wiki/Sudoku)

###Sudoku Solution Validator Write a function validSolution that accepts a 2D array representing a Sudoku board, and returns true if it is a valid solution, or false otherwise. The cells of the sudoku board may also contain 0's, which will represent empty cells. Boards containing one or more zeroes are considered to be invalid solutions.
"""

def validSolution(board):
    for row_3 in range(3):
        a, b, c = 0, 0, 0
        for row in range(3):
             check = board[3 * row_3 + row]
             a += sum(check[0:3])
             b += sum(check[3:6])
             c += sum(check[6:9])
             if 0 in check:
                 return False
        if (a or b or c) != 45:
            return False
        for element in board:
            if sum(element) != 45:
                return False
        row = board[0]
    for r in board[1:]:
        row = [sum(x) for x in zip(row, r)]
    if not 45 in row:
        return False
    return True


print(validSolution([[5, 3, 4, 6, 7, 8, 9, 1, 2], 
                     [6, 7, 2, 1, 9, 5, 3, 4, 8],
                     [1, 9, 8, 3, 4, 2, 5, 6, 7],
                     [8, 5, 9, 7, 6, 1, 4, 2, 3],
                     [4, 2, 6, 8, 5, 3, 7, 9, 1],
                     [7, 1, 3, 9, 2, 4, 8, 5, 6],
                     [9, 6, 1, 5, 3, 7, 2, 8, 4],
                     [2, 8, 7, 4, 1, 9, 6, 3, 5],
                     [3, 4, 5, 2, 8, 6, 1, 7, 9]]))

print(validSolution([[5, 3, 4, 6, 7, 8, 9, 1, 2], 
                     [6, 7, 2, 1, 9, 0, 3, 4, 9],
                     [1, 0, 0, 3, 4, 2, 5, 6, 0],
                     [8, 5, 9, 7, 6, 1, 0, 2, 0],
                     [4, 2, 6, 8, 5, 3, 7, 9, 1],
                     [7, 1, 3, 9, 2, 4, 8, 5, 6],
                     [9, 0, 1, 5, 3, 7, 2, 1, 4],
                     [2, 8, 7, 4, 1, 9, 6, 3, 5],
                     [3, 0, 0, 4, 8, 1, 1, 7, 9]]))