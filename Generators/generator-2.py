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