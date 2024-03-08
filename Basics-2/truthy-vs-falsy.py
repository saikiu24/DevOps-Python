is_old = bool('hello')
is_licenced = bool(5)

print(f'bool("hello"): {bool("hello")}') # True
print(f'bool(5): {bool(5)}') # True
print(f'\n')
print(f'bool(""): {bool("")}') # False
print(f'bool(0): {bool(0)}') # False
print(f'bool(None): {bool(None)}')
print(f'\n')

# Truthy and Falsy

if is_old and is_licenced:
    
    print(f'you are old enough to drive, and you have a licence!')
    
else:
    
    print(f'you are not of age!')
    print(f'\n')
    print(f'okokok')