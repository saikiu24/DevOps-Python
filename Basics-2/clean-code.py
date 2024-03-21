# clean code
def is_odd_or_even(num):
    if (num % 2 == 0):
        print(f'{num} is even')
        
    elif (num % 2 != 0):
        print(f'{num} is odd')
        
def is_even(num):
    return num % 2 == 0
    
is_odd_or_even(21757789)

print(f'\n')

print(is_even(222222))
