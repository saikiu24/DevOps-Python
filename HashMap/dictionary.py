hashMap = {
    "first_name": "naga",
    "last_name": "sai nikhil",
    "age": 21,
    3: 4
}

# Iterate through each key
# to get each key.value
for i in hashMap.keys():
    print(f'Iterating hashMap.key.values: ')
    print(hashMap[i])
    print('')
    print('')
    
print('========================')    
# x => hashMap.key
# y => hashMap.key.value

# Remove an Object key "age" in hashMap
hashMap.pop("age")
# Clear all keys
#hashMap.clear()

for x, y in hashMap.items():
    print(f'hashMap.key+" "+hashMap.key.value')
    # Integer cannot append to string
    # NOT using Type coersion
    # Use type conversion
    print(str(x)+" "+str(y))
    print('')
    print('')
    #print("key is {placeholder1}, value is {placeholder2}".format(x,y))
    #print("key is {}, value is {}".format(x,y))
    print(f'hashMap\nkey is {x}, value is {y}')


print('========================')
    

# print('')
# print(f'Lenght of {hashMap}: ', len(hashMap))

# Get keys of a hashMap Object only
# print('')
# print(f'hashMap.keys(): ', hashMap.keys())

# Gey key values only
# print('')
# print(f'hashMap.values(): ', hashMap.values())

# Get key items (Tuple) only
# print('')
# print(f'hashMap.items() in Tuple: ', hashMap.items())

# Get 1st key value
# print('')
# print(f'1st key value - hashMap["first_name"]: ', hashMap["first_name"])



