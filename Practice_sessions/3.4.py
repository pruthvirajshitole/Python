# 1. Write a Python program to print the reverse of a number using a loop.

# n = 321
# rev = 0
# while n!=0:
#     d = n%10
#     rev = 10*rev+d
#     n = n//10
# print(rev)


# 2. Write a Python program to check if a number is a palindrome or not.

n = 234
# temp = n
# rev = 0
# while n!=0:
#     d = n%10
#     rev = 10*rev+d
#     n = n//10
# if temp == rev:
#     print("It's a palindrome.")
# else:
#     print("It's not a palindrome.")


# 3. Write a Python program to check if a number is an Armstrong number.

# n = 153
# n = str(n)
# l = len(n)
# arm = 0
# n = int(n)
# temp = n
# while n!=0:
#     d = n%10
#     arm = arm+d**l
#     n = n//10
# if temp == arm:
#     print("It's an Armstrong number.")
# else:
#     print("It's not a Armstrong number.")


# 4. Write a Python program to check if a number is a perfect number.

# n = 6
# sum_d = 0
# for i in range(1,n):
#     if n%i==0:
#         sum_d+=i
# if sum_d == n:
#     print("It's a perfect number.")
# else:
#     print("It's not a perfect number.")


# 5. Write a Python program to print all prime numbers up to a given number.

# start = int(input("Enter start of range: "))
# end = int(input("Enter the end of range: "))
# l = []
# for n in range(start+1,end):
#     flag = True
#     for i in range(2,n):
#         if n%i==0 and n==1:
#             flag = False
#             break
#     if flag == True:
#         l.append(n)
# print(l)


# 6. Write a Python program to check if a number is prime or not.

# n = 21
# flag = True
# for i in range(2,n):
#     if n%i==0:
#         flag = False
#         break
# if flag == True:
#     print("It's a prime number.")
# else:
#     print("It's not a prime number.")


# 7. Write a Python program to find all perfect numbers in a given range.

# start = int(input("Enter start of range: "))
# end = int(input("Enter the end of range: "))
# l = []
# for n in range(start,end):
#     sum_d = 0
#     for i in range(1,n):
#         if n%i==0:
#             sum_d+=i
#     if sum_d == n:
#         l.append(n)
# print(l)


# 8. Write a Python program to find all Armstrong numbers in a given range.

# start = int(input("Enter start of range: "))
# end = int(input("Enter the end of range: "))
# lst = []
# for n in range(start,end):
#     n = str(n)
#     l = len(n)
#     arm = 0
#     n = int(n)
#     temp = n
#     while n!=0:
#         d = n%10
#         arm = arm+d**l
#         n = n//10
#     if temp == arm:
#         lst.append(temp)
# print(lst)


# 9. Write a Python program to find the sum of digits of a number using a loop.

# n = int(input("Enter a number: "))
# sum_digits = 0
# while n!=0:
#     d = n%10
#     sum_digits = sum_digits+d
#     n = n//10
# print(sum_digits)


# 10. Write a Python program to count the number of even and odd digits in a list.

# l = [1,2,3,24,5,6,7,8,9]
# count_even,count_odd = 0,0
# for i in l:
#     while i!=0:
#         d = i%10
#         if d%2==0:
#             count_even += 1
#         else:
#             count_odd += 1
#         i = i//10    
# print(f'Even count is: {count_even}\nOdd count is: {count_odd}')


# 11. Write a Python program to check if a number is a strong number. #145

# n = int(input("Enter a number: "))
# temp = n
# sum_digits=0
# while n!=0:
#     d = n%10
#     fact = 1
#     for i in range(1,d+1):
#         fact*=i
#     sum_digits = sum_digits+fact
#     n = n//10
# if temp == sum_digits:
#     print("It's a strong number.")
# else:
#     print("It's not a strong number.")


# 12. Write a Python program to print Fibonacci series up to a given number using a loop.

# n = int(input("Enter a number: "))
# a,b = 0,1
# l = []
# l.append(a)
# l.append(b)
# k = 1
# while k<n-1:
#     c = a+b
#     l.append(c)
#     a,b = b,c
#     k+=1
# print(l)


# 13. Write a Python program to print all the divisors of a number.

# n = int(input("Enter a number: "))
# l = []
# for i in range(1,n+1):
#     if n%i==0:
#         l.append(i)
# print(l)


# 14. Write a Python program to check if a number is an abundant number.
# 12,18,20

# n = int(input("Enter a number: "))
# sum_divisors = 0
# for i in range(1,n):
#     if n%i==0:
#         sum_divisors += i
# if sum_divisors>n:
#     print("It's an abundant number.")
# else:
#     print("It's not an abundant number.")


# 15. Write a Python program to check if a number is a perfect square using a loop.

# n = int(input("Enter a number: "))
# flag = False
# for i in range(1,n):
#     if i**2 == n:
#         flag = True
#         break
# if flag == True:
#     print("It's a perfect square number.")
# else:
#     print("It's not a perfect square number.")
    

# 16. Write a Python program to find the sum of all prime numbers in a given range.

# start = int(input("Enter start of range: "))
# end = int(input("Enter the end of range: "))
# sum_primes = 0
# for n in range(start+1,end):
#     flag = True
#     for i in range(2,n):
#         if n%i==0 and n==1:
#             flag = False
#             break
#     if flag == True:
#         sum_primes+=n
# print(sum_primes)


# 17. Write a Python program to check if a number is an Armstrong number with n digits.

# n = int(input("Enter a number: "))
# n = str(n)
# l = len(n)
# n = int(n)
# temp = n
# arm = 0
# while n!=0:
#     d = n%10
#     arm = arm+d**l
#     n = n//10
# if temp==arm:
#     print("It's a armstrong number.")
# else:
#     print("It's not a armstrong number.")



# 18. Write a Python program to find the factorial of a number using a loop.

# n = int(input("Enter a number: "))
# fact = 1
# for i in range(1,n+1):
#     fact *= i
# print(fact)


# 19. Write a Python program to print the first n numbers of the Fibonacci sequence.

# n = int(input("Enter a number: "))
# a,b = 0,1
# l = []
# l.append(a)
# l.append(b)
# k = 1
# while k<n-1:
#     c = a+b
#     l.append(c)
#     a,b = b,c
#     k+=1
# print(l)


# 20. Write a Python program to check if a number is a Narcissistic number.
# Armstrong number

# n = int(input("Enter a number: "))
# n = str(n)
# l = len(n)
# narci = 0
# n = int(n)
# temp = n
# while n!=0:
#     d = n%10
#     narci = narci+d**l
#     n = n//10
# if temp == narci:
#     print("It's a Narcissistic number.")
# else:
#     print("It's not a Narcissistic number.")