# map, filter, zip, reduce
from functools import reduce

# global [] = immutable
# No side-effects
my_list = [1,2,3]
your_list = [10, 20, 30]
their_list = [5, 4, 3]

# Accepting a list of data as item argument
def multiply_by2(item):
    
    return item * 2

# accept my_list (item) as an argument
# return odd numbers in the list only
def check_odd(item):
    
    return item % 2 != 0
        
def accumulator(acc, item):
    #print(1,2) => 3
    #print(3,3) => 6
    print(f'(acc, item): {(acc, item)}')
    return acc + item


# print(list(reduce(func, sequence, data))
# default acc = 0
print(f'reduce(accumulator, my_list, 0):\n{reduce(accumulator, my_list, 0)}')

