# *args **kwargs

# *args = accept as many arguments as possible
#def super_func(*args):

# def super_func(args):
    #print(args)
    #return sum(args)
    
#super_func(1,2,3,4,5) # () takes 1 positional arguments but 5 were given

#print(super_func(1,2,3,4,5)) # 15

def super_func(*args, **kwargs):
    #print(args) # (1, 2, 3, 4, 5)
    print(kwargs)
    
    total = 0
    
    for item in kwargs.values():
        print(f'item: {item}')
        total += item
        
    return sum(args) + total # 15 + 15

# Rule: params, *args, default parameters, **kwargs
# **kwargs => num1, num2
print(super_func(1,2,3,4,5, num1=5, num2=10))
