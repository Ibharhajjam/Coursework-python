import copy
import time

#Grids 1-5 are 2x2
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

grid7 = [[8, 0, 9, 0, 2, 0, 3, 0, 0],
[0, 3, 7, 0, 6, 0, 5, 0, 0],
[0, 0, 0, 4, 0, 9, 7, 0, 0],
[0, 0, 2, 9, 0, 1, 0, 6, 0],
[1, 0, 0, 3, 0, 6, 0, 0, 0],
[0, 0, 0, 0, 0, 0, 1, 0, 3],
[7, 0, 0, 0, 0, 0, 0, 0, 8],
[5, 0, 0, 0, 0, 0, 0, 1, 4],
[0, 0, 0, 2, 8, 4, 6, 0, 5]]

grids = [(grid1, 2, 2), (grid2, 2, 2), (grid3, 2, 2), (grid4, 2, 2), (grid5, 2, 2), (grid6, 2, 3), (grid7, 3, 3)]
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

	for i in range(n_rows):
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


def generate_range(grid, row, col):
    '''
    This function replaces all the zeros in a grid into a set containing numbers from 1 to the maximum number in a grid.
    '''
    a = grid
    max = row * col
    for i in range(row * col):
        for j in range(col * row):
            if not a[i][j]:
                a[i][j] = {(i + 1) for i in range(max)}
    return a


def remove(item, num):
    '''
    This function will remove a number from a set.
    '''
    try:
        item.remove(num)
        return item
    except KeyError:
        return item
    

def simplify(grid, row, col):
    '''
    This function will search for sets of length 1 in a grid and change it into the integer.
    '''
    for i in range(row * col):
        for j in range(col * row):
            if not isinstance(grid[i][j], int) and len(grid[i][j]) == 1:
                grid[i][j] = sum(grid[i][j])
            elif not isinstance(grid[i][j], int) and len(grid[i][j]) == 0:
                return False
    return grid


def find_least(grid, row, col):
    '''
    This function searches for the set in a grid with the least length, and returns its list index.
    '''
    row_count = 0
    col_count = 0
    least_lenth = row * col
    row_num = 0
    col_num = 0
    while row_count < row * col:
        while col_count < col * row:
            if isinstance(grid[row_count][col_count], set) and len(grid[row_count][col_count]) < least_lenth:
                temp = list(grid[row_count][col_count])
                row_num = row_count
                col_num = col_count
                least_lenth = len(grid[row_count][col_count])
            col_count += 1
        col_count = 0
        row_count += 1
    return row_num, col_num
    

def check_row(grid, row, col):
    '''
    Start eliminating by row elements.
    '''
    appeared = []
    blank = []
    for i in range(row * col):
        for j in range(col * row):
            if isinstance(grid[i][j], int):
                appeared.append(grid[i][j])
            else:
                blank.append(j)
        for j in blank:
            for k in appeared:
                remove(grid[i][j], k)
        appeared = []
        blank = []
    result = simplify(grid, row, col)
    if result:
        return result
    else:
        return False


def check_col(grid, row, col):
    '''
    Start eliminating by column elements.
    '''
    appeared = []
    blank = []
    for i in range(row * col):
        for j in range(col * row):
            if isinstance(grid[j][i], int):
                appeared.append(grid[j][i])
            else:
                blank.append(j)
        for j in blank:
            for k in appeared:
                remove(grid[j][i], k)
        appeared = []
        blank = []
    result = simplify(grid, row, col)
    if result:
        return result
    else:
        return False


def check_box(grid, row, col):
    '''
    Start eliminating by square elements.
    '''
    appeared = []
    blank_row = []
    blank_col = []
    row_count = 0
    column_count = 0
    while column_count < row:
        while row_count < col:
            for i in range(row):
                for j in range(col):
                    if isinstance(grid[i + row * row_count][j + col * column_count], int):
                        appeared.append(grid[i + row * row_count][j + col * column_count])
                    else:
                        blank_row.append(i + row * row_count)
                        blank_col.append(j + col * column_count)
            for i in range(len(blank_row)):
                for j in appeared:
                    remove(grid[blank_row[i]][blank_col[i]], j)
            row_count += 1
            appeared = []
            blank_row = []
            blank_col = []
        column_count += 1
        row_count = 0
    result = simplify(grid, row, col)
    if result:
        return result
    else:
        return False
    

def check_fin(grid, row, col):
    '''
    Checks if there are still sets remained in a grid. If no, then the grid is finished.
    '''
    for i in range(row * col):
        for j in range(col * row):
            if isinstance(grid[i][j], set):
                return False
    return True


def stuck(grid, row, col):
    '''
    Start a set of eliminating based on the value returned from the 'find_least' function.
    '''
    copylist = copy.deepcopy(grid)
    r, c = find_least(grid, row, col)
    least = list(grid[r][c])
    for x in least:
        grid = copy.deepcopy(copylist)
        grid[r][c] = x
        result = check_for_m(grid, row, col)
        if result:
            return result
    if not result:
        return False


def check(grid, row, col):
    '''
    Simplified function to call all the checkers.
    '''
    while not check_fin(grid, row, col):
        copylist = copy.deepcopy(grid)
        grid = check_box(check_col(check_row(grid, row, col), row, col), row, col)
        if copylist == grid:
            grid = stuck(grid, row, col)
    return grid


def check_for_m(grid, row, col):
    '''
    A complex function to use the checkers, with more if statement to prevent crash.
    '''
    while grid and not check_fin(grid, row, col):
        copylist = copy.deepcopy(grid)
        if grid:
            grid = check_row(grid, row, col)
        if grid:
            grid = check_col(grid, row, col)
        if grid:
            grid = check_box(grid, row, col)
        if not grid:
            return False
        if copylist == grid:
            grid = stuck(grid, row, col)
    if grid and check_solution(grid, row, col):
        return grid
    else:
        return False


def recursive_solve(grid, n_rows, n_cols):
    return check(generate_range(grid, n_rows, n_cols), n_rows, n_cols)


def random_solve(grid, n_rows, n_cols, max_tries=500):

	for i in range(max_tries):
		pass

	return grid


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