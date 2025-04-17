# class Students:
#     company = 'Codenera'

#     def __init__(self,name,city):
#         self.name = name
#         self.city = city

#     def display(self):
#         print(f'Name: {self.name}\nCity: {self.city}')

#     @classmethod
#     def show(cls):
#         print(f'Comapamy: {cls.company}')
    
#     @staticmethod
#     def static_view():
#         print('I am Static method.')

# print('-----Instancemethod-----')
# s = Students('Lucifer','Hell')
# s.display()

# print('-----Classmethod-----')
# Students.show()

# print('-----Staticmethod-----')
# Students.static_view()


# 1.Write a Python class Student with instance variables name and marks. 
# Add an instance method display() that prints the student's details.


# class Student:
#     def __init__(self,name,marks):
#         self.name = name
#         self.marks = marks
    
#     def display(self):
#         print(f'Name: {self.name}\nMarks: {self.marks}')

# s = Student('Lucifer','09')
# s.display()


# 2.Modify the Student class to include a method update_marks(new_marks),
# which updates the marks of a student.

# class Student:
#     def __init__(self,name,marks):
#         self.name = name
#         self.marks = marks
    
#     def display(self):
#         print(f'Name: {self.name}\nMarks: {self.marks}')

#     def update_marks(self,new_marks):
#         self.new_marks = new_marks
#         print(f'Updated Marks: {self.new_marks}')

# s = Student('Lucifer','09')
# s.display()
# s.update_marks(99)


# 3.Define a class Company with a class variable company_name = "TechCorp". 
# Add a class method set_company_name(cls, new_name) to change the company name.

# class Company:
#     company_name = "TechCorp"

#     @classmethod
#     def set_company_name(cls,new_name):
#         cls.company_name = new_name
#         print(f'Updated Company Name: {cls.company_name}')

# Company.set_company_name("TechHell")


# 4.Create a class Person with name and age attributes.
# Add a class method from_birth_year(cls, name, birth_year) that calculates the age from the birth year.

# class Person:
#     def __init__(self,name,age):
#         self.name = name
#         self.age = age

#     @classmethod
#     def from_birth_year(cls,name,birth_year):
#         cls.name = name
#         cls.birth_year = birth_year
#         age = 2025-cls.birth_year
#         print(f'Name: {cls.name}\nAge: {age}')

# p = Person("Tom",20)
# Person.from_birth_year('Lucy',2003)


# 5.Define a class MathOperations that includes a static method
# add(x, y) which returns the sum of x and y.

# class MathOperations:
#     @staticmethod
#     def add(x,y):
#         return x+y
    
# print(MathOperations.add(2,3))


# 6.Create a class Vehicle with:
# --Instance attributes brand and model.
# --A class method set_default_brand(cls, brand_name).
# --A static method is_motor_vehicle(wheels) that returns True if wheels > 2.

# class Vehicle:
#     def __init__(self,brand,model):
#         self.brand = brand
#         self.model = model
    
#     @classmethod
#     def set_default_brand(cls,brand_name):
#         cls.brand = brand_name
#         print(f'default brand: {cls.brand}')

#     @staticmethod
#     def is_motor_vehicle(wheels):
#         if wheels>2:
#             return True
#         else:
#             return False
        
# Vehicle.set_default_brand('Tesla')
# print(Vehicle.is_motor_vehicle(3))


# 7.Define a class Car with an instance variable model.
# Use a class variable count to track the number of car instances and a class method get_count() to return the count.

class Car:
    count = 0
    def __init__(self,model):
        self.model = model
        Car.count += 1

    @classmethod
    def get_count(cls):
        return cls.count

c1 = Car("Tata")
c2 = Car("Tesla")
c3 = Car("Hyundai")
print(Car.get_count())


# 8.Create a class User with an instance variable username.
# Implement a static method is_valid_username(username) that checks
# if a username is at least 5 characters long.

# class User:
#     def __init__(self,username):
#         self.username = username

#     @staticmethod
#     def is_valid_username(username):
#         if len(username) >= 5:
#             print(True)
#         else:
#             print(False)

# User.is_valid_username('Amendeil')
