# Square
my_list = [5,4,3]

print(f'list(map(lambda item: item ** 2, my_list))')
new_list = list(map(lambda num: num ** 2, my_list))
print(f'new_list:\n{new_list}')


# List Sorting based on 2nd value
a = [(0,2), (4,3), (9,9), (10,-1)]

# a.sort(key='', reverse='')
a.sort(key=lambda x: x[1])
print(f'a:\n{a}')