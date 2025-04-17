# Section A: Theory (10 Questions)

# Q1.Explain the features of Python.
# Ans: -High level language
#      -Dinamically typed language
#      -Simple syntax and ease of use
#      -Interpreted language
#      -Object Oriented language


# Q2.What is Garbage Collection.
# PENDING TOPIC 


# Q3.What are Python’s mutable and immutable types?
# Ans: Mutable - we can edit or change the elements.
#      Immutable - changes are not possible.


# Q4.Difference between Deep copy and Shallow copy?
# PENDING TOPIC


# Q5.What is a Python module?  
# Ans: Python module is library with massive number of functions and tools.

# Q6.What are Python's built-in functions?
# Ans: The functions which are already present in python no need to redefine them again.


# Q7.How does Python’s `set` handle duplicate values?
# Ans: Python's 'set'  does not allow duplicate values. If we try to enter multiple duplicates then it will treat as a single value.

# Q8.What is the difference between `*args` and `**kwargs`?
# Ans: *args is multiple length arguments.
#      **kwargs are multiple length keyword arguments.


# Q9.What is Python Operators, and Describe it?
# Ans: Python Operators are use to perform operations on any values or variables.
#     There multiple type of operators: 
#     +, -, =, ==, !=, <, >, <=, >=, *, / , //, %, |, &.


# Q10.What is the difference between a list and a tuple?  
# Ans: List is mutable and tuple is immutable



                                                  
# Section B: Correct the Code (10 Questions)

# Q1.

# num = int(input("Enter a number: "))
# if num > 0:
#     print("Positive number")
# elif num < 0:
#     print("Negative number")
# else:
#     print("Zero")

# NO CORRECTION NEEDED


# Q2.

# char = input("Enter a character: ").lower()
# if char in 'aeiou':
#     print("Vowel")
# elif char.isalpha():
#     print("Consonant")
# else:
#     print("Invalid input")

# NO CORRECTION NEEDED


# Q3.

# my_list = [1, 2, 3, 4]
# for i in range(5):
#     print(my_list[i])

# CORRECTED CODE:
# my_list = [1, 2, 3, 4]
# for i in range(4):
#     print(my_list[i])


# Q4. 

# num1 = float(input("Enter first number: "))
# num2 = float(input("Enter second number: "))
# operation = input("Enter operation (+, -, *, /): ")

# if operation == '+':
#     print(f"Result: {num1 + num2}")
# elif operation == '-':
#     print(f"Result: {num1 - num2}")
# elif operation == '*':
#     print(f"Result: {num1 * num2}")
# elif operation == '/':
#     if num2 != 0:
#         print(f"Result: {num1 / num2}")
#     else:
#         print("Division by zero is not allowed")
# else:
#     print("Invalid operation")

# NO CORRECTION NEEDED



# Q5.

# a = int(input("Enter first number: "))
# b = int(input("Enter second number: "))
# c = int(input("Enter third number: "))

# if a >= b and a >= c:
#     print(f"The largest number is {a}")
# elif b >= a and b >= c:
#     print(f"The largest number is {b}")
# else:
#     print(f"The largest number is {c}")

# NO CORRECTION NEEDED



# Q6.

# def calculate_area(length, breadth):  
#     area = length * breadth  
#     print("The area of the rectangle is: ", area)  
# calculate_area(10)

# CORRECTED CODE:

# def calculate_area(length, breadth):  
#     area = length * breadth  
#     print("The area of the rectangle is: ", area)  
# calculate_area(10,2)


# Q7.

# num = int(input("Enter a number: "))
# if num > 1:
#     for i in range(2, int(num ** 0.5) + 1):
#         if num % i == 0:
#             print(f"{num} is not a prime number")
#             break
#     else:
#         print(f"{num} is a prime number")
# else:
#     print(f"{num} is not a prime number")

# NO CORRECTION NEEDED


# Q8.

# result = reduce(lambda x, y: x + y, [1, 2, 3, 4, 5])
# print("Sum: " + result)

# CORRECTED CODE:

# import functools as f
# result = f.reduce(lambda x, y: x + y, [1, 2, 3, 4, 5])
# print("Sum: ",+ result)


# Q9.

# text = input("Enter a string: ")
# if text == text[::-1]:
#     print(f'"{text}" is a palindrome')
# else:
#     print(f'"{text}" is not a palindrome')

# NO CORRECTION NEEDED


# Q10.

# def add(a, b, c):
#     return a + b + c

# result = add(5, 10)
# print("Result: ", result)

# CORRECTED CODE
# def add(a, b, c):
#     return a + b + c

# result = add(5, 10, 15)
# print("Result: ", result)




# Section C: Write Code For (10 Questions)

# Q1.Check the number is Automorphic or not?
# PENDING


# Q2.WAP to take input and print perimeter of square?

# side = int(input("Enter side of a squre: "))
# perimeter = 4*side
# print(f"perimeter of the square with side {side} is {perimeter}")


# Q3.WAP to take a list and print the even numbers between 50 to 100.

# Q4.Sort the list in descending order.

# Q5.Create a dictionary with keys as numbers from 1 to 5 and values as their squares.

# Q6.Unpack the tuple into three variables.

# Q7.WAP print all the palindrom items from the list.
#    l=[12,121,789,414,111,99,56,567,191]

# Q8.Pattern:
# *       
# * *     
# * * *   
# * * * * 
# * * * 
# * *   
# *  

# for i in range(1,8):
#     for j in range(1,5):
#         if j<=i and i<=4:
#             print('*',end="")
#         elif j<=8-i and i>=4:
#             print('*',end="")
#         else:
#             print(" ",end="")
#     print()
       

# Q9.All the even itmes shoud be in left side and odd items should be in right side.

# Q10.Write a program to count the occurrence of each element in a list and store it in a dictionary.