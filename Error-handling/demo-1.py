from colorama import Fore

def hoho():
    try:
        # TypeError
        #print(Fore.WHITE + 1 + f'hello')
        
        # ZeroDivisionError
        #print(Fore.WHITE + 5/0)
        
        # IndexError in []
        # li = [1,2,3]
        # li[5]
        
        # KeyError in {}
        dict = {'a': 1, 'b': 2}
        print(f'dict["c"]: {dict["c"]}')

    except TypeError as e:
        print(Fore.YELLOW + f'TypeError...\n{e}')
    
    except IndexError as e:
        print(Fore.YELLOW + f'IndexError...\n{e}')
    
    except KeyError as e:
        print(Fore.YELLOW + f'KeyError...\n{e}')
        
    except ZeroDivisionError as e:
        print(Fore.YELLOW + f'ZeroDivisionError...\n{e}')
    
hoho()