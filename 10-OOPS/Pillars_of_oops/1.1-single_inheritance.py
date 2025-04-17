'''
Parent-Child Relationship
one base class and one derived class

'''

class A:
    def display(self):
        print("You are in Base class")

class B(A):
    def show(self):
        print("Yor are in Derived class")

print('-----object of A------')
a = A()
a.display()

print('-----object of B------')
b = B()
b.show()
b.display()