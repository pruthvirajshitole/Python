'''
Syntax:

for iterator in range(initialization, condition, incr/decr)
    for body
'''

# 1-Numbers from 0 to 10

print('-----------1------------')
for i in range(11):
    print(i)


# 2-Numbers from 1 to 10

print('-----------2------------')
for i in range(1, 11):
    print(i)


# 3-Numbers from 0 to 10 with a step of 2

print('-----------3------------')
for i in range(0,11,2):
    print(i)


# 4-Numbers from 10 to 20

print('-----------4------------')
for i in range(10,21):
    print(i)


# 5-Even numbers between 10-20

print('-----------5------------')
for i in range(10,21):
    if i % 2 == 0:
        print(i)


# 6-Odd numbers between 10-20

print('-----------6------------')
for i in range(10,21):
    if i % 2 != 0:
        print(i)


# 7-Numbers between 10-0

print('-----------7------------')
for i in range(10,-1,-1):
    print(i)


# 8-Numbers between 50-25

print('-----------8------------')
for i in range(50,24,-1):
    print(i)


# 9-Even numbers between 20-10

print('-----------9------------')
for i in range(20,9,-1):
    if i % 2 == 0:
        print(i)


# 10-Odd numbers between 50-25

print('-----------10-----------')
for i in range(50,24,-1):
    if i % 2 != 0:
        print(i)