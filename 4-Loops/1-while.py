'''
Syntax:

initialization
while condition:
    while-body
    incr/decr

'''

# 1-Simple while loop

print('-----------1------------')
i = 0         # initialization
while i<10:   # condition
    print(i)  # body
    i += 1    # increment


# 2-Simple while loop

print('-----------2------------')
i = 0         # initialization
while i<=10:   # condition
    print(i)  # body
    i += 1    # increment


# 3-numbers between 24 and 50

print('-----------3------------')
i = 0
while i<50:
    i += 1
    if i>24:
        print(i)


# 4-even numbers from 1 to 20

print('-----------4------------')
i = 1
while i <= 20:
    if i % 2 == 0:
        print(i)
    i += 1


# 5-odd numbers between 10 and 25

print('-----------5------------')
i = 10
while i <= 25:
    if i % 2 != 0:
        print(i)
    i += 1

# 6-numbers between 10 to 0

print('-----------6------------')
i = 10
while i >= 0:
    print(i)
    i -= 1

'''
i : iteratior
-------------------------------------
            iterations
i   condition   print(i)    inc/Depr
-------------------------------------
10T  i >= 0       10         i -= 1
9T   i >= 0       9          i -= 1
8T   i >= 0       8          i -= 1
7T   i >= 0       7          i -= 1
6T   i >= 0       6          i -= 1
5T   i >= 0       5          i -= 1
4T   i >= 0       4          i -= 1
3T   i >= 0       3          i -= 1
2T   i >= 0       2          i -= 1
1T   i >= 0       1          i -= 1
0F   i >= 0       0          i -= 1
'''


# 7-numbers between 50-25

print('-----------7------------')
i = 50
while i >= 25:
    print(i)
    i -= 1


# 8-even numbers between 50-25

print('-----------8------------')
i = 50
while i >= 25:
    if i % 2 == 0:
        print(i)
    i -= 1


# 9-even numbers between 50-25

print('-----------9------------')
i = 50
while i >= 25:
    if i % 2 != 0:
        print(i)
    i -= 1


    

        
