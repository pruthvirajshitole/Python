# 1.Create a BankAccount class with a constructor that initializes the account holder's name 
# and initial balance. Implement methods to deposit and withdraw money.

# class BankAccount:
#     def __init__(self,name,bal):
#         self.name = name
#         self.bal = bal
    
#     def deposit(self):
#         dep = float(input("Enter the amount to deposit: "))
#         self.bal += dep
#         print(f'Available Balance is: {self.bal}')
        
#     def withdraw(self):
#         wit = float(input("Enter the amount you wanted to withdraw: "))
#         if wit <= self.bal:
#             self.bal -= wit
#         else:
#             print("Insufficient Balance to withdraw.")
#         print(f"Available Balance : {self.bal}")

# c = BankAccount('Lucy',1000)
# c.deposit()
# c.withdraw()

    
# 2.Create a Student class with a constructor that takes the student's name and marks in three subjects. 
# Implement a method to calculate the average marks and determine the grade based on the average.

# class Student:
#     def __init__(self,name,m1,m2,m3):
#         self.name = name
#         self.m1 = m1
#         self.m2 = m2
#         self.m3 = m3
    
#     def average(self):
#         self.avg_marks = (self.m1+self.m2+self.m3)/3
#         print(f"The average marks are: {self.avg_marks}")
    
#     def grade(self):
#         if self.avg_marks > 90:
#             print(f"Student have secured grade: A")
#         elif self.avg_marks > 80 and self.avg_marks <= 90:
#             print(f"Student have secured grade: B")
#         elif self.avg_marks > 70 and self.avg_marks <= 80:
#             print(f"Student have secured grade: C")
#         else:
#             print("Fail")

# s = Student('Lucy',89,78,99)
# s.average()
# s.grade()


# 3.Create a Rectangle class with a constructor that initializes the length and width. 
# Implement methods to calculate the area and perimeter of the rectangle

# class Rectangle:
#     def __init__(self,length,width):
#         self.length = length
#         self.width = width
    
#     def perimeter(self):
#         print(f'Perimeter of rectangle is : {2*(self.length+self.width)}')
    
#     def area(self):
#         print(f"Area of rectangle : {self.length*self.width}")

# r = Rectangle(2,4)
# r.perimeter()
# r.area()


# 4.Create an Employee class that has a constructor accepting name, designation, and salary. 
# Implement a method to increase the salary by a given percentage.

# class Employee:
#     def __init__(self,name,designation,salary):
#         self.name = name
#         self.designation = designation
#         self.salary = salary
    
#     def increase_salary(self,percentage):
#         self.salary += self.salary*(percentage/100)
#         print(f"Total salary after increment: {self.salary}")
# e = Employee('Lucy','Junior Engg',10000)
# e.increase_salary(10)


# 5.Create a NumberCheck class with a constructor (__init__) that initializes a number.
# and check a Number is Armstrong or not. Disply in a method.

# class NumberCheck:
#     def __init__(self,num):
#         self.num = num
#     def armstrong(self):
#         temp = self.num
#         l = len(str(temp))
#         sum = 0
#         while temp!=0:
#             d = temp%10
#             sum += d**l
#             temp = temp//10

#         if sum == self.num:
#             print(f"It's an armstrong number.")
#         else:
#             print(f"It's Not an armstrong number.")

# n = NumberCheck(153)
# n.armstrong()


class NumberCheck:
    pass
print(id(NumberCheck))
print(type(NumberCheck))
