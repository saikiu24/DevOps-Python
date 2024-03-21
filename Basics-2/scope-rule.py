'''
Scope - what variables do I have access to?
'''

a = 1

def parent():
    a = 10
    
    def confusion():

        return a

    return confusion()


print(f'a: {a}') # 1
print(f'parent(): {parent()}') # 10

'''
1 - Start with local
2 - Parent local?
3 - Global
4 - built-in python functions
'''