# map, filter, zip, reduce

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
        
# Zipping 2 lists together
print(list(zip(my_list, your_list))) # [(1, 10), (2, 20), (3, 30)]
print(f'\n')
print(list(zip(my_list, your_list, their_list))) # [(1, 10, 5), (2, 20, 4), (3, 30, 3)]