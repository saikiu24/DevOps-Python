wizard = {
    'name': 'Wizard1',
    'power': 50
}
              

def multiply_by2(li):
    
    new_list = []
    
    for item in li:
        new_list.append(item * 2)
    
    print(f'li:\n{li}')
    print(f'\n')
    print(f'new_list:\n{new_list}')
       
    # returning something => adding stuff to global scope 
    return new_list

    
multiply_by2([1,2,3])