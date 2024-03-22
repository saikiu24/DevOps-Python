
while True:
    try:
        age = int(input('What is your age? '))
        10/age
    
    except ValueError as e:
        print('ValueError...\nPlease enter a number')
        continue
    
    except ZeroDivisionError as e:
        print('ZeroDivisionError...\nPlease enter age > 0')
        continue
    
    else:
        print(f'age:\n{age}')
        break
        
    finally:
        print(f'ran once...')
    
    