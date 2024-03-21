'''
:=
Assigns values to variables as part of a larger expression.
It is affectionately known as "the Walrus operator" due to its
resemblance to the eyes and tusks of a Walrus.

n := len(a)
'''

a = 'hellooooooooooo'

if ((n := len(a)) > 10):
    print(f'too long {n} elements')

# while len(a) > 10
# remove last character from a
# util len(a) == 10
while ((n := len(a)) > 10):
    print(f'n: {n}')
    a = a[:-1]

print(a)