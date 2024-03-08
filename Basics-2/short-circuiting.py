# Short Circuiting

is_Friend = True
is_User = True

# True
print(f'is_Friend and is_User: {is_Friend and is_User}')
print(f'\n')


if is_Friend and is_User:
    print(f'best friends forever')


print(f'\n')    
print(f'"a" > "b": {"a" > "b"}') # False
print(f'\n')
print(f'"a" > "A": {"a" > "A"}') # True
print(f'\n')
print(f'1 < 2 > 3 < 4: {1 < 2 > 3 < 4}') # False
print(f'\n')

print(f'not(True): {not(True)}')
print(f'\n')