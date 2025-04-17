# 1. Write a Python program to create a class Car with attributes brand and model.
# Create an object of this class and print the attribute values.  

# class Car:
#     brand = "Tata"
#     model = "Harrier"
# c = Car()
# print("Brand:",c.brand)
# print("Model:",c.model)


# 2.Define a class Book with an attribute title. Create a method display_title
# that prints the book title. Create an object and call the method.  

# class Book:
#     title = 'The Girl In Room 105'
#     def display_method(self):
#         print("Title",self.title)
# b = Book()
# b.display_method()


# 3. Create a class Person with a method greet that prints "Hello!".
# Call this method using an object of the class.  

# class Person:
#     def greet(self):
#         print("Hello!")
# p = Person()
# p.greet()


# 4.Define a class Rectangle with attributes length and width.
# Create a method area that returns the area of the rectangle.  

# class Rectangle:
#     def __init__(self,length,width):
#         self.length = length
#         self.width = width
#     def area(self):
#         print("Area:",self.length*self.width)
# r = Rectangle(5,5)
# r.area()


# 5. Write a program to create a class Laptop with an attribute brand.
# Modify the attribute value after object creation and print it.

# class Laptop:
#     brand = 'Tata'
# l = Laptop()
# l.brand = 'Maruti'
# print(l.brand)


# 6. Create a class Circle with an attribute radius. Add a method
# circumference that returns the circumference of the circle.

# class Circle:
#     def circumference(self,r):
#         return f'Circumference: {3.14*2*r}'
# c = Circle()
# print(c.circumference(10))


# 7.Define a class Student with an attribute name. Add a method display_name
# that prints the name. Create multiple objects and call the method for each. 

# class Student:
#     def __init__(self):
#         self.name = input("Enter name: ")
#     def display_name(self):
#         print(f"Name: {self.name}")

# s1 = Student()
# s1.display_name()

# s2 = Student()
# s2.display_name()


# 8. Create a class Calculator with methods add and multiply to perform
# addition and multiplication of two numbers.

# class Caclulator:
#     def __init__(self):
#         self.a = int(input("Enter first number: "))
#         self.b = int(input("Enter second number: "))
    
#     def add(self):
#         print(f'Addition: {self.a}+{self.b}={self.a+self.b}')
   
#     def mul(self):
#         print(f'Multiplication: {self.a}*{self.b}={self.a*self.b}')
# c = Caclulator()
# c.add()
# c.mul()


# 9.Define a class Employee with an attribute salary. Write a method
# increase_salary that increases salary by a given percentage.  

# class Employee:
#     def __init__(self):
#         self.salary = float(input("Enter your salary: "))

#     def increase_salary(self):
#         per = float(input("Enter the percent you want to increase: "))
#         total = self.salary+self.salary*per
#         print(f'Increased salary: {total}')
# e = Employee()
# e.increase_salary()


# 10. Write a Python program to demonstrate method overloading by creating
# a class MathOperations with a method add that works with different numbers of arguments. 

# class MathOperations:
#     def add(self,a,b=None,c=None):
#         if b==None and c==None:
#             print(f'add: {a}')
#         elif c==None:
#             print(f'add: {a}+{b}={a+b}')
#         else:
#             print(f'add: {a}+{b}+{c}={a+b+c}')
# m = MathOperations()
# m.add(1)
# m.add(1,2)
# m.add(1,2,3) 


# 11. Implement method overriding in Python by creating a base class Animal
# with a method speak, and a derived class Dog that overrides this method. 

# class Animal:
#     def speak(self):
#         print('Speak of Animal class')
# class Dog(Animal):
#     def speak(self):
#         print('Speak of Dog class')
# d = Dog()
# d.speak()


# 12. Create a class Shape with a method draw(). Derive classes Circle and Square
# from it and override the draw() method in both subclasses.  

# class Shape:
#     def draw(self):
#         print("draw of Shape")
# class Circle(Shape):
#     def draw(self):
#         print("draw of Circle")
# class Square(Shape):
#     def draw(self):
#         print("draw of Square")
    
# c = Circle()
# c.draw()
# s = Square()
# s.draw()


# 13.Define a class Vehicle with a method speed(). Create subclasses Bike and Car
# that override speed() differently.  

# class Vehicle:
#     def speed(self):
#         print("speed of Vehicle")
# class Bike(Vehicle):
#     def speed(self):
#         print("speed of Bike")
# class Car(Vehicle):
#     def speed(self):
#         print("speed of Car")

# b = Bike()
# b.speed()
# c = Car()
# c.speed()


# 14. Write a Python program that demonstrates polymorphism with a function
# that takes different class objects but calls the same method from each.  

# class A:
#     def show(self):
#         print('hello')
# class B(A):
#     def show (self):
#         super().show()
#         print('l like pune')
# class C(A):
#     def show(self):
#         super().show()
#         print('apna clg')
# a = A()
# a.show()

# b = B()
# b.show()

# b=C()
# b.show()


# 15. Implement a class Media with a method play(). Create subclasses Audio
# and Video that override play() with specific implementations.

# class Media:
#     def play(self):
#         print('play of Media')
# class Audio(Media):
#     def play(self):
#         print('play of Audio')
# class Video(Media):
#     def play(self):
#         print('play of Video')
# a = Audio()
# a.play()
# v = Video()
# v.play()


# 16.Define a base class Animal with a method make_sound().
# Derive multiple subclasses (Dog, Cat, Cow) and override make_sound() accordingly.  

# class Animal:
#     def make_sound(self):
#         print('make_sound of Animal')
# class Dog(Animal):
#     def make_sound(self):
#         print('make_sound of Dog')
# class Cat(Animal):
#     def make_sound(self):
#         print('make_sound of Cat')
# class Cow(Animal):
#     def make_sound(self):
#         print('make_sound of Cow')
# d = Dog()
# d.make_sound()

# c = Cat()
# c.make_sound()

# w = Cow()
# w.make_sound()


# 17. Write a program to demonstrate abstraction by creating an abstract class Appliance
# with an abstract method turn_on(), and implement it in derived classes Fan and Light.  

# from abc import ABC,abstractmethod
# class Appliance(ABC):
#     @abstractmethod
#     def turn_on(self):
#         pass
# class Fan(Appliance):
#     def turn_on(self,switch):
#         return f'turn {switch} Fan'
# class Light(Appliance):
#     def turn_on(self,switch):
#         return f'turn {switch} Light'
# f = Fan()
# print(f.turn_on('ON'))

# l = Light()
# print(l.turn_on("OFF"))
    

# 18. Implement an abstract class Device with an abstract method start().
# Create concrete subclasses Computer and Mobile that implement start().  

# from abc import ABC,abstractmethod

# class Device(ABC):
#     @abstractmethod
#     def start(self):
#         pass
# class Computer(Device):
#     def start(self):
#         print("Computer is a Device")
# class Mobile(Device):
#     def start(self):
#         print("Mobile is a Device")
# c = Computer()
# c.start()
# m = Mobile()
# m.start()


# 19. Create an abstract class Instrument with an abstract method play().
# Implement subclasses Piano and Guitar that provide their own versions of play().

# from abc import ABC,abstractmethod

# class Instrument(ABC):
#     @abstractmethod
#     def start(self):
#         pass
# class Piano(Instrument):
#     def start(self):
#         print("Piano is a Instrument")
# class Guitar(Instrument):
#     def start(self):
#         print("Guitar is a Instrument")
# c = Piano()
# c.start()
# m = Guitar()
# m.start()


# 20. Write a Python program demonstrating an abstract class Transport with an
# abstract method move(). Implement subclasses Car and Airplane that define move()
# differently.  

# from abc import ABC,abstractmethod

# class Transport(ABC):
#     @abstractmethod
#     def move(self):
#         pass
# class Car(Transport):
#     def move(self):
#         print("Car is a Transport")
# class Airplane(Transport):
#     def move(self):
#         print("Airplane is a Transport")
# c = Car()
# c.move()
# m = Airplane()
# m.move()
