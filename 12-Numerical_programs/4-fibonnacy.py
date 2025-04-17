a = 0
b = 1
print(a)
print(b)
n = 1
while n<=8:
    c = a+b
    print(c)
    a = b
    b = c
    n += 1

'''
a   b   a+b=c   a=b  b=c
0   1     1      1    1
1   1     2      1    2
1   2     3      2    3
2   3     5      3    5
3   5     8      5    8
5   8     13     8    13
8   13    21     13   21
13  21    34     21   34
''' 

# # first 10 elements of febonnaci series

# l = []
# a = 0
# b = 1
# n = 1
# l.append(a)
# l.append(b)
# while n<=8:
#     c = a+b
#     a = b
#     b = c
#     n += 1
#     l.append(c)
# print(l)


# first 25-50 elements of febonnaci series

l = []
a = 0
b = 1
n = 1
c = 0
while c<=100:
    c = a+b
    if c>25 and c<50:
        l.append(c)
    a,b = b,c
    n+=1
print(l)




