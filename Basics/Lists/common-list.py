basket = ['a', 'x', 'b', 'c', 'd', 'e', 'd']

print(f'basket: {basket}')
print(f'\n')

basket.sort() # a b c d d e x
basket.reverse()

print(f'basket: {basket}') # x e d d c b a
print(f'\n')
print(f'basket[:]: {basket[:]}')
print(f'\n')

# This creates a new list
new_list = basket[::-1]

print(f'new_list: {new_list}') # a b c d d e x
print(f'\n')

print(f'range(1,100): {range(1,101)}')
print(f'\n')
print(f'list(range(1,100)):\n{list(range(1,101))}')
print(f'\n')

sentence = ' '

# This creates a new sentence for us
new_sentence = sentence.join(['hi', 'my', 'name', 'is', 'JO JO'])
print(f'sentence: {sentence}') # !
print(f'\n')

# hi my name is JOJO
print(f'new_sentence: {new_sentence}') 