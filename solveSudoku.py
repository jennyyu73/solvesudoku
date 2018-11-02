##############
# Backtracking sudoku solver
# Jenny Yu
##################

import math

###### Solve Sudoku

def isValidInput(board, n, row, col):
    if board[row][col] != 0:
        return False
    sizeOfBlock=round(math.sqrt(len(board)))
    if n in board[row]: #checks n isn't in row
        return False
    elif n in [board[i][col] for i in range(len(board))]: #n isn't in col
        return False
    topLeftRow=sizeOfBlock*(row//sizeOfBlock)
    topLeftCol=sizeOfBlock*(col//sizeOfBlock)
    #checks n isn't in the block
    for i in range(topLeftRow, topLeftRow+sizeOfBlock):
        for j in range(topLeftCol, topLeftCol+sizeOfBlock):
            if n == board[i][j]:
                return False
    return True

def solveHelper(board, inputs, row, col):
    if row == len(board)-1 and col == len(board)-1 and board[row][col] != 0:
        #board is complete if we're at the lower right corner and it's filled
        return board
    #set the index of the next square we're moving to/looking at
    if col == len(board)-1: 
        newRow, newCol=row+1, 0
    else:
        newRow, newCol=row, col+1
    #if the board is empty at the next square, try a value
    if board[newRow][newCol] == 0:
        for num in inputs: 
            if isValidInput(board, num, newRow, newCol): #checks if valid move
                board[newRow][newCol]=num
                tmpSolution=solveHelper(board, inputs, newRow, newCol)
                if tmpSolution != None: return tmpSolution
                board[newRow][newCol]=0 #if not a valid try, reverse the move
        return None
    #if the board isn't empty at square, don't try a value, keep moving on
    tmpSolution=solveHelper(board, inputs, newRow, newCol)
    if tmpSolution != None: return tmpSolution
    return None

def solveSudoku(board):
    #possible inputs based on board size
    inputs=[i for i in range(1,len(board)+1)]
    #uses solve helper function and starting off the board 
    solution=solveHelper(board, inputs, 0, -1)
    return solution

###### Test Cases

def testEvaluate():
    print('Testing evaluate...', end='')
    assert(evaluate(2, 3, '+') == 5)
    assert(evaluate(3, 2, "+") == 5)
    assert(evaluate(5, 6, "*") == 30)
    assert(evaluate(6, 5, "*") == 30)
    assert(evaluate(5, 6, '-') == -1)
    assert(evaluate(6, 5, '-') == 1)
    print('passed!')

def testEvalPrefixNotation():
    print('Testing evalPrefixNotation...', end='')
    assert(evalPrefixNotation(['+', 2, '*', 3, 4]) == 14)
    assert(evalPrefixNotation([4]) == 4)
    assert(evalPrefixNotation(['+', '*', 2, 3, '*', 4, 5]) == 26)
    assert(evalPrefixNotation(
        ['*', '+', 2, '*', 3, '-', 8, 7, '+', '*', 2, 2, 5]) == 45)
    print('passed!')

board1 = [
        [ 5, 3, 0, 0, 7, 0, 0, 0, 0 ],
        [ 6, 0, 0, 1, 9, 5, 0, 0, 0 ],
        [ 0, 9, 8, 0, 0, 0, 0, 6, 0 ],
        [ 8, 0, 0, 0, 6, 0, 0, 0, 3 ],
        [ 4, 0, 0, 8, 0, 3, 0, 0, 1 ],
        [ 7, 0, 0, 0, 2, 0, 0, 0, 6 ],
        [ 0, 6, 0, 0, 0, 0, 2, 8, 0 ],
        [ 0, 0, 0, 4, 1, 9, 0, 0, 5 ],
        [ 0, 0, 0, 0, 8, 0, 0, 7, 9 ]]

solution1 = [
            [5, 3, 4, 6, 7, 8, 9, 1, 2], 
            [6, 7, 2, 1, 9, 5, 3, 4, 8], 
            [1, 9, 8, 3, 4, 2, 5, 6, 7], 
            [8, 5, 9, 7, 6, 1, 4, 2, 3], 
            [4, 2, 6, 8, 5, 3, 7, 9, 1], 
            [7, 1, 3, 9, 2, 4, 8, 5, 6], 
            [9, 6, 1, 5, 3, 7, 2, 8, 4], 
            [2, 8, 7, 4, 1, 9, 6, 3, 5], 
            [3, 4, 5, 2, 8, 6, 1, 7, 9]]

board2=[[0]*9 for i in range(9)]

solution2=[[1, 2, 3, 4, 5, 6, 7, 8, 9], 
           [4, 5, 6, 7, 8, 9, 1, 2, 3], 
           [7, 8, 9, 1, 2, 3, 4, 5, 6], 
           [2, 1, 4, 3, 6, 5, 8, 9, 7], 
           [3, 6, 5, 8, 9, 7, 2, 1, 4], 
           [8, 9, 7, 2, 1, 4, 3, 6, 5], 
           [5, 3, 1, 6, 4, 2, 9, 7, 8], 
           [6, 4, 2, 9, 7, 8, 5, 3, 1], 
           [9, 7, 8, 5, 3, 1, 6, 4, 2]]

board3=[[0, 0, 9, 0, 2, 8, 7, 0, 0],
        [8, 0, 6, 0, 0, 4, 0, 0, 5],
        [0, 0, 3, 0, 0, 0, 0, 0, 4],
        [6, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 2, 0, 7, 1, 3, 4, 5, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 2],
        [3, 0, 0, 0, 0, 0, 0, 0, 0],
        [9, 0, 0, 4, 0, 0, 8, 0, 7],
        [0, 0, 1, 2, 5, 0, 3, 0, 0]]

solution3=None

board4=[[6,0,0,0,0,8,9,4,0],
        [9,0,0,0,0,6,1,0,0],
        [0,7,0,0,4,0,0,0,0],
        [2,0,0,6,1,0,0,0,0],
        [0,0,0,0,0,0,2,0,0],
        [0,8,9,0,0,2,0,0,0],
        [0,0,0,0,6,0,0,0,5],
        [0,0,0,0,0,0,0,3,0],
        [8,0,0,0,0,1,6,0,0]]

def testSolveSudoku():
    print('Testing solveSudoku...',end='')
    assert(solveSudoku(board1) == solution1)
    assert(solveSudoku(board2) == solution2)
    assert(solveSudoku(board3) == solution3)
    print('passed!')

testSolveSudoku()
