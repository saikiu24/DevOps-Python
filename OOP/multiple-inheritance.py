class User():
    def __init__(self, email):
        self.email = email
        print(f'init complete')
    
    def sign_in(self):
        print(f'{self.email} logged in')


class Wizard(User):
    
    def __init__(self, name, power):
        self.name = name
        self.power = power
    
    def attack(self):
        print(f'{self.name} is attacking with power: {self.power}')


class Archer(User):
    
    def __init__(self, name, arrows):
        self.name = name
        self.arrows = arrows
        
    def check_arrows(self):
        print(f'{self.arrows} arrows remaining')
        
    def run(self):
        print(f'{self.name} ran really fast')
        

# Create a new class based on class Wizard & class Archer
class HybridBorg(Wizard, Archer):
    
    # consolidating all inheritance from class Wizard, Archer
    def __init__(self, name, power, arrows):
        self.name = name
        self.power = power
        self.arrows = arrows


hybridBorg1 = HybridBorg(name='Player1', power='Sleeping', arrows=100)
hybridBorg1.run()
hybridBorg1.attack()
hybridBorg1.check_arrows()