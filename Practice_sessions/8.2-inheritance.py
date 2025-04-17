# 1.Wap create a parent class that takes a list and finds min and max number and 
# make a child class and print a table of that max and min number.

# class Parent:
#     def __init__(self,l):
#         self.l = l
    
#     def min_max(self):
#         self.min = min(self.l)
#         self.max = max(self.l)

# class Child(Parent):

#     def display(self):
#         print('-----table of min-----')
#         for i in range(1,11):
#             print(f'{self.min}*{i}={self.min*i}')

#         print('-----table of max-----')
#         for i in range(1,11):
#             print(f'{self.max}*{i}={self.max*i}')

# l = [54,675,75,3,4]

# c = Child(l)
# c.min_max()
# c.display()


# 2.Create a class that takes a list of integers and calculates the sum and average.
# Then create a derived class that prints the sum and average and also prints the square of sum and square of average.

# class Integers:
#     def __init__(self,l):
#         self.l = l
#         self.total = 0
    
#     def sum(self):
#         self.total = sum(self.l)

#     def avg(self):
#         self.avg_value = self.total/len(self.l)
        
# class Display(Integers):

#     def show(self):
#         print(f'''Sum: {self.total}
# Average: {self.avg_value}
# Square of Sum: {self.total**2}
# Square of Average: {self.avg_value**2}''')

# l = [1,2,3,4,5,6,7,8,9]
# i = Display(l)
# i.sum()
# i.avg()
# i.show()


# 3.Create a class that takes a string and counts the number of vowels and consonants. 
# then create a derived class that prints these counts and also prints the string in reverse.

# class String:
#     def __init__(self,s):
#         self.s = s
#         self.vowel_count,self.consonant_count = 0,0

#     def count_chars(self):
#         vowels = 'aeiouAEIOU'
#         for i in self.s:
#             if i in vowels:
#                 self.vowel_count += 1
#             elif i == ' ':
#                 continue
#             else:
#                 self.consonant_count += 1

# class Display(String):
#     def show(self):
#         print(f'Vowels: {self.vowel_count}\nConsonants: {self.consonant_count}')
    
#     def reverse(self):
#         print(self.s[::-1])

# a = Display('Good Morning')
# a.count_chars()
# a.show()
# a.reverse()


# 4.Create a class that takes a string and checks whether it is a palindrome.
# Then, create a derived class that also counts the number of uppercase and lowercase letters.

# class Palindrome:
#     def __init__(self,s):
#         self.s = s
    
#     def check_palindrome(self):
#         if self.s == self.s[::-1]:
#             print("It's a Palindrome.")
#         else:
#             print("It's Not a Palindrome.")

# class CaseCount(Palindrome):

#     def count_char_case(self):
#         self.upper_count, self.lower_count = 0,0
#         for i in self.s:
#             if i.isupper():
#                 self.upper_count += 1
#             else:
#                 self.lower_count += 1
#         print(f'Upper count: {self.upper_count}\nLower count: {self.lower_count}')

# p = CaseCount(' MadaM ')
# p.check_palindrome()
# p.count_char_case()


# 5.Create a class that takes a list of numbers and finds the even and odd numbers separately.
# Then, create a derived class that prints these even and odd numbers in ascending and descending order, respectively.

# class Numbers:

#     def __init__(self,l):
#         self.l = l
#         self.even, self.odd = [],[]
    
#     def even_odd(self):
#         for i in self.l:
#             if i%2==0:
#                 self.even.append(i)
#             else:
#                 self.odd.append(i)

# class Display(Numbers):

#     def show(self):
#         print(f'''Even numbers in ascending order: {sorted(self.even)}
# Even numbers in descending order: {sorted(self.even, reverse = True)}
# Odd numbers in ascending order: {sorted(self.odd)}
# Odd numbers in descending order: {sorted(self.odd, reverse = True)}''')

# n = Display([54,65,21,45,76])
# n.even_odd()
# n.show()

# 6.Create a class Employee that takes an employee's name and salary.
# Then, create a derived class that calculates the tax on the salary (assuming a fixed percentage) and prints the net salary.

# class Employee:
#     def __init__(self,name,salary):
#         self.name = name
#         self.salary = salary
    
# class Tax(Employee):
#     def tax(self):
#         tax = self.salary*(18/100)
#         net_salary = self.salary-tax
#         print(f"Net salary of Emplyoyee: {net_salary}")

# e = Tax('Dan',10000)
# e.tax()


# 7.Create a class Student that takes a student's name and marks in five subjects.
# Then, create a derived class that calculates the total, percentage, and grade.

# class Student:
#     def __init__(self,name,m1,m2,m3,m4,m5):
#         self.name = name
#         self.m1 = m1
#         self.m2 = m2
#         self.m3 = m3
#         self.m4 = m4
#         self.m5 = m5
    
# class Calculations(Student):

#     def marks_sheet(self):
#         total = self.m1 + self.m2 + self.m3 + self.m4 + self.m5
#         percentage = total/5
#         print(f'Total marks: {total}\nPercentage: {percentage}')
#         if percentage > 90:
#             print("A grade")
#         elif percentage > 80 and percentage <= 90:
#             print("B grade")
#         elif percentage > 70 and percentage <= 80:
#             print("C grade")
#         elif percentage > 60 and percentage <= 70:
#             print("D grade")
#         else:
#             print("Fail")

# s1 = Calculations('Andy',87,89,55,76,99)
# s1.marks_sheet()


# 8.Create a class that takes a list of words and finds the longest and shortest words. 
#   Then create a derived class that prints these words and also prints their lengths.

# class Words:
#     def __init__(self,l):
#         self.l = l

#     def longest_word(self):
#         self.longest = 0
#         for i in self.l:
#             if len(i)>self.longest:
#                 self.longest = len(i)
#                 self.longest_word_is = i
    
#     def shortest_word(self):
#         self.shortest = float('inf')
#         for i in self.l:
#             if len(i)<self.shortest:
#                 self.shortest = len(i)
#                 self.shortest_word_is = i

# class Display(Words):
#     def show(self):
#         print("Longest word:",self.longest_word_is,';',"with length:",self.longest)
#         print("Shortest word:",self.shortest_word_is,';',"With length:",self.shortest)

# w = Display(['apple','tom','jerryeee','hell'])
# w.longest_word()     
# w.shortest_word()
# w.show()


# 9.Create a class that takes a list of tuples representing (name, age) and finds the oldest and youngest persons. 
#   Then create a derived class that prints these persons.

# class Person:
#     def __init__(self,l):
#         self.l = l
#         self.ages = {}
#         for name,age in self.l:
#             self.ages[age] = name

#     def role(self):
#         self.oldest_person = max(self.ages.keys())
#         self.youngest_person = min(self.ages.keys())

# class Display(Person):
#     def show(self):
#         print(f'''Youngest: {self.ages[self.youngest_person]}
# Oldest: {self.ages[self.oldest_person]}''')
    
# p = Display([('Lucy',13),('Dan',20),('Linda',108),('Lofez',3)])
# p.role()
# p.show()

    
# 10.Create a class that takes a list of temperatures and finds the highest and lowest temperatures. 
# Then create a derived class that prints the highest and lowest temperatures
# and also prints the temperature range.

class Temperature:
    def __init__(self,l):
        self.l = l
    
    def conditons(self):
        self.high = max(self.l)
        self.low = min(self.l)

class Display(Temperature):
    def show(self):
        print(f'Highest temp: {self.high}\nLowest temp: {self.low}')
        print(f'Temp range is between {self.low} to {self.high}')

t = Display([43,34,33,38,52,32,15])
t.conditons()
t.show()