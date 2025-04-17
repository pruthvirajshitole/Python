'''
Membership Operators  (in , not in)

in :
    It returns a result as True if it finds a given object in the sequence.
    Otherwise, it returns False.

not in :
    It returns True if the object is not present in a given sequence.
    Otherwise, it returns False

'''

print('------in------')
l=[1,2,3,4]
print(3 in l)  # True
print(5 in l)  # False


print('------not in------')
l=[1,2,3,4]
print(5 not in l)  # False
print(3 not in l)  # True