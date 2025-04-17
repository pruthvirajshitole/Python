'''
Sequence Type:
    collection of hetrogenous(different type) data,
    indexed and ordered,
    mutable(changes),
    allows duplicate values,
    elements written in square brackets[]


    - Mutation:
      append()
      extend()
      insert()
      update()

    - Delete:
      remove()
      pop()
      clear()
      del

    - Operation:
      concatenate (+)
      product (*)

'''

print('------Heterogenous list------')
l = [1, 2, 3, 4.99, True, 'Jordy']
print(l)
print(type(l))  # <class 'list'>

print('------Homogenous list------')
l1 = [1, 2, 3, 4, 5, 3, 1]
print(l1)
fruits = ['apple', 'banana', 'cherry']
print(fruits)

# Index : starts with 0
# list have a sequence of index from 0 to len(l)-1
# each value in list have a index

print(f'length of l: len(l)')  # gives the total count of elements


# Slicing

print('-----Slicing------')

# Positive slicing:
# syntax:
    # variable_name[index]
print(l[0])
print(l[4])

# Negative slicing:
# starts with -1
# so last element is on -1 index
print(l[-1])
print(l[-4])

# Positive range
# syntax:
    # variable_name[start_index:end_index]

print(l[1:4])

# Negative range:
# syntax:
    # variable_name[start_index:end_index]

print(l[-3:-1])

# Positive step:
# syntax:
    # variable_name[start_index:end_index:step_size]

print(l[0:5:1])  # default step size is 1

print(l[0:5:2])  # skips 1 element

print(l[0:5:3])  # skips 2 elements

# Negative step:
# syntax:
    # variable_name[start_index:end_index:step_size]

print(l[::-1])  # reverse the list
print(l[-2::-1])

# we can perform slicing on lists because lists are indexed.
l = [1,2,[4,5,6]]
print(l[2][1])

n=[1,2,3,[4,'Jeff',13,[5,'Bezos'],41],5,13 ]
print(n[3][1],n[3][3][1])


m=[1,2,3,['William',13,[0,21,['Gates']],41],5,[1,5,['Henry'],3],'III']
# William Henry Gates III

print(m[3][0],m[5][2][0],m[3][2][2][0],m[6])


# Mutation (changes) in a list

# append() - creates single index at end of a list and add value
           # adds only a single index at the end of the list

print('-------append()-------')

l = [10,20,30,40,50]

l.append(60)
print(l)      # [10, 20, 30, 40, 50, 60]

l.append(90)
print(l)      # [10, 20, 30, 40, 50, 60, 90]

# extend() - creates multiple indexes at the end of list and adds those values.

print('-------extend()-------')

l.extend([1,2,3,4])
print(l)    # [10, 20, 30, 40, 50, 60, 90, 1, 2, 3, 4]

l.extend((1,2,3))
print(l)   # [10, 20, 30, 40, 50, 60, 90, 1, 2, 3, 4, 1, 2, 3]

l.append(['a', 'b'])  # treats as a single element 
print(l)   # [10, 20, 30, 40, 50, 60, 90, 1, 2, 3, 4, ['a', 'b']]

names = ["Alice", "Bob", "Peter"]
name = input("Enter your name : ")
print(name)

names.append(name)
print(names)

friends = ["Virat", "Rohit", "Dhoni"]
print(friends)

names.extend(friends)
print(names)


# insert() - inserts element in a list with index

print('-------insert()-------')

l = [10,20,30,40,50]
l.insert(3, 35)
print(l)    # [10, 20, 30, 35, 40, 50]

l.insert(4,[40.1, 42.2])
print(l)    # [10, 20, 30, 35, [40.1, 42.2], 40, 50]

l.insert(-1,90)
print(l)    # [10, 20, 30, 35, [40.1, 42.2], 40, 90, 50]


# Update elements of a list

print('--------update---------')

l = [10,20,30,40,50]

l[2] = 'Thirty'
print(l)    # [10, 20, 'Thirty', 40, 50]

l[:2] = 'Ten', 'Twenty'
print(l)    # ['Ten', 'Twenty', 'Thirty', 40, 50]

l[-3:] = 'C','D','E','F'
print(l)    # ['Ten', 'Twenty', 'C', 'D', 'E', 'F']


# Delete elements from a list

# 1 - remove()

print('--------remove()---------')

l = [1,2,3,4,5,6,7]
l.remove(4)  # remove(value)
print(l)    # [1, 2, 3, 5, 6, 7]

l = [1,2,3,4,5,4,6,4]
l.remove(4)  # removes the first occurrence of 4
print(l)    # [1, 2, 3, 5, 4, 6, 4]


# 2 - pop()
# it returns popped element

print('--------pop()---------')

l = [10,20,30,40,50]
l.pop(3)    # pop(index)
print(l)    #[10, 20, 30, 50]



r = l.pop()    # pop() removes the last element
print(r,l)    # 50 [10, 20, 30, 50]




# 3 - del 

print('--------del---------')

l = [10,20,30,40,50,60,70,80,90,100]

del l[3]    # del is not a function, it's a keyword
print(l)    # [10, 20, 30, 50, 60, 70, 80, 90, 100]

del l[-1]
print(l)    # [10, 20, 30, 50, 60, 70, 80, 90]

del l[5:]   # del can removes multiple values with range
print(l)    # [10, 20, 30, 50, 60]


# 5 - clear()

print('--------clear()---------')

l = [10,20,30,40,50]
l.clear()
print(l)    # []

del l 

'''
print(l)

NameError: name 'l' is not defined

'''

# clear removes all the elements from the list but list will exist
# del removes the list itself and list will not exist


# concatenate multiple lists

print('--------Concatenation(+)---------')

l1 = [1,2,3,4]
l2 = [5,6,7,8]
l3 = [9,10]
l = l1 + l2 + l3
print(l)    # [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]


# product of lists

print('--------Replication(*)---------')

l = 3*l3
print(l)    #[9, 10, 9, 10, 9, 10]

l = l3*0    # empty list
print(l)    # []