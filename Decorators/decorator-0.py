def hello():
    print(f'hellllllooooooooo')
    
greet = hello
del hello

try:
    print(f'hello():\n{hello()}')
except NameError as e:
    print(f'NameError:\n{e}')

print(f'\n')

try:
    print(f'greet():\n{greet()}')
except NameError as e:
    print(f'NameError:\n{e}')