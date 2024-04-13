# iterable
# generators
# range(100) = a generator
# a special type of thing to yield that pauses & resumes functions
print(list(range(100)))
print(f'\n')

def make_list(num):
    result = []
    
    # using range(parsedNum) to create a list
    # then append to empty result []
    for i in range(num):
        result.append(i * 2)
        
    # returning result to global memory
    return result

my_list = make_list(100)
print(f'my_list:\n{my_list}')

