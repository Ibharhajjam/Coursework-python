# -*- coding: utf-8 -*-
"""
Created on Wed Mar 29 23:39:14 2023

@author: Ibhar
"""

import random
import copy
import time

#Grids 1-4 are 2x2
grid1 = [
		[1, 0, 4, 2],
		[4, 2, 1, 3],
		[2, 1, 3, 4],
		[3, 4, 2, 1]]

grid2 = [
		[1, 0, 4, 2],
		[4, 2, 1, 3],
		[2, 1, 0, 4],
		[3, 4, 2, 1]]

grid3 = [
		[1, 0, 4, 2],
		[4, 2, 1, 0],
		[2, 1, 0, 4],
		[0, 4, 2, 1]]

grid4 = [
		[1, 0, 4, 2],
		[0, 2, 1, 0],
		[2, 1, 0, 4],
		[0, 4, 2, 1]]

grid5 = [
		[1, 0, 0, 2],
		[0, 0, 1, 0],
		[0, 1, 0, 4],
		[0, 0, 0, 1]]

grid6 = [
		[0, 0, 6, 0, 0, 3],
		[5, 0, 0, 0, 0, 0],
		[0, 1, 3, 4, 0, 0],
		[0, 0, 0, 0, 0, 6],
		[0, 0, 1, 0, 0, 0],
		[0, 5, 0, 0, 6, 4]]

grids = [(grid1, 2, 2), (grid2, 2, 2), (grid3, 2, 2), (grid4, 2, 2), (grid5, 2, 2)]
'''
===================================
DO NOT CHANGE CODE ABOVE THIS LINE
===================================
'''

def check_section(section, n):
    """
    Check whether a section (row, column, or square) of a Sudoku board is valid.

    Args:
    - section: A list of integers representing a row, column, or square in a Sudoku board.
    - n: The size of the board (i.e., the number of rows or columns in each square).

    Returns:
    - True if the section is valid (i.e., contains each integer from 1 to n^2 exactly once),
      False otherwise.
    """
#Ensure that there are no duplicate components in the section.
#It also ensures that all integers from 1 to n**2 appear precisely once in the section.
#the size of the grid integres is n**2 
    if len(set(section)) == len(section) and sum(section) == sum(range(1, (n**2)+1)):
        return True
    return False

def get_squares(grid, n_rows, n_cols):
    """
    Get a list of all squares in a Sudoku board.

    Args:
    - grid: A 2D list of integers representing a Sudoku board.
    - n_rows: The number of rows in each square of the board.
    - n_cols: The number of columns in each square of the board.

    Returns:
    - A list of lists, where each sublist represents a square in the board.
    """
    squares = []
    for i in range(n_cols):
        cols = (i*n_cols, (i+1)*n_cols)
        for j in range(n_rows):
            rows = (j*n_rows, (j+1)*n_rows)
            square = []
            for k in range(rows[0], rows[1]):
                line = grid[k][cols[0]:cols[1]]
                square += line
            squares.append(square)
    return squares

#To complete the first assignment, please write the code for the following function
def check_solution(grid, n_rows, n_cols):
	'''
	This function is used to check whether a sudoku board has been correctly solved

	args: grid - representation of a suduko board as a nested list.
	returns: True (correct solution) or False (incorrect solution)
	'''
	n = n_rows*n_cols

	for row in grid:
		if check_section(row, n) == False:
			return False

	for i in range(n_rows**2):
		column = []
		for row in grid:
			column.append(row[i])

		if check_section(column, n) == False:
			return False

	squares = get_squares(grid, n_rows, n_cols)
	for square in squares:
		if check_section(square, n) == False:
			return False

	return True




def find_empty(grid):
    """
    Find the index of the first empty cell in a Sudoku board.

    Args:
    - grid: A 2D list of integers representing a Sudoku board.

    Returns:
    - A tuple (i, j) representing the row and column indices of the first empty cell in the board,
      or None if there are no empty cells.
    """
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j] == 0:
                return (i, j)
    return None

def find_most_filled(grid):
    n_rows = len(grid)
    n_cols = len(grid[0])
    number_squares = [] # a list to store the number of the cells are filled in each square.
    for i in range(n_rows):
        for j in range(n_cols):
            count = 0 #  a counter to count filled cells in each square.
            for k in range(n_rows): # Loop through all indices of the current square.
                for l in range(n_cols):
                    if grid[i*n_rows+k][j*n_cols+l] != 0: 
                        count += 1 #Increase the counter if the cell is full.
            # Append the number of filled cells to the list of squares.
            number_squares.append(count)
    # Find the index of the square with the most filled cells.
    max_idex = number_squares.index(max(number_squares))
    # Find the row and column indices of the top-left cell in the most filled square.
    row_idex = (max_idex // n_cols) * n_rows
    col_idex = (max_idex % n_cols) * n_cols
    # Loop over each cell in the most filled square.
    for i in range(n_rows):
        for j in range(n_cols):
            # If the cell is empty, return its row and column indices.
            if grid[row_idex+i][col_idex+j] == 0:
                return (row_idex+i, col_idex+j)
    # If no empty cells are found in the most filled square, use find_empty function.
    return find_empty(grid)




def recursive_solve(grid, n_rows, n_cols): #incomplete
    '''
    This function uses recursion to exhaustively search all possible solutions to a grid
    until the solution is found

    args: grid, n_rows, n_cols
    return: A solved grid (as a nested list), or None
    '''

    # N is the maximum integer considered in this board
    n = n_rows * n_cols
    # Find an empty place in the grid
    empty = find_empty(grid)

    # If there's no empty places left, check if we've found a solution
    if not empty:
        # If the solution is correct, return it.
        if check_solution(grid, n_rows, n_cols):
            return grid
        else:
# If the solution is incorrect, return None
                return None
  
    row, col = empty 

# Loop through possible values
    for i in range(1, n+1):

 # Check if the value is allowed in this position
        if i not in [grid[k][col] for k in range(n_rows**2)]:
            square_row = (row // n_rows) * n_rows
            square_col = (col // n_cols) * n_cols
            if i not in [grid[square_row + j][square_col + k] for j in range(n_rows) for k in range(n_cols)]:
                # Place the value into the grid
                grid[row][col] = i
                # Recursively solve the grid
                ans = recursive_solve(grid, n_rows, n_cols)
                # If we've found a solution, return it
                if ans:
                    return ans

                # If we couldn't find a solution, that must mean this value is incorrect.
                # Reset the grid for the next iteration of the loop
                grid[row][col] = 0

# If we get here, we've tried all possible values. Return none to indicate the previous value is incorrect.
    return None



def random_solve(grid): #needs checking and editting
    '''
    This function uses random trial and error to solve a Sudoku grid

    args: grid, n_rows, n_cols, max_tries
    return: A solved grid (as a nested list), or the original grid if no solution is found
    '''
    row, col= find_most_filled(grid)
    if row == -1 and col == -1:
        return True
    for v in random.sample(range(1,len(grid)+1), len(grid)):
        if check_solution( row, col, v):
            grid[row][col] = v
            if random_solve(grid):
                return grid
            grid[row][col] = 0
    return None


def fill_board_randomly(grid, n_rows, n_cols):  #needs checking and editting
    '''
    This function will fill an unsolved Sudoku grid with random numbers

    args: grid, n_rows, n_cols
    return: A grid with all empty values filled in
    '''
    n = n_rows * n_cols
    # Make a copy of the original grid
    filled_grid = copy.deepcopy(grid)

    # Loop through the rows
    for i in range(len(grid)):
        # Loop through the columns
        for j in range(len(grid[0])):
            # If we find a zero, fill it in with a random integer
            if grid[i][j] == 0:
                # Keep trying different numbers until we find one that works
                valid_numbers = list(range(1, n+1))
                random.shuffle(valid_numbers)
                for num in valid_numbers:
                    filled_grid[i][j] = num
                    if check_solution(filled_grid, n_rows, n_cols):
                        break
                else:
                    # If no valid numbers work, reset to 0 and return None
                    filled_grid[i][j] = 0
                    return None

    return filled_grid


def solve(grid, n_rows, n_cols):
    '''
    Solve function for Sudoku coursework.
    Comment out one of the lines below to either use the random or recursive solver
    '''

    # return random_solve(grid, n_rows, n_cols)
    return recursive_solve(grid, n_rows, n_cols)

'''
===================================
DO NOT CHANGE CODE BELOW THIS LINE
===================================
'''
def main():

	points = 0

	print("Running test script for coursework 1")
	print("====================================")
	
	for (i, (grid, n_rows, n_cols)) in enumerate(grids):
		print("Solving grid: %d" % (i+1))
		start_time = time.time()
		solution = solve(grid, n_rows, n_cols)
		elapsed_time = time.time() - start_time
		print("Solved in: %f seconds" % elapsed_time)
		print(solution)
		if check_solution(solution, n_rows, n_cols):
			print("grid %d correct" % (i+1))
			points = points + 10
		else:
			print("grid %d incorrect" % (i+1))

	print("====================================")
	print("Test script complete, Total points: %d" % points)


if __name__ == "__main__":
	main()