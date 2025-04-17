# Section A: Theory (10 Questions)

# Q1. What is slicing in python? Brief it.
# Ans: Slicing means a way to get only the required region or elements from a given iterable or sequence.


# Q2. What is Keywords in python?
# Ans: There are few keywords like def, tuple, etc which we can't use for assigning the name to variables.


# Q3. How can you remove duplicates from a list? Provide at least two methods.
# Ans: We can use typecasting by converting to set. And also by looping the list and removing duplicates by remove() method.


# Q4. What are the main characteristics of a tuple in Python?
# Ans: Tuples are immutable, indexed, ordered, heterogenous, and allows duplicate values.


# Q5. What is the difference between a class and an object in Python?
# Ans: Class is a blueprint of the objects while objects are instances of that class.


# Q6. What are main pillars in OOPS. Brief it.
# Ans: 1-Polymorphism: Multiple form of a single method.
#      2-Inheritance: The process of inheriting or using the attribures or methods of one class by another class.
#      3-Abstraction: Hiding the implementation from the user.
#      4-Encapsulation: The process of wrapping or covering the codes or direct access from user.


# Q7. What is negative indexes and why are they used?
# Ans: Negative indexes are the indexes with negative signs which are used to accessing the elements from end or last.


# Q8. What are Python’s mutable and immutable types?
# Ans: Mutables means after the creation of datatype we can change or update the sequence.
#      Ex: list,set,dictionary
#      Immutable means once the datatype or seaquence is created we can't change them.
#      Ex: tuple,string,float,int

 
# Q9. Explain Python’s list comprehensions.
# Ans: list comprehension is a technique to reduce the size of code and making the program more efficient and readable.


# Q10. What is difference between module and a package?
# Ans: Module is a file with extension '<filename>.py' where multiple methods are defined.
#      Package is the collection of multiple modules in a folder called as directory with '__init__.py' file.



# Section B: Correct the Code (10 Questions)

# Q1.
# num = -5
# if num < 0:
#     print("Negative")
# elif num == 0
#     print("Zero")
# else
#     print("Positive")

# CORRECTED CODE

# num = -5
# if num < 0:
#     print("Negative")
# elif num == 0:
#     print("Zero")
# else:
#     print("Positive")


# Q2. 
# year = 2024
# if (year % 4 == 0 and year % 100 != 0) or year % 400 == 0:
# print(f"{year} is a leap year.")
# else:
# print(f"{year} is not a leap year.")

# CORRECTED CODE

# year = 2024
# if (year % 4 == 0 and year % 100 != 0) or year % 400 == 0:
#     print(f"{year} is a leap year.")
# else:
#     print(f"{year} is not a leap year.")


# Q3.
# a = 10
# b = 20
# c = 15
# if a > b and c:
#     print("The highest number is", a)
# elif b > a and c:
#     print("The highest number is", b)
# else:
#     print("The highest number is", c)

# CORRECTED CODE

# a = 10
# b = 20
# c = 15
# if a > b and a > c:
#     print("The highest number is", a)
# elif b > a and b > c:
#     print("The highest number is", b)
# else:
#     print("The highest number is", c)


# Q4. What will be the output of this code?
   
# x = 10
# for i in range(x):
#     if i % 2 == 0:
#         continue
#     print(i)

# OUTPUT: odd numbers
# 1
# 3
# 5
# 7
# 9


# Q5. 
# for i in range(1, 21):
# if i % 2 == 0:
# print(i)

# CORRECTED CODE

# for i in range(1, 21):
#     if i % 2 == 0:
#         print(i)


# Q6.

# num = 1234
# total = 0
# while num > 0:
#     total += num % 10
#     num = num // 10
# print("Sum of digits:", total) 

# NO CORRECTION NEEDED


# Q7.
# score = int(input("Enter your score: "))  

# if score >= 90  
#     print("Grade: A")  
# elif score >= 80:  
#     print("Grade: B")  
# elif score >= 70:  
#     print("Grade: C")  
# elif score >= 60:  
#     print("Grade: D")  
# else  
#     print("Grade: F") 

# CORRECTED CODE

# score = int(input("Enter your score: "))  

# if score >= 90: 
#     print("Grade: A")  
# elif score >= 80:  
#     print("Grade: B")  
# elif score >= 70:  
#     print("Grade: C")  
# elif score >= 60:  
#     print("Grade: D")  
# else: 
#     print("Grade: F")


# Q8.
# rows = 5
# for i in range(1, rows + 1):
#     for j in range(1, i + 1):
#         print("*", end=' ')
#         j+=1
#     print()
#     i+=1

# CORRECTED CODE

# rows = 5
# for i in range(1, rows + 1):
#     for j in range(1, i + 1):
#         print("*", end=' ')
#         j+=1
#     print()
#     i+=1


# Q9.
# class Car:
# def __init__(self, model):
#     self.model = model
# def describe(self):
#     print("This is a", self.model)

# car = Car("Toyota")
# car.describe()

# CORRECTED CODE

# class Car:
#     def __init__(self, model):
#         self.model = model
#     def describe(self):
#         print("This is a", self.model)

# car = Car("Toyota")
# car.describe()


# Q10.
# class Animal:
# def __init__(self, name):
#     self.name = name
# def speak(self):
#     print("Animal speaks")

# class Dog(Animal):
# def speak(self):
#     print("Woof")

# dog = Dog("Buddy")
# dog.speak()

# CORRECTED CODE

# class Animal:
#     def __init__(self, name):
#         self.name = name
#     def speak(self):
#         print("Animal speaks")

# class Dog(Animal):
#     def speak(self):
#         super().speak()
#         print("Woof")

# dog = Dog("Buddy")
# dog.speak()




# Section C: Write Code For (10 Questions) 

# Q1. Write a Python function to count the frequency of each word in a given text document and return
# a dictionary with word frequencies.

# def frequency(s):
#     d = {}
#     for i in s:
#         if i not in d:
#             d[i] = 1
#         else:
#             d[i] += 1
#     print(d)
# frequency('pruthviraj')


# Q2. Write a lambda function that returns "Even" if a number is even and "Odd" if it is odd.

# n = int(input("Enter a number: "))
# print((lambda x:'Even' if x%2==0 else 'Odd')(n))


# Q3. Write a Python program to create a dictionary that stores student names as keys and their scores as values. 
#     Write a function that returns the name of the student with the highest score.

# d = {}
# k = 1
# while k<=5:
#     name = input("Enter the name of student: ")
#     score = float(input("Enter the score: "))
#     if name not in d:
#         d[name] = score
#     k+=1

# def high_score(d):
#     highest = 0
#     for i,j in d.items():
#         if j>highest:
#             highest = j
#             std = i
#     print(f'The name of hightest scorer is: {std} and the score is: {highest}')

# high_score(d)


# Q4. Develop a function that finds the word with the maximum frequency in a given text document and
# returns the word along with its frequency.

# s = input("Enter the text: ").split(' ')
# d= {}
# for i in s:
#     if i not in d:
#         d[i] = 1
#     else:
#         d[i] += 1
# print(d)
# def high_freq(d):
#     highest = 0
#     for i,j in d.items():
#         if j>highest:
#             highest = j
#             word = i
#     print(f'The name of highest occured word is: {word} and the frequency is: {highest}')
# high_freq(d)


# Q5. Employee Management System – Implement an Employee class with subclasses like Manager and Engineer,
# using inheritance and polymorphism.

# class Employee:
#     def show(self):
#         print('You are working at Codenera.')

# class Manager(Employee):
#     def show(self):
#         super().show()
#         print('You are Manager at Codenera.')
# class Engineer(Employee):
#     def show(self):
#         super().show()
#         print("There is no need of an Engineer at Codenera.")

# e = Employee()
# e.show()

# print('------object of class Manager------')
# m = Manager()
# m.show()

# print('------object of class Engineer------')
# en = Engineer()
# en.show()


# Q6. Write a Python program using reduce() to find the maximum number in a list.
#     # Input: [3, 7, 2, 8, 5]
#     # Output: 8

# from functools import reduce
# l=[3, 7, 2, 8, 5]
# a=reduce(lambda x,y:x if x>y else y,l)
# print(a)


# Q7. Create a dictionary from two lists without using zip function.

# l1=[1,2,3,4,5,6]
# l2=[3,5,7,7,8,5]
# print(dict(zip(l1,l2)))


# Q8. Given two dictionaries, write a function to find and return a new dictionary containing only
# the common keys and their corresponding values.

# d1 = {'a':3, 'b':7, 'c':2, 'k':6}
# d2 = {'a':3, 'd':7, 'c':2}
# d = {}
# for i,j in d1.items():
#     if i in d2.keys():
#         d[i]=j
# print(d)


# Q9. Write a Python class called Circle that has a method to calculate the area and the circumference of the circle.

# class Circle:
#     def area(self,r):
#         area_circle = 3.14*r**2
#         print('area circle:',area_circle)
    
#     def circumference(self,r):
#         circum_circle = 2*3.14*r
#         print('circumferemce of circle:',circum_circle)
# c = Circle()
# c.area(4)
# c.circumference(10)

# Q10. Create a class BankAccount that has the following properties and methods:
#      balance (initially set to 0)
#      deposit(amount) method that adds the amount to the balance
#      withdraw(amount) method that subtracts the amount from the balance
#      display_balance() method to show the current balance
#      A validation check to ensure that withdrawal does not exceed the available balance.
