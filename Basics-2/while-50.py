i = 0
count = 0
break_condition = 'bye'

while 0 < 100:
    print(i)
    count += 1
    
    if (count == 50):
        print(f'count: {count}')
        print(f'this has looped for 50 times\nbreaking...')
        break
        
while True:
    response = input('Say something: ')
    
    if (response == break_condition):
        print(f'you\'ve entered: {break_condition}')
        print(f'exiting...')
        break