# Section A: Theory (10 Questions)

# Q1. What is OPPS? Brief it.

# OOP stands for Object-Oriented Programming.
# It is a programming paradigm that uses objects and classes in programming.


# Q2. What is difference between Function and Method.

# A function is a piece of code that is called by name.
# It can be passed data to operate on (i.e. the parameters) and can optionally return data (the return value).
# All data that is passed to a function is explicitly passed.
# A method is a piece of code that is called by a name that is associated with an object.
# In most respects it is identical to a function except for two key differences:
# A method is implicitly passed the object on which it was called.


# Q3. What is class, brief it.

# A class is a blueprint for creating objects (a particular data structure),
# providing initial values for state (member variables or attributes),
# and implementations of behavior (member functions or methods).


# Q4. Discuss the use of the map, reduce, and filter functions in Python. Provide a brief example for each.

# map() function returns a map object(which is an iterator) of the results after applying the given
# function to each item of a given iterable (list, tuple etc.)
# reduce() function is for performing some computation on a list and returning the result.
# filter() function constructs an iterator from elements of an iterable for which a function returns true.


# Q5. Explain the use of try-except blocks. How do they help in handling errors in Python programs?

# The try block lets you test a block of code for errors.
# The except block lets you handle the error.
# The finally block lets you execute code, regardless of the result of the try- and except blocks.
 

# Q6. What is the purpose of return statement in function.

# The return statement is used to exit a function and go back to the place from where it was called.
# The value of the expression is returned to the caller.


# Q7. What is Inheritance, And types of Inheritance, brief it.

# Inheritance is a mechanism in which one class acquires the property of another class.
# The class that inherits the properties of another class is known as the subclass or derived class.
# The class whose properties are inherited by the subclass is known as the superclass or base class.
# Types of Inheritance:
# 1. Single Inheritance
# 2. Multiple Inheritance
# 3. Multilevel Inheritance
# 4. Hierarchical Inheritance
# 5. Hybrid Inheritance


# Q8. What are nested loops? Describe a real-life scenario where nested loops can be used effectively. 
 
# A nested loop is a loop inside a loop.
# The "inner loop" will be executed one time for each iteration of the "outer loop".
# Real-life scenario where nested loops can be used effectively:
# - Printing a multiplication table.


# Q9. How can you pass arguments to a function in python?

# Arguments are specified after the function name, inside the parentheses.
# You can add as many arguments as you want, just separate them with a comma.
# The arguments are passed by value, which means that if you change the value of the argument within
# the function, it does not get changed in the calling function.


# Q10. Explain the concept of scope in Python with examples of local and global variables.

# A variable is only available from inside the region it is created. This is called scope.
# A variable created inside a function belongs to the local scope of that function,
# and can only be used inside that function.
# A variable created in the main body of the Python code is a global variable and belongs to the global scope.


#--------------------------------------------------------------------------------------------------------------
                                                  
# Section B: Write Code For (10 Questions) 

# Q1.Create a function that takes two numbers and checks if they are divisible by each other. 
#    Return a message accordingly.  

def divisible(a,b):
    if a%b == b%a:
        return f'Both numbers are divisible by each other.'
    else:
        return f'Both numbers are not divisible by each other.'
print(divisible(2,2))


# Q2. You are given a nested list of integers. Write a program to flatten the list 
#     and calculate the sum of all numbers in the flattened list. 

# Q3. Write a program to find the second largest number in a list without sorting it.

# Q4. Write a function that accepts a list of strings and returns the longest string 
#     using the reduce function.  

# Q5  Wap take a number from user as an argument and check it is palindrome or not  
#     if no is palindrome then return true else return false using class and object.

# Q6. Create a BankAccount class with attribute balance. Then, create a SavingsAccount class that tries to access it.

# Q7. Write a Python class Rectangle with methods to calculate the area and perimeter. 
#     Include a constructor to initialize the length and width.

# Q8. Create an class Shape and calculate area(). Then, create Rectangle and Circle classes that implement this method
    
# Q9. How does Python's super() function work with multiple inheritance? Give example.

# Q10.Take input in constructor and display in method, print frequency of each character of String.
 




# Section C: Correct the Code (10 Questions)

# 1.  

# num = input("Enter a number: ")
# if num % 2 == 0:
#     print("Even number")
# else:
#     print("Odd number")
  
# 2.  

# my_list = [1, 2, 3, 4]
# for i in range(5):
#     print(my_list[i])
  
# 3.  

# def add_numbers(a, b):
#     result = a + b
# print(result)
  
# 4.  

# numbers = [1, 2, 3, 4, 5]
# squared = map(lambda x: x ** 2, numbers)
# print(squared)
  
# 5.  

# def calculate_area(radius):
#     return 3.14 * radius ** 2

# area = calculate_area()
# print(area)
  
# 6.  

# data = [10, 20, 30, 40]
# for value in data:
#     if value > 20:
#         print("Value: ", value)
#     else:
#         break
  
# 7.  

# try:
#     num1 = 10
#     num2 = 0
#     result = num1 / num2
# except:
#     print("Error")
  
# 8.  

# text = "Hello World"
# print(text[12])
  
# 9.  

# result = reduce(lambda x, y: x + y, [1, 2, 3, 4, 5])
# print("Sum: " + result)
  
# 10.  

# def add(a, b, c):
#     return a + b + c

# result = add(5, 10)
# print("Result: ", result)
  