# OOP
from colorama import Fore, Back, Style

# private?
class PlayerCharacter:
    
    # Class Object Attribute => self.attribute
    # NOT change across objects built with same Class
    membership = True
    
    # __ => Do NOT fuck with my stuff ;) thanks
    
    # __init__ = class Constructor
    # similar to constructor(attr1, attr2) { super(attr1) } in javascript
    # __init__ is called whenever we instantiate a Class
    # self refers to this Class itself as PlayerCharacter
    # self. = this. in javascript
    def __init__(self, name='anonymous', age=0):  
        # name='anonymous', age=0 => default values
                
        # Instantiating only if age > 18
        if (age > 18):
            
            # _.variable => Do NOT fuck with my vairable thanks ;)
            self._name = name
            self._age = age
        elif (age == 0):
            print(Fore.RED + f'Failed to instantiate this Class with {self}:\nname: {name}\nage: {age}')
            print(Fore.RED + f'Please check whether you\'ve provided age')
        
            
        # If this.membership = True
        if (self.membership):
            self._name = name # attributes / properties
            self._age = age # attributes / properties
        
    # Instantiating Class with self (this)
    def run(self, hello):
        print(f'{hello} {self._name} is running :D')
        return 'done'
    
    def shout(self):
        print(Fore.YELLOW + f'My name is: {self._name}')
        
    def speak(self):
        print(f'my name is {self._name}, and I am {self._age} years old')
    
    # Decorator
    # to write a function
    # using @classmethod => you'll have access to cls (Class)
    # @classmethod is commonly used when we wanna track & change
    # Class.Attributes => self.name, self.age etc.
    @classmethod
    def adding_things(cls, num1, num2):
        try:
            # Instantiate an Object using cls(name, age)
            # player1.adding_things(): <__main__.PlayerCharacter object at 0x0000019E072F5E50>
            return cls('Teddy', num1 + num2)
        
        except TypeError as e:
            print(Fore.RED + f'TypeError:\n{e}')
    
    # Decorator
    # to write a function
    # using @staticmethod => you'll NOT have access to cls (Class)
    # @staticmethod is commonly used when we do NOT care
    # about Class States => self.name, self.age etc.
    # using @staticmethod when NOT gonna change self.attributes
    @staticmethod
    def adding_things2(num1, num2):
        try:
            # when using @staticmethod
            # cannot be used to access cls (Class)
            return num1 + num2
        except TypeError as e:
            print(Fore.RED + f'TypeError:\n{e}')
        

# Instantiating player1 using class PlayerCharacter
# with default values
player1 = PlayerCharacter('Player1', 20)
#help(player1)
print(Fore.YELLOW + f'player1:\n{player1}')
print(Fore.YELLOW + f'player1.name: {player1._name}') 
print(Fore.YELLOW + f'player1.age: {player1._age}')
print(f'\n')
print(f'player1.speak()')
player1.speak()
print(f'\n')
print(Fore.YELLOW + f'player1.run(): {player1.run("OMG!")}')

player1.name = '!!!'
player1.speak = 'BOOOO'


'''
If everyone keeps doing things like this
The world is gonna end
Cuz everyone's hard work will get totally wiped out...
'''
print(player1.speak) # BOOO