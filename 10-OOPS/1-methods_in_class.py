print('--------------1---------------')
class Demo:
    def show(self):
        print("I am show of Demo")
    
d = Demo()
d.show()

# self is a container of class
# The self parameter is a reference to the current instance of the class,
# and is used to access variables that belong to the class.


# create a class Test with method display to print text

print('--------------2---------------')
class Test:
    def display(self):
        print("Hello boyz!!!")
t = Test()
t.display()


# create a method details of class Students to print
# Name:
# Age:
# Class:
# Total Marks: /500
# Percentage:
# using variables  and fstring
# calculate percentange using total marks which is less than 500

print('--------------3---------------')
class Students:
    def details(self):
        name = input("Enter student's name: ")
        age = int(input("Enter student's age: "))
        section = input("Enter student's class: ")
        marks = float(input("Enter student's total marks out of 500: "))
        if marks<500:
            perc = (marks/500)*100
            return f'''
Name: {name}
Age: {age}
Class: {section}
Total Marks: {marks}
Pecentage: {perc}
        '''
        else:
            return ("Total marks can't be more than 500.")

s1 = Students()
print(s1.details())


print('--------------4---------------')
class Calc:
    def add(self,x,y):
        print(f'{x} + {y} = {x+y}')
    def sub(self,x,y):
        print(f'{x} - {y} = {x-y}')
    def mul(self,x,y):
        print(f'{x} * {y} = {x*y}')
    def div(self,x,y):
        print(f'{x} / {y} = {x/y}')
    def mode(self,x,y):
        print(f'{x} % {y} = {x%y}')
    def floor(self,x,y):
        print(f'{x} // {y} = {x//y}')
    def expo(self,x,y):
        print(f'{x} ** {y} = {x**y}')

c = Calc()
c.add(1,2)
c.sub(3,1)
c.mul(6,20)
c.div(12,3)
c.floor(3,2)
c.expo(2,5)


print('--------------5---------------')
class Calc:
    def add(self,x,y):
        print(f'{x} + {y} = {x+y}')
    def sub(self,x,y):
        print(f'{x} - {y} = {x-y}')
    def mul(self,x,y):
        print(f'{x} * {y} = {x*y}')
    def div(self,x,y):
        print(f'{x} / {y} = {x/y}')
    def mode(self,x,y):
        print(f'{x} % {y} = {x%y}')
    def floor(self,x,y):
        print(f'{x} // {y} = {x//y}')
    def expo(self,x,y):
        print(f'{x} ** {y} = {x**y}')

c = Calc()
a = int(input("Enter value of a: "))
b = int(input("Enter value of b: "))
c.add(a,b)
c.sub(a,b)
c.mul(a,b)
c.div(a,b)
c.floor(a,b)
c.expo(a,b)


print('--------------6-without return---------------')
class Calc:
    def add(self):
        x = int(input("Enter value of a: "))
        y = int(input("Enter value of b: "))
        print(f'{x} + {y} = {x+y}')

    def sub(self):
        x = int(input("Enter value of a: "))
        y = int(input("Enter value of b: "))
        print(f'{x} - {y} = {x-y}')

    def mul(self):
        x = int(input("Enter value of a: "))
        y = int(input("Enter value of b: "))
        print(f'{x} * {y} = {x*y}')

    def div(self):
        x = int(input("Enter value of a: "))
        y = int(input("Enter value of b: "))
        print(f'{x} / {y} = {x/y}')

    def mode(self):
        x = int(input("Enter value of a: "))
        y = int(input("Enter value of b: "))
        print(f'{x} % {y} = {x%y}')

    def floor(self):
        x = int(input("Enter value of a: "))
        y = int(input("Enter value of b: "))
        print(f'{x} // {y} = {x//y}')

    def expo(self):
        x = int(input("Enter value of a: "))
        y = int(input("Enter value of b: "))
        print(f'{x} ** {y} = {x**y}')

c = Calc()
c.add()
c.sub()
c.mul()
c.div()
c.floor()
c.expo()


print('--------------7-with return---------------')
class Calc:
    def add(self):
        x = int(input("Enter value of a: "))
        y = int(input("Enter value of b: "))
        return (f'{x} + {y} = {x+y}')

    def sub(self):
        x = int(input("Enter value of a: "))
        y = int(input("Enter value of b: "))
        return (f'{x} - {y} = {x-y}')

    def mul(self):
        x = int(input("Enter value of a: "))
        y = int(input("Enter value of b: "))
        return (f'{x} * {y} = {x*y}')

    def div(self):
        x = int(input("Enter value of a: "))
        y = int(input("Enter value of b: "))
        return (f'{x} / {y} = {x/y}')

    def mode(self):
        x = int(input("Enter value of a: "))
        y = int(input("Enter value of b: "))
        return (f'{x} % {y} = {x%y}')

    def floor(self):
        x = int(input("Enter value of a: "))
        y = int(input("Enter value of b: "))
        return (f'{x} // {y} = {x//y}')

    def expo(self):
        x = int(input("Enter value of a: "))
        y = int(input("Enter value of b: "))
        return (f'{x} ** {y} = {x**y}')

c = Calc()
print(c.add())
print(c.sub())
print(c.mul())
print(c.div())
print(c.floor())
print(c.expo())

