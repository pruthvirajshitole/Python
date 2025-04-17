'''
Create a calculator
That calculates
1- Add   
2- Sub
3- Mul
4- Div
5- Mode
6- Floor Div
7- Exponential
0- Exit
choice given by user 
till 5 valid attempts
all function returns the output 
and at last when user exit the total will
get printed
'''


class Calculator:

    def add(self,a,b):        
        return f'{a}+{b} = {a+b}'

    def sub(self,a,b):
        return f'{a}-{b} = {a-b}'

    def mul(self,a,b):
        return f'{a}*{b} = {a*b}'
    
    def div(self,a,b):
        return f'{a}/{b} = {a/b}'
    
    def mode(self,a,b):
        return f'{a}%{b} = {a%b}'
    
    def floor(self,a,b):
        return f'{a}//{b} = {a//b}'

    def expo(self,a,b):
        return f'{a}**{b} = {a**b}'

c = Calculator()

print('''------Welcome to Calculator------
1- Add   
2- Sub
3- Mul
4- Div
5- Mode
6- Floor Div
7- Exponential
0- Exit
---------------------------------''')
i = 1
while i<=5:
    ch = int(input('Choose the operation: '))
    if ch == 1:
        a = int(input("Enter value of a: "))
        b = int(input("Enter value of b: "))
        print(c.add(a,b))
        i+=1

    elif ch == 2:
        a = int(input("Enter value of a: "))
        b = int(input("Enter value of b: "))
        print(c.sub(a,b))
        i+=1

    elif ch == 3:
        a = int(input("Enter value of a: "))
        b = int(input("Enter value of b: "))
        print(c.mul(a,b))
        i+=1

    elif ch == 4:
        a = int(input("Enter value of a: "))
        b = int(input("Enter value of b: "))
        print(c.div(a,b))
        i+=1

    elif ch == 5:
        a = int(input("Enter value of a: "))
        b = int(input("Enter value of b: "))
        print(c.mode(a,b))
        i+=1

    elif ch == 6:
        a = int(input("Enter value of a: "))
        b = int(input("Enter value of b: "))
        print(c.floor(a,b))
        i+=1

    elif ch == 7:
        a = int(input("Enter value of a: "))
        b = int(input("Enter value of b: "))
        print(c.expo(a,b))
        i+=1

    elif ch == 0:
        print("Thank You!!!")
        break

    else:
        print('Invalid choice...')
    print(f'{6-i} attempts left!!!')






















'''

Create a calculator

That calculates

1- Add   

2- Sub

3- Mul

4- Div

5- Mode

6- Floor Div

7- Exponential

0- Exit

choice given by user 

till 5 valid attempts

all function returns the output 

and at last when user exit the total will

get printed

'''