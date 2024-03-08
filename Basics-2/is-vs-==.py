print(f'True == 1: {True == 1}') # True
print(f'True == bool(1): {True == bool(1)}')
print(f'"" == 1: {"" == 1}') # False
print(f'[] == 1: {[] == 1}') # False
print(f'10 == 10.0: {10 == 10.0}') # True
print(f'[] == []: {[] == []}') # True
print(f'bool([]): {bool([])}') # False
print(f'1 == 1: {"1" == 1 }') # False
print(f'bool("1"): {bool("1")}') # True
print(f'bool("0"): {bool("0")}') # True

print(f'True is 1: { True is 1 }') # False True is True
print(f'"1" is "1": {"1" is "1"}') # True

# Everytime we create a []
# this is a unique list in the memory location
# When we create another unique [] 
# this second [] is also in separate memory location
print(f'[] is []: { [] is [] }') # False

print(f'[1,2,3] is [1,2,3]: {[1,2,3] is [1,2,3]}') # False

a = [1,2,3] # a as a list [] is stored in its own memory location
b = [1,2,3] # b as a list [] is stored in its own memory location
print(f'a is b: { a is b }') # False

# Equality checks only check each list's elements' value
print(f'a == b: { a == b }') # True
