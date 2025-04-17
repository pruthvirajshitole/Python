# 1. Define a class Person with attributes for name and age.
#    Implement a subclass Employee with attributes emp_id, department.
#    Use method-overiding.

# class Person:

#     def __init__(self,name,age):
#         self.name = name
#         self.age = age
    
#     def display(self):
#         print(f'''Name: {self.name}
# Age: {self.age}''')

# class Employee(Person):

#     def display(self,emp_id,department):
#         self.emp_id = emp_id
#         self.department = department
#         super().display()
#         print(f'''Emp ID: {self.emp_id}
# Department: {self.department}''')

# e = Employee('Samay Raina',30)
# e.display(123321,'Dark Comedian')


# 2. Define a class device brand and price.
#    Implement a subclass laptop with RAM and processor.
#    Overrides a method specification() to display all details.

# class Device:
#     def __init__(self,brand,price):
#         self.brand = brand
#         self.price = price

#     def specification(self):
#         print(f'''
# Brand: {self.brand}
# Price: {self.price}''')

# class Laptop(Device):        
    
#     def specification(self,ram,processor):
#         super().specification()
#         self.ram = ram
#         self.processor = processor
#         print(f'''RAM: {self.ram}
# Processor: {self.processor}''')
        
# l = Laptop('Dell',70000)
# l.specification('16GB','i5')


# 3. Define a class Employee with name,basic_salary.
#    Implement a subclass SalesEmployee with attributes sales_amount and commission_rate,
#    Override calculate_salary() to compute total_salary.

# class Employee:
#     def __init__(self,name,basic_salary):
#         self.name = name
#         self.basic_salary = basic_salary
    
#     def calculate_salary(self):
#         print(f'''Name: {self.name}
# Basic Salary: {self.basic_salary}''')

# class SalesEmployee(Employee):
#     def calculate_salary(self,sales_amount,comission_rate):
#         super().calculate_salary()
#         total_salary = self.basic_salary+(sales_amount*(comission_rate/100))
#         print(f'Total Salary: {total_salary}')

# e = SalesEmployee('Alex',10000)
# e.calculate_salary(5000,20)
        

# 4. Define a class Student has name and marks (list of 3 subjects)
#    Method calculate_percentage() in Student gives average.
#    EngineeringStudent adds 2 more marks (for lab subjects) and overrides percentage logic.
#    Use super().calculate_percentage() to get base average and then compute combined.

# class Student:

#     def __init__(self,name,m1,m2,m3):
#         self.name = name
#         self.m1 = m1
#         self.m2 = m2
#         self.m3 = m3
    
#     def calculate_percentage(self):
#         self.avg = (self.m1+self.m2+self.m3)/3
#         print(f"Base Average: {self.avg}")
    
# class EngineeringStudent(Student):

#     def calculate_percentage(self,m4,m5):
#         super().calculate_percentage()
#         combine_avg = (self.m1+self.m2+self.m3+m4+m5)/5
#         print(f"Combined Average: {combine_avg}")

# e = EngineeringStudent("Samay",34,45,97)
# e.calculate_percentage(65,44)


# 5.Product has name and price.
#   Method final_price() returns price.
#   DiscountedProduct adds discount_percent and overrides final_price() to apply discount.
#   Use super().final_price() to get original price before discounting.

class Product:
    def __init__(self,name,price):
        self.name = name
        self.price = price

    def final_price(self):
        print(f'Original price: {self.price}')

class DiscountedProduct(Product):
    def final_price(self,discount_percent):
        super().final_price()
        final_price = self.price-(self.price*(discount_percent/100))
        print(f'Final price after discount: {final_price}')

d = DiscountedProduct('Cooler',5000)
d.final_price(20)