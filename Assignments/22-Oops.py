# 1. Write a function that takes a dictionary where keys are strings and values
# are lists of numbers. The function should return a new dictionary where each key
# is mapped to the sum of squares of its values.  

# d = {'a':[1,2,3], 'bc':[6,5,4], 'c':[9,7,4]}
# def squares(d):
#     l = [(sum(i))**2 for i in d.values()]
#     new_d = {}
#     k=0
#     for j in d:
#         if j not in new_d:
#             new_d[j] = l[k]
#             k+=1
#     print(new_d)
# squares(d)


# 2. Given a dictionary of students and their marks, write a function that returns
# the name of the student with the highest average marks. Use loops and dictionary methods.  

# d = {'omkar':90, 'tom':75, 'uday':95, 'shreyash':35}
# def high_avg(d):
#     high_marks = 0
#     for i,j in d.items():
#         if j>high_marks:
#             high_marks = j
#             student = i
#     return f'{student} scores the highest average marks which are {high_marks}'
# print(high_avg(d))


# 3. Write a function that takes a dictionary of words and their frequencies and returns the
# top N most frequent words. Implement without using built-in sorting functions.  

# PENDING

# d = {'a':3, 'i':1, 'am':2 , 'devil':4, 'of':5, 'world':7 , 'my':6}

# def sorted_dict(d):
#     updated_d = {}
#     for i in range(len(d.values())):
#         for m in range(0,(len(d.values())-i-1)):
#             if d[m]>d[m+1]:
#                 d[m],d[m+1] = d[m+1],d[m]
                

#     return updated_d
# print(sorted_dict(d))


# 4. Implement a function that takes a nested dictionary and flattens it,
# converting nested keys into a single key separated by dots (.).
# Example: {'a': {'b': {'c': 1}}} should become {'a.b.c': 1}.  


# 5. Write a function that takes a dictionary with numeric values and a target sum.
# The function should return all pairs of keys whose corresponding values sum up to the target.  



# 6. Given a dictionary with lists as values, write a function to generate all possible unique pairs of elements from different lists and store them in a new dictionary.  

#    7. Write a function that rotates the keys of a dictionary based on a given number. For example, if the dictionary is {1: 'a', 2: 'b', 3: 'c'} and rotation is 1, the result should be {2: 'a', 3: 'b', 1: 'c'}.  
   
#    8. Define a class Book with attributes title and author. Create a method display that prints the book details. Create two book objects and call the method.  

#    9. Create a class Rectangle with attributes length and width. Define a method area to return the area of the rectangle. Create an instance and print its area.  

#    10. Define a class BankAccount with attributes account_number and balance. Implement a method deposit that adds a given amount to the balance and another method withdraw that deducts an amount (if sufficient balance exists).  

#    11. Write a class Car with an attribute speed. Implement a method increase_speed that increases speed by a given amount and a method decrease_speed that reduces speed. Ensure speed never goes below zero.  

#    12. Create a class Student with attributes name and marks. Implement a method grade that returns 'Pass' if marks are above 40, else 'Fail'.  

#    13. Define a class Circle with an attribute radius. Implement a method circumference that returns the circumference of the circle.  

#    14. Implement a class Employee with attributes name and salary. Create a method display_details that prints the employee's details. Create three employee objects and call the method.  

#    15. Write a class Movie with attributes title and rating. Implement a method is_hit that returns True if the rating is above 7, otherwise False.