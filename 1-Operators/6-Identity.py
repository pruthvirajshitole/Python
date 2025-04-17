'''
Identity Operators    (is, is not)

is :
    The 'is' operator returns Boolean True or False.
    It returns True if the memory address first value is equal to the second value.
    Otherwise, it returns False

is not :
    The 'is not' operator returns Boolean True or False.
    It returns True if the memory address first value is not equal to the second value.
    Otherwise, it returns False

'''

print('------is------')
a=[1,2,3]
b=[1,2,3]
c=a 
print(a==b)    # check the content is same or not
print(a is b)  # check that 2 datatype are same object or not
print(c is a)  # true
print(a is c)  # true

print(id(a)) 
print(id(b)) 
print(id(c)) 
# address of a and c is same 
# while address of a and b are different

print('------is not------')
print(a is not b)  #True
print(c is not a)  #False
print(a is not c)  #False