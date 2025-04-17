'''
Zip:
    to combine two or more iterables (like lists, tuples, or strings)
    element-wise, creating an iterable of tuples where each tuple 
    contains elements from the corresponding position in the input 
    iterables.
'''

print('----------zip()----------')
a = ['a','b']
b = [1,2,3]
print(list(zip(a,b)))


print('----------dict using zip()----------')
even = [i for i in range(10,21) if i%2 == 0]
odd = [i for i in range(11) if i%2 == 1]
print(f'{dict(zip(even,odd))}')
