selfish = '01234567'

# String slicing
# selfish[start:stop:stepover]

# Immutability
# String in Python are Immutable = Cannot be changed

# This will work
selfish = 100
print(selfish)

selfish = '01234567'
# This does NOT work
#selfish[0] = '8'

# This works
selfish += '8'
print(selfish)