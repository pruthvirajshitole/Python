# Section A: Theory (10 Questions)

# Q1. What is slicing in python? Brief it.
# Ans: Slicing refered to extracting or getting a small part of the whole iterable in required manner.
# We can perform slicing on all type of sequences like list,tuple,set,dictionary and string.


# Q2. What is Keywords in python?
# Ans: Keywords are predifined keys or name of functional word which we can't used to name a variable or function.


# Q3. What is break, continue, pass in python?
# Ans:
# break- it is used to teminate from a loop.
# continue- it is used to skip or ignore the specific iterations or conditions in a loop.
# pass- it is used to create a empty function or loops in python which we can be useful in future.


# Q4. What is an iterator in Python?
# Ans: Iterator is the one which can used to perform iterations on different datatypes.


# Q5. What is Dyanamically Typed language?
# Ans: Dynamically typed language means there is no need to define the type of variable created in python
# Python handles it itself.


# Q6. When should you use lambda functions in Python?
# Ans: When there is no need of creating a function for one line or one single expression we can use lambda fuctions.


# Q7. What is negative indexes and why are they used?
# Ans: Negative indexes are the indexes used when the sequence is too long or lenght of sequence in unknow but 
# we need to access the elements at or from end.


# Q8. What is join() and split() function in python?
# Ans: join() is used to join all the sequence with the occurence of special character or word.
# split() is used to split all sequence with the occurence of special character or word.


# Q9. Explain difference between discard() and remove()?
# Ans: dicard() and remove() are the fuctions use to remove items or elements from a set.
# If you want to remove an element which is not present in the set then remove() will raise an error
# but discard() will not raise any error.


# Q10. What is module?
# Ans: Module is file whis may contain functions and methods which can be imported to another file or folder
# where we can use the functions present in the imported module without defining or creating it in a current
# file. to use it only we have to call it by using module name and function name.



# Section B: Correct the Code (10 Questions)

# Q1.

# age = input("Enter your age: ")

# if age >= 18:
# print("You are eligible to vote.")
# elif age < 18:
# print("You are not eligible to vote.")
# else
# print("Invalid input.")

# CORRECTED CODE:

# age = int(input("Enter your age: "))

# if age >= 18:
#     print("You are eligible to vote.")
# elif age < 18:
#     print("You are not eligible to vote.")
# else:
#     print("Invalid input.")


# Q2. What will be the output of this code?
   
#    x = 10
#    for i in range(x):
#        if i % 2 == 0:
#            continue
#        print(i)

# Output:
# There is Indentation error but if we ignore it
# We will get odd numbers: 1,3,5,7,9


# Q3.The following code contains an error. Identify and correct it:

# def my_func(x, y):
#     return x + y
# result = my_func(5)
# print(result)

# CORRECTED CODE:

# def my_func(x, y):
#     return x + y
# result = my_func(5,2)
# print(result)


# Q4. What will be the output of this code?
   
#    x = 10
#    for i in range(x):
#        if i % 2 == 0:
#            continue
#        print(i)

# OUTPUT:
# We will get odd numbers: 1,3,5,7,9


# Q5. What will be the output of this code?
   
#    a = (1, 2, 3)
#    b = list(a)
#    b.append(4)
#    print(a)

# OUTPUT:
# [1, 2, 3]


# Q6.
# num = int(input("Enter a number: "))  

# if num > 0  
#     print("The number is positive.")  
# elif num = 0:  
#     print("The number is zero.")  
# else:  
#     print("The number is negative.")  

# CORRECTED CODE:

# num = int(input("Enter a number: "))  

# if num > 0:  
#     print("The number is positive.")  
# elif num == 0:  
#     print("The number is zero.")  
# else:  
#     print("The number is negative.")  


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

# CORRECTED CODE:

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
# for i in range(3):  
# for j in range(3):  
#     print("*", end=" ")  
# print()  

# CORRECTED CODE:

# for i in range(3):  
#     for j in range(3):  
#         print("*", end=" ")  
#     print()  


# Q9.
# for i in range(1, 10):  
#     if i % 2 == 0  
#         continue  
#     print(i) 

# CORRECTED CODE:

# for i in range(1, 10):  
#     if i % 2 == 0:  
#         continue  
#     print(i) 


# Q10.
# count = 1  
# while count <= 5  
# print(count)  
#     count = count + 1  

# CORRECTED CODE:

# count = 1  
# while count <= 5:
#     print(count)  
#     count = count + 1  



# Section C: Write Code For (10 Questions) 

# Q1. Write a lambda function to find the square of a given number.

# n = int(input("Enter a number: "))
# print((lambda a:a**2)(n))


# Q2. Write a lambda function that returns "Even" if a number is even and "Odd" if it is odd.

# n = int(input("Enter a number: "))
# def trial():
#     if ((lambda x:x%2==0)(n))==True:
#         return 'Even'
#     else:
#         return 'Odd'
# print(trial())


# Q3. Write a Python program to create a dictionary that stores student names as keys and their scores as values. 
#     Write a function that returns the name of the student with the highest score.

# d = {}
# k = int(input("Enter the number of students: "))
# i = 1
# while i<=k:
#     names = input("Enter the name of student: ")
#     scores = int(input("Enter the score of student: "))
#     if names=='stop':
#         break
#     elif names not in d:
#         d[names] = scores
#     else:
#         print("The name is already exist.")
#     i+=1
# count = 0
# for m in d:
#     if d[m]>count:
#         count = d[m]
#         name = m
# print(f'The name of student with highest score is {name} with score {count}')


# Q4. Write a Python program using map() to double all the numbers in a list.
#     # Input: [1, 2, 3, 4, 5]
#     # Output: [2, 4, 6, 8, 10]

# l = [1, 2, 3, 4, 5]
# print(list(map(lambda x:x*2,l)))


# Q5. Write a Python program using filter() to extract words with more than 5 characters from a list.
#     # Input: ["apple", "banana", "cat", "elephant"]
#     # Output: ["banana", "elephant"]

# l = ["apple", "banana", "cat", "elephant"]
# print(list(filter(lambda x:len(x)>5,l)))


# Q6. Write a Python program using reduce() to find the maximum number in a list.
#     # Input: [3, 7, 2, 8, 5]
#     # Output: 8

# from functools import reduce
# l=[3,7,2,8,5]  
# a=reduce(lambda x,y: x if x>y else y,l)
# print(a)


# Q7. Create a dictionary from two lists.

# l1 = [1,2,3,4,5,6]
# l2 = [1,4,9,16,25,36]
# print(dict(zip(l1,l2)))


# Q8. Given two dictionaries, write a function to find and return a new dictionary containing only
# the common keys and their corresponding values.

# PENDING

# d1 = {'virat':18, 'rohit':45, 'gayle':333 }
# d2 = {'dhobi':7, 'ronaldo':7, 'virat':18, 'gayle':333}
# d = {}
# for i in d1:
#     for j in d2:
#         if i == j:
#             d[i] = d1[i]
# print(d)


# Q9. Print number pyramid:

# 1
# 12
# 123
# 1234
# 12345

# for i in range(1,6):
#     for j in range(1,i+1):
#         print(j,end='')
#     print()


# Q10. Given a dictionary marks = {'Math': 90, 'Science': 85, 'English': 88},
# calculate and print the total marks.

# marks = {'Math': 90, 'Science': 85, 'English': 88}

# total = 0
# for i in marks.values():
#     total += i
# print(total)
