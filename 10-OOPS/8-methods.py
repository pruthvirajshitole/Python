'''
1) Instance Methods:
    methods that are operated on an instance of a class
    and can be accessed and modified by the instance attribute.

2) Class Method:
    methods that are operated by the class itself
    rather than instance of a class.
    To access the class level variable.
    By conventions we pass 'cls' as argument.

3) Static method:
    methods that don't operated on an instance of a class or by class
    they are utility functions that are logically related to class.

'''

print('--------Instance Method--------')
# 1- Instance method
class A:
    def __init__(self,x):
        self.x = x
    
    def show(self):
        print(self.x)
a = A(5)
a.show()
A(7).show()


print('--------Class Method--------')
# 2- Class method
class Car:
    brand = 'Toyota'

    @classmethod
    def get_brand(cls):
        return cls.brand

print(Car.get_brand())

class B:
    a = 33
    b = 22
    @classmethod
    def sub(cls):
        print(cls.a-cls.b)
B.sub()


print('--------Static Method--------')
# 3- Static method
class A:
    @staticmethod
    def add(a,b):
        print(f"add:{a+b}")
A.add(3,2)


class A:
    @staticmethod
    def sub(x,y):
        print(x-y)

A.sub(4,2)