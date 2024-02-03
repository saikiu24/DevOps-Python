#selfish = 'me me me'
selfish = '01234567'
#01234567
#m 0
#e 1
#  2
#m 3
#e 7

# [start:stop]
print('m0e1 2m3')
# Will only get all the way to 3

# [start:stop:stepover]

# print(selfish[1:])
# 1234567

print('==========')
# [start=0:stop=4]
print(selfish[0:4]) #0123
print('==========')
# [start=0:stop=5]
print(selfish[:5]) #01234
print('==========')
# [start=0:stop=0:stepover=1]
print(selfish[::1]) #01234567
# [start:stop:stepover]
print(selfish[-3]) #5
print('==========')
# Stepping over from the back with stepover=1
print(selfish[::-1])
print('==========')
# Stepping over from the back with stepover=1
print(selfish[::-2])
print('==========')

for i in selfish:
    print(i)
    print('==========')
    if i == '1':
        print('WoW! This i is 1')
