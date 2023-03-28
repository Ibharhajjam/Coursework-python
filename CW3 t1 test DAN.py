#the aim here is to build a giant matrix with all possible options in a big nes
#ted list. or maybe a dictionary type situation
# can you have lists with dictionaries? yes.

grid2 = [
		[1, 0, 4, 2],
		[4, 2, 1, 3],
		[2, 1, 0, 4],
		[3, 4, 2, 1]]

grid5 = [
		[1, 0, 0, 2],
		[0, 0, 1, 0],
		[0, 1, 0, 4],
		[0, 0, 0, 1]]




def find_set(grid, row, col):
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



def generate_options(grid):
    this_dict = {}
    for f in range(4):
        for g in range(4):
            if grid[f][g] == 0:
                row = f
                col = g
                options = find_set(grid, f, g)
                print('row =', f, 'col =', g, 'options=', options)
                key = [f,g]
                value = options
                this_dict[f, g] = value
    print('this_dict = ', this_dict)
    print('length of dictionary:', len(this_dict))
    print(this_dict.values())
    
generate_options(grid5)

            
#ok so I have successfully created a program that finds all zeroes and all candidates.
#next is to alter the recursive code so that it prioritises the zero with the least
#candidates. Now, i'm not very sure as to how to do this. but I'll try some time tomorrow

            
            
            






