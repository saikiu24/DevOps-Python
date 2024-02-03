name = 'Jedi'
age = 1000
relationship_status = 'single'
relationship_status = 'it\'s complicated'

print(f'relationship_status: ', relationship_status)

birth_year = input(f'What year were you born? [yyyy]: ')
age = 2024 - int(birth_year)
print(f'Your age is: {age}')