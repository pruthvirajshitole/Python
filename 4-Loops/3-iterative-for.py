'''
Syntax:
for iterator in iterable:
    for body
    
list, tuple etc (iterables)
'''

# 1-iterate a list

print('-----------1------------')
l = [10,20,30,40,50]
for i in l:
    print(i)


# 2-iterate a tuple

print('-----------2------------')
t = (10,20,30,40,50)
for i in t:
    print(i)


# 3-iterate a set

print('-----------3------------')
s = {10,20,30,40,50}
for i in s:
    print(i)


# 4-iterate a dictionary

print('-----------4------------')
d = {'a':1, 'b':2, 'c':3}
for i,j in d.items():
    print(i,j)


# 5-iterate a string

print('-----------5------------')
s = 'hello'
for i in s:
    print(i)


print('---------Ex-1-----------')
l = [10,2,30,64,51,36,76,38,99]

# find even numbers in the list
for i in l:
    if i % 2 == 0:
        print('Even:',i)

# find odd numbers in the list
for i in l:
    if i % 2 != 0:
        print('Odd:',i)


print('---------Ex-2-----------')
l=[10,2,30,64,51,36,76,38,99]
even = []
odd = []

for i in l:
    if i % 2 == 0:
        even.append(i)
    else:
        odd.append(i)
print(f'''Even : {even}, Odd : {odd}''')





