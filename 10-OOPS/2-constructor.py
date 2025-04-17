'''
Constructor:
    A magical or dunder method,
    that get excecuted as we create the instance of a class

Defined as:
def __init__():
    body

Bacuase it starts and ends with double underscores
it is called as dunder method (Double UnderScore)


The self Parameter:
    -The self parameter is a reference to the current instance of the class,
     and is used to access variables that belong to the class.
    -It does not have to be named self, you can call it whatever you like, 
     but it has to be the first parameter of any function in the class.

'''

print('-----------constructor-----------')
class A:
    def __init__(self):
        print("Hello I'm constructor")

    def test(self):
        print("Hi I'm test")

print('----calling only test()----')
a = A()
a.test()

print('----instantiating object----')
b = A() # wihtout calling test automatically __init__() get excecuted.

# method __init__()
# get excecuted as we have create the object a of class A
# while we have called test() using a


'''
Types of constructor:
1- Non parameterized
2- Parameterized
'''

print('-----------Non-parametrized constructor-----------')
class B:
    def __init__(self):
        self.a = 1000
        print("Hello I'm constructor",self.a)

    def test(self):
        print("Hi I'm test",self.a)

ob = B()
ob.test()


print('-----------parameterized constructor-----------')
class D:
    def __init__(self,name):
        self.a = name
        print("Hello I'm constructor of",self.a)

ob = D("'D'")


print('-----------Ex: parameterized constructor-----------')
class Calc:
    def __init__(self,a,b):
        self.a = a
        self.b = b
    
    def add(self):
        print(f'{self.a} + {self.b} = {self.a+self.b}')
    
    def sub(self):
        print(f'{self.a} - {self.b} = {self.a-self.b}')

a = int(input("Enter value for a: "))
b = int(input("Enter value for b: "))
c = Calc(a,b)
c.add()
c.sub()