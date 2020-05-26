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

sudoku1 = [[4,1,0,2,7,0,8,0,5],
          [0,8,5,1,4,6,0,9,7],
          [0,7,0,5,8,0,0,4,0],
          [9,2,7,4,5,1,3,8,6],
          [5,3,8,6,9,7,4,1,2],
          [1,6,4,3,2,8,7,5,9],
          [8,5,2,7,0,4,9,0,0],
          [0,9,0,8,0,2,5,7,4],
          [7,4,0,9,6,5,0,2,8]]


print(np.matrix(sudoku))  # print out empty sudoku puzzle


# Function to detect possible answer to the empty sudoku tile (y-axis, x-axis, possible number)
def possible_answer(x, y, num):
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


# Function to solve sudoku using the possible_answer function above
def solve_sudoku():  # no parameter because global variable will be used
    global sudoku
    for x in range(0, 9):
        for y in range(0, 9):  # to iterate through every element in the list
            if sudoku[x][y] == 0:  # if the element is not yet filled with possible number
                for n in range(1, 10):  # iterate through every possible numbers from 1 to 9
                    if possible_answer(y, x, n):  # check if True is returned
                        sudoku[x][y] = n  # assign n as the answer in the list
                        if solve_sudoku():  # recursion so the function runs again until every 0 is assigned to a number
                            return True
                        sudoku[x][y] = 0  # if there is no possible answer (wrong input or something)
    return True  # so it goes back (out of the if command)
    print(np.matrix(sudoku))  # print the completed sudoku

solve_sudoku()
print(np.matrix(sudoku))
print(possible_answer(5, 4, 4))
