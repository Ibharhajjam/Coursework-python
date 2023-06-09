#!/usr/bin/env python

import time
import sys

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

grids = [(grid1, 2, 2), (grid2, 2, 2), (grid3, 2, 2), (grid4, 2, 2), (grid5, 2, 2),(grid6,2,3), (grid7,3,3),(grid8,3,3),(grid9,2,3),(grid10, 3,3),(grid11,3,3),(grid12,3,3)]


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



#'find-empty()' function replaced with 'find_set()'

def find_set(grid, row, col, n_rows, n_cols, total):
    """
    finds all possible options for a specified row/column coordinate that will have been
    identified as a zero.
    arguments: grid, row coordinate, column coordinate
    returns: a set of all possible options

    """
    n= n_rows*n_cols
    givens = set()
    
    for i in range(n):
        row_no = grid[row][i]
        givens.add(row_no)
        #adds all numbers in the zero's row to a set of 'given' numbers. Repetitions eliminated by definition

    for j in range(n):
        
        col_no = grid[j][col]
        givens.add(col_no)
    #adds all numbers in the zero's column to the same set
        
        for k in range(n):
            if k//n_rows== row//n_rows:
                for l in range(n):
                    if l//n_cols == col//n_cols:
                        box_no = grid[k][l]
                        givens.add(box_no)
    #adds all numbers in the zero's square to the set
    # chooses only those rows which have the same remainder when divided by 3 i.e. in the same box. for example, the square with row numbers
    #0,1,2 and column 3,4,5 will be indexed as square 0, 1. This is matched with the given row and col coordinates

    options = total - givens
    return options

   
def best_zero(grid, n_rows, n_cols, total):
    n = n_rows*n_cols
    options_list = []
    for f in range(n):
        for g in range(n):
            if grid[f][g] == 0:
                
                options = find_set(grid, f, g, n_rows, n_cols, total)
                if len(options) == 1:
                    return f,g, options
                #if there are any zeros with only one option, the function can end as no better zero can be found
                
                    
                    
                options_list.append([f,g, options, len(options)])
                #creates a nested list with the coordinates of the zero, the set of options, and the length of the options set, so it can be sorted
                
    
    if len(options_list) ==0:
        return None
    #stopping case for recursive function
    
    sorted_options_list = sorted(options_list, key=lambda x: x[3])
    return sorted_options_list[0]
    #uses a throwaway variable lambda to sort the options_list by fewest options, then returns the list at index 0.
    



    
    
    
def recursive_solve(explain_requested, grid, n_rows, n_cols):
    '''
    This function uses recursion to exhaustively search all possible solutions to a grid
    until the solution is found

    args: grid, n_rows, n_cols
    return: A solved grid (as a nested list), or None
    '''
    #print('recursive solving')
    n = n_cols*n_rows
    
    total = set()
    for m in range(1, n+1):
        total.add(m)
    #N is the maximum integer considered in this board
    #Find an empty place in the grid
    zero = best_zero(grid, n_rows, n_cols, total)
    #If there's no empty places left, check if we've found a solution
    if not zero:
        #If the solution is correct, return it.
        if check_solution(grid, n_rows, n_cols):
            return grid
        else:
            #If the solution is incorrect, return None
            return None
    else:
            #the row and column locations is outputted by the function best_zero()
        row = zero[0]
        col = zero[1]
            # the options are also outputted by the function best_zero()

        options = zero[2]
    #Loop through possible values
        for i in options:
            #Place the value into the grid
            grid[row][col] = i
            #Recursively solve the grid
            ans = recursive_solve(explain_requested, grid, n_rows, n_cols)
            #If we've found a solution, return it
            if ans:
                return ans 

            #If we couldn't find a solution, that must mean this value is incorrect.
            #Reset the grid for the next iteration of the loop
            grid[row][col] = 0 

    #If we get here, we've tried all possible values. Return none to indicate the previous value is incorrect.
    return None

def wavefront_solve(explain_requested, grid, n_rows, n_cols):
    print('wavefront solving')
    print('explain requested?', explain_requested)

    return



def explain():
    print('explain function activated')
    return

def file_retrieve(input_address):
    print('retrieving file')
    print('location:', input_address)
    return grid, n_rows, n_cols



def hint(N):
    print('hint function activated')
    print('N is ', N)
    return

def profile(wavefront_requested):
    #should use 'solve' function to differentiate between wavefront and recursive.
    print('profile function activated')


def arguments(args):
    
    wavefront_requested = False
    explain_requested = False
    file_requested = False
    hint_requested = False
    profile_requested = False
    
    input_address = None
    output_address = None
    N = None
    
    if '-wavefront' in args:
        wavefront_requested = True
        
    
    if '-explain' in args:
        explain_requested = True
        
    if '-profile' in args:
        profile_requested = True

    
    counter = 0
    while counter < len(args):
        
        if args[counter] == '-file':
            file_requested = True
            input_address = args[counter +1]
            output_address = args[counter +2]
        if args[counter] == '-hint':
            hint_requested = True
            N = int(args[counter+1])
        counter +=1
    
        

        
    
    
    

    return wavefront_requested, explain_requested, file_requested, input_address, output_address, hint_requested, N, profile_requested


def solve(explain_requested, wavefront_requested, grid, n_rows, n_cols):
    print('explain requested?', explain_requested)

    if wavefront_requested:
        return wavefront_solve(explain_requested, grid, n_rows, n_cols)
    else:
        return recursive_solve(explain_requested, grid, n_rows, n_cols)




    
    
def main(args):
    
    wavefront_requested, explain_requested, file_requested, input_address, output_address, hint_requested, N, profile_requested = arguments(args)
    print(arguments(args))
    
    if profile_requested:
        profile(wavefront_requested)
        
    elif file_requested:
        
        grid, n_rows, n_cols = file_retrieve(input_address)
        solution = solve(explain_requested, wavefront_requested, grid, n_rows, n_cols)
        print(solution)
        if hint_requested:
            hint(N)
            
    elif file_requested == False:
        
        for (i, (grid, n_rows, n_cols)) in enumerate(grids):
            print("Solving grid: %d" % (i+1))
            solution = solve(explain_requested, wavefront_requested, grid, n_rows, n_cols)
            print(solution)
            if hint_requested:
                hint(N)
        
        
        
if __name__ == '__main__':
    main(sys.argv[1:])
