import numpy as np
sudoku = [[0, 0, 0, 0, 0, 0, 0, 0, 0],
          [0, 3, 0, 0, 0, 0, 1, 6, 0],
          [0, 6, 7, 0, 3, 5, 0, 0, 4],
          [6, 0, 8, 1, 2, 0, 9, 0, 0],
          [0, 9, 0, 0, 8, 0, 0, 3, 0],
          [0, 0, 2, 0, 7, 9, 8, 0, 6],
          [8, 0, 0, 6, 9, 0, 3, 5, 0],
          [0, 2, 6, 0, 0, 0, 0, 9, 0],
          [0, 0, 0, 0, 0, 0, 0, 0, 0]]


# Function to detect possible answer to the empty sudoku tile (y-axis, x-axis, possible number)
def possible_answer(y, x, num):
    global sudoku  # Use the variable sudoku from outside of the function's scope
    for i in range(0, 9):  # because we have 9 possible elements
        if sudoku[y][i] == num:  # if the possible number is already in the y-axis:
            return False
    for i in range(0, 9):  # so it iterates once more
        if sudoku[i][x] == num:  # if the possible number is already in the x-axis:
            return False
    xbox = (x//3) * 3  # group the elements in 3 boxes. used floor division to get either the number 0, 3 or 6
    ybox = (y//3) * 3
    for i in range(0, 3):  # only 0 - 2 to get the value of element in between 0, 3, 6 and 9
        for j in range(0, 3):
            if sudoku[xbox + i][ybox + j] == num:  # to make a box in the x- and y-axis
                return False
    return True  # if num is not in any of the requirements above, then the number might be the correct answer

print(np.matrix(sudoku))
possible_answer(4, 5, 2)

