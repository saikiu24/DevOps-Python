# list unpacking
basket = [1,2,3,4,5,6,7,8,9]

a,b,c, *others, d = basket
print(f'a: {a}') # 1
print(f'b: {b}') # 2
print(f'c: {c}') # 3

# Unpacking all elements
print(f'others: {others}') # [4, 5, 6, 7, 8]
print(f'd: {d}') # 9
