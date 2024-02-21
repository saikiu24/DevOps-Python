# sets = only values 
# unordered collection of unique objects
# No duplicates, every item = unique
my_set = {1,2,3,4,5}
print(f'my_sets: {my_set}') # {1, 2, 3, 4, 5}
# Adding 100 to my_sets
my_set.add(100) # This can add
my_set.add(2) # This cannot be added cuz NOT unique
print(f'my_sets: {my_set}')

my_list = [1,2,3,4,5,5]
# Converting my_list to a set
print(f'set(my_list): {set(my_list)}') # {1, 2, 3, 4, 5, 5}
#print(f'my_sets[0]: {my_sets[0]}') # TypeError: 'set' object does NOT support indexing
print(f'1 in my_set: {1 in my_set}') # True = 1 is in my_set
print(f'len(my_set): {len(my_set)}') # 5

# Copying from my_set to a new set
new_set = my_set.copy()
# Clearing out my_set after Copy
my_set.clear()
print(f'my_set: {my_set}')
print(f'new_set: {new_set}')