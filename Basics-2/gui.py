# Exercise!
picture = [
    [0,0,0,1,0,0,0],
    [0,0,1,1,1,0,0],
    [0,1,1,1,1,1,0],
    [1,1,1,1,1,1,1],
    [0,0,0,1,0,0,0],
    [0,0,0,1,0,0,0]
]

#1 iterate over picture.
    # if 0 -> print ''
    # elif 1 -> print '*'

count = 0
# Printing 2 trees
while count < 2:
    # Looping through each row in picture
    for row in picture:
        # Looping through each pixel in 1 row
        for pixel in row:
            
            if (pixel == 1):
                print(f'*', end='')
                
            else:
                print(f' ', end='')
        
        # Print a new line at the end of
        # looping through all pixels of each row
        print(f'')
    
    # Printing 2 trees
    # Finish 1 loop of one single row
    count += 1
    
    if (count == 2):
        break

