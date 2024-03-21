# DRY
def say_hello():
    print(f'hellooooooo')
    
# call once
say_hello()

# Exercise!
picture = [
    [0,0,0,1,0,0,0],
    [0,0,1,1,1,0,0],
    [0,1,1,1,1,1,0],
    [1,1,1,1,1,1,1],
    [0,0,0,1,0,0,0],
    [0,0,0,1,0,0,0]
]

def show_tree():
    
    # Looping through each row in picture
    for row in picture:
        for pixel in row:
                
            if (pixel == 1):
                print(f'*', end='')
                    
            else:
                print(f' ', end='')
            
        # Print a new line at the end of each row
        print(f'')

show_tree()
show_tree()