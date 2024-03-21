'''
Scope - what variables do I have access to?

This is a very BAD function
'''

def outer():
    
    x = 'local'
    
    def inner():
        # nonlocal = hoisting in javascript
        # Jump up to parent scope
        # Grab any matching variables for x
        nonlocal x
        
        x = 'nonlocal'
        print(f'inner x: {x}')
    
    inner()
    
    print(f'outer x: {x}')

outer()
# inner x: nonlocal
# outer x: nonlocal

'''
1 - Start with local
2 - Parent local?
3 - Global
'''