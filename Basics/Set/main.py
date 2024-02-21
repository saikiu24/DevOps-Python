my_set = {1, 2, 3, 4, 5}
your_set = {4, 5, 6, 7, 8, 9, 10}

# {1, 2, 3}
print(f'my_set.difference(your_set):\n{my_set.difference(your_set)}')

# .discard()
# .discard() remove an item from my_set if it's a member
#print(my_set.discard(5)) # None
#print(my_set) # {1, 2, 3, 4}
print(f'\n')

# .difference_update()
#print(my_set.difference_update(your_set)) # None
#print(f'my_set: {my_set}')# {1,2,3}
# .intersection()
print(f'\n')

# Printing common elements in my_set, your_set
#print(my_set.intersection(your_set)) # {4,5}
#print(my_set & your_set) #{4,5}

print(f'\n')
# .isdisjoint()
print(f'\n')

#print(my_set.isdisjoint(your_set)) # False => Cuz my_set & your_set have common elements {4,5}
# .issubset()
print(f'\n')

# .issuperset()
# .union()
print(f'\n')

# Combining another set & Creating a new set
#print(my_set.union(your_set)) # {1,2,3,4,5,6,7,8,9,10}
print(my_set | your_set) # {1,2,3,4,5,6,7,8,9,10}