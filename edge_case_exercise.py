def move(my_list, direction):

    # Finds the index of the one in the list
    index_of_one = my_list.index(1)

    # Move the one to the left or to the right
    if direction == 'right':
        my_list[index_of_one] = 0
        my_list[index_of_one + 1] = 1

    elif direction == 'left':
        my_list[index_of_one] = 0
        my_list[index_of_one - 1] = 1

    return my_list
    
def move(my_list, direction):
    index = my_list.index(1)

    if direction == 'left':
        if index > 0:
            my_list[index], my_list[index - 1] = my_list[index - 1], my_list[index]
    elif direction == 'right':
        if index < len(my_list) - 1:
            my_list[index], my_list[index + 1] = my_list[index + 1], my_list[index]

    return my_list


