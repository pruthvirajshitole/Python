# 1-10 set

print('-----set comprehension-----')
s = {i for i in range(11)}
print(s)


print('-----set comprehension with-if-----') 
s ={i for i in range(21) if i%2 == 0}
print(s)


print('-----set comprehension with if-else-----')
s = {str(i)+':even' if i%2 == 0 else str(i)+':odd' for i in range(10)}
print(s)

 
print('-----iterative set comprehension-----')
s = {1,3,5,7,8,9,6,5,4,67,8}
s1 = {x for x in s if x%2 != 0 }
print(s1)


# TypeError: 'set' object is not subscriptable
'''
even and odd idexed elements

t = {1,3,5,7,8,9,6,5,4,67,8}

even_indexed = {str(x)+':'+str(t[x]) for x in range(len(t)) if x%2 == 0}
print(even_indexed)

odd_indexed = {str(x)+':'+str(t[x]) for x in range(len(t)) if x%2 != 0}
print(odd_indexed)
'''