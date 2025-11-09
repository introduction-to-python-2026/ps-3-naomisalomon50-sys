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
    index_of_one = my_list.index(1)
    the_pig_location = [1, 0, 0, 0]
    if direction == 'left':
        if my_list[index_of_one] == 0:
            print(the_pig_location)

# Test when the `1` is at the right edge
the_pig_location = [0, 0, 0, 0, 1]
direction = 'right' or 'left'
index_of_one = the_pig_location.index(1)

if direction == 'right':
  if index_of_one == -1:
   print(the_pig_location)


