'''
OOPS:
    Object Oriented Programming (OOP) in python is a programming
    style that uses classes  and objects to organize code.

class:
    Blue print of objects.
    Collection of attributes(variables) and methods(functions)

objects:
    Instance of class.
'''

print('---------class----------')

class A:        # class defination
    x = 6       # attribute

obj = A()      # instantiate   # object
print(obj.x)   # object of A

obj1 = A()
print(obj1.x)


print('---------class with multiple objects----------')

# create a class Employee with attribues name,age,salary,join,designation
# and print it using f-string
class Employee:
    name = 'Tom'
    age = 22
    salary = 50000
    join = '1/2/2023'
    role = 'Developer'

e1 = Employee()
print(f'''
Name: {e1.name}
Age: {e1.age}
Salary: {e1.salary} Rs
Date of joining: {e1.join}
Designation: {e1.role}
''')


