this_dict = {1:[3,4], 'fred':[5], ('little','shit'): [5,9,10]}

this_dict =  {(0, 1): {3, 4}, (0, 2): {3, 4}, (1, 0): {2, 3, 4}, (1, 1): {2, 3, 4}, (1, 3): {3}, (2, 0): {2, 3}, (2, 2): {2, 3}, (3, 0): {2, 3, 4}, (3, 1): {2, 3, 4}, (3, 2): {2, 3}}


def min_dict(dictionary):
    """
    converts 'set' to 'list'
    returns the item in a dictionary with the least amount of values.
    
    arguments: dictionary
    output: dictionary item in the form {tuple:list}

    """
    values = list(dictionary.values())
    shortest = values[0]
    counter = 1

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
    
    
    item_at_index = list(dictionary.items())[index]
    
#     print('min dict = ', min_dict)
#     print(item_at_index)
    return item_at_index
    
min_dict(this_dict)




