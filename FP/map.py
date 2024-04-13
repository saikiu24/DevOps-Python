# map, filter, zip, reduce


# global [] = immutable
# No side-effects
my_list = [1,2,3]

# Accepting a list of data as item argument
def multiply_by2(item):
    
    return item * 2

#print(map(multiply_by2, [1,2,3])) # <map object at 0x000001FD094671F0>
print(f'my_list:\n{my_list}')
print(f'\n')
print(f'list(map(multiply_by2, my_list)):\n{list(map(multiply_by2, my_list))}') 
# [2, 4, 6]