'''
Scope:
    A variable is only available from inside 
    the region it is created. 
    This is called scope.

Local Scope:    
    A variable created inside a function belongs 
    to the local scope of that function, 
    and can only be used inside that function.

Global Scope
    A variable created in the main body of the 
    Python code is a global variable
    and belongs to the global scope.

Global variables are available from 
within any scope, global and local.

'''

x = 4
def demo():
    y = 7
    print("Global variable x: ",x,"Local variable y: ",y)

def test():
    z = 9
    print("Global variable x: ",x,"Local variable z: ",z)

demo()
test()
print(x)

# y- local variable (within a local scope i.e within function demo())
# x- global variable(within a global scope i.e accessable within 
# function demo() and outside anywhere in application )


print('----Function inside a function----')
a = 4
def demo1():
    print(a)
    b=5
    print(b)

    def demo2():
        print(a,b)
        c=11
        print(c)
    demo2()
demo1()
print(a)


print('----Naming variable----')
a = 3
print(a)  # 3
def read():
    a = 2
    print(a)  # 2
read()
print(a)  # 3


print('----Global keyword----')
def testing1():
    global w
    w=5
testing1()
print("w:",w)   # calling outside the fuction tesing()

def testing():
    global w
    w=5
    def ready():
        global u
        u=10
        print(u)
    ready()
    print("w:",w,"u:",u)  # calling u outside the  fuction ready()

testing()  # calling u outside the  fuction testing(), ready()
