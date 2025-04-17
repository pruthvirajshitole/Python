'''
Operator Overloading:
    How operators(+,*,-) behaves to object and class
+:
3 + 5 = 8 Addition
'a' + 'b' = 'ab' Concatenation
obj = obj1 + obj2

'''


'''
Feature __str__, __repr__:

    Purpose: User-friendly string representation
            Debugging and development representation

    Usage: Used by print(obj) and str(obj)
        Used by repr(obj), debugging, and interpreter

    Intended Audience: End-users (readable format)
                    Developers (detailed format)

    Fallback Behavior: If not defined, Python falls back to __repr__
                    If not defined, Python prints a default object reference

Example Output for a Point Class:
    "Point at (2, 3)"
    "Point(2, 3)"

| Feature             | `__str__`                                    | `__repr__`                                   |

|---------------------|----------------------------------------------|----------------------------------------------|

|   Purpose           | User-friendly string representation          | Debugging and development representation     |

|   Usage             | Used by `print(obj)` and `str(obj)`          | Used by `repr(obj)`, debugging, and interpreter |

|   Intended Audience | End-users (readable format)                  | Developers (detailed format)                  |

|   Fallback Behavior | If not defined, Python falls back to
   
 '''


print('--------Point--------')

class Point:
    def __init__(self,x,y):
        self.x = x
        self.y = y
    
    def __add__(self,other):
        return Point(self.x + other.x, self.y + other.y)

    def __repr__(self):
        return f"Point({self.x,self.y})"

point1 = Point(1,2)
point2 = Point(3,4)
# point3 = Point(1,1)
point = point1+point2
print(point)


'''
Step 1: Defining the Point Class:
    -The Point class has an initializer (__init__) that takes two parameters: x and y.
    -These parameters are assigned to instance variables (self.x and self.y),
     representing the coordinates of a point in a 2D space.

Step 2: Overloading the + Operator with __add__:
    -The + operator is overloaded using the __add__ method.
    -When two Point objects are added, a new Point object is created with:
        x coordinate as the sum of both x values.
        y coordinate as the sum of both y values.
    -This ensures that Point objects can be added like numerical values.
    -Example Calculation: If point1 = Point(1,2) and point2 = Point(3,4),        
     then point1 + point2 results in Point(4,6).

Step 3: Overloading __repr__ to Format Output:
    -The __repr__ method returns a formatted string representation of the object.
    -When a Point object is printed, this method is called automatically.

Step 4: Creating Point Objects:
    -Two Point objects are created:
        point1 with coordinates (1,2)
        point2 with coordinates (3,4)

Step 5: Adding Points:
    point = point1 + point2

Step 5.1: point1 + point2
    -Calls __add__ method
    Point(1+3, 2+4) → Point(4, 6)
    A new Point(4,6) object is created.

Step 6: Printing the Result:
    -print(point)
    -Calls __repr__ method for Point(4,6).
    -Point((4, 6))

Final Output:
    Point((4, 6))

'''


print('---------Add---------')

class Add:
    def __init__(self,x,y):
        self.x = x
        self.y = y

    def __add__(self,other):
        return Add(self.x+other.x, self.y+other.y)
    
    def __repr__(self):
        return f'Addition: ({self.x,self.y})'

a = Add(1,2)
b = Add(3,4)
c = a+b
print(c)


print('---------Sub---------')

class Sub:
    def __init__(self,x,y):
        self.x = x
        self.y = y
    
    def __sub__(self,other):
        return Sub(self.x-other.x, self.y-other.y)
    
    def __repr__(self):
        return f'Substraction: ({self.x,self.y})'

s1 = Sub(5,6)
s2 = Sub(3,2)
s = s1-s2
print(s)
