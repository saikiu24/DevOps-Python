some_list = ['a', 'b', 'c', 'b', 'd', 'm', 'n', 'n']

duplicates = []

for value in some_list:
    if some_list.count(value) > 1:
        if value not in duplicates:
            duplicates.append(value)
            
print(f'duplicates:\n{duplicates}')

print(f'\n')

# set(['b', 'b', 'n', 'n']) => {'b', 'n'}
# list({'b', 'n'}) => ['n', 'b']
my_list = list(set([element for element in some_list
        if some_list.count(element) > 1]))
print(f'my_list:')
print(my_list)
