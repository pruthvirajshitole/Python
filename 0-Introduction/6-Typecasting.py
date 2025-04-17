 
a = 1  # input possible as str: int,float,str
b = 2
c = a+b #12 (concatenation)
print(c)

'''
Type casting : Converting data from one type to another type

Types:
    1- Implicit casting: The Python interpreter automatically performs an
                        implicit Type conversion, which avoids loss of data.
    2- Explicit casting:The explicit type conversion is performed by the
                        user using built-in functions.
'''


print('------implicit casting------')
a = 3
b = 4.0
print(f'{a}: {type(a)}, {b}: {type(b)}')
c = a+b
print(f'{c}: {type(c)}')


print('------explicit casting------')
a = 3
b = 4.0
print(f'{a}: {type(a)}, {b}: {type(b)}')
c = a+b
c = int(c)  # explicit casting
print(f'{c}: {type(c)}')