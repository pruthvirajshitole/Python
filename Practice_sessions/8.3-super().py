# 1.Define a class Person with attributes for name and age. 
#   Implement a subclass Employee that adds an attribute for salary and a method to calculate the annual bonus.
#   (e.g., 10% of salary).


# class Person:
#     def __init__(self,name,age):
#         self.name = name
#         self.age = age
#         print(f'Name: {self.name}\nAge: {self.age}')
    
# class Employee(Person):
#     def __init__(self,name,age,salary):
#         super().__init__(name,age)
#         self.salary = salary
#         print(f'Salary: {self.salary}')
    
#     def cal_bonus(self):
#         bonus =  0.10*self.salary
#         print(f'Bonus: {bonus}')

# e = Employee('Linda',22,10000)
# e.cal_bonus()


# 2. Create 3 class person(name,age), student(grade) and teacher(subject) perform Hierarchical Inheritance 
#    and print the information of student and teacher. Use super method.

# class Person:
#     def __init__(self,name,age):
#         self.name = name
#         self.age = age

# class Student(Person):
#     def __init__(self,name,age,grade):
#         super().__init__(name,age)
#         self.grade = grade
    
#     def student_details(self):
#         print(f'''Name: {self.name}
# Age: {self.age}
# Grade: {self.grade}''')
        
# class Teacher(Person):
#     def __init__(self,name,age,subject):
#         super().__init__(name, age)
#         self.subject = subject
    
#     def teacher_details(self):
#         print(f'''Name: {self.name}
# Age: {self.age}
# Subject: {self.subject}''')

# s = Student("Alex",22,'B')
# s.student_details()

# print('--------------------')

# t = Teacher('Lizaa',30,'ML')
# t.teacher_details()

    
# 3.Define a class Vehicle with attributes for brand and year.
# Implement a subclass Car that adds an attribute for mileage and a method to calculate
# the fuel cost for a trip given a distance and cost per kilometer.

# class Vehicle:
#     def __init__(self,brand,year):
#         self.brand = brand
#         self.year = year

# class Car(Vehicle):
#     def __init__(self,brand,year,milage):
#         super().__init__(brand, year)
#         self.milage = milage

#     def cal_fuel_cost(self,distance,rate):
#         cost = rate*distance
#         print(f'Cost of trip: {cost} Rupees.')

# c = Car('Bently',2006,20)
# c.cal_fuel_cost(10,104)


# 4.Define a class Appliance with attributes for brand and power (in watts).
# Implement a subclass WashingMachine that adds an attribute for capacity (in kg)
# and a method to calculate electricity usage for a given number of hours.

# class Appliance:
#     def __init__(self,brand,power):
#         self.brand = brand
#         self.power = power

# class WashingMachine(Appliance):
#     def __init__(self,brand,power,capacity):
#         super().__init__(brand, power)
#         self.capacity = capacity

#     def cal_electricity(self,time):
#         usage = self.power/1000*time
#         print(f'Electricity usage: {usage} Kilowatts.')

# w = WashingMachine('Samsung',12000,6)
# w.cal_electricity(2)


# 5.Create a base class Shape with a method to set dimensions.
# Create two derived classes Rectangle and Triangle that calculate and display the area.

class Shape:
    def set_dimensions(self,length,width):
        self.length = length
        self.width = width
    
class Rectangle(Shape):
    def area(self):
        print(f"Area of Rectangle: {self.length*self.width}")

class Triangle(Shape):
    def area(self):
        print(f"Area of Triangle: {(self.length*self.width)/2}")


r = Rectangle()
t = Triangle()

r.set_dimensions(3,4)
r.area()

t.set_dimensions(5,2)
t.area()