# Formatted strings
name = 'Johnny'
age = 55

print(f'Hi! {name}. You\'re {age} years old')
print(f'\n\n')

# .format
print('Hi {}. You\'re {} years old'.format(name, age))

print(f'\n\n')

# specific order
print('Hi {new_name}. You\'re {age} years old'.format(new_name='Sally', age=70))