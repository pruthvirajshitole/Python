'''
Sequence Type:
    collection of hetrogenous(different type) data,
    unindexed and unordered,
    mutable(changes),
    duplicate values not allowed (unique values),
    elements written in curly brackets{}


    - Mutation:
      add()
      update()

    - Delete:
      remove()
      discard()
      pop()
      clear()
      del

    - Operations:
      union (|)
      intersection (&)
      intersectin_update()
      difference()
      symmetric_difference()

    - Methods:
      isdisjoint()
      issubset()
      issuperset()
'''

print('-------------set-------------')

s = {1, 2, 'a', 3, 4, 5, 5, 'Lucifer', 3.99,1,1}
print(s)
print(type(s))   # <class 'set'>
print(s)  # unordered will get different sequence of output each time

print('--------Typecasting---------')
l = [1,2,3,1,2,3,1,2,3]
l = set(l)
print(l)
l = list(l)
print(l)

# list() converts other datatypes into list
# tuple() converts other datatypes into tuple
# set() converts other datatypes into set
# dict() converts other datatypes into dictionary

l = [1,2,3,1,2,3,1,2,3]
print(list(set(l)))   # [1, 2, 3]

'''
s = {1, 2, 'a', 3, 4, 5, 5, 'Lucifer', 3.99,1,1}
print(s[2])  # TypeError: 'set' object is not subscriptable
'''

# can't perform slicing in set because it is unindexed


# Mutation (changes)

# 1- add()

print('-------add()--------')

s = {1, 2, 'a', 3, 4, 5, 5, 'Lucifer', 3.99,1,1}
s.add('Tom')
print(s)

'''
s.add([100,101])
print(s)  # TypeError: unhashable type: 'list'
'''

print('-------update()--------')

s.update([100,101])
print(s)

s.update([99])
print(s)

'''
s.update(100)
print(s)  # TypeError: unhashable type: 'int'
'''

'''
add() is used for adding a single element.
update() is used for adding multiple elements from one or more iterables.
add() accepts a single immutable element.
update() accepts one or more iterables and adds their elements to the set.
'''

# 2 - delete elements in a set

print('-------remove()--------')

s = {1, 2, 'a', 3, 4, 5, 5, 'Lucifer', 3.99,1,1}
s.remove(1)
print(s)

print('-------discard()--------')

s.discard(2)
print(s)

'''
s.remove(100)
print(s)  # KeyError: 100
'''

s.discard(100)
print(s)  

# if we try to remove an element that is not present in the set, it will raise an key error.
# while discard() will not give any error.

print('-------pop()--------')

s.pop()    # pop() will remove an arbitrary element from the set
print(s)   # 3.99

print('-------clear()--------')

s.clear()
print(s)   # set()  # it will remove all elements from the set

'''
del s
print(s)  # NameError: name 's' is not defined  # it will delete the set itself
'''


# join()

# 1- union()

print('-------union(|)--------')

s1 = {1,2,3}
s2 = {4,5,6}
s3 = {7,8,9}
 
s4 = s1.union(s2,s3)  # creates a new set 
print(s4)   # {1, 2, 3, 4, 5, 6, 7, 8, 9}

s1.update([22,24])  # we update existing set
print(s1)   # {1, 2, 3, 22, 24}

# 2- intersection()

print('-------intersection(&)--------')

s1 = {1,2,3}
s2 = {2,3,5,6}

s3 = s1.intersection(s2)  # creates a new set with common elements
print(s3)   # {2, 3}

print('-------intersection_update()--------')

s1.intersection_update(s2)  # # updates existing set with common elements
print(s1)   # {2, 3}

s2.intersection_update(s1)
print(s2)   # {2, 3}


# 3- difference()

print('-------difference()--------')

s1 = {1,2,3}
s2 = {3,5,6}

s3 = s1.difference(s2)  # creates a new set with different elements of first set with second set
print(s3)   # {1, 2}

s4 = s2.difference(s1)
print(s4)   # {5, 6}

print('-------symmetric_difference()--------')

s5 = s1.symmetric_difference(s2)  # creates a new set with different elements of both sets
print(s5)

print('-------symmetric_difference_update()--------')

s1.symmetric_difference_update(s2)  # udates an existing set with different elements of both sets
print(s1,s2)    # {1, 2, 3} {3, 5, 6}

s2.symmetric_difference_update(s1)  
print(s1,s2)    # {1, 2, 3} {1, 2, 5, 6}


# Set Methods

print('-------isdisjoint()--------')

s1 = {1,2,3}
s2 = {3,5,6}

print(s1.isdisjoint(s2))  # False # returns True if two sets have no elements in common

s1 = {1,2,3}
s2 = {5,6}

print(s1.isdisjoint(s2)) # True

print('-------issubset()--------')

s1 = {1,2,3}
s2 = {1,2,3,4,5,6,7,8}

print(s1.issubset(s2)) # True # returns True if all elements of the set are present in the other set

print('-------issuperset()--------')

print(s2.issuperset(s1)) # True # returns True if all elements of the other set are present in the set
