# 1-without parameter without return:

def cal():
    print(f'''
Addition: {a+b}
Substraction: {a-b}
Division: {a/b}
Multiplication: {a*b}
        ''')

a = int(input("Enter a number: "))
b = int(input("Enter a number: "))
cal()


# 2-with parameter without return:

def cal(a,b):
    print(f'''
Addition: {a+b}
Substraction: {a-b}
Division: {a/b}
Multiplication: {a*b}
        ''')

a = int(input("Enter a number: "))
b = int(input("Enter a number: "))
cal(a,b)


# 3-without parameter with return:

def cal():
   return a+b, a-b, a/b, a*b

a = int(input("Enter a number: "))
b = int(input("Enter a number: "))

c1,c2,c3,c4 = cal()
print(f'''
Addition: {c1}
Substraction: {c2}
Division: {c3}
Multiplication: {c4}
''')


# 4-with parameter with return:

def cal(a,b):
   return a+b, a-b, a/b, a*b

a = int(input("Enter a number: "))
b = int(input("Enter a number: "))

c1,c2,c3,c4 = cal(a,b)
print(f'''
Addition: {c1}
Substraction: {c2}
Division: {c3}
Multiplication: {c4}
''')