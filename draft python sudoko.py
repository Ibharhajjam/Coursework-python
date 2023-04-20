import random
import copy
import time
import math

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

#Grids 6-12 are 3x3

grid6 = [
		[0, 0, 6, 0, 0, 3],
		[5, 0, 0, 0, 0, 0],
		[0, 1, 3, 4, 0, 0],
		[0, 0, 0, 0, 0, 6],
		[0, 0, 1, 0, 0, 0],
		[0, 5, 0, 0, 6, 4]]

grid7 = [
        [9, 0, 6, 0, 0, 1, 0, 4, 0],
        [7, 0, 1, 2, 9, 0, 0, 6, 0],
        [4, 0, 2, 8, 0, 6, 3, 0, 0],
        [0, 0, 0, 0, 2, 0, 9, 8, 0],
        [6, 0, 0, 0, 0, 0, 0, 0, 2],
        [0, 9, 4, 0, 8, 0, 0, 0, 0],
        [0, 0, 3, 7, 0, 8, 4, 0, 9],
        [0, 4, 0, 0, 1, 3, 7, 0, 6],
        [0, 6, 0, 9, 0, 0, 1, 0, 8]]

grid8 = [
        [0, 0, 0, 2, 6, 0, 7, 0, 1],
        [6, 8, 0, 0, 7, 0, 0, 9, 0],
        [1, 9, 0, 0, 0, 4, 5, 0, 0],
        [8, 2, 0, 1, 0, 0, 0, 4, 0],
        [0, 0, 4, 6, 0, 2, 9, 0, 0],
        [0, 5, 0, 0, 0, 3, 0, 2, 8],
        [0, 0, 9, 3, 0, 0, 0, 7, 4],
        [0, 4, 0, 0, 5, 0, 0, 3, 6],
        [7, 0, 3, 0, 1, 8, 0, 0, 0]]

grid9 = [
        [0, 3, 0, 4, 0, 0],
        [0, 0, 5, 6, 0, 3],
        [0, 0, 0, 1, 0, 0],
        [0, 1, 0, 3, 0, 5],
        [0, 6, 4, 0, 3, 1],
        [0, 0, 1, 0, 4, 6]]

grid10 =[
        [0, 0, 0, 6, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 5, 0, 1],
        [3, 6, 9, 0, 8, 0, 4, 0, 0],
        [0, 0, 0, 0, 0, 6, 8, 0, 0],
        [0, 0, 0, 1, 3, 0, 0, 0, 9],
        [4, 0, 5, 0, 0, 9, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 3, 0, 0],
        [0, 0, 6, 0, 0, 7, 0, 0, 0],
        [1, 0, 0, 3, 4, 0, 0, 0, 0]]

grid11=[
       [8, 0, 9, 0, 2, 0, 3, 0, 0],
       [0, 3, 7, 0, 6, 0, 5, 0, 0],
       [0, 0, 0, 4, 0, 9, 7, 0, 0],
       [0, 0, 2, 9, 0, 1, 0, 6, 0],
       [1, 0, 0, 3, 0, 6, 0, 0, 0],
       [0, 0, 0, 0, 0, 0, 1, 0, 3],
       [7, 0, 0, 0, 0, 0, 0, 0, 8],
       [5, 0, 0, 0, 0, 0, 0, 1, 4],
       [0, 0, 0, 2, 8, 4, 6, 0, 5]]

grid12=[
       [0, 2, 0, 0, 0, 0, 0, 1, 0],
       [0, 0, 6, 0, 4, 0, 0, 0, 0],
       [5, 8, 0, 0, 9, 0, 0, 0, 3],
       [0, 0, 0, 0, 0, 3, 0, 0, 4],
       [4, 1, 0, 0, 8, 0, 6, 0, 0],
       [0, 0, 0, 0, 0, 0, 0, 9, 5],
       [2, 0, 0, 0, 1, 0, 0, 8, 0],
       [0, 0, 0, 0, 0, 0, 0, 0, 0],
       [0, 3, 1, 0, 0, 8, 0, 5, 7]]

grids = [(grid1, 2, 2), (grid2, 2, 2), (grid3, 2, 2), (grid4, 2, 2), (grid5, 2, 2),(grid6, 3,3),(grid7,3,3),(grid8,3,3),(grid9,3,3),(grid10, 3,3),(grid11,3,3),(grid12,3,3)]
'''
===================================
DO NOT CHANGE CODE ABOVE THIS LINE
===================================
'''

def check_section(section, n):

	if len(set(section)) == len(section) and sum(section) == sum([i for i in range(n+1)]):
		return True
	return False

def get_squares(grid, n_rows, n_cols):

	squares = []
	for i in range(n_cols):
		rows = (i*n_rows, (i+1)*n_rows)
		for j in range(n_rows):
			cols = (j*n_cols, (j+1)*n_cols)
			square = []
			for k in range(rows[0], rows[1]):
				line = grid[k][cols[0]:cols[1]]
				square +=line
			squares.append(square)


	return(squares)

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
	'''
	This function returns the index (i, j) to the first zero element in a sudoku grid
	If no such element is found, it returns None

	args: grid
	return: A tuple (i,j) where i and j are both integers, or None
	'''

	for i in range(len(grid)):
		row = grid[i]
		for j in range(len(row)):
			if grid[i][j] == 0:
				return (i, j)
            
                

	return None
# Find the row and column indices of the top-left cell in the square

def count_filled_cells(grid, squares):
    filled_counts = []
    for s in squares:
        # Finding the idices numbers of the current square
        square_cells_num = int((len(grid))**0.5)

        # Find the row and column indices of the top-left cell in the square
        row_start = (s[0] // square_cells_num) * square_cells_num

        col_start = (s[1] // square_cells_num) * square_cells_num


        # Count the number of filled cells in the square
        count = 0
        for i in range(row_start, row_start + square_cells_num):
            for j in range(col_start, col_start + square_cells_num):
                if grid[i][j] != 0:
                    count += 1

        # Add the square number and the count of filled cells to the list
        filled_counts.append((s, count))

    # Sort the list of tuples based on the count of filled cells in each square in descending order
    filled_counts.sort(key=lambda x: x[1], reverse=True)

    return filled_counts

def sort_squares_by_filled_cells(grid, square_size):
    counts = count_filled_cells(grid, square_size)
    sorted_squares = sorted(counts, reverse=True)
    return sorted_squares


    


#def find_most_filled(grid, n_rows, n_cols, empty_cells):
    n_rows = len(grid)
    n_cols = len(grid[0])
    square_cells_num = int((len(grid))**0.5)
    for i in range(n_rows):
        row = grid[i]
        for j in range(len(row)):
            col= row[j]
    row_start = (row // square_cells_num) * square_cells_num
    col_start = (col // square_cells_num) * square_cells_num
    empty_cells = find_empty(grid)
    
    square_cells_num = int((len(grid))**0.5)
    number_cells = [] # a list to store the number of the cells are filled in each square.
    for i in range(n_rows):
        for j in range(n_cols):
           count = count_filled_cells(grid, i*n_rows//square_cells_num, j*n_cols//square_cells_num, n_rows//square_cells_num, n_cols//square_cells_num)
            # Append the number of filled cells to the list of squares.
           number_cells.append(count)
    # Find the index of the square with the most filled cells.
    max_index = number_cells.index(max(number_cells))
    # Find the row and column indices of the top-left cell in the most filled square.
    row_index = (max_index // square_cells_num) * (n_rows//square_cells_num)
    col_index = (max_index % square_cells_num) * (n_cols//square_cells_num)
    # Loop over each cell in the most filled square.
    for i in range(n_rows//square_cells_num):
        for j in range(n_cols//square_cells_num):
            # If the cell is empty, return its row and column indices.
            if grid[row_index+i][col_index+j] == 0:
                return (row_index+i, col_index+j)
    # If no empty cells are found in the most filled square, use find_empty function.
    return find_empty(grid)


def guessing_values(grid, row, col, n_rows, n_cols):
    # Create a set of all possible values
    all_values = set(range(1, n_rows * n_cols + 1))

    # Find the values in the same row as the empty cell
    row_values = set(grid[row])

    # Find the values in the same column as the empty cell
    col_values = set(grid[i][col] for i in range(n_rows * n_cols))

    # Find the values in the same 3x3 square as the empty cell
    square_row = (row // n_rows) * n_rows
    square_col = (col // n_cols) * n_cols
    square_values = set(grid[i][j] for i in range(square_row, square_row + n_rows) 
                                        for j in range(square_col, square_col + n_cols))

    # Return the set of values that are not present in any of the above sets
    available_values = all_values - row_values - col_values - square_values

    # If there is only one available value, return it
    if len(available_values) == 1:
        return available_values.pop()

    # Sort the squares by the number of filled cells
    sorted_squares = sort_squares_by_filled_cells(grid)

    # Loop through the sorted squares to start guessing the numbers
    for count, row_start, col_start in sorted_squares:
        for i in range(row_start, row_start + n_rows):
            for j in range(col_start, col_start + n_cols):
                if grid[i][j] == 0:
                    for value in available_values:
                        # Make a copy of the grid to try out the value
                        temp_grid = [row[:] for row in grid]
                        temp_grid[i][j] = value

                        # Recursively call the function with the new grid
                        result = guessing_values(temp_grid, i, j, n_rows, n_cols)

                        # If a solution is found, return it
                        if result is not None:
                            return result

    # If no solution is found, return None
    return None




def recursive_solve(grid, n_rows, n_cols):
    '''
    This function uses recursion to exhaustively search all possible solutions to a grid
    until the solution is found

    args: grid, n_rows, n_cols
    return: A solved grid (as a nested list), or None
    '''

    #N is the maximum integer considered in this board
    n = n_rows*n_cols

    # Sort squares by the number of filled cells in each square
    square_indices = [(i, j) for i in range(0, n_rows, 3) for j in range(0, n_cols, 3)]
    sorted_squares = sort_squares_by_filled_cells(grid, square_indices)

    # Find an empty place in the grid in the most filled square
    for count, row_start, col_start in sorted_squares:
        for row_offset in range(n_rows // 3):
            for col_offset in range(n_cols // 3):
                row = row_start + row_offset
                col = col_start + col_offset
                if grid[row][col] == 0:
                    #Loop through possible values
                    for i in range(1, n+1):
                        #Place the value into the grid
                        grid[row][col] = i
                        # Check if the new value is valid
                        if check_solution(grid, n_rows, n_cols):
                            #Recursively solve the grid
                            ans = recursive_solve(grid, n_rows, n_cols)
                            #If we've found a solution, return it
                            if ans:
                                return ans 
                        #If the value is not valid, reset the cell to 0 for the next iteration
                        grid[row][col] = 0 
                    #If we get here, we've tried all possible values. Return none to indicate the previous value is incorrect.
                    return None
    #If there are no empty cells left, check if we've found a solution
    if check_solution(grid, n_rows, n_cols):
        return grid 
    else:
        #If the solution is incorrect, return None
        return None


def random_solve(grid, n_rows, n_cols, max_tries=50000):
	'''
	This function uses random trial and error to solve a Sudoku grid

	args: grid, n_rows, n_cols, max_tries
	return: A solved grid (as a nested list), or the original grid if no solution is found
	'''

	for i in range(max_tries):
		possible_solution = fill_board_randomly(grid, n_rows, n_cols)
		if check_solution(possible_solution, n_rows, n_cols):
			return possible_solution

	return grid

def fill_board_randomly(grid, n_rows, n_cols):
	'''
	This function will fill an unsolved Sudoku grid with random numbers

	args: grid, n_rows, n_cols
	return: A grid with all empty values filled in
	'''
	n = n_rows*n_cols
	#Make a copy of the original grid
	filled_grid = copy.deepcopy(grid)

	#Loop through the rows
	for i in range(len(grid)):
		#Loop through the columns
		for j in range(len(grid[0])):
			#If we find a zero, fill it in with a random integer
			if grid[i][j] == 0:
				filled_grid[i][j] = random.randint(1, n)

	return filled_grid 

def solve(grid, n_rows, n_cols):

	'''
	Solve function for Sudoku coursework.
	Comment out one of the lines below to either use the random or recursive solver
	'''
	
	#return random_solve(grid, n_rows, n_cols)
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