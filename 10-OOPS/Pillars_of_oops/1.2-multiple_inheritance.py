'''
Parent-Child Relationship
Multiple Parents(Base classes) of
a Child(Derived class) class
'''

class A:
    def display_A(self):
        print("You are in display of A")

class B:
    def display_B(self):
        print("You are in display of B")

class C(A,B):
    def show(self):
        print("Yor are in show of C")

print('-----object of A------')
a = A()
a.display_A()

print('-----object of B------')
b = B()
b.display_B()

print('-----object of C------')
c = C()
c.show()
c.display_A()
c.display_B()
