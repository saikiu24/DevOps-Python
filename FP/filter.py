# map, filter, zip, reduce


# global [] = immutable
# No side-effects
my_list = [1,2,3]

# Accepting a list of data as item argument
def multiply_by2(item):
    
    return item * 2

# accept my_list (item) as an argument
# return odd numbers in the list only
def check_odd(item):
    
    return item % 2 != 0
        

print(list(filter(check_odd, my_list))) # [1, 3]