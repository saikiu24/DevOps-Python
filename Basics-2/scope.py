'''
Scope - what variables do I have access to?
'''

'''
NameError: name 'name' is not defined
function scope
'''
'''
def some_func():
    total = 100

print(f'total: {total}')
'''

def some_func2():
    total = 100
    return total

total = some_func2()
print(f'total: {total}')