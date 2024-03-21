def highest_even(li):
    
    highest_even = 0
    
    for item in li:
        if (item > highest_even) and (item % 2 == 0):
            highest_even = item
    
    return highest_even

print(f'highest_even([10,2,3,4,8,11]): {highest_even([10,2,3,4,8,11])}')


def highest_even2(li):
    
    # Preparing to store even items using an empty list / array
    evens = []
    
    # Looping through each item in passed in [] as li
    for item in li:
        
        # if remainder of 2 == 0 => even
        if item % 2 == 0:
            # append that item to evens []
            evens.append(item)
        
    # after looping through
    # return max in evens []
    return max(evens)

print(highest_even2([10,2,3,4,8,11]))