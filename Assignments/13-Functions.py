# 1. Write a Python function that takes two numbers as parameters and returns their sum.  

# def add(a,b):
#     return a+b
# a = int(input("Enter a: "))
# b = int(input("Enter b: "))
# c = add(a,b)
# print(f'Additon is: {c}')


# 2. Create a function that prints "Hello, World!" without taking any parameters or returning a value.  
 
# def display():
#     print('Hello, World!')

# display()


# 3. Define a function that takes a string as input and returns the reversed string.  

# s = input("Enter a string: ")
# def reverse():
#     print(s[::-1])
# reverse()


# 4. Write a function to check if a given number is prime.
# It should take a number as a parameter and return True or False.

# num = int(input("Enter a number: "))
# def prime(num):
#     flag = True
#     for i in range(2,num):
#         if num%i == 0:
#             flag = False
#             break
#     if flag == True:
#         return True
#     else:
#         return False

# print(prime(num))


# 5. Implement a function that calculates the factorial of a number without using recursion.
# The function should accept one parameter and return the result.

# def factorial(num):
#     result=1
#     for i in range(1,num+1):
#       result*=i
#     return result    
# print(factorial(5))


# 6. Create a function that takes a list of integers as input and prints all even numbers in the list.

# l = input("Enter a list of numbers: ").split(',')
# res = []
# def eve_nums():
#     for i in l:
#         i = int(i)
#         if i%2 == 0:
#             res.append(i)
#     print(res)

# eve_nums()


# 7. Write a function to convert Celsius to Fahrenheit. The function should accept a temperature
# in Celsius as a parameter and return the equivalent temperature in Fahrenheit.

# def temp(c):
#     f = c*(9/5)+32
#     return f
# celsius = int(input("Enter temperature in celsius: "))

# fahrenheit = temp(celsius)
# print(fahrenheit)


# 8. Define a function that takes no parameters and prints the current date and time.  

# PENDING


# 9. Implement a function to calculate the area of a rectangle. The function should
# take the length and width as parameters and return the area. 

# def area_rectangle(length,width):
#     return length*width
# l = int(input("Enter length of rectangle: "))
# w = int(input("Enter width of rectangle: "))

# area = area_rectangle(l,w)
# print(area)


# 10. Write a function to check if a string is a palindrome. The function
# should take a string as input and return True or False.  

# def palindrome():
#     if s == s[::-1]:
#         return True
#     else:
#         return False
# s = input("Enter a string: ")

# print(palindrome())


# 11. Create a function that takes a list of numbers and returns the largest number in the list.  

# num= input("Enter a list of numbers: ").split(',')
# def largest():
#     la = 0
#     for i in num:
#         i = int(i)
#         if i>la:
#             la=i
#     print(la)
# print(largest())


# 12. Write a function that accepts a list of words and returns a dictionary
# with each word as the key and its length as the value.  

# def dict_len():
#     s = input("Enter a string: ").lower()
#     d = {}
#     for i in s:
#         if i in d:
#             d[i] += 1
#         else:
#             d[i] = 1
#     return d

# print(dict_len())


# 13. Define a function that takes a number as input and prints all its factors
#  The function should not return any value.  

# def factors():
#     num = int(input("Enter a number: "))
#     l = []
#     for i in range(1,num+1):
#         if num%i == 0:
#             l.append(i)
#     print(l)

# factors()


# 14. Create a function that takes two numbers and an operator (as a string: "+", "-", "*", "/")
# as input and performs the corresponding arithmetic operation. Return the result.

# n1 = int(input("Enter first number: "))
# n2 = int(input("Enter first number: "))
# op = input("Enter operator: ")

# def operation():
#     if op == '+':
#         c = n1+n2
#     elif op == '-':
#         c = n1-n2
#     elif op == '*':
#         c = n1*n2
#     elif op == '/':
#         c = n1/n2
#     return c

# print(operation())


# 15. Write a function to calculate the sum of squares of the first n natural numbers.
# The function should take n as a parameter and return the result.
