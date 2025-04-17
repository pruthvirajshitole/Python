# 1. Write a Python program to create a class Car with attributes brand and model.
# Create an object of this class and print the attribute values.  

# class Car:
#     brand = 'Tata'
#     model = 'Harrier'

# c = Car()
# print(f'Brand: {c.brand}, Model: {c.model}')


# 2. Define a class Book with an attribute title. Create a method display_title that prints the book title.
# Create an object and call the method.

# class Book:
#     title = "400 Hundred Days."
#     def display_title(self):
#         print(self.title)
# b = Book()
# b.display_title()


# 3. Create a class Person with a method greet that prints "Hello!".
# Call this method using an object of the class.  

# class Person:
#     def greet(self):
#         print("Hello!")
# p = Person()
# p.greet()


# 4. Define a class Rectangle with attributes length and width.
# Create a method area that returns the area of the rectangle.

# class Rectangle:
#     length = 10
#     width = 20

#     def area(self):
#         print(f'Area = {self.length*self.width}')

# r = Rectangle()
# r.area()


# 5. Write a program to create a class Laptop with an attribute brand.
# Modify the attribute value after object creation and print it.

# class Laptop:
#     brand = 'Dell'
# l = Laptop()
# print('Brand',l.brand)
# l.brand = 'Dell G-15'
# print('Updated Brand:',l.brand)


# 6. Create a class Circle with an attribute radius. Add a method circumference
# that returns the circumference of the circle.

# class Circle:
#     radius = 5

#     def circumference(self):
#         print("Circumference of the circle is:",2*3.14*self.radius)

# c = Circle()
# c.circumference()


# 7. Define a class Student with an attribute name. Add a method display_name that prints the name.
# Create multiple objects and call the method for each.

# class Student:
#     def __init__(self):
#         self.name = input("Enter the name: ")

#     def display_name(self):
#         print("Name:",self.name)

# s1 = Student()
# s1.display_name()

# s2 = Student()
# s2.display_name()

# s2 = Student()
# s2.display_name()


# 8. Create a class Calculator with methods add and multiply to perform
# addition and multiplication of two numbers.

# class Calculator:
#     def __init__(self):
#         self.n1 = int(input("Enter first number: "))
#         self.n2 = int(input("Enter second number: "))
    
#     def add(self):
#         print("Addition:",self.n1+self.n2)

#     def multiply(self):
#         print("Multiplication:",self.n1*self.n2)

# c = Calculator()
# c.add()
# c.multiply()


# 9. Define a class Employee with an attribute salary. Write a method increase_salary
# that increases salary by a given percentage.  

# class Employee:
#     def __init__(self):
#         self.salary = 10000
#         self.increment = float(input("Enter the increment you wanted in your salary: "))
#     def increase_salary(self):
#         print("Increase salary:",self.salary+(self.salary*self.increment/100))

# e = Employee()
# e.increase_salary()


# 10. Write a Python program to demonstrate method overloading by creating a class MathOperations
# with a method add that works with different numbers of arguments.

# class MathOperations:
#     def add(self,a,b=None,c=None):
#         if b == None and c==None:
#             return a
#         elif c==None:
#             return a+b
#         else:
#             return a+b+c

# ob = MathOperations()
# print('Addition:',ob.add(2))
# print('Addition:',ob.add(1,2))
# print('Addition:',ob.add(1,2,3))


# 11. Implement method overriding in Python by creating a base class Animal with a method speak
# and a derived class Dog that overrides this method.

# class Animal:
#     def dog(self):
#         print("Dog barks bowww!!")
#     def display(self):
#         print("Dog is also an animal")

# class Speak(Animal):
#     def cat(self):
#         print("Cat makes meoww!!!")

# a = Animal()
# a.dog()
# a.display()

# print("----object of Speak----")
# c = Speak()
# c.cat()
# c.display()
# c.dog()


# 12. Create a class Shape with a method draw().Derive classes Circle
# and Square from it and override the draw() method in both subclasses.

# class Shape:
#     def draw(self):
#         print('I am draw of Shape')

# class Circle(Shape):
#     def draw(self):
#         super().draw()
#         print('I am draw of Circle')

# class Square(Shape):
#     def draw(self):
#         super().draw()
#         print('I am draw of Square')

# c = Circle()
# c.draw()

# s = Square()
# s.draw()


# 13. Define a class Vehicle with a method speed(). Create subclasses
# Bike and Car that override speed() differently.

# class Vehicle:
#     def speed(self):
#         print('Vehicle used to travel.')

# class Bike(Vehicle):
#     def speed(self):
#         super().speed()
#         print('Bike is much cheaper than car')

# class Car(Vehicle):
#     def speed(self):
#         super().speed()
#         print('Car is faster than bike')

# b = Bike()
# b.speed()

# c = Car()
# c.speed()


# 14. Write a Python program that demonstrates polymorphism with a function that takes different
# class objects but calls the same method from each.  




# 15. Implement a class Media with a method play(). Create subclasses Audio and Video that
# override play() with specific implementations.  

# class Media:
#    def play(self):
#       print("Play of media")

# class Audio(Media):
#    def play(self):
#       super().play()
#       print("Play Audio")

# class Video(Media):
#    def play(self):
#       super().play()
#       print("Play of Video")

# a=Audio()
# a.play()

# v=Video()
# v.play()


# 16. Define a base class Animal with a method make_sound(). Derive multiple subclasses (Dog, Cat, Cow)
# and override make_sound() accordingly.  

# 17. Write a program to demonstrate abstraction by creating an abstract class Appliance with an
# abstract method turn_on(), and implement it in derived classes Fan and Light.

# from abc import ABC,abstractmethod

# class Appliance(ABC):
#    @abstractmethod
#    def turn_on(self):
#       pass
   
# class Fan(Appliance):
#    def turn_on(self):
#       return 'fan turn on'

# class Light(Appliance):
#     def turn_on(self):
#        return 'light turn on' 

# f=Fan()
# print(f.turn_on())

# l=Light()
# print(l.turn_on())


# 18. Implement an abstract class Device with an abstract method start().
# Create concrete subclasses Computer and Mobile that implement start().

# from abc import ABC,abstractmethod
# class Device(ABC):
#    @abstractmethod
#    def start(self):
#       pass
   
# class Computer(Device):
#    def start(self):
#       return 'computer start'

# class Mobile(Device):
#    def start(self):
#       return 'Mobile start'

# c=Computer()
# print(c.start())

# m=Mobile()
# print(m.start())


# 19. Create an abstract class Instrument with an abstract method play().
# Implement subclasses Piano and Guitar that provide their own versions of play().  

# 20. Write a Python program demonstrating an abstract class Transport with an abstract method move().
# Implement subclasses Car and Airplane that define move() differently.  
