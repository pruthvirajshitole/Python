'''
Raise:
    if developer has to throw his own
    exception under certain condition
'''
print('------raise------')
age = -1
if age<0:
    raise Exception("Age can't be zero")

x = 'e'
if not type(x) is int:
    raise TypeError("Only integers are possible")