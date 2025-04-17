
print('----Generating list with range()----')
l = list(range(11))
print(l)


print('-----list comprehension-----')

print('-----------Ex-1------------')
l = [x for x in range(11)]
print(l)

'''
same as:
s = []
for i in range(11):
    s.append(i)
print(s)
'''

print('-----------Ex-2------------')
l = [i for i in range(11) if i%2==0]
print(l)

'''
same as:
l = []
for i in range(11):
    if i%2 == 0:
        l.append(i)
print(l)
'''


# 10-20 odd numbers

print('-----------Ex-3------------')
l = [i for i in range(10,21) if i%2 != 0]
print(l)


print('----if-else with comprehension----')
l = [str(i)+':even' if i%2 == 0 else str(i)+':odd' for i in range(10,21)]
print(l)


print('---------iterative-for--------')
l = list(range(21))
l1 = [i for i in l if i%2 == 0]
print(l1)


# create a list of fruits who have 'a' in their name

fruits = ['apple', 'banana', 'kiwi', 'lemon', 'grapes']
l = [i for i in fruits if 'a' in i]
print(l)

f = [i for i in fruits if 'a' not in i]
print(f)

l = [i for i in range(1,9) if i%2==0]
print(l)

l = [i for i in range(1,9) if i%4==0]
print(l)


print('-----------Ex-4------------')
def odd(i):
    return str(i)+':odd'

def even(i):
    return str(i)+':even'

l = [even(i) if i%2==0 else odd(i) for i in range(10,21)]
print(l)