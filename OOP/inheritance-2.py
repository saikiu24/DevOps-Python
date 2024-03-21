'''
users
 - Wizards
 - Archers
 - Orges
'''

class User():

    '''
    if do NOT use __init__
    '''
    def sign_in(self):
        print(f'{self} logged in')        
        
        
# inheriting class User()
class Wizard(User):
    
    def __init__(self, name, power):
        self.name = name
        self.power = power
        
    def attack(self):
        print(f'{self.name} is attacking with power of {self.power}')

# inheriting class User()
class Archer(User):
    def __init__(self, name, num_arrows):
        self.name = name
        self.num_arrows = num_arrows
        
    def attack(self):
        print(f'{self.name} is attacking with arrows: arrows left- {self.num_arrows}')
        

wizard1 = Wizard('Shi Ro', 50)
archer1 = Archer('Red A', 100)
# wizard1.sign_in()
# wizard1.attack()
# archer1.attack()

'''
isinstance(instance, Class)
'''
print(f'\n')
print(f'isinstance(wizard1, Wizard):\n{isinstance(wizard1, Wizard)}')
print(f'\n')
print(f'isinstance(wizard1, object):\n{isinstance(wizard1, object)}')

# both objects below inherit __repr__ from Python object-based Class
[].__repr__
wizard1.__repr__