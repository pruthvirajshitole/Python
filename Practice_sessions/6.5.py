# 1. Write a program that finds the largest number that can be formed by rearranging
# the digits of a given number using loops.
    
# n = int(input("Enter a number: "))
# l = []
# d = 0
# while n!=0:
#     d = n%10
#     l.append(d)
#     n = n//10

# for i in range(len(l)):
#     for j in range(i,len(l)):
#         if l[i]>l[j]:
#             l[i],l[j] = l[j],l[i]

# largest = ''
# for k in l:
#     largest = str(k)+largest
# print("Rearranged largest number:",largest)    


# 2. Convert a decimal number to its binary.

# n = int(input("Enter a decimal number: "))
# temp = n
# decimal_form = 0
# binary = ''
# while n!=0:
#     d = n%2
#     print(d)
#     binary += str(d)
#     n = n//2
# print(f'binaary representation of {temp} is: {binary[::-1]}')


# 3. Find the smallest number that is both a square and a cube within a given range.
# 64

# start = int(input("Enter starting range: "))
# end = int(input("Enter end range: "))
# for i in range(start,end):
#     for j in range(1,i+1):
#         if i == j**2:
#             for k in range(1,i+1):
#                 if i==k**3:
#                     print(i)
#                     break


# 4. Calculate the sum of all prime numbers below a given number.

# n = int(input("Enter a number: "))
# sum_prime = 0
# for i in range(2,n):
#     flag = True
#     for j in range(2,i):
#         if i%j==0:
#             flag = False
#             break
#     if flag==True:
#         sum_prime+=i
# print("Sum of all prime numbers:",sum_prime)


# 5. Determine the number of trailing zeros in the factorial of a given number.

# n = int(input("Enter a number: "))
# fact = 1
# for i in range(1,n+1):
#     fact*=i
# n = fact
# count_zeros = 0
# while n!=0:
#     d = n%10
#     if d == 0:
#         count_zeros += 1
#     else:
#         break
#     n = n//10
# print(count_zeros)


# 6. WAP and Check a number is a Harshad number or not.

# num = int(input("Enter a number: "))
# t = num
# s = 0
# while num!=0:
#     d = num%10
#     s = s+d
#     num = num//10
# if t%s == 0:
#     print(t,' is a harshad number.')
# else:
#     print(t,' is not a harshad number.')


# 7. WAP and print the prime number in a range and sum of it.

# start = int(input("Enter starting range: "))
# end = int(input("Enter end range: "))
# sum_prime = 0
# for i in range(start,end):
#     flag = True
#     if i == 1:
#         flag = False
#     for j in range(2,i):
#         if i%j==0:
#             flag = False
#             break
#     if flag==True:
#         sum_prime+=i
#         print(i,end=' ')
# print("\nSum of all prime numbers:",sum_prime)


# 8. Write a python program that when user will turn 100 years old.

# age = int(input("Enter your age: "))
# print(f'You will be 100 years old on {2025-age+100}.')


# 9. Write a Python Program to Return Middle Three Characters of a String

# s = input("Enter a string: ")
# l = len(s)//2
# print(s[l-1:l+2])


# 10. WAP to convert list of Tuples into Dictionary.

l = [(1,2),(3,4),(5,6)]