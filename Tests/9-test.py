# ----THEORY QUESTIONS-----

# 1.What are the benefits of using list comprehensions over traditional for loops? Provide examples.

# Ans: List comprehensions provide more efficient and readable code which is simple and short so the 
#      list comprehension are useful over traditional for loops.
# Example:
# l = [1,2,3,4,5,6]
# even = []
# for i in l:
#     if i%2==0:
#         even.append(i)
# print(even)

# com_even = [i for i in l if i%2==0]
# print(com_even)


# 2.How do you handle multiple exceptions in a single try block? Provide an example.

# Ans: By using multiple except statement
# Example
# try:
#     num = int(input("Enter a number: "))
#     result = 10 / num
# except ValueError:
#     print("You must enter a valid number!")
# except ZeroDivisionError:
#     print("Cannot divide by zero!")


# 3.Explain the concept of file pointers and how they are managed in Python.

# PENDING


# 4.What are the advantages of using a tuple over a list?

# Ans: Tuple are immutable so once we created it we can't change it anymore, so it provides a
#      data security to the data while list is mutable, so it can change the important data.


# 5.Discuss the difference between a shallow copy and a deep copy of a list. Provide examples.

# Shallow copy: changes in original will not affect in copy.
# l = [1,2,3,4]
# l1 = l.copy()
# l2 = l1

# Deep copy: changes in one will affect in its copy
# l2.append(12)
# l.append(100)
# print('Original list:',l)
# print('Deep copy:',l2)


# 6.What are raw strings in Python and how are they useful? Provide examples.

# PENDING


# 7.Explain the concept of polymorphism in Python with examples.

# Ans: Polymorphism is the concept of existing multiple forms of a single or same method.
#      for example Drone, Birds, Insects, Aeroplane all can have a function fly but all
#      excecutes that function in a differently.


# 8.What is encapsulation in OOP and how does Python achieve it?

# Ans: Encapsulation is the process of bundling or binding the classes and objects in a single unit.
#      Python achieves encapsulation using controlled method like getters and setters to access the
#      attributes and methods there is a controlled manner which must have to follow.


# 9.What is the role of the '__init__' method in Python classes?

# Ans: '__init__' method in python is known as constructor or magical method which automatically excecutes
#       whenever object of that perticular class is created. There is no need to call it explicitly like
#       other normal methods.


# 10.Explain the use of decorators in Python with examples.

# Ans: Decorators provides the ability to enhance a function without changing its internal implementation.
#      Decorators are used in processes like authentication, logins and many more.


# 11.What is the difference between a class method and a static method in Python?

# Ans: class method is created with @classmethod decorator and static method is created using @staticmethod
#      decorator. class methdo takes 'cls' argument whereas static method accepts arguments same as normal 
#      methods


# 12.Explain the concept of inheritance in Python. How does the 'super()' function work?

# Ans: Inheritance is the process of accessing attributes and methods from one class to another class.
#      super() function is used to overcome the issue of method overriding by using super() function we
#      can access the methods with same name in both parent and child classes.


# 13.How can you efficiently read large files in Python without loading the entire file into memory?

# PENDING


# 14.Explain the purpose of the finally block in exception handling.

# Ans: Finally block is executed it is not dependent on other exceptions like try and except blocks.


# 15.Describe the different types of exceptions in Python. How can you create custom exceptions?

# Ans: Try: let you test the block of code
#      Except: let you handle the error/exception
#      finally: let you excecute the block of code regardless of the result of try except
#      else: let you excecute the block of code if there will be no error in try




# -----PRACTICAL QUESTIONS------

# 1.Write a function that reads an integer from the user and raises a custom exception if the number is not in the range 1-100. 
# Handle the exception and prompt the user until a valid number is entered.

# def check_range(number):
#     if number < 1 or number > 100:
#         raise Exception("Number must be between 1 and 100.")

# def get_valid_number():
#     while True:
#         try:
#             num = int(input("Enter a number between 1 and 100: "))
#             check_range(num)
#             print(f"Valid number entered: {num}")
#             return num
#         except ValueError:
#             print("Invalid input! Please enter an integer.")
#         except Exception as e:
#             print(e)

# get_valid_number()


# 2.Write a function that accepts a list of integers and returns a list of integers where each element is the square of the original list element, 
# but only include squares of even numbers.

# def sqrs(l):
#     sq = [i**2 for i in l if i%2==0]
#     print(sq)
# sqrs([2,4,7,9,6,12,25])


# 3.Write a Python function that attempts to divide two numbers, catching and handling ZeroDivisionError, TypeError, and custom exceptions for negative input values.

# PENDING


# 4.Write a Python script that counts the number of lines, words, and characters in a given text file.

# PENDING


# 5.Write a function that takes a list of integers and returns the list sorted in ascending order, but with all duplicates removed.

# def sorted_list(l):
#     l = list(set(l))
#     print(sorted(l))
# sorted_list([2,4,7,9,15,4,6,12,252,1])


# 6.Create a function that merges two lists into a dictionary, where the elements of the first list are the keys and the elements of the second list are the values. 
# Handle cases where the lists are of unequal length.

# def merges(l1,l2):
#     print(dict(zip(l1,l2)))

# merges(['Lucifer','Chloe','Amendeil','Linda','Dan'],['Devil','LAPD','Angel','Doctor'])


# 7.Write a function that takes a string and returns a new string with all duplicate characters removed.

# def remove_duplicates(s):
#     new_s = ''
#     for i in s:
#         if i not in new_s:
#             new_s += i
#     return new_s
# print(remove_duplicates('I am a Devil of My World'))


# 8.Write a function that takes a string and returns True if it is a valid palindrome,
# ignoring spaces, punctuation, and case.

# def palindrome(s):
#     s = (s.strip()).lower()
#     if s == s[::-1]:
#         print('Ture')
#     else:
#         print('False')
# palindrome('    Madam')
# palindrome('Sir')


# 9.Create a class 'Library' that maintains a list of books.
# Implement methods to add a book, remove a book, and list all books currently in the library. 
# Ensure proper error handling for cases like trying to remove a book that doesn't exist.

# class Library:
#     def __init__(self):
#         self.books = ['The Girl In Room 105','400 Days','One Night Stand']
    
#     def add_book(self,book):
#         if book not in self.books:
#             self.books.append(book)
#         else:
#             print(f'{book} is already present in library.')
    
#     def remove_book(self,book):
#         if book in self.books:
#             self.books.remove(book)
#         else:
#             print(f'{book} is not present in library.')

#     def all_books(self):
#         print(f'All books: {self.books}')

# b = Library()

# b.all_books()

# b.add_book('The Last Lie')
# b.all_books()

# b.add_book('The Last Lie')
# b.all_books()

# b.remove_book('The Last Lie')
# b.all_books()

# b.remove_book('The Last Lie')


# 10.Write a function that accepts a list of integers and returns a list of the first n Fibonacci numbers,
# where n is the length of the input list.

# def fibonacci(l):
#     n = len(l)
#     a,b = 0,1
#     fib = []
#     fib.extend([a,b])
#     while a<n:
#         c = a+b
#         fib.append(c)
#         a,b = b,c
#     return fib
# print(fibonacci([1,2,3,4,5,6,7]))


# 11.Write a function that takes a string and returns a new string with each word
# reversed but the word order preserved.

# def reversed_words(s):
#     res = ''
#     for i in s.split():
#         res += i[::-1]+' '
#     return res
# print(reversed_words('reficuL saw .tneconni'))


# 12.Create a function that takes a string and returns the longest substring without repeating characters.

# s = 'Lucifer mornigstar'
# substrings = []
# for i in range(len(s)):
#     for j in range(i+1,len(s)+1):
#         substrings.append(s[i:j])
# non_repeating = []
# for i in substrings:
#     flag = True
#     for j in i:
#         if i.count(j)>1:
#             flag = False
#             break
    
#     if flag:
#         non_repeating.append(i)
            
# longest = 0
# for i in non_repeating:
#     if len(i)>longest:
#         longest = len(i)
#         longest_substring = i
        
# print(f'Longest substring is: {longest_substring}')


# 13.Define a class Person with attributes for name and age
# Implement a subclass Employee that adds an attribute for salary and a method to 
# calculate the annual bonus (e.g., 10% of salary).

# class Person:
#     def __init__(self,name,age):
#         self.name = name
#         self.age = age

# class Employee(Person):
#     def e_salary(self,salary):
#         self.salary = salary
    
#     def calculate_bonus(self,bonus):
#         print(f'Name: {self.name}\nAge: {self.age}')
#         print(f'Annual bonus: {12*self.salary*(bonus/100)}')

# e = Employee('Virat',36)
# e.e_salary(10000)
# e.calculate_bonus(float(input("Enter the bonus rate: ")))


# 14.Implement a function that generates a random password of a given length.
# The password should include uppercase and lowercase letters, digits,and special characters.

# PENDING


# 15.Create a function that takes a string and returns a dictionary with the frequency count of each character. Ignore case and non-alphabetic characters.

# def characters(s):
#     d = {}
#     for i in s.lower():
#         if i not in d:
#             d[i] = 1
#         else:
#             d[i] += 1
#     return d
# print(characters('Lucifer was innocent.'))