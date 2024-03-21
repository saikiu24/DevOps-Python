class User():

    def __init__(self, email):
        self.email = email
        
    '''
    if do NOT use __init__
    '''
    def sign_in(self):
        print(f'{self} logged in')  
    
    def attack(self):
        print(f'{self} do nothing')
        
        
# inheriting class User()
class Wizard(User):
    
    def __init__(self, name, power, email):
        
        # super() = class User => 1 class over Wizard
        #super().__init__(self, email)
        self.name = name
        self.power = power
        self.email = email
        
    def attack(self):
        User.attack(self)
        print(f'{self.name} is attacking with power of {self.power}')

# inheriting class User()
class Archer(User):
    def __init__(self, name, num_arrows, email):
        self.name = name
        self.num_arrows = num_arrows
        self.email = email
        
    def attack(self):
        User.attack(self)
        print(f'{self.name} is attacking with arrows: arrows left- {self.num_arrows}')
        

wizard1 = Wizard(name='Shi Ro', power='Unlimited Blade Works', email='ShiRo@gmail.com')
#print(wizard1.sign_in())
print(f'wizard1.name:\n{wizard1.name}')
print(f'\n')
print(f'wizard1.email:\n{wizard1.email}')
print(f'\n')
print(f'wizard1.power:\n{wizard1.power}')

#archer1 = Archer('Red A', 100)