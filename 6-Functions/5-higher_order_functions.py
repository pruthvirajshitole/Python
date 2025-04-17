'''
Higher Order Functions(HOF):
    The function that takes function as an argument
    or returns a new function is called HOF

1-Map:

The map() function applies a given function to each item in 
an iterable (like a list, tuple, etc.)
and returns a map object (an iterator) with the results. 
It is used when you want to transform all elements in an iterable.

Syntax: map(function, iterable)


2-Filter:

The filter() function applies a given function (predicate) to each item in
an iterable and returns a filter object (an iterator) containing only 
the elements for which the function returns True. 
It is used for selecting specific elements based on a condition.

Syntax: filter(function, iterable)
 

3-Reduce:

The reduce() function from the functools module applies a rolling 
computation to pairs of items in an iterable, reducing it to a 
single cumulative value. It is often used for aggregation 
tasks like summing, multiplying, or finding maximum values.
Syntax: reduce(function, iterable)

'''

# 1-Map

print('----------map()----------')

print('----------Ex-1----------')
l = [1,2,3,4]
def add(x):
    return x+3
m = map(add,l)  # creates a map object
print(list(m))


print('----------Ex-2----------')
l1 = [1,2,3,4]
l2 = [4,5,6,7]
def add(x,y):
    return x+y
m = map(add,l1,l2)
print(list(m))


print('----------Ex-3----------')
def sub(x,y):
    return y-x
m = map(sub,l1,l2)
print(list(m))


print('----------Ex-3----------')
def mul(x,y):
    return x*y
m = map(mul,l1,l2)
print(list(m))


print('----------Ex-4----------')
def div(x,y):
    return y/x
m = map(div,l1,l2)
print(list(m))


print('----------Ex-5----------')
print(list(map(lambda l1,l2:l1+l2,l1,l2)))


# 2-Filter

print('----------filter()----------')

print('----------Ex-6----------')
l = [i for i in range(1,11)]
def even(x):
    if x%2==0:
        return x
print(list(filter(even,l)))


print('----------Ex-7----------')
f = list(filter(lambda x:x%2==0,l))
print(f)


# 3-Reduce

print('----------reduce()----------')

print('----------Ex-8----------')
from functools import reduce

l = [1,2,3,4,5]
def add(x,y):
    return x+y
a = reduce(add,l)
print(a)


print('----------Ex-9----------')
print(reduce(lambda x,y:x+y,l))


# find the factorial of n using reduce
print('----------Ex-10----------')
n = int(input("Enter a number: "))
l = [i for i in range(1,n+1)]
print(reduce(lambda x,y:x*y,l))


print('----------Ex-11----------')
n = int(input('Enter a number: '))
l = []
while n!=0:
    d = n%10
    l.append(d)
    n = n//10
print(reduce(lambda x,y:x+y,l))

