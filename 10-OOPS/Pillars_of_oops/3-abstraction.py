'''
Abstraction:
    hiding complex information or implementation from user
    Ex: Keyboard

Rules:
    1- import ABC (Abstract Base Classes) and abstractmethod from abc module
    2- To create a abstract class class should inherit ABC Eg: class A(ABC):
    3- Apply @abstractmethod to a method of abstract class to create a abstract method
    4- Can't instantiate Abstract Class (can't create Abstract class object)
    5- Those class inherits Abstract class must implement abstract method
       of that Abstract class
    6- there can be multiple abstract methods

'''

from abc import ABC,abstractmethod

class Shape(ABC):
    @abstractmethod
    def area(self):
        pass

# class Circle
class Circle(Shape):
    def area(self,radius):
        return 3.14*radius*radius

c = Circle()
print("Area of Circle",c.area(4))

# class Square
class Square(Shape):
    def area(self,length):
        return length**2

s = Square()
print("Area of Square:",s.area(10))

# class Triangle
class Triangle(Shape):
    def area(self,h,w):
        return (h*w)/2

t = Triangle()
print("Area of Triangle:",t.area(6,8))

# Rectangle
class Rectangle(Shape):
    def area(self,length,breadth):
        return (length*breadth)

r = Rectangle()
print("Area of Rectangle:",r.area(3,4))


print('------abstractmethods------')
print(Shape.__abstractmethods__)


'''
Shape is Abstract class, area() is abstract method
Circle must implement  area() if inherits Shape
But Can't create object of Shape 

Hidden Implementation:
1. Abstract Classes: Hide 'how' something is done and enforce 'what' needs to be done
2. Encapsulation: Hides data and implementation details, making them accessible only
   through controlled methods.
'''


from abc import ABC,abstractmethod

class Vehicle(ABC):
    def __init__(self,n):
        self.no_of_tyres = n
    @abstractmethod
    def start(self):
        pass
    
class Bike(Vehicle):
    def start(self,n):
        self.no_of_tyres = n
        print(f"Bike has {self.no_of_tyres} number of tyres.")

class Car(Vehicle):
    def start(self,n):
        self.no_of_tyres = n
        print(f"Car has {self.no_of_tyres} number of tyres.")

b = Bike(2)
b.start(2)

c = Car(2)
c.start(4)