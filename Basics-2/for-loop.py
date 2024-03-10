# 'Zero to Master' = iterable to loop over
for item in 'Zero to Mastery':
    
    # print each letter on each line
    # 1 at a time
    print(f'{item}') 
    
print(f'\n')
# For loop a set { }
for item in {1, 2, 3, 4, 5}:
    print(f'{item}')
# 1
# 2 
# 3 
# 4
# 5
    
print(f'\n')
# For loop a tuple (1,2,3,4,5)
for item in (1,2,3,4,5):
    print(f'{item}')
# 1
# 2 
# 3 
# 4
# 5
    
print(f'\n')
# For loop a dictionary {a: 1, b: 2, c:3}
for item in (1,2,3,4,5):
    for x in ['a', 'b', 'c']:
        print(f'(item, x): {(item, x)}')