print('-------dictionary comprehension------')
d = {i:i**2 for i in range(5)}
print(d)


print('-------dictionary comprehension with-if------')
d = {i:i+1 for i in range(10) if i%2 == 0}
print(d)


print('-------iterative dictionary comprehension------')
d = {0: 1, 2: 3, 4: 5, 6: 7, 8: 9, 10: 11, 12: 13, 14: 15, 16: 17, 18: 19, 20: 21}
even = {i:j for i,j in d.items() if i%3 == 0}
print(even)
