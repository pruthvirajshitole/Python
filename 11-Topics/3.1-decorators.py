'''
In Python, decorators are a powerful and flexible way to modify or extend
the behavior of functions or methods, without changing their actual code.
A decorator is essentially a function that takes another function as an
argument and returns a new function with enhanced functionality.

Use:
    Decorators are often used in scenarios such as logging, authentication and memorization.

'''

print('------decorator function------')
def decorator(func):
    def wrapper():
        print("Before calling the function.")
        func()
        print("After calling the function.")
    return wrapper

# Applying the decorator to a function
@decorator

def greet():
    print("Hello, World!")
greet()

# decorator takes the greet function as an argument.
# It returns a new function (wrapper) that first prints a message,
# calls greet() and then prints another message.
# The @decorator syntax is a shorthand for greet = decorator(greet).


print('------Ex------')
def initialize(fun):
    def wrapper():
        print("START")
        fun()
        print("END")
    return wrapper

@initialize

def body():
    print("body")
body()

''' 
Types of Decorators:
  1- Function Decorators:
      The most common type of decorator, which takes a function as input
      and returns a new function. The example above demonstrates this type.
  
  2- Method Decorators:
      Used to decorate methods within a class. They often handle special cases,
      such as the self argument for instance methods.
  
  3. Class Decorators:
      Class decorators are used to modify or enhance the behavior of a class.
      Like function decorators, class decorators are applied to the class definition.
      They work by taking the class as an argument and returning a modified version
      of the class.

Common Built-in Decorators in Python: @staticmethod, @classmethod, @property

'''
