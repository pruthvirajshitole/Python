# When we create a tuple, we normally assign values to it.
# This is called "packing" a tuple.

print('------packing------')
fruits = ('apple','banana','grapes')
print(fruits)


# Python allows to extract the values back into variables.
# This is called "unpacking"

print('------unpacking------')
fruits = ('apple','banana','grapes')
red,yellow,black = fruits
print(red)

fruits = ['apple','banana','grapes']
red,yellow,purple = fruits
print(purple)

fruits = {'apple','banana','grapes'}
red,pale_yellow,black = fruits
print(pale_yellow)   # set is unordered


'''
Note: The number of variables must match the number of values in the tuple,
if not, you must use an asterisk to collect the remaining values as a list.
'''


# If the number of variables is less than the number of values,
# you can add an * to the variable name and the values will be assigned to the variable as a list.

# If the asterisk is added to another variable name than the last,
# Python will assign values to the variable until the number of values
# left matches the number of variables left.

print('------Using Asterisk*------')
fruits = ("apple", "mango", "papaya", "pineapple", "cherry")
(green, *tropic, red) = fruits

print(green)
print(tropic)
print(red)

# with list
l = [1,2,3,4,5,6,7,8]
a,*b,c = l
print(*b)


# Python Method creates an immutable Set object from an iterable.
# It is a built-in Python function. As it is a set object, therefore,
# we cannot have duplicate values in the frozenset.

print('------frozenset()------')
fruits = frozenset(["apple", "banana", "orange"])
print(fruits)

# fruits.add("cherry")
# AttributeError: 'frozenset' object has no attribute 'add'

l = [1,2,3,4,1,2,1,9]
print(type(l))
f = frozenset(l)
print(type(f),f)
