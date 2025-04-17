# In-Built functions:
'''
print()
list()
tuple()
dict()
len()
type()
append()
remove()
sum()
int()
str()
'''

# User Defined Functions:
'''
Function:
    A block of code is  get executed when it is called.

Syntax:
# Defination of a function
def func_name(parameters/arguments):
    func-body

# How to call a function
func_name(arguments/parameters)

Function will get executed when it is called.

'''


# Defination of a function
def greet():
    print("Good evening!!!")

greet()

# Display function to print some text
def display():
    print("Hello, Today is a holiday.")

display()

print('----------Ex-1-----------')
def profile():
    name = 'Pruthviraj'
    age = 21
    city = 'Kolhapur'
    occupation = 'Student'
    print(f'''Name: {name}
Age: {age}
From: {city}
Occupation: {occupation}''')
    
profile()


print('----------Ex-2-----------')
def add():
    a = 2
    b = 3
    print(f"Addition: {a+b}")

add()


print('----------Ex-3-----------')
def mul():
    a = 3
    b = 10
    print(f"Multiplication: {a*b}")

mul()


# Parameters/arguments:

# Non-parametrized function/ without arguments

print('----------Non-parametrized function-----------')
def sub():
    a = 2
    b = 3
    print(f"Substraction: {a-b}")

sub()


# Parametrized function/ with arguments

print('----------Parametrized function-----------')
def mul(a,b):
    print(f'Multiplication: {x*y}')

x = int(input("Enter a number: "))
y = int(input("Enter a number: "))
    
mul(x,y)


# Ex- Non-parametrized function with user input

def mode():
    x = int(input("Enter a number: "))
    y = int(input("Enter a number: "))
    print(f'Mode: {x%y}')

mode()    

# return type
def display():
    name = 'Tom'
    return name
n = display()
print(n)
print(display())

def add():
    a = 3
    b = 4
    return a+b

c = add()
print(c)

'''

1-without parameter without return

2-with parameter without return

3-without parameter with return

4-with parameter with return

'''