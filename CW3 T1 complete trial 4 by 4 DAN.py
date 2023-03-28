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

#add the stuff in about finding the best zero.
def find_set(grid, row, col):
    """
    finds all possible options for a specified row/column coordinate that will have been
    identified as a zero.
    arguments: grid, row coordinate, column coordinate
    returns: a set of all possible options

    """
    givens = set()
    
    for i in range(4):
        row_no = grid[row][i]
#         print('row_no =',row_no)
        givens.add(row_no)
    
    for j in range(4):
        
        col_no = grid[j][col]
#         print('col_no =',col_no)
        givens.add(col_no)
    
    for k in range(4):
        if k//2== row//2:
#             print('k =',k)
            for l in range(4):
                if l//2 == col//2:
#                     print('l = ', l)
                    box_no = grid[k][l]
#                     print('box_no = ', box_no)
                    givens.add(box_no)
    
#     print('givens = ',givens)
    
    total = set()
    for m in range(1,5):
        total.add(m)
#     print('total options = ',total)
    options = total - givens
#     print('options:', options)
    return options

   
def best_zero(grid):
    options_dict = {}
    for f in range(4):
        for g in range(4):
            if grid[f][g] == 0:
                
                options_dict[f, g] = find_set(grid, f, g)
    #then I need to min-dict options_dict
    
    
    values = list(options_dict.values())
#     print('values = ', values)
    if len(values) == 0:
        return None
    shortest = values[0]
    counter = 1
    index = 0

    while counter < len(values):
        len_shortest = len(shortest)
#         print('length of shortest = ', len_shortest)
        l = values[counter]
        len_l = len(l)
#         print('length of l = ', len_l)
        if len_l < len_shortest:
            shortest = l
#             print('therefore new shortest = ', shortest)
            index = counter
        counter +=1

#     print('final shortest = ', shortest, 'at position', index)
    
    
    zero = list(options_dict.items())[index]
    
    zero = list(zero)
    zero[1] = tuple(zero[1])
    return zero




    
    
    
def recursive_solve(grid, n_rows, n_cols):
    '''
    This function uses recursion to exhaustively search all possible solutions to a grid
    until the solution is found

    args: grid, n_rows, n_cols
    return: A solved grid (as a nested list), or None
    '''

    #N is the maximum integer considered in this board
    n = n_rows*n_cols
    #Find an empty place in the grid
    zero = best_zero(grid)
#   print(zero)
# 	empty = find_empty(grid)
# 	print(empty)
    #If there's no empty places left, check if we've found a solution
    if not zero:
        #If the solution is correct, return it.
        if check_solution(grid, n_rows, n_cols):
            return grid 
        else:
            #If the solution is incorrect, return None
            return None
    else:
        row = zero[0][0]
#         print('row = ', row)
        col = zero[0][1]
#         print('col = ', col)
        options = zero[1]
#         print('options=', options)
    #Loop through possible values
        for i in options:
            
    #         print('option = ', i)
            #Place the value into the grid
            grid[row][col] = i
            #Recursively solve the grid
            ans = recursive_solve(grid, n_rows, n_cols)
            #If we've found a solution, return it
            if ans:
                return ans 

            #If we couldn't find a solution, that must mean this value is incorrect.
            #Reset the grid for the next iteration of the loop
            grid[row][col] = 0 

    #If we get here, we've tried all possible values. Return none to indicate the previous value is incorrect.
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