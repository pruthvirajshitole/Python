from Calculator import add,sub,mul,div,floor_div,expo,mode

a = int(input("Enter value of a: "))
b = int(input("Enter value of b: "))
operation = input('''
choose one operation:
for additon +
for substraction -
for multiplication *
for division /
for floor division //
for mode %
for exponentioal **
:

''')

if operation == '+':
    s=add.add(a,b)
    print(s)
elif operation == '-':
    s=sub.sub(a,b)
    print(s)
elif operation == '*':
    s=mul.mul(a,b)
    print(s)
elif operation == '/':
    s=div.div(a,b)
    print(s)
elif operation == '//':
    s=floor_div.floor_div(a,b)
    print(s)
elif operation == '%':
    s=mode.mode(a,b)
    print(s)
elif operation == '**':
    s=expo.expo(a,b)
    print(s)



# from Demo import even
# print(even.h)