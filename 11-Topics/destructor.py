'''
| Feature          | Destructor (`__del__`)                         |

|------------------|------------------------------------------------|

|   Purpose        | Cleans up resources before deletion            |

|   When Called?   | When an object is deleted or goes out of scope |

|   Parameters     | self (instance reference)                      |

|   Use Case       | Closing files, releasing memory                |

|   Automatic?     |called automatically when the object is deleted |


A destructor is a special method in object-oriented programming that is
automatically called when an object is destroyed or goes out of scope.
In Python, the destructor method is defined using __del__().

Key Points about Destructors:

    - Used to free up resources like closing files, releasing memory, or closing database connections.
    - Automatically called when an object is no longer referenced.
    - Python has automatic garbage collection, so destructors are rarely needed explicitly.

'''

# Destructors are called when an object gets destroyed.

class Car:
    def __init__(self, brand):
        print(f"Car {brand} is created.")
        self.brand = brand

    def __del__(self):
        print(f"Car {self.brand} is destroyed.")

# Creating an object
car1 = Car("Tesla")

# Deleting the object
del car1

# print(car1)  # NameError: name 'car1' is not defined.

# The destructor is called automatically when the program ends or when there are no references to the object.
