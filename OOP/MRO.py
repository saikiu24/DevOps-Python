# MRO - Method Resolution Order
class A:
    num = 10

# class B inherits class A
class B(A):
    pass

class C(A):
    num = 1
    
class D(B, C):
    pass

print(f'D.num: {D.num}')

# Viewing Inheritance Chain using MRO
# # Inheritance chain D -> B -> C -> A
print(f'D.mro(): {D.mro()}')