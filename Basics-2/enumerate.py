# we must give something to enumerate()
# to iterate over

# enumerate() is special
# it gives you an index, each element
# i, char

# enumearting a string
print(f'enumerating a string')
for i, char in enumerate('Helloooo'):
    print(i, char)
    #print(f'(i, char):\n{(i, char)}')
    
print(f'enumerating a list []')
# enumerating a list / array in javascript [] 
for i, char in enumerate([1,2,3]):
    print(i, char)
    #print(f'(i, char):\n{(i, char)}')
    
# enumerating a tuple ()
print(f'enumerating a tuple()')
for i, char in enumerate((1,2,3)):
    print(i, char)
    #print(f'(i, char):\n{(i, char)}')

# enumerating a list of range(100)
print(f'enumerating a list of range(100)')
print(f'Finding index of 50')
for i, char in enumerate(list(range(100))):
    print(i, char)
    
    if (char == 50):
        print(f'index of 50 is: {i}')