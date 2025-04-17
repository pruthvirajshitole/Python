# swapping values with temporary variable
print('----swapping values with temporary variable-----')
a = 5
b = 2
c = 0
print(f'before swapping a = {a}, b = {b}')

c = a  # a=5 b=2 c=5
a = b  # a=2 b=2 c=5
b = c  # a=2 b=5 c=5
print(f'after swapping a = {a}, b = {b}')


# swapping values using operator
print('----swapping values using operator----')
a = 5
b = 2
print(f'before swapping a = {a}, b = {b}')
a = a + b  # a=7, b=2

b = a-b  # a=7, b=5
a = a-b 

print(f'after swapping a = {a}, b = {b}')


# swapping values wihtout operator and temporary variable    
print('----swapping values wihtout operator and temporary variable----')
a = 5
b = 2
print(f'before swapping a = {a}, b = {b}')

a,b = b,a
print(f'after swapping a = {a}, b = {b}')