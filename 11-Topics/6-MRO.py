'''
MRO (Method Resolution Order): 
    MRO in Python defines the order in which classes are searched when executing a method.
    It is especially important in multiple inheritance, where a class can inherit from multiple parent classes.

MRO and C3 Linearization (C3 Algorithm):
    Python follows the C3 Linearization (also called the C3 MRO algorithm)
    to determine the order of method resolution.
    
The rules are:
    1- Children before parents:
        The class itself appears before its base classes.
    2- Left-to-right order:
        If a class has multiple parents,
        Python follows the order in which they are inherited.
    3- No class appears before its parent classes:
        Ensures that parent classes appear only after their
        child classes have been considered.

Accessing MRO:
    ClassName.mro()
    ClassName.__mro__

Why MRO Matters?
    Ensures consistent and predictable method resolution.
    Prevents diamond problem
    (where ambiguity arises in multiple inheritance).

'''

class A:
    def show(self):
        print("A")

class B(A):
    def show(self):
        print("B")

class C(A):
    def show(self):
        print("C")

class D(C, B):
    pass

d = D()
d.show()
l = D.mro()  # Check the MRO of class D
for i in l:
    print(i)


print('------Animals(MRO)------')

class Wild_Animal:
    def __init__(self,name):
        self.name = input("Enter the name : ")

    def show_wild(self):
        return self.name
  
class Pet_Animal:
    def __init__(self, name):
        self.name = name

    def show_pet(self):
        return self.name
   
class Pet(Wild_Animal,Pet_Animal):
    def __init__(self,name):
        super().__init__(name)
        Pet_Animal.__init__(self,name)

p = Pet("Cat")       
print(p.show_pet())
print(p.show_wild())

print('-----checking MRO of class---')
print(Pet.__mro__)

print('------or------')
print(Pet.mro())

print(help(Pet))