class A:
    def display_A(self):
        print("You are in display of A")

class B(A):
    def display_B(self):
        print("You are in display of B")

class C(A):
    def display_C(self):
        print("Yor are in display of C")

class D(A):
    def display_D(self):
        print("You are in display of D")

print('-----object of A------')
a = A()
a.display_A()

print('-----object of B------')
b = B()
b.display_B()
b.display_A()

print('-----object of C------')
c = C()
c.display_C()
c.display_A()

print('-----object of D------')
d = D()
d.display_D()
d.display_A()
