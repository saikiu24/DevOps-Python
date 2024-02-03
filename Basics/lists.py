# Python Lists are Arrays
list1 = [1,2,3,4,5]
list2 = ['a','b','c']
# Tuples
list3 = [1,2,'a', True]

# Data Structure
cart = ['notebooks', 'sunglasses']
print(f'In Cart cart[1]: {cart[1]}')

# List slicing
cart2 = [
    'notebooks',
    'sunglasses',
    'toys',
    'grapes'
    ]
# Printing first 2 items in cart2 only
# [start:stop:stepover]
print(f'cart2[0:2]: {cart2[0:2]}')

# Mutating an item in cart2
# List slicing
new_cart = cart2[0:3]
new_cart[0] = 'laptop'
print(f'cart2: {cart2}')
print(f'new_cart: {new_cart}')

# This will mutate the original cart list
# Because of Memory Pass-by-Reference
# Mutating Lists are copied via Shallow Copy
# Can do Deep Copy via new_cart = JSON.PARSE(JSON.STRINGIFY(object))
new_cart = cart2
new_cart[0] = 'gum'
print(f'new_cart: {new_cart}')
print(f'cart2: {cart2}')
