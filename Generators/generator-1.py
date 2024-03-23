# iterable
# generators

def generator_function(num):
    for i in range(num):
        # pause the func
        # if 'keep going' is told => keep going
        yield i * 2

g = generator_function(100)
print(g)
'''
<generator object generator_function at 0x000001BA03E698A0>
'''

next(g) # 2
next(g) # 4
print(next(g)) # 4




# for item in generator_function(1000):
#     print(f'item: {item}')


'''
def make_list(num):
    result = []
    
    for i in range(num):
        result.append(i * 2)
    
    return result


my_list = make_list(100)
'''

