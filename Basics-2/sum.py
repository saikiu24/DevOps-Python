def sum(num1, num2):
    return num1 + num2

# Should do one thing really well.
# Should return something.

print(sum(2,8))

print(f'\n')
total = sum(10, 5)
print(sum(10, total))

print(f'\n')
def sum2(num1, num2):
    
    def another_func(num1, num2):
        return num1 + num2
    
    total = another_func(10, 10)
    return total

print(f'sum2(10, 10): {sum2(10, 10)}')