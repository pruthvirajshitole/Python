# 1. Write a Python program that prints all prime numbers between 1 and 500 using a loop.  

# res = []
# for i in range(2,501):
#     flag = True
#     for j in range(2,i):
#         if i%j==0:
#             flag = False
#             break
#     if flag == True:
#         res.append(i)
# print(res)


# 2. Implement a program to find the sum of all numbers in a given list without using built-in sum().  

# l = [1,2,3,4,5,6,7,8,9]
# sum_l = 0
# for i in l:
#     sum_l += i
# print(sum_l)


# 3. Write a function that takes a list of integers as input and returns the second-largest number.  

# l=[11,22,34,52,54,24,67,86,87]
# l1=[]
# largest=float('-inf')
# second_large=float('-inf')
# for i in l:
#   if i>largest:
#     second_large=largest
#     largest=i
#   elif i>second_large and i!=largest:
#     second_large=i
# print("second large is:",second_large)


# 4. Implement a function that accepts a string and returns a dictionary with the count of
# each vowel present in the string.

# def vowels(s):
#     vowel = 'aeiouAEIOU'
#     d = {}
#     for i in s:
#         if i in vowel:
#             if i in d:
#                 d[i] += 1
#             else:
#                 d[i] = 1
#     return d
# s = input("Enter a string: ")
# print(vowels(s))


# 5. Write a Python program to sort a list of tuples based on the second element
# using a lambda function.  

# t=[(4,3),(2,1),(5,2),(6,0)]
# sorted_l=sorted(t, key=lambda x:x[1])
# print(sorted_l)x


# 6. Implement a function using lambda to filter out numbers divisible by both 3 and 5 from a given list.  

# l=[10,20,30,40,50,60]
# def divisible(x):
#   if x%3==0 and x%5==0:
#     return x
# a=list(filter(divisible,l))
# print(a)


# 7. Write a recursive function to compute the sum of digits of a given number.  

# def sum_of_digit(n):
#   if n==0:
#     return 0
#   else:
#     return n%10 +sum_of_digit(n//10)
# n=1234
# print(f'sum of digits {n}: {sum_of_digit(n)}')


# 8. Implement a recursive function to generate all subsets of a given set. 

# PENDING 


# 9. Given a string containing only '(' and ')', find the length of the longest valid (well-formed) parentheses substring.  

# PENDING 


# 10. Write a Python program to reverse a string using recursion. 

# def reverse(s):
#   if len(s)==0:
#     return s
#   else:
#     return reverse(s[1:])+s[0]
# s='hello'
# print(f'reverse of string {s}:{reverse(s)}')


# 11. Given a string, find the longest palindromic substring.  

# PENDING 


# 12. Write a Python program to create a file and write "Hello, Python!" into it.  

# open("Assignments_tests/21.1hello.py",'w')
# with open("Assignments_tests/21.1hello.py",'w') as file:
#     file.write("Hello, Python!")


# 13. Implement a function to read the contents of a file and print each line with line numbers.  

with open(r'C:\Users\pruth\OneDrive\Desktop\Data_Science_Codenera\Assignments_tests','r') as file:
    lines = file.readlines()
    print(lines)

for x in lines:
    print(x)


# 14. Write a Python program to insert a new line at the beginning of an existing file without overwriting its content.  

# 15. Implement a program to delete a specific line from a text file.  
