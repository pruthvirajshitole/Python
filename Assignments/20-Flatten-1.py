# 1. Write a program to find the second largest number in a given list without using sorting.

# l = [6,7,5,1,3,9,98,2,100]
# largest = float('-inf')
# second_largest = float('-inf')
# for i in l:
#     if i>largest:
#         second_largest = largest
#         largest = i
#     elif i>second_largest and i!=largest:
#         second_largest = i
# print("second largest is:",second_largest)


# 2. Implement a program that checks if a string is a palindrome without using string slicing or built-in functions.  

# s = input("Enter a string: ")
# rev = ''
# for i in s:
#     rev = i+rev
# if s == rev:
#     print("Given string is a palindrome.")
# else:
#     print("Given string is not a palindrome.")


# 3. Write a function that takes a list of integers and returns a new list where each element
# is the product of all other elements except itself (without using division).

# l = [1,5,4,2,3]
# res = []
# for i in l:
#     product = 1
#     for j in l:
#         if i!=j:
#             product *= j
#     res.append(product)
# print(res)


# 4. Implement a function that removes all duplicate characters from a given string while
# maintaining the order of characters.

# s = input("Enter a string: ")
# res = ''
# for i in s:
#     if i not in res:
#         res += i
# print(res)


# 5. Write a lambda function that filters out all words from a list that have an odd length.  

# l = ['Lucifer','was','innocent','true','false']
# print(list(filter(lambda n:(len(n))%2==1,l)))


# 6. Implement a lambda function to compute the sum of squares of all odd numbers in a given list.  

# from functools import reduce
# l = [1,2,3,4,5,6,7,8,9,10]
# l = [i**2 for i in l if i%2==1]
# print(reduce(lambda x,y:x+y,l))


# 7. Write a recursive function to check whether a number is a palindrome (do not convert the number to a string).  

# def palindrome(n):
#     temp = n
#     s = 0
#     while n!=0:
#         d = n%10
#         s = 10*s+d
#         n = n//10
#     if temp == s:
#         return 'Its a Palindrome.'
#     else:
#         return 'Its not a Palindrome.'
# print(palindrome(1221))


# 8. Implement a recursive function to find the Greatest Common Divisor (GCD) of two numbers without
# using any built-in functions.  

# def gcd(x,y):
#     if x>y:
#         largest_divisor = float('-inf')
#         for i in range(1,y+1):
#             if x%i==0 and y%i==0:
#                 if i>largest_divisor:
#                     largest_divisor = i
#     else:
#         largest_divisor = float('-inf')
#         for i in range(1,x+1):
#             if x%i==0 and y%i==0:
#                 if i>largest_divisor:
#                     largest_divisor = i
#     print(largest_divisor)
# x = int(input("Enter first number: "))
# y = int(input("Enter second number: "))
# gcd(x,y)




# 9. Write a function that takes another function as input and applies it to every element of a given list,
# returning a new list with modified values.

# PENDING

# l = [1,2,3,4,5,6,7,8,9]
# def outer_f(l):
#     def inner_f(l):
#         for i in l:
#             l[i] = i+1
#         return l
# print(outer_f(l))


# 10. Implement a function that takes a list of numbers and a function, and applies the function only to prime numbers in the list.  

# NEED TO FIX PRIME==1

# l = [2,3,4,5,6,7,8,9]
# def square(l):
#     updated_l = []
#     for i in l:
#         flag = True
#         for j in range(2,i):
#             if i%j==0:
#                 flag = False
#                 break
#         if flag == True:
#             updated_l.append(i)
#     print(list(map(lambda x:x**2,updated_l)))
# square(l)


# 11. Write a program that prints all the indices of a given character in a string without using any
# built-in functions like .find() or .index().

# l = 'Lucifer was innocent.'
# c = input("Enter a character: ")
# indices = []
# for i in range(len(l)):
#     if c == l[i]:
#         indices.append(i)
# print(indices)


# 12. Implement a function that takes a list of words and returns a dictionary where keys are word
# lengths and values are lists of words with that length, using enumeration.  

# def enumerating(l):
#     d = {}
#     for length,word in enumerate(l):
#         length = len(word)
#         if length not in d:
#             d[length] = []
#         d[length].append(word)
#     return d
# l = input("Enter a list of words seperated by comma: ").split(',')
# print(enumerating(l))


# 13. Write a function that counts the number of vowels and consonants in a given string without using any built-in functions.  

# def s_counts(s):
#     vowels = 'aeiouAEIOU'
#     c_vowels,c_consonants = 0,0
#     for i in s:
#         if i in vowels:
#             c_vowels+=1
#         elif i == ' ':
#             continue
#         else:
#             c_consonants+=1
#     return f'counts of vowels: {c_vowels}, consonants: {c_consonants}'  
# s = input("Enter a string: ")  
# print(s_counts(s))


# 14. Implement a function that finds the first non-repeating character in a given string without using dictionaries.

# s = 'the lucifer morningstar was innocent who ruled out of heaven'
# for i in range(0,len(s)):
#     if s[i] not in s[i+1:]:
#         print(s[i])
#         break


# 15. Write a program that simulates a basic mathematical module with addition, subtraction,
# multiplication, and division, and allows importing these functions from another file.

# from Assignments_tests import calculator

# a = int(input("Enter value of a: "))
# b = int(input("Enter value of b: "))
# operation = input('''
# choose one operation:
# for additon +
# for substraction -
# for multiplication *
# for division /
# :
# ''')

# if operation == '+':
#     s=add.add(a,b)
#     print(s)
# elif operation == '-':
#     s=sub.sub(a,b)
#     print(s)
# elif operation == '*':
#     s=mul.mul(a,b)
#     print(s)
# elif operation == '/':
#     s=div.div(a,b)
#     print(s)



# 16. Flatten a nested list of integers:

#    Input:  
#    [[1, 2, [3, 4, [5, 6]]], [7, 8], [9]]

# flattened_list = []
# l = [[1, 2, [3, 4, [5, 6]]], [7, 8], [9]]
# def flatten(l):
#     for i in l:
#         if isinstance(i,(list)):
#             flatten(i)
#         else:
#             flattened_list.append(i)
#     return flattened_list
# print(flatten(l))


# 17. Flatten a list of dictionaries with nested lists:

#    Input:  
#    [{'a': [1, 2], 'b': [3, 4]}, {'c': [5, 6]}, {'d': [7]}]

# flattened_list = []
# l = [{'a': [1, 2], 'b': [3, 4]}, {'c': [5, 6]}, {'d': [7]}]
# def flatten(l):
#     for i in l:
#         if isinstance(i,(dict,list)):
#             flatten(i)
#         else:
#             flattened_list.append(i)
#     return flattened_list
# print(flatten(l))


# 18. Flatten a list of tuples containing nested tuples or lists:

#    Input:  
#    [(1, 2, (3, 4, [5, 6])), (7, (8, 9))]

# flattened_list = []
# l = [(1, 2, (3, 4, [5, 6])), (7, (8, 9))]
# def flatten(l):
#     for i in l:
#         if isinstance(i,(tuple,list)):
#             flatten(i)
#         else:
#             flattened_list.append(i)
#     return flattened_list
# print(flatten(l))


# 19. Flatten a list of lists of strings:

#    Input:  
#    [["apple", "banana"], ["cherry", "date"], ["elderberry", "fig"]]

# flattened_list = []
# l = [["apple", "banana"], ["cherry", "date"], ["elderberry", "fig"]]
# def flatten(l):
#     for i in l:
#         if isinstance(i,list):
#             flatten(i)
#         else:
#             flattened_list.append(i)
#     return flattened_list
# print(flatten(l))
        


# 20. Flatten a dictionary with nested lists, dictionaries, or other data types:

#    Input:  
#    {'a': {'b': [1, 2]}, 'c': {'d': {'e': [3, 4]}}, 'f': 5}

# def flatten_dict(d, parent_key='', sep='.'):
#     flattened_dict = {}

#     for key, value in d.items():
#         new_key = f"{parent_key}{sep}{key}" if parent_key else key
        
#         if isinstance(value, dict):
#             flattened_dict.update(flatten_dict(value, new_key, sep))
#         else:
#             flattened_dict[new_key] = value

#     return flattened_dict

# l = {'a': {'b': [1, 2]}, 'c': {'d': {'e': [3, 4]}}, 'f': 5}
# print(flatten_dict(l))
