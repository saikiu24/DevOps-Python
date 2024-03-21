class SuperList(list):
    
    def __len__(self):
        return 1000
        
    
super_list1 = SuperList()
super_list1.append(5)

print(f'len(super_list1):\n{len(super_list1)}')
print(f'\n')
print(f'super_list1[0]: {super_list1[0]}') # 5
print(f'\n')
print(f'issubclass(list, object):\n{issubclass(list, object)}')