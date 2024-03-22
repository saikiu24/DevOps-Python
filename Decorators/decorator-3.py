#Decorator

def my_decorator(func):
    def wrap_func(*args, **kwargs):
        print(f'*********')
        func(*args, **kwargs)
        print(f'*********')
    
    return wrap_func

@my_decorator
def hello(greeting='Hi', emoji=':('):
    print(f'greeting:\n{greeting} {emoji}')
    
a = my_decorator(hello)


'''
*********
greeting:
Hi There! Yo! :D
*********
'''
hello('Hi There!', 'Yo! :D') 