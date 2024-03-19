# range(0, 100) => NOT tuple
print(range(100))

for number in range(0, 101):
    print(f'number: {number}')
    # printing each number: 0
    # printing each number: ...
    # printing each number: 100
    
# Using _ cuz not caring about itself
# just loop 0 to 100
for _ in range(0, 101):
    print(f'_: {_}')
    # _: 0
    # _: ...
    # _: 100
    
# for _ in range(start, end, stepover):
for _ in range(0, 101, 2):
    print(f'_: {_}')
    # _: 0
    # _: 2
    # _: 4
    # _: ...
    # _: 98
    # _: 100
    
# going from opposite direction
# Must specify stepover to go for a Reverse Loop
for _ in range(10, 0, -2):
    print(f'_: {_}')
    # _: 10
    # _: 8
    # _: ...
    # _: 2
    
    print(f'list(range(10)): {list(range(10))}')
    # _: 10 => [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    # _: 8 => [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    # _: 6 => [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    # _: 4 => [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    # _: 2 => [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]