import time
import matplotlib.pyplot as plt


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
    n = n_rows*n_cols #the size of the grid
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
    



    
    
    
def recursive_solve(grid, n_rows, n_cols):
    '''
    This function uses recursion to exhaustively search all possible solutions to a grid
    until the solution is found
    args: grid, n_rows, n_cols
    return: A solved grid (as a nested list), or None
    '''
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
            ans = recursive_solve(grid, n_rows, n_cols)
            #If we've found a solution, return it
            if ans:
                return ans 

            #If we couldn't find a solution, that must mean this value is incorrect.
            #Reset the grid for the next iteration of the loop
            grid[row][col] = 0 

    #If we get here, we've tried all possible values. Return none to indicate the previous value is incorrect.
    return None


grids_dic ={"grid1":[[1, 0, 4, 2],[4, 2, 1, 3],[2, 1, 3, 4],[3, 4, 2, 1]],
            "grid2":[[1, 0, 4, 2],[4, 2, 1, 3],[2, 1, 0, 4],[3, 4, 2, 1]],
            "grid3":[[1, 0, 4, 2],[4, 2, 1, 0],[2, 1, 0, 4],[0, 4, 2, 1]],
            "grid4":[[1, 0, 4, 2],[0, 2, 1, 0],[2, 1, 0, 4],[0, 4, 2, 1]],
            "grid5":[[1, 0, 0, 2],[0, 0, 1, 0],[0, 1, 0, 4],[0, 0, 0, 1]],
            "grid6":[[0, 0, 6, 0, 0, 3],[5, 0, 0, 0, 0, 0],[0, 1, 3, 4, 0, 0],[0, 0, 0, 0, 0, 6],[0, 0, 1, 0, 0, 0],[0, 5, 0, 0, 6, 4]],
            "grid7":[[9, 0, 6, 0, 0, 1, 0, 4, 0],[7, 0, 1, 2, 9, 0, 0, 6, 0],[4, 0, 2, 8, 0, 6, 3, 0, 0],[0, 0, 0, 0, 2, 0, 9, 8, 0],[6, 0, 0, 0, 0, 0, 0, 0, 2],[0, 9, 4, 0, 8, 0, 0, 0, 0],[0, 0, 3, 7, 0, 8, 4, 0, 9],[0, 4, 0, 0, 1, 3, 7, 0, 6],[0, 6, 0, 9, 0, 0, 1, 0, 8]],
            "grid8":[[0, 0, 0, 2, 6, 0, 7, 0, 1],[6, 8, 0, 0, 7, 0, 0, 9, 0],[1, 9, 0, 0, 0, 4, 5, 0, 0],[8, 2, 0, 1, 0, 0, 0, 4, 0],[0, 0, 4, 6, 0, 2, 9, 0, 0],[0, 5, 0, 0, 0, 3, 0, 2, 8],[0, 0, 9, 3, 0, 0, 0, 7, 4],[0, 4, 0, 0, 5, 0, 0, 3, 6],[7, 0, 3, 0, 1, 8, 0, 0, 0]],
            "grid9":[[0, 3, 0, 4, 0, 0],[0, 0, 5, 6, 0, 3],[0, 0, 0, 1, 0, 0],[0, 1, 0, 3, 0, 5],[0, 6, 4, 0, 3, 1],[0, 0, 1, 0, 4, 6]],
            "grid10":[[0, 0, 0, 6, 0, 0, 0, 0, 0],[0, 0, 0, 0, 0, 0, 5, 0, 1],[3, 6, 9, 0, 8, 0, 4, 0, 0],[0, 0, 0, 0, 0, 6, 8, 0, 0],[0, 0, 0, 1, 3, 0, 0, 0, 9],[4, 0, 5, 0, 0, 9, 0, 0, 0],[0, 0, 0, 0, 0, 0, 3, 0, 0],[0, 0, 6, 0, 0, 7, 0, 0, 0],[1, 0, 0, 3, 4, 0, 0, 0, 0]],
            "grid11":[[8, 0, 9, 0, 2, 0, 3, 0, 0],[0, 3, 7, 0, 6, 0, 5, 0, 0],[0, 0, 0, 4, 0, 9, 7, 0, 0],[0, 0, 2, 9, 0, 1, 0, 6, 0],[1, 0, 0, 3, 0, 6, 0, 0, 0],[0, 0, 0, 0, 0, 0, 1, 0, 3],[7, 0, 0, 0, 0, 0, 0, 0, 8],[5, 0, 0, 0, 0, 0, 0, 1, 4],[0, 0, 0, 2, 8, 4, 6, 0, 5]],
            "grid12":[[0, 2, 0, 0, 0, 0, 0, 1, 0],[0, 0, 6, 0, 4, 0, 0, 0, 0],[5, 8, 0, 0, 9, 0, 0, 0, 3],[0, 0, 0, 0, 0, 3, 0, 0, 4],[4, 1, 0, 0, 8, 0, 6, 0, 0],[0, 0, 0, 0, 0, 0, 0, 9, 5],[2, 0, 0, 0, 1, 0, 0, 8, 0],[0, 0, 0, 0, 0, 0, 0, 0, 0],[0, 3, 1, 0, 0, 8, 0, 5, 7]]}

'''
This function takes the grids dictionary as argument to return a counter dictionary 
in the form {name: count} where name is the name of the grid and count is the empty cells.
'''

def find_empty(grids_dic):
    counter={}
    for name, grid in grids_dic.items(): # loop over each grid in the grids dictionary
        count=0
        for i in range(len(grid)): # loop over each row in the grid
            row = grid[i]
            for j in range(len(row)): # loop through each column in the row
                if grid[i][j] == 0:
                    count+=1 # if the cell is empty, increase the counter for empty cells by one
        counter[name]=count # store the count for this grid in the counter dictionary
    return counter



counters =find_empty(grids_dic) #call the function
'''
This function calculates the percentage of the difficulty on each grid 
based on the number of the empty cells in the grid to the number of the total cells
in the grid.
arguments:grids_dic, counters
it returns a dictionary in the form {name: difficulty percentage}
'''

def find_difficulty(grids_dic, counters):
    difficulty = {} #initialize a dictionary
    list_diif = [] #initialize a list to store the difficulty percentages of the grids
    for name, grid in grids_dic.items(): # loop through each grid in the grids dictionary
        count = counters[name] ## get the count of empty cells for the current grid
        size_grid = len(grid) * len(grid[0]) # calculate the total number of cells in the grid
        difficulty_per = round((count / size_grid)*100,2) # calculate the percentage of empty cells in the grid
        difficulty[name] = difficulty_per # store the difficulty percentage for the current grid in the difficulty dictionary
        list_diif.append(difficulty_per)
    return difficulty,list_diif

difficulty_levels,list_diif = find_difficulty(grids_dic,counters) #call the function


'''
This function calculalates the average tame of 10 trials of solving the soduku grids.
arguments: grids, n_trials
it returns a dictionary in the form {name: average time}
'''

def average_time(grids, n_trials):
    n_trials=10
    ave_times = {}
    for i, (grid, n_rows, n_cols) in enumerate(grids): # loop through each grid in the list
        t = 0
        for j in range(n_trials): # repeat the solving process for the same grid for the number of trials
            starting_time = time.time() # get the current time before starting to solve the grid
            recursive_solve(grid, n_rows, n_cols) # solve the grid 
            ending_time = time.time() # get the current time after finishing to solve the grid
            complete_time = ending_time - starting_time # calculate the time taken to solve the grid
            t += complete_time # add the time taken to the total time
            print("Solved in: %f seconds" % complete_time) # print the time taken to solve the grid
        average_time = t / n_trials # calculate the average time taken to solve the grid
        ave_times[i] = average_time # store the average time for this grid in the ave times dictionary
        print(f"Grid {i+1}: {average_time:.2f} seconds") # print the average time taken to solve the grid
    return ave_times

grids = [(grid1, 2, 2), (grid2, 2, 2), (grid3, 2, 2), (grid4, 2, 2), (grid5, 2, 2),
         (grid6, 2, 3), (grid7, 3, 3), (grid8, 3, 3), (grid9, 2, 3), (grid10, 3, 3), (grid11, 3, 3), (grid12, 3, 3)]


n_trials = 10 #number of trials
average_times = average_time(grids, n_trials) #call the function

for i, time in average_times.items():
    print(f"Grid {i+1}: {time:.2f} seconds")
    
time_average = []
for i, time in average_times.items(): # loop over each item in average times dictionary and store the average time in the time_average list
    time_average.append(time) #store the average time in the list






'''
This function plot the difficulty percenatges of the grids and the average times
taken to solve them.
arguments: list_diif, time_average, grids
it returns a Bar chart plot
'''

def profile(list_diif, time_average, grids):
    fig, ax = plt.subplots(figsize=(9, 8)) #set the size of the plot figure
    ax.set_title('Difficulty Percentage vs Average Time') #write the title of the plot
    
    # create bar plot for difficulty percentage
    x = list(range(len(list_diif))) #select the x-axis to be the numbers in the list diif while assigning to each grid a specific color
    colors = ['red', 'blue', 'green', 'orange', 'purple','pink','yellow','aqua','brown','gray','turquoise','crimson']
    bars = ax.bar(x, time_average, color=colors, alpha=0.5)

    # create legend for bar colors
    legend_labels = [f"{i+1}\n{grids[i][1]}x{grids[i][2]}" for i in range(len(grids))]
    ax.legend(bars, legend_labels)

    # set tick labels for x-axis
    ax.set_xticks(x)
    ax.set_xticklabels([f"{v}%" for v in list_diif])

    # set axis labels
    ax.set_xlabel('Difficulty Percentage')
    ax.set_ylabel('Average Time (s)')

    # create bar labels for time average
    for i, v in enumerate(time_average):
        ax.text(i, v, f"{v:.2f}", ha='center', va='bottom')

    # display plot
    fig.tight_layout()
    plt.show()



#call the function
profile(list_diif, time_average,grids)

