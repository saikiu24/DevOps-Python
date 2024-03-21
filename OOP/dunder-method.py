class Toy():
    
    def __init__(self, color, age):
        self.color = color
        self.age = age
        self.my_dict = {
            'name': 'HoHo',
            'has_pets': False
        }
        
    '''
    define our own method
    e.g.
    modifying str() dunder method from Python str()
    
    __str__(self) = only change self.__str__
    does NOT affect Class.__str__
    '''
    def __str__(self):
        return f'{self.color}'
    
    def __len__(self):
        return 5
    
    def __call__(self):
        return('yess??')
    
    def __getitem__(self, i):
        return self.my_dict[i]
        
action_figure = Toy(color='red', age=0)

'''
dunder method = __method__()
'''
print(f'action_figure.__str__():\n{action_figure.__str__()}')
print(f'\n')
print(f'str(action_figure): {str(action_figure)}')
print(f'\n')

number1 = 100
number1 = str(number1)
print(f'str(number1): {str(number1)}') # 100
print(f'\n')
print(f'type(number1): {type(number1)}') # <class 'str'>
print(f'\n')
print(f'len(action_figure):\n{len(action_figure)}') # 5
print(f'\n')
print(f'action_figure.__call__():\n{action_figure.__call__()}') # yess?
print(f'\n')
print(f'action_figure["name"]:\n{action_figure["name"]}') # HoHo
print(f'\n')
print(f'action_figure["has_pets"]:\n{action_figure["has_pets"]}') # False