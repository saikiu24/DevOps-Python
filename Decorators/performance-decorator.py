# Decorator
from time import time

# creating a higher function performance
# to wrap a func to accept *args, **kwargs
def performance(fn):
    
    # Thus we can pass as many params as possible
    def wrapper(*args, **kwargs):
        
        time1 = time()
        
        result = fn(*args, **kwargs)
        
        time2 = time()
        print(f'took time2-time1: {time2-time1} seconds')
        
        return result
    
    return wrapper
        

@performance
def long_time():
    
    for i in range(0, 1000000000):
        i * 5


long_time()