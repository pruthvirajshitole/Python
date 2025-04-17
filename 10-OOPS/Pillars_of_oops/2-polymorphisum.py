'''
Polymorphism: poly-many morphism-form
              multiple forms of a method

Types:
    1- Compile Time Polymorphism (method overloading)
    2- Run Time Polymorphism (method overriding)

'''


'''
def add():
    print("add 1")

def add(a):
    print("add 2")

def add(a,b):
    print("add 3")

def add(a,b,c):
    print("add 4")

add()
add(1)
add(2,3)
add(2,3,4)

TypeError: add() missing 3 required positional arguments:
 'a', 'b', and 'c'

Not Possible in Python

'''


# 1- Compile Time Polymorphism (method overloading)

print('-------method overloading-------')
def add(a,b=None,c=None):
    if b == None and c==None:
        return a
    elif c==None:
        return a+b
    else:
        return a+b+c
    
print('Addition:',add(1))
print('Addition:',add(1,2))
print('Addition:',add(1,2,3))

'''
Method Overloading:
    Concept of implementing same name method with different parameters

def add():
    pass

def add(a):
    pass

def add(a,b):
    pass

Compile Time:
    behaviour of method is determined at the time of compilation not at the runtime.

we can't implement multiple functions with same name in python 
like add(), add(a), add(a,b)
so we can implement add(a,b=None,c=None) to implement compile time polymorphism

'''


# Runtime Polymorphism (method overriding)

print('-------method overriding-------')
class A:
    def show(self):
        print("I am show of A")
    def a(self):
        print('a')
class B(A):
    def show(self):
        show()
        print("I am show of B")
    def b(self):
        print('b')   

# ob1 = A()
# ob1.a()
# ob1.show()

ob2 = B()
ob2.b()
ob2.show()

'''
Method Overriding:
    Parent class get overridden when we create same methods in Parent and child class
    To avoid overridding we can use super() to the parent class method in child class

'''

'''
Reference Type:
    determines which method can be called

Compile time only knows refrence type.


Object Type:
    determines which implementation of method is executed at rutime

Runtime:
     method to be called depends on object type 
     which is determined when program is running.             

'''

print('-------with super()-------')
# To avoid overridding we can use super() to the parent class method in child class
class A:
    def show(self):
        print("I am show of A.")

    def a(self):
        print('a')

class B(A):
    def show(self):
        super().show()
        print("I am show of B.")

    def b(self):
        print('b')

# B is the child of A or A is the parent of B
obj1=A()
obj1.a()
obj1.show()

obj2=B()
obj2.b()
obj2.show()

