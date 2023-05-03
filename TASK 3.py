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



test1 = [[{1,2,3,4},{3},{4,2},{1,2}],
        [{1,3,4},{1,3},{4,1}, {2}],
        [{2},{1,3,2},{1,4,3},{1,4,2,3}],
        [{1,2,3},{1,2,3,4},{1,2},{1,2}]]

test2 = [[{1}, {2},{3},{4}],
        [{1}, {2},{3},{4}],
        [{1}, {2},{3},{4}],
        [{1}, {2},{3},{4}]]

test3 = [[{1}, {1,2,3,4},{1,2,3,4},{1,2,3,4}],
         [{1,2,3,4}, {1,2,3,4},{1,2,3,4},{1,2,3,4}],
         [{1,2,3,4}, {1,2,3,4},{1,2,3,4},{1,2,3,4}],
         [{1,2,3,4}, {1,2,3,4},{1,2,3,4},{1,2,3,4}]]
test4 = [[set(), set(), set(), set()],
         [set(), set(), set(), set()],
         [set(), set(), set(), set()],
         [set(), set(), set(), set()]]
         



# test = shortest_set(test1,2,2)
# print(test)
# test = shortest_set(test2,2,2)
# print(test)
# test = shortest_set(test3,2,2)
# print(test)


#fix this to work with sets





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



   
# def best_zero(grid, n_rows, n_cols, total):
#     n = n_rows*n_cols
#     options_list = []
#     for f in range(n):
#         for g in range(n):
#             if grid[f][g] == 0:
#                 
#                 options = find_set(grid, f, g, n_rows, n_cols, total)
#                 if len(options) == 1:
#                     return f,g, options
#                 #if there are any zeros with only one option, the function can end as no better zero can be found
#                 
#                     
#                     
#                 options_list.append([f,g, options, len(options)])
#                 #creates a nested list with the coordinates of the zero, the set of options, and the length of the options set, so it can be sorted
#                 
#     
#     if len(options_list) ==0:
#         return None
#     #stopping case for recursive function
#     
#     sorted_options_list = sorted(options_list, key=lambda x: x[3])
#     return sorted_options_list[0]
    #uses a throwaway variable lambda to sort the options_list by fewest options, then returns the list at index 0.

def build_sets(n):
    
    sudoku = []
    for i in range(n):
        comb_row = []

        for j in range(n):
            combinations = set()
            for k in range(1,n+1):
                combinations.add(k)
                
            comb_row.append(combinations)
        sudoku.append(comb_row)
    return sudoku

sets = build_sets(4)


def remove_duplicates(value, row, col, sudoku, n_rows, n_cols):
    """

    # Remove value from all sets in the same row, column and square
    
    """
    n = n_rows*n_cols
    
    for i in range(n):
        row_set = sudoku[row][i]
#         print('set =', row_set)
        row_set.discard(value)
#         print('new set =', row_set)
        #removes all numbers in the zero's row from a set of 'given' numbers. 

    for j in range(n):
        
        col_set = sudoku[j][col]
        col_set.discard(value)
        
    #removes all numbers in the value's column from the same set
#         
    for k in range(n):
        if k//n_rows== row//n_rows:
            for l in range(n):
                if l//n_cols == col//n_cols:
                    box_set = sudoku[k][l]
                    box_set.discard(value)
    #removes all numbers in the value's square from the set
    
    
    
    
    
    
    return sudoku

# y = remove_duplicates(3, 0, 1, sets, 2, 2)
# print(y)



def process_rows(grid, n_rows, n_cols):
    n = n_rows*n_cols
    sudoku = build_sets(n)

    for row in range(n):
        for col in range(n):
            value = grid[row][col]
#             if value != 0:
#                 print('value:',value)
                
#             else:
#             print('code resumed again')
            removed_board = remove_duplicates(value, row, col, sudoku, n_rows, n_cols)
            
#             print(removed_board)
            
    
    
    return removed_board


#could then send this off to a program that measures the smallest set, then puts all the things back and takes out the set notation



test_process= process_rows(grid2, 2, 2)
# print(test_process)

def shortest_set(grid, n_rows, n_cols):
    n = n_rows*n_cols
    
    length = 1
    while length <= n:
        row = 0
        
        while row < n:
            
            col = 0
            while col < n:
#                 print('length:', length)
#                 print('row:', row)
#                 print('col:', col)
                combs = grid[row][col]
                if len(combs) == length:
                    return combs, row, col
                col +=1
            row +=1
    
        length +=1

    #should return none ONLY if all sets have length 1. if no lengths shorter than the other, return the very first grid
        
    return None

print(shortest_set(test4, 2,2))
    
    
def wavefront_solve(explain_requested, grid, n_rows, n_cols):
    '''
    This function uses recursion to exhaustively search all possible solutions to a grid
    until the solution is found

    args: grid, n_rows, n_cols
    return: A solved grid (as a nested list), or None
    '''
    #print('recursive solving')
    n = n_cols*n_rows
    
    removed_board = process_rows(grid, n_rows, n_cols)
   
    #N is the maximum integer considered in this board
    #Find an empty place in the grid
    combs, row, col = shortest_set(removed_board, n_rows, n_cols)
    
    print('combs, row, col', combs, row, col)
    print('new grid', grid)
    #could just put this in the first set!
    
    #will need a function that strips off all 'set' notation'. Maybe puts it all back after? or maybe don't need to do any of that.    
    
    #If there's no empty places left, check if we've found a solution
    if not combs:     
        print('complete grid')
        
        
        #PUT ALL THE NUMBERS BACK AS THEY WERE!
        #CONVERT FROM SETS TO JUST NUMBERS
        
        
        for row in range(n):
            for col in range(n):
                
                test2[row][col] = tuple(grid[row][col])[0]
                
                
                
        #If the solution is correct, return it.
        if check_solution(grid, n_rows, n_cols):
            return grid
        else:
            #If the solution is incorrect, return None
            return None
    else:
            #the row and column locations is outputted by the function best_zero()
            # the options are also outputted by the function best_zero()

    #Loop through possible values
        for i in combs:
            #Place the value into the grid
            grid[row][col] = i
            #Recursively solve the grid
            ans = wavefront_solve(explain_requested, grid, n_rows, n_cols)
            #If we've found a solution, return it
            if ans:
                return ans 

            #If we couldn't find a solution, that must mean this value is incorrect.
            #Reset the grid for the next iteration of the loop
        #this would be where I'd need to reclass the iterations
            
            grid[row][col] = combs

    #If we get here, we've tried all possible values. Return none to indicate the previous value is incorrect.
    return None

def best_comb(grid, n_rows, n_cols):
    
    n = n_rows*n_cols
    sudoku = build_sets(n)

    for row in range(n):
        for col in range(n):
            value = grid[row][col]
#             if value != 0:
#                 print('value:',value)
                
#             else:
#             print('code resumed again')
            removed_board = remove_duplicates(value, row, col, sudoku, n_rows, n_cols)
            
#             print(removed_board)
            
    
    
    combs, row, col = shortest_set(removed_board, 2,2)
    return row, col, combs
    


















def recursive_solve(explain_requested, grid, n_rows, n_cols):
    '''
    This function uses recursion to exhaustively search all possible solutions to a grid
    until the solution is found

    args: grid, n_rows, n_cols
    return: A solved grid (as a nested list), or None
    '''
    #print('recursive solving')
    n = n_cols*n_rows
    
    
    
    combs = best_comb(grid, n_rows, n_cols)
    print(combs)
    
    
    #If there's no empty places left, check if we've found a solution
    if not combs:
        #If the solution is correct, return it.
        if check_solution(grid, n_rows, n_cols):
            return grid
        else:
            #If the solution is incorrect, return None
            return None
    else:
            #the row and column locations is outputted by the function best_zero()
        row = combs[0]
        col = combs[1]
            # the options are also outputted by the function best_zero()

        options = combs[2]
        print('row=',row,col, options)
        print('col=',col)
        print('options=',options)
    #Loop through possible values
        for i in options:
            #Place the value into the grid
            print(i)
            grid[row][col] = i
            print(i)
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

print(recursive_solve(False,grid5,2,2))

# solution =wavefront_solve(False, grid4, 2,2)
# print(solution)
