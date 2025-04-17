# 1. Write a Python program to find the sum of the digits of a number without using a function.

# n = int(input("Enter a number: "))
# sum_digits = 0
# while n!=0:
#     digit = n%10
#     sum_digits = sum_digits+digit
#     n = n//10
# print(f'Sum of digits: {sum_digits}')


# 2. WAP and check number is Spy or not.
# 123, 1124

# n = int(input("Enter a number: "))
# sum_digits = 0
# product_digits = 1
# while n!=0:
#     digit = n%10
#     sum_digits = sum_digits+digit
#     product_digits = product_digits*digit
#     n = n//10
# if sum_digits == product_digits:
#     print("It's a Spy number.")
# else:
#     print("It's not a Spy number.")


# 3. Create a program to print the Fibonacci sequence up and sum of it.

# n = int(input("Enter the number: "))
# l = []
# a,b = 0,1
# l.extend([a,b])
# k = 2
# while k<n:
#     c = a+b
#     l.append(c)
#     a,b = b,c
#     k+=1
# print("Fibonacci sequence: ",l)
# print('sum: ',sum(l))


# 4. Give maximum number from 4 user input number.

# nums = input("Enter 4 numbers:").split(' ')
# max_num = float('-inf')
# for i in nums:
#     i = int(i)
#     if i>max_num:
#         max_num = i
# print("maximum number is: ",max_num)


# 5. Implement a program to count the number of even and odd digits in a given number.

# num = int(input("Enter a number: "))
# even_digits, odd_digits = 0,0
# while num!=0:
#     digit = num%10
#     if digit%2 == 0:
#         even_digits += 1
#     else:
#         odd_digits += 1
#     num = num//10
# print("Even count: ",even_digits)
# print("Odd count: ",odd_digits)


# 6. Convert a binary number to its decimal representation.

# n = int(input("Enter a binary number: "))
# temp = n
# decimal_form = 0
# k = 0
# while n!=0:
#     digit = n%10
#     decimal_form += digit*(2**k)
#     n = n//10
#     k+=1
# print(f'decimal representation of {temp} is: {decimal_form}')


# 7. Check if a Number is Efficient or not.

# n = int(input("Enter a number: "))
# sum_divisors = 0
# for i in range(1,n):
#     if n%i==0:
#         sum_divisors += i
# if sum_divisors>n:
#     print("It's an Efficient number.")
# else:
#     print("It's not an Efficient number.")


# 8. Write a Python program that finds the GCD (Greatest Common Divisor) of two numbers.
# HCF

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


# 9. Write a Python program to find the LCM (Least Common Multiple) of two numbers.

# n1 = int(input("Enter first number: "))
# n2 = int(input("Enter second number: "))
# temp1,temp2 = n1,n2

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

# lcm = (temp1*temp2)/gcd
# print('Greatest comman devisor: ',lcm)


# 10. Write a program to reverse the digits of a number using loops.

# n = int(input("Enter a number: "))
# rev = 0
# while n!=0:
#     d = n%10
#     rev = 10*rev+d
#     n = n//10
# print("reverse is: ",rev)


# 11. Write a Python program to calculate the sum of the digits of a number until the result is a single digit.

# n = int(input("Enter a number: "))

# def result(n):
#     sum_digits = 0
#     while n!=0:
#         d = n%10
#         sum_digits += d
#         n = n//10
#         r = sum_digits
#     if r<10:
#         return r
#     else:
#         return result(r)
    
# print("single digit sum: ",result(n))


# 12. Create a Python program that checks if a list is a palindrome without using string manipulation.

# l = [1,'r','a','d','a','r',1]
# rev = []
# for i in l:
#     rev.insert(0,i)

# if l == rev:
#     print("It's a palindrome.")
# else:
#     print("It's not a palindrome.")


# 13. Take one list and reverse it,  and print all palindrome number from list. 

# l = [123,121,334,3357,7667]
# rev = []
# for i in l:
#     rev = l[::-1]
# print(rev)
# for i in rev:
#     temp = i
#     pal = 0
#     while i!=0:
#         d = i%10
#         pal = 10*pal+d
#         i = i//10
#     if temp == pal:
#         print(temp, end=" ")


# 14.Create a program and print the perfect square number in a specific range.

# start = int(input("Enter starting of range: "))
# end = int(input("Enter end of range: "))
# for x in range(start,end+1):
#     n = x
#     flag = False
#     for i in range(1,n):
#         if i**2 == n:
#             flag = True
#             break
#     if flag == True:
#         print(n,end=' ')


# 15. Create a program that counts how many times a specific digit appears in a given number.

# n = input("Enter a number: ")
# s = input("Enter a specific digit: ")
# count = 0
# for i in n:
#     if i==s:
#         count+=1
# print(f'Count of {s} in {n} is: {count}')
