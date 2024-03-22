# hello(func) accepts any another functions
def hello(func):
    func()
    
def greet():
    print(f'hellooooo')
    
#del hello

a = hello(greet)

print(a)

'''
@decorator 
supercharge functions
'''