'''
Scope - what variables do I have access to?
'''

a = 10

def confusion(b):
    print(f'b: {b}')
    
    a = 90

confusion(300) # 300

total = 0

def count():
    
    # using global to access global scope variables
    global total 
    
    total += 1
    return total

total = count()
print(f'total: {total}') # UnboundLocalError: local variable 'total' referenced before assignment

'''
1 - Start with local
2 - Parent local?
3 - Global
4 - built-in python functions
'''