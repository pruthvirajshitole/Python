# 1-10 tuple

print('-----tuple comprehension-----')
t = tuple(i for i in range(11))
print(t)


print('-----tuple comprehension with-if-----')
t = tuple(i for i in range(21) if i%2 == 0)
print(t)


print('-----tuple comprehension with if-else-----')
t = tuple(str(i)+':even' if i%2 == 0 else str(i)+':odd' for i in range(10))
print(t)


print('-----iterative tuple comprehension-----')
t = (1,3,5,7,8,9,6,5,4,67,8)
t1 = tuple(x for x in t if x%2 != 0 )
print(t1)


# even and odd idexed elements

t = (1,3,5,7,8,9,6,5,4,67,8)

even_indexed = tuple(str(x)+':'+str(t[x]) for x in range(len(t)) if x%2 == 0)
print(even_indexed)

odd_indexed = tuple(str(x)+':'+str(t[x]) for x in range(len(t)) if x%2 != 0)
print(odd_indexed)