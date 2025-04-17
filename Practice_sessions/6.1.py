# 1. Find the largest palindrome made from the product of two 3-digit numbers.

# def palindrome(p):
#     temp = p
#     rev = 0
#     while p!=0:
#         d = p%10
#         rev = 10*rev+d
#         p = p//10

#     if temp == rev:
#         return rev

# l = float('-inf')
# for i in range(999,99,-1):
#     for j in range(i,99,-1):
#         p = i*j
#         if p<=l:
#             break
#         if palindrome(p):
#             l = p
# print("Largest Palindrome:",l)        
        

# 2. Find the sum of all multiples of 3 and 5 below 1000.

# sum_is = 0
# for i in range(1,1000):
#     if i%3==0 and i%5==0:
#         sum_is+=i
# print("sum:",sum_is)


# 3. Implement a function to calculate the nth Fibonacci number using a loop between 10-100.

# n = int(input("Enter a number between 10-100: "))
# if n>=10 and n<100:
#     a,b = 0,1
#     i=1
#     while i<=n-2:
#         c = a+b
#         a,b = b,c
#         i+=1
#     print('Fibonacci number:',c)
# else:
#     print('You have to choose in given number.')


# 4. Reverse the digits of an integer without converting it to a string.

# p = int(input("Enter a number: "))
# rev = 0
# while p!=0:
#     d = p%10
#     rev = 10*rev+d
#     p = p//10
# print('reverse:',rev)


# 5. Implement a program to check if a number is prime.

# n = int(input("Enter a number: "))
# flag = True
# if n == 1:
#     flag = False
# for i in range(2,n):
#     if n%i==0:
#         flag = False
#         break
# if flag == True:
#     print(f'{n} is Prime.')
# else:
#     print(f'{n} is not a Prime.')


# 6. Calculate the sum of the digits of a number raised to a given power.

# n = int(input("Enter a number: "))
# p = int(input("Enter power of num: "))
# d_sum = 0
# while n!=0:
#     d = n%10
#     d_sum += d
#     n = n//10
# print(f'Power of number is: {d_sum**p}')


# 7. Generate all prime numbers less than a given number

# n = int(input("Enter a number: "))
# for x in range(2,n):
#     flag = True
#     if n == 1:
#         flag = False
#     for i in range(2,x):
#         if x%i==0:
#             flag = False
#             break
#     if flag == True:
#         print(x, end=" ")



# 8. Find the GCD (Greatest Common Divisor) of two numbers

# n1 = int(input("Enter first number: "))
# n2 = int(input("Enter second number: "))

# if n2>n1:
#     n1,n2 = n2,n1
# if n1>n2:
#     if n1%n2 == 0:
#         gcd = n2
#     else:
#         gcd = float('-inf')
#         for i in range(1,n2):
#             if n1%i == 0 and n2%i == 0:
#                 if i>gcd:
#                     gcd = i
# print('Greatest comman devisor: ',gcd)


# 9. Find the first 100 prime numbers.

# l = []
# n = 2
# while True:
#     flag = True
#     for i in range(2,n):
#         if n%i==0:
#             flag = False
#             break
#     if flag == True:
#         l.append(n)
#     n+=1
#     if len(l) == 100:
#         break
# print(l)



# 10. Implement a program to find the number of Armstrong numbers in a given range using while loop.

# start = int(input("Enter start range: "))
# end = int(input("Enter end range: "))
# while start <= end:
#     temp = start
#     l = len(str(temp))
#     arm = 0
#     while temp!=0:
#         d = temp%10
#         arm = arm+d**l
#         temp = temp//10
#     if start == arm:
#         print(arm,end=' ')
#     start+=1


# 11. Print all Fibonacci numbers up to a given number N.

# n = int(input("Enter a number: "))
# l = []
# a,b = 0,1
# l.append(a)
# l.append(b)
# k = 1
# while k<n:
#     c = a+b
#     a,b = b,c
#     l.append(c)
#     k+=1
# print(l)


# 12. Check a number is Krishnamurthy or not.

n = int(input("Enter a number: "))
temp = n
s = 0
while n!=0:
    d = n%10
    fact = 1
    for i in range(1,d+1):
        fact *= i
    s += fact
    n = n//10
if temp==s:
    print(f'{temp} is a Krishnamurthy number.')
else:
    print(f'{temp} is not a Krishamurthy number.')