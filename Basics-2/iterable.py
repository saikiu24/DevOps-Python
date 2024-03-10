# For loop a dictionary {a: 1, b: 2, c:3}
#for item in (1,2,3,4,5):
    #for x in ['a', 'b', 'c']:
        #print(f'(1, "c"): {(1, "c")}')
        #print(f'\n')
        #print(f'(item, x): {(item, x)}')
        
# iterable - list, dictionary, tuple, set, string
# iterated -> 1 by 1 check each item in the collection
user = {
    'name': 'Golem',
    'age': 5006,
    'can_swim': False
}

for item in user:
    print(f'item: {item}')
    #item: name
    #item: age
    #item: can_swim


print(f'\n')
# Get value pair in tuples
print(f'Getting dictionary key: value pair shown in tuples')
for item in user.items():
    
    # dictionary unpacking
    # HashMap destructuring in Javascript
    key, value = item
    print(f'(key, value): {(key, value)}')
    
    print(f'item: {item}')
    print(f'\n')
    
    #item: ('name', 'Golem')
    #item: ('age', 5006)
    #item: ('can_swim', False)
    

print(f'\n')
# Getting dictionary keys shown in tuples
print(f'Getting dictionary keys shown in tuples')
for item in user.keys():
    print(f'item: {item}')
    
    #item: ('name', 'Golem')
    #item: ('age', 5006)
    #item: ('can_swim', False)
    

print(f'\n')
# Getting dictionary values shown in tuples
print(f'Getting dictionary values shown in tuples')
for item in user.values():
    print(f'item: {item}')
    
    #item: ('name', 'Golem')
    #item: ('age', 5006)
    #item: ('can_swim', False)
