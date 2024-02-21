my_set = {1, 2, 3, 4, 5}
your_set = {4, 5, 6, 7, 8, 9, 10}

# {1, 2, 3}
print(f'my_set.difference(your_set):\n{my_set.difference(your_set)}')

# .discard()
print(my_set.discard(5)) # None
print(my_set) # {1, 2, 3, 4}

# .difference_update()
# .intersection()
# .isdisjoint()
# .issubset()
# .issuperset()
# .union()