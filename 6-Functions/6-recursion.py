'''
Recursion:
    A function that calls itself till certain condition

'''

print('----------factorial with recursion----------')
def fact(n):
    if n == 1:
        return 1
    else:
        return n*fact(n-1)
print(fact(5))

'''
fact(5)
n       n*fact(n-1)
---------------------
5       5*fact(4)
4       5*4*fact(3)
3       5*4*3*fact(2)
2       5*4*3*2*fact(1)
1       5*4*3*2*1 = 120

'''


print('----fibonacci sequence with recursion----')
def fab(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fab(n-1)+fab(n-2)
l = [fab(x) for x in range(5)]
print(l)

'''

x         fibo(n-1)+fibo(n-2)                    print(finb(x)) 
----------------------------------------------------------------

0             0                                       0
1             1                                       1

2           f(1)+f(0)                                 1
            =1 +0 =1                                   

3           f(2)+f(0)                                 2
            =1 +1 =2

4           f(3 )+f(1)                                3    
            =2 +2 =3

5           f(4)+f(3)                                 5
            =3+2=5                                             

'''


print('----sum of digits of numbers using recursion----')
def s(x):
    if x == 0:
        return 0
    else:    
        return x%10+(s(x//10))
n = int(input("Enter a number: "))
print(f"sum of digits of {n} is {s(n)}")

'''

n              x%10+(s(x//10)
-----------------------------------------------
123           3 + sum(12)                   3

12            3 + 2 + sum(1)                5

1             3 + 2 + 1 + sum(0)            6

0             3 + 2 + 1 + 0 = 0             6

'''



print('----reverse of number using recursion----')
def r(x,rev):
    if x == 0:
        return rev
    else:
        d = x%10
        rev = rev*10+d
        return (r(x//10,rev))
n = int(input("Enter a number: "))
print(f"reverse of numbers of {n} is {r(n,0)}")

'''
n       rev     rev = rev * 10 + d      r(x//10,rev))
------------------------------------------------------
123     0       0*10+3=3                (12,3)
12      3       3*10+2=32               (1,32)
1       32      32*10+1=321             (0,321)
0       321     321

'''

# prodcut of two numbers without using product(*) operator

print('----using loop----')
n1 = 5
n2 = 4
product = 0
for i in range(1,n2+1):
    i = n1
    product+= i
print(product)

print('----using recursion----')
def mul(x,y):
    product = 1
    if y==0:
        return product
    else:
        return x+mul(x,y-1)
print(mul(5,4))

'''
x   y   x+mul(x,y-1)    product
5   4   5+mul(5,3)      5
5   3   5+mul(5,2)      10
5   2   5+mul(5,1)      15
5   1   5+mul(5,0)      20
5   0                   20

'''