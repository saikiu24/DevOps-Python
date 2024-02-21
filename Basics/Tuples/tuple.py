# Tuples are Immutable Lists
my_tuple = (1,2,3,4,5,5)
x = my_tuple[0]
y = my_tuple[1]
z = my_tuple[0:2]
print(f'x: {x}\ny: {y}\nz:{z}')
# Immutable = Cannot modify 2nd item in my_tuple
#my_tuple[1] = 'z'

print(f'\ndict_items:\n{5 in my_tuple}\n') # True

user = {
    'basket': [1,2,3],
    'greet': 'hello',
    'age': 20
}

print(user.items()) # dict_items([('basket', [1, 2, 3]), ('greet', 'hellow'), ('age', 20)])

x,y,z, *other = (1,2,3,4,5)
print(f'\n')
print(f'x:{x}\ny:{y}\nz:{z}\nother:{other}')
print(f'\n')

# Tuple method
# .count()
# .index()
# my_tuple = (1,2,3,4,5,5)
print(f'my_tuple.count(5): {my_tuple.count(5)}') # 2
print(f'my_tuple.index(5): {my_tuple.index(5)}') # 4
print(f'len(my_tuple): {len(my_tuple)}') # 6