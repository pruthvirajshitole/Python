# Shallow copy: changes in original will not affect in copy.

print('------shallow copy------')
l = [1,2,3,4]
l1 = l.copy()
l2 = l1
print('Original list:',l)
print('Copy:',l1)
print('Deep copy:',l2)

l1.append(9)
l.append(10)
print('Original list:',l)
print('Copy:',l1)


# Deep copy: changes in one will affect in its copy

print('------deep copy------')
l2.append(12)
l.append(100)
print('Original list:',l)
print('Deep copy:',l2)

print(id(l))
print(id(l1))
print(id(l2))