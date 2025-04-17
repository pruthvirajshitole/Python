'''
Nested if-else:
    if we create conditional(if or if-else)
    in side if or else or in if and else
'''
# 1-Greatest of three numbers

print('-----------1------------')
a = 4
b = 3
c = 2

if a>b:  
    if a>c:  # a>b, a>c, so a is the greatest
        print("a is greatest")
    else:  # a>b, c>a, so c is the greatest
        print("c is greatest")
else: # b>a
    if b>c:  # b>a, b>c, so b is the greatest
        print("b is greatest")
    else:  # b>a, c>b, so c is the greatest
        print("c is greatest")


# 2-Smallest of three

print('-----------2------------')
a = 44
b = 32
c = 126

if a<b:  
    if a<c:  # a<b, a<c, so a is the smallest
        print("a is smallest")
    else:  # a<b, c<a, so c is the smallest
        print("c is smallest")
else: # b<a
    if b<c:  # b<a, b<c, so b is the smallest
        print("b is smallest")
    else:  # b<a, c<b, so c is the smallest
        print("c is smallest")


# 3-Middle of three numbers

print('-----------3------------')
a = 15
b = 14
c = 13

if a>b:
    if a<c:
        middle = a
    elif b>c:
        middle = b
    else:
        middle = c
else:
    if b<c:
        middle = b
    elif a>c:
        middle = a
    else:
        middle = c
print("The middle vlaue is : ",middle)