# 1. Write a function to flatten a nested list of strings into a single list.  
#    Input: [['a', ['b', 'c']], ['d', 'e']] → Output: ['a', 'b', 'c', 'd', 'e']  

# l = [['a', ['b', 'c']], ['d', 'e']]

# def flatten(l):
#     res = []
#     for i in l:
#         if isinstance(i,list):
#             res.extend(flatten(i))
#         else:
#             res.append(i)
#     return res
# print(flatten(l))

# without using recursion function

# l1=[]
# for x in l:
#   if isinstance(x,list):
#     for y in x:
#       l1.extend(y)
#   else:
#       l1.append(x)
# print(l1)


# 2. Implement a recursive function to flatten a deeply nested list of floating-point numbers.  
#    Input: [[1.1, [2.2, [3.3]]], 4.4] → Output: [1.1, 2.2, 3.3, 4.4]  

# l = [[1.1, [2.2, [3.3]]], 4.4]
# def flatten(l):
#     res = []
#     for i in l:
#         if isinstance(i,list):
#             res.extend(flatten(i))
#         else:
#             res.append(i)
#     return res
# print(flatten(l))


# 3. Given a list containing nested lists of booleans, write a function to return a flattened version of it.  
#    Input: [[True, [False, [True]]], False] → Output: [True, False, True, False]

# l = [[True, [False, [True]]], False]
# def flatten(l):
#     res = []
#     for i in l:
#         if isinstance(i,list):
#             res.extend(flatten(i))
#         else:
#             res.append(i)
#     return res
# print(flatten(l))


# 4. Write a Python function that flattens a nested list while preserving the order of dictionary elements.  
#    Input: [[{'a': 1}, [{'b': 2}, {'c': 3}]], {'d': 4}] → Output:  [{'a': 1}, {'b': 2}, {'c': 3}, {'d': 4}]  

# l = [[{'a': 1}, [{'b': 2}, {'c': 3}]], {'d': 4}]

# def flatten(l):
#     res = []
#     for i in l:
#         if isinstance(i,list):
#             res.extend(flatten(i))
#         else:
#             res.append(i)
#     return res
# print(flatten(l))


# 5. Convert a nested list of complex numbers into a single flat list using a generator function.  
#    Input: [[1+2j, [3+4j, [5+6j]]], 7+8j] → Output: [1+2j, 3+4j, 5+6j, 7+8j]  

# PENDING

# l=[[1+2j, [3+4j, [5+6j]]], 7+8j] 
# def flatten(l):
#     res = []
#     for i in l:
#         if isinstance(i,list):
#             res.extend(flatten(i))
#         else:
#             res.append(i)
#     return res
# t = flatten(l)
# print(t[1])


# 6. Write a function to flatten a nested tuple of strings into a single tuple.  
#    Input: (('a', ('b', 'c')), ('d', 'e')) → Output: ('a', 'b', 'c', 'd', 'e')  

# t=(('a', ('b', 'c')), ('d', 'e'))
# def flatten(t):
#     res = []
#     for i in t:
#         if isinstance(i,tuple):
#             res.extend(flatten(i))
#         else:
#             res.append(i)
#     return tuple(res)
# print(flatten(t))


# 7. Implement a recursive approach to flatten a deeply nested tuple of integers.  
#    Input: ((1, (2, (3, 4))), 5) → Output: (1, 2, 3, 4, 5)  

# t=((1, (2, (3, 4))), 5)
# def flatten(t):
#     res = []
#     for i in t:
#         if isinstance(i,tuple):
#             res.extend(flatten(i))
#         else:
#             res.append(i)
#     return tuple(res)
# print(flatten(t))


# 8. Given a tuple containing nested tuples of lists, write a function to return a flattened version of it.  
#    Input: ((['a', 'b'], (['c', 'd'])), ['e', 'f']) → Output: ('a', 'b', 'c', 'd', 'e', 'f') 

# t=((['a', 'b'], (['c', 'd'])), ['e', 'f'])
# def flatten(t):
#     res = []
#     for i in t:
#         if isinstance(i,(tuple,list)):
#             res.extend(flatten(i))
#         else:
#             res.append(i)
#     return tuple(res)
# print(flatten(t))


# 9. Write a Python function that flattens a nested tuple while maintaining the order of set elements inside it.  
#    Input: (({1, 2}, ({3, 4}, 5)), {6, 7}) → Output: (1, 2, 3, 4, 5, 6, 7)  

# t=(({1, 2}, ({3, 4}, 5)), {6, 7})
# def flatten(t):
#     res = []
#     for i in t:
#         if isinstance(i,(tuple,list,set)):
#             res.extend(flatten(i))
#         else:
#             res.append(i)
#     return tuple(res)
# print(flatten(t))


# 10. Convert a nested tuple of booleans into a single flat tuple using a generator function.  
#    Input: ((True, (False, (True, False))), True) → Output: (True, False, True, False, True)  

# t=((True, (False, (True, False))), True)
# def flatten(t):
#     res = []
#     for i in t:
#         if isinstance(i,(tuple)):
#             res.extend(flatten(i))
#         else:
#             res.append(i)
#     return tuple(res)
# print(flatten(t))


# 11. Given a list containing nested tuples, write a function to flatten it into a list.  
#    Input: [('a', ('b', 'c')), ('d', 'e')] → Output: ['a', 'b', 'c', 'd', 'e']  

# t=[('a', ('b', 'c')), ('d', 'e')]
# def flatten(t):
#     res = []
#     for i in t:
#         if isinstance(i,(tuple)):
#             res.extend(flatten(i))
#         else:
#             res.append(i)
#     return res
# print(flatten(t))


# 12. Write a recursive function to flatten a list containing both tuples and nested lists of mixed data types.  
#    Input: [1, (2, [3, (4, 5)]), 'a', ('b', ['c', 'd'])] → Output: [1, 2, 3, 4, 5, 'a', 'b', 'c', 'd'] 

# t=[1, (2, [3, (4, 5)]), 'a', ('b', ['c', 'd'])]
# def flatten(t):
#     res = []
#     for i in t:
#         if isinstance(i,(tuple,list)):
#             res.extend(flatten(i))
#         else:
#             res.append(i)
#     return res
# print(flatten(t))


# 13. Use the lambda function to find the maximum of two given numbers.  
#    Input: (7, 10) → Output: 10  

# x = int(input("Enter first number: "))
# y = int(input("Enter second number: "))
# print((lambda x,y:x if x>y else y)(x,y))


# 14. Implement a Python program using lambda and map to capitalize each word in a list of strings.  
#    Input: ['hello', 'world'] → Output: ['Hello', 'World']

# l = ['hello', 'world']
# print(list(map(lambda x:x.capitalize(),(l))))


# 15. Write a Python function using lambda and filter to extract all strings that start with 'A' from a list.  
#    Input: ['Apple', 'Banana', 'Avocado', 'Cherry'] → Output: ['Apple', 'Avocado']  

# l = ['Apple', 'Banana', 'Avocado', 'Cherry']
# print(list(filter(lambda i:i[0]=='A',l)))