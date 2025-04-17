# 1. Question: Write a Python program to accept a list of numbers from the user and calculate the
# sum of integers, count of floats, and total number of elements using a loop.

# l = input("Enter a list of numbers seperated by comma: ").split(",")
# sum_integers = 0
# count_floats = 0
# total_elements = 0
# for i in l:
#     total_elements += 1
#     if '.' in i:
#         count_floats += 1
#     else:
#         sum_integers += int(i)

# print("sum of integers is: ",sum_integers)
# print("total count of floats is: ",count_floats)
# print("total number of elements is: ",total_elements)


# 2. Question: Write a program to find whether the sum of the digits of a number entered by the
# user is even or odd. Use loops to calculate the sum and conditions to check its parity.

# num = input("Enter a number: ")
# t = num
# r = 0
# for i in num:
#     i = int(i)
#     d = i%10
#     r = r+d
#     i = i//10
# if r%2 == 0:
#     print(f'sum of all digits of {t} is even')
# else:
#     print(f'sum of all digits of {t} is odd')


# 3. Question: Create a Python program to generate the following pattern based on a user-input number N:  
#    - For odd N:  
#      1
#      1 2
#      1 2 3
#      1 2 3 4
#      1 2 3 4 5

#    - For even N:  
#          1
#        2 2
#      3 3 3
#    4 4 4 4

# n = int(input("Enter a number: "))
# if n%2 != 0:
#     for i in range(n,n+6):
#         for j in range(n,i+1):
#             print(j, end=' ')
#         print()


# PENDING : LOGIC IS NOT APPLICABLE FOR BIG VALUES

# else:
#     for i in range(n,n+5):
#         for j in range(n,n+10-i):
#             print(' ', end=' ')
#         for k in range(n,i+1):
#             print(i, end=' ')
#         print()

    
# 4. Question: Write a Python program to generate the first N numbers in the Fibonacci sequence and display them in a triangular pattern.  
#    Example for N=5:  
#    0
#    1 1
#    2 3 5

# n = 0
# a,b = 0,1
# for x in range(0,3):
#     for i in range(0,n+1):
#         print(a, end=' ')
#         c = a+b
#         a,b = b,c
#     print()
#     n += 1


# 5. Question: Write a Python program to input a mixed list of integers, floats, and strings.
# Use conditions to separate and count them. If the count of integers is higher than floats,
# print a message: "Integers dominate!" Otherwise, print: "Floats dominate!"

# PENDING

# l = input("Enter any inputs (such as int, float, and strings: ) ").split(',')
# count_intergers, count_float, count_strings = 0,0,0
# for i in l:
#     if i != int(i):
#         count_strings += 1
#     elif '.' in i:
#         count_float += 1
#     else:
#         count_intergers += 1
# if count_intergers > count_float:
#     print("Integers Dominate!")   
# else:
#     print("Floats Dominate!")


# 6. Question: Create a program to check if a number is an Armstrong number, and if it is,
# print the digits of the number in reverse order.

# n = input("Enter a number: ")
# l = len(n)
# n = int(n)
# r = 0
# reverse = 0
# t = n

# while n != 0:
#     d = n%10
#     r = r + d**l
#     reverse = 10*reverse + d
#     n = n//10
# if r == t:
#     print(f'reverse of {t} is {reverse}')
# else:
#     print(f'{t} is not an armstrong number.')



# 7. Question: Write a program to check if a number is a palindrome. If it is,
# check whether the reversed number is prime. Use both loops and conditions in your solution.

# num = int(input("Enter a number: "))
# r=0
# t = num
# while num != 0:
#     d = num%10
#     r = r*10 + d
#     num = num//10

# if r == t:
#     flag = True
#     i = 2
#     while i<r:
#         if r%i==0:
#             flag = False
#             break
#         i+=1
#     if flag == True:
#         print(f'The number {t} is polindrome. and reverse of {t} is a prime number.')
#     else:
#          print(f'The number {t} is polindrome. but reverse of {t} is not a prime number.')



# 8. Question: Write a program to generate the following pattern for numbers that are divisible by 3 up to a given N:  
#    Example for N=10:  
#    3
#    3 6
#    3 6 9

# PENDING

# n = 10
# for i in range(1,n+1):
#     if i%3 == 0:
#         for j in range(1,i+1):
#             print(i, end=' ')
#         print()



# 9. Question: Accept a string from the user and display the characters in the following pattern using loops:  
#    Example for HELLO:  
#    H
#    H E
#    H E L
#    H E L L
#    H E L L O

# s = input("Enter a string:")
# l = len(s)
# for i in range(1,l+1):
#     for j in range(i):
#         print(s[j], end = ' ')
#     print()


# 10. Question: Write a program to take an integer input from the user.  
#    - If it is divisible by both 5 and 3, display: "FizzBuzz."  
#    - Otherwise, check if the reversed number is an Armstrong number. If yes, display: "Armstrong."


# 11. Question: Write a program to generate a pyramid pattern of stars (*) where the total rows depend on a user-input number N.  
#    - If N is odd, print a normal pyramid.  
#    - If N is even, print the numbers from 1 to N instead of stars.  
#    Example for N=4:  
#        1
#       1 2
#      1 2 3
#     1 2 3 4


# 12. Question: Create a program to take a number N from the user and print:  
#    - Its Fibonacci value if N is prime.  
#    - Its digits in reverse if N is not a palindrome.  
#    - A triangular star pattern if N is an Armstrong number.