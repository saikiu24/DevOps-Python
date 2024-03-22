# Error Handling
from colorama import Fore

def check_age():
    while True:
        try:
            age = int(input('What is your age? '))
            10/age
            print(Fore.WHITE + f'age: {age}')
            print(f'\n')

        except ValueError as e:
            print(Fore.YELLOW + f'ValueError...\n{e}')
            print(Fore.YELLOW + f'Please enter a number')
            print(f'\n')
            
        # 
        except ZeroDivisionError as e:
            print(Fore.YELLOW + f'ZeroDivisionError...\n{e}')
            print(Fore.YELLOW + f'Please enter age > 0')
            print(f'\n')

        else:
            print(f'Thanks')
            break

#check_age()
    

def sum():
        
    while True:
        try:
            num1 = input('Please enter num1: ')
            num2 = input('Please enter num2: ')
    
            num1 = int(num1)
            num2 = int(num2)
            
            total = num1 + num2
            10/total     
            
            print(Fore.WHITE + f'total: {total}')
        
        except (ValueError, ZeroDivisionError, TypeError) as e:
            print(Fore.YELLOW + f'Error...\n{e}')
            print(f'\n')
                    
        else:
            print(Fore.WHITE + f'Done')
            break
            
        finally:
            print(Fore.WHITE + f'Thanks')
        
sum()
    
    
    