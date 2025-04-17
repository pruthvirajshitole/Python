# Q1. What is OPPS? Brief it.

# Ans: OOPS stands for Object Oriented Programing.
#      All things or entites are treated as obejcts which belongs to a class.


# Q2. What is difference between Function and Method.

# Ans: Fuction is a set of statements or instructions which is executed by calling it's name.
#      Where as method is also set of function but it is defined within a class.


# Q3. What is class, brief it.

# Ans: class is blue print of objects. In which different types of methods and variable can be created
#      as instances.


# Q4. Discuss the use of the map, reduce, and filter functions in Python. Provide a brief example for each.

# Ans: map(): map is used to apply functions on iterables. map() takes two arguments which are function
#             and iterable respectively. It returns map object.
#      filter(): filter also takes two arguments function and iterables but it returns only filtered elements
#                from a given sequence. It returns filter object.
#      reduce(): reduce takes two arguments and performs the fuction with returning only a single value
#                which is the evaluated expression


# Q5. Explain the use of try-except blocks. How do they help in handling errors in Python programs?  


# Q6. What is the purpose of return statement in function.

# Ans: return statement in function return the value or output of a function after the excecution of function.


# Q7. What is Inheritance, And types of Inheritance, brief it.

# Ans: Inheritance is concept in which a Child class can inherits the properties or attributes of Parent class.
#      Types:
#      1.Single Inheritance
#      2.Multiple Inheritance
#      3.Multilevel Inheritance
#      4.Hierarchical Inheritance
#      5.Hybrid Inheritance


# Q8. What are nested loops? Describe a real-life scenario where nested loops can be used effectively. 

# Ans: Nested loops are the loops in which a single loop can contain multiple loops under it's body.
#      Ex: If you have to pick a perticular student from a college.
#          Firtst step is to search his division from all the divisions. (first loop)
#          Second step is to search from all students of a perticular division. (again a loop)=>(nested loop)


# Q9. How can you pass arguments to a function in python?

# Ans: after calling function within the paranthesis pass the arguments.


# Q10. Explain the concept of scope in Python with examples of local and global variables.

# Ans: Scope: A scope of variable is starts wherever it is defined.
#      global variable: a vaiable which is accessible any where within a file.
#      local variable: a varible which is accessible only within the function where it is created.


                                                  

# Section B: Write Code For (10 Questions) 

# Q1.Create a function that takes two numbers and checks if they are divisible by each other. 
#    Return a message accordingly.

# n1 = int(input("Enter first number: "))
# n2 = int(input("Enter second number: "))
# if n1%n2 == 0 and n2%n1 == 0:
#     print(f'{n1} and {n2} are divisible by each other')
# else:
#     print(f'{n1} and {n2} are not divisible by each other')


# Q2. You are given a nested list of integers. Write a program to flatten the list 
#     and calculate the sum of all numbers in the flattened list.

# l = [1,[2,4],[5,[4,7],[10]]]
# flatten_list = []
# def flatten(l):
#     for i in l:
#         if isinstance(i,list):
#             flatten(i)
#         else:
#             flatten_list.append(i)
#     return flatten_list
# print(flatten(l))
# print('sum of flattened list is: ',sum(flatten_list))


# Q3. Write a program to find the second largest number in a list without sorting it.

# l = [2,5,7,4,3,8,9,4,35,1]
# largest = float('-inf')
# for i in l:
#     if i>largest:
#         second_largest = largest
#         largest = i
#     elif i>second_largest and i!=largest:
#         second_largest = i
# print("Second largest is: ",second_largest)


# Q4. Write a function that accepts a list of strings and returns the longest string 
#     using the reduce function.  

# from functools import reduce
# l = ['Lucifer','was','innocent','but','he','is','devil']

# def longest(l):
#     print(reduce(lambda x,y:x if len(x)>len(y) else y, l))
# longest(l)


# Q5  Wap take a number from user as an argument and check it is palindrome or not  
#     if no is palindrome then return true else return false using class and object.

# class Palindrome:
#     def checking(self,n):
#         temp = n
#         rev = 0
#         while n!=0:
#             d = n%10
#             rev = 10*rev+d
#             n = n//10
#         if temp == rev:
#             return True
#         else:
#             return False

# obj = Palindrome()
# print(obj.checking(1221))


# Q6. Create a BankAccount class with attribute balance. Then, create a SavingsAccount class that tries
# to access it.

# class BankAccount:
#     def balance(self):
#         self.balance = 100
#         print("balance of BankAccount",self.balance,"What will you do with that much money.")

# class SavingsAccount(BankAccount):
#     def display(self):
#         pass

# a = SavingsAccount()
# a.balance()
      

# Q7. Write a Python class Rectangle with methods to calculate the area and perimeter. 
#     Include a constructor to initialize the length and width.

# class Rectangle:
#     def __init__(self):
#         self.length = int(input("Enter the length: "))
#         self.width = int(input("Enter the width: "))

#     def perimeter(self):
#         print(f'Perimeter of rectangle: {2*(self.length+self.width)}')
    
#     def area(self):
#         print(f'Area of rectangle: {self.length*self.width}')
        
# r = Rectangle()
# r.perimeter()
# r.area()


# Q8. Create an class Shape and calculate area(). Then, create Rectangle and Circle
# classes that implement this method

# from abc import ABC,abstractmethod

# class Shape(ABC):
#     @abstractmethod
#     def area(self):
#         pass

# class Circle(Shape):
#     def area(self,radius):
#         return 3.14*radius*radius

# c = Circle()
# print(c.area(4))

# class Square(Shape):
#     def area(self,breadth,width):
#         return breadth*width

# s = Square()
# print(s.area(2,3))


# Q9. How does Python's super() function work with multiple inheritance? Give example.

# PENDING


# Q10.Take input in constructor and display in method, print frequency of each character of String.
 
# PENDING



# Section C: Correct the Code (10 Questions)

# 1.  
# num = input("Enter a number: ")
# if num % 2 == 0:
#     print("Even number")
# else:
#     print("Odd number")

# CORRECTED CODE

# num = int(input("Enter a number: "))
# if num % 2 == 0:
#     print("Even number")
# else:
#     print("Odd number")

  
# 2.
# num = input("Enter a number: ")
# if num % 2 == 0:
#     print("Even number")
# else:
#     print("Odd number")

# CORRECTED CODE

# my_list = [1, 2, 3, 4]
# for i in range(4):
#     print(my_list[i])

  
# 3.  
# def add_numbers(a,b):
#     result = a+b
# print(result)

# CORRECTED CODE

# def add_numbers(a, b):
#     result = a + b
#     print(result)
# ad = add_numbers(1,2)


# 4.  
# numbers = [1, 2, 3, 4, 5]
# squared = map(lambda x: x ** 2, numbers)
# print(squared)

# CORRECTED CODE

# numbers = [1, 2, 3, 4, 5]
# squared = list(map(lambda x: x ** 2, numbers))
# print(squared)
  

# 5.
# def calculate_area(radius):
#     return 3.14 * radius ** 2
# area = calculate_area()
# print(area)

# CORRECTED CODE

# def calculate_area(radius):
#     return 3.14 * radius ** 2
# area = calculate_area(10)
# print(area)

  
# 6.
# data = [10, 20, 30, 40]
# for value in data:
#     if value > 20:
#         print("Value: ", value)
#     else:
#         break

# CORRECTED CODE 

# data = [10, 20, 30, 40]
# for value in data:
#     if value > 20:
#         print("Value: ", value)
#     else:
#         pass

  
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

# CORRECTED CODE

# text = "Hello World"
# print(text[:])

  
# 9.
# result = reduce(lambda x, y: x + y, [1, 2, 3, 4, 5])
# print("Sum: " + result)

# CORRECTED CODE

# from functools import reduce
# result = reduce(lambda x, y: x + y, [1, 2, 3, 4, 5])
# print("Sum: ", result)
  

# 10.  
# def add(a, b, c):
#     return a + b + c
# result = add(5, 10)
# print("Result: ", result)

# CORRECTED CODE

def add(a, b, c):
    return a + b + c
result = add(5, 10, 15)
print("Result: ", result)
