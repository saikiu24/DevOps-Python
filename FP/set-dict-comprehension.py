# list [] , set {} , dict { 'a': 'a', 'b': 'b' }

# set {} does NOT allow duplicated elements
my_list = {char for char in 'hello'}
my_list2 = {num for num in range(0,100)}

# list [] allows duplicated elements
my_list3 = [num ** 2 for num in range(0,100)]

my_list4 = {num ** 2 for num in range(0,100)
            if num % 2 == 0}

print(f'my_list4:\n{my_list4}')

print(f'\n')
simple_dict = {
    'a': 1,
    'b': 2    
}

# NOT affecting original dictionary {}
# { } = {key: value ** 2 for key, value in iterable}

my_dict = {key: value ** 2 for key, value in simple_dict.items()
           if value % 2 == 0} # only Even values being added to my_dict {}
print(f'simple_dict:\n{simple_dict}')
print(f'my_dict:\n{my_dict}')


print(f'\n')
list1 = [1, 2, 3]

my_dict2 = {num: num * 2 for num in list1}
print(f'my_dict2:\n{my_dict2}')