'''
Sequence Type:
    collection of hetrogenous(different type) data,
    indexed and ordered,
    immutable(changes not possible),
    allows duplicate values,
    elements written in round brackets()
'''

print('-------tuple-------')
t = (1, 2, 3, 4, 5, 5, 'Lucifer', 3.99)
print(t)    # (1, 2, 3, 4, 5, 5, 'Lucifer', 3.99)

print(type(t))  # <class 'tuple'>

t1 = (1)    
t2 = [2]

print(type(t1))  # <class 'int'>
print(type(t2))  # <class 'list'>

t = 1,2,3
print(type(t))   # <class 'int'>


# Slicing

print('-------Slicing-------')

# Positive slicing:
# syntax:
    # variable_name[index]

l = (1, 2, 3, 4, 5, 5, 'Lucifer', 3.99)
print(l[0])

print(l[4])

# Negative slicing:
# starts with -1
# so last element is on -1 index

print(l[-1])

print(l[-4])

# Positive range
# syntax:
    # variable_name(start_index:end_index)

print(l[1:4])

# Negative range:
# syntax:
    # variable_name(start_index:end_index)

print(l[-3:-1])

# Positive step:
# syntax:
    # variable_name(start_index:end_index:step_size)

print(l[0:5:1]) # default step size is 1

print(l[0:5:2]) # skips 1 element

print(l[0:5:3]) # skips 2 elements

# Negative step:
# syntax:
    # variable_name(start_index:end_index:step_size)

print(l[::-1]) # reverse the list

print(l[-2::-1])

# we can perform slicing on tuples because tuples are indexed.
l = (1,2,(4,5,6))
print(l[2][1])

# Jeff Bezos
n=(1,2,3,(4,'Jeff',13,(5,'Bezos'),41),5,13 )
print(n[3][1],n[3][3][1])

# William Henry Gates III
m=(1,2,3,('William',13,(0,21,('Gates')),41),5,(1,5,('Henry'),3),'III')
print(m[3][0],m[5][2][0],m[3][2][2][0],m[6])

print('-------AttributeError-------')

# append() - 

l = (10,20,30,40,50)

l.append(60)
print(l)  # AttributeError: 'tuple' object has no attribute 'append'

# extend() 

l.extend((1,2,3,4))
print(l)  # AttributeError: 'tuple' object has no attribute 'extend'

# Deletes elements from a tuple

# 1 - remove()

l = (1,2,3,4,5,6,7)
l.remove(4)  # remove(value)
print(l)  # AttributeError: 'tuple' object has no attribute 'remove'

# 2 - pop()

l = (10,20,30,40,50)
l.pop(3)   
print(l)  # AttributeError: 'tuple' object has no attribute 'pop'

# 3 - del 

l = (10,20,30,40,50,60,70,80,90,100)

del l

'''
NameError: name 'l' is not defined
print(l)
'''

# 4 - clear()
# clear() is used to remove all elements from a list. It does not work with tuples.