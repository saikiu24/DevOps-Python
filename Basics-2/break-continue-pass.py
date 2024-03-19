my_list = [1,2,3]

for item in my_list:
    print(f'item: {item}')
    #break
    # break = Break current enclosing loop
    
    # continue = Continue on the top of enclosing loop
    # anything below continue will NOT be run
    continue


print(f'\n')
print(f'while loop')
i = 0
while i < len(my_list):
    print(f'my_list[i]: {my_list[i]}')
    i += 1
    break

# pass = Add a pass to at least pass something
# so Python does NOT bug us
# e.g. We wanna think logic about while loop first
# thus we leave 'pass' in the for loop
for item in my_list:
    pass

i = 0
while i < len(my_list):
    print(f'my_list[i]: {my_list[i]}')
    i += 1
    break