'''
Lambda:
    A small anonymous(unknown, have no identity) function to perform small tasks.

Syntax:
lambda args:expression

Multiple arguments are possible (x,y,z)
But must have single expression (a+b, x**y)

'''
print('----------lambda function-----------')
print((lambda a,b:a+b)(3,5))

print((lambda a,b,c:a*b-c)(2,3,4))


print('----------lambda function with boolean output-----------')
print((lambda n:n%2 == 0)(4))

print((lambda a: a%2==1)(4))


print('----------lambda function with user input()-----------')
a = int(input("Enter a: "))
print((lambda a,b,c:a*(b-c))(a,6,4))

c = lambda a,b:a+b
print(c(1,2))
print(type(c))  # <class 'function'>