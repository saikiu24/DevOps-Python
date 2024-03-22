'''
@decorator

Adding extra functionalities to our functions

Higher order functions:
map()
filter()
reduce()
zip()
'''

def my_decorator(func): 
    def wrap_func():
        print(f'********')
        func()
        print(f'********')
    
    # NOT calling wrap_func
    # just returning wrap_func to global scope
    return wrap_func


'''
********
helloooooo
********
'''
#@my_decorator
def hello():
    print('helloooooo')

@my_decorator
def bye():
    print('see ya later')

hello()
print(f'\n')
my_decorator(hello)()
print(f'\n')
bye()

