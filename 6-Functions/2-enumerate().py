'''
Enumerate:
    adds a counter to an iterable (like a list, tuple, or string) 
    and returns it as an enumerate object.
    This object can then be iterated to access both the index 
    and the value of each element in the iterable.
'''

print('----------enumerate()----------')

print('----------Ex-1----------')
l = [i for i in range(1,11)]
print(l)

for index,value in enumerate(l):
    print(f'{index}:{value}')


# print idexes and values of even index with list

print('----------Ex-2----------')
l = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

for index,value in enumerate(l):
    if index%2 == 0:
         print(f'{index}:{value}')


# for tuple

print('----------Ex-3----------')
t = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)

for index,value in enumerate(t):
    if index%2 == 0:
         print(f'{index}:{value}')


# for set

print('----------Ex-4----------')
s = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10}

for index,value in enumerate(s):
    if index%2 == 0:
         print(f'{index}:{value}')

# for dictionary

