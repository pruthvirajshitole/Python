# 1. Write a Python program to check if a given number is a prime number.
# (Hint: A prime number is only divisible by 1 and itself.)  

# num = int(input("Enter a number: "))
# flag = True
# for i in range(2,num):
#     if num%i == 0:
#         flag = False
#         break
# if flag == True:
#     print(f'{num} is a prime number.')
# else:
#     print(f'{num} is not a prime number.')


# 2. Create a program to determine if a number is an Armstrong number.
# (Hint: An Armstrong number is equal to the sum of its digits raised to the power of the number of digits.)

# n = input("Enter a number: ")
# l = len(n)
# n = int(n)
# t = n
# a = 0
# while n!=0:
#     d = n%10
#     a = a+d**l
#     n = n//10
# if t == a:
#     print(f'{t} is an armstrong number.')
# else:
#     print(f'{t} is not an armstrong number')


# 3. Develop a Python program to check if a number is a Neon number.
# (Hint: A Neon number's square has a digit sum equal to the number itself.)

# n = int(input("Enter a number: "))
# sq = n**2
# t = n
# s = 0
# while sq!=0:
#     d = sq%10
#     s = s+d
#     sq = sq//10
# if t == s:
#     print(f'{t} is a neon number.')
# else:
#     print(f'{t} is not a neon number.')


# 4. Write a program to determine if a number is a Harshad number.
# (Hint: A Harshad number is divisible by the sum of its digits.)

# num = int(input("Enter a number: "))
# t = num
# s = 0
# while num!=0:
#     d = num%10
#     s = s+d
#     num = num//10
# if t%s == 0:
#     print(t,' is a hurshad number')
# else:
#     print(t,' is not a harshad number')


# 5. Create a Python script to check if three given numbers form a Pythagorean triplet.
# (Hint: Check if the square of one number equals the sum of the squares of the other two.)

# a = int(input("Enter first number: "))
# b = int(input("Enter second number: "))
# c = int(input("Enter third number: "))

# if a**2 + b**2 == c**2:
#     print("Given numbers are Pythogorean triplet.")
# else:
#     print("Not a Pythogorean triplet.")


# 6. Write a program to find the factorial of a given number.
# (Hint: The factorial of n is the product of all positive integers less than or equal to n.)

# n = int(input("Enter a number: "))
# fact = 1
# for i in range(1,n+1):
#     fact *= i
# print(f'{n}! = {fact}')
    

# 7. Create a Python program to determine if a number is a perfect number.
# (Hint: A perfect number equals the sum of its proper divisors, excluding itself.)

# n = int(input("Enter a number: "))
# sum = 0
# for x in range(1,n):
#     if n%x == 0:
#         sum+=x
# if sum==n:
#     print(f"{n} is a perfect number.")
# else:
#     print(f"{n} is not a perfect number.")


# 8. Write a Python script to generate all Fibonacci numbers up to a given number.
# (Hint: Each number is the sum of the previous two numbers, starting with 0 and 1.)

# r = int(input("Enter a number: "))
# l = []
# a = 0
# b = 1
# n = 1
# l.append(a)
# l.append(b)
# while n<=r:
#     c = a+b
#     a,b = b,c
#     n += 1
#     l.append(c)
# print(l)


# 9. Develop a Python program to check if a number is a strong number.
# (Hint: A strong number equals the sum of the factorials of its digits.)145

# n = int(input("Enter a number: "))
# t = n
# s = 0
# while n!=0:
#     d = n%10
#     fact = 1
#     for i in range(1,d+1):
#         fact *= i
#     s = s + fact
#     n = n//10
# if t == s:
#     print(f'{t} is a strong number.')
# else:
#     print(f'{t} is not a strong number.')
    

# 10. Write a program to check if a number is a palindrome.
# (Hint: A palindrome reads the same forwards and backwards.)

# num = int(input("Enter a number: "))
# t = num
# r = 0
# while num != 0:
#     d = num % 10
#     r = r * 10 + d
#     num = num // 10
# if t == r:
#     print(f"The entered number {t} is a palindrome.")
# else:
#     print(f"The entered number {t} is not a palindrome.")


# 11. Create a Python program to find the greatest common divisor (GCD) of two numbers.
# (Hint: GCD is the largest number that divides both numbers without leaving a remainder.)

# a = int(input("Enter first number: "))
# b = int(input("Enter second number: "))
# l = []
# for i in range(1,(a+1 or b+1)):
#     if a%i == 0 and b%i == 0:
#         l.append(i)
# divisor = l[-1]
# print(f'The greatest common divisor (GCD) of two numbers is {divisor}')


# 12. Write a Python program to check if a number is a perfect square.
# (Hint: A perfect square is the square of an integer.)

# n = int(input("Enter a number:"))
# flag = True
# for i in range(1,n):
#     if i**2 == n:
#         flag = False
#         break

# if flag == False:
#     print(f'{n} is a perfect square number.')
# else:
#     print(f'{n} is not a perfect square number.')
        

# 13. Develop a Python script to print first 10 prime nos.

# l = []
# for i in range(1,11):
#     num = i
#     flag = True
#     for j in range(2,num):
#         if num%j == 0:
#             flag = False
#             break
#     if flag == True:
#         l.append(num)
# print(l)

    
# 14. Create a program to generate all prime numbers within a given range.
# (Hint: Use a loop and check divisibility for each number in the range.)

# start = int(input("Enter starting of range:"))
# end = int(input("Enter ending of range:"))

# l = []
# for i in range(start,end+1):
#     num = i
#     flag = True
#     for j in range(2,num):
#         if num%j == 0:
#             flag = False
#             break
#     if flag == True:
#         l.append(num)
# print(f'All prime numbers between range {start} to {end} is: {l}')


# 15. Write a Python program to find the LCM (least common multiple) of two numbers.
# (Hint: LCM is the smallest positive number divisible by both numbers.)

a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
l = []
for i in range(2,(a+1 or b+1)):
    if a%i == 0 and b%i == 0:
        l.append(i)
divisor = l[0]
print(f'The LCM (least common multiple) of two numbers is: {divisor}')
