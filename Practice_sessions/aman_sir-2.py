# 1. WAP that takes two numbers as arguments and returns their GCD (Greatest Common Divisor).  
#    - Hint: GCD (HCF) of two numbers is the largest number that divides both numbers completely.
#      Use the Euclidean algorithm.  

# def gcd(a,b):
#     while b:
#         a, b = b,a%b
#     return f'GCD:{a}'
# print(gcd(105,252))


# 2. WAP that takes a number as an argument and returns True if it is a perfect number, otherwise False.  
#    - Hint: A perfect number is a number whose sum of proper divisors equals the number itself (e.g., 6 = 1 + 2 + 3).  

# def perfect(n):
#     sum = 0
#     for i in range(1,n):
#         if n%i==0:
#             sum += i
#     if sum == n:
#         return True
#     else:
#         return False
# print(perfect(28))


# 3. WAP that takes a number as an argument and returns True if it is a strong number, otherwise False.  
#    - Hint: A strong number is a number where the sum of the factorial of its digits equals the number
#      itself (e.g., 145 = 1! + 4! + 5!).

# def strong(n):
#     t = n
#     sum = 0
#     while t!=0:
#         d = t%10
#         fact = 1
#         for i in range(1,d+1):
#             fact *= i
#         sum += fact
#         t = t//10
#     if n == sum:
#         return True
#     else:
#         return False
# print(strong(145))


# 4. WAP that takes two numbers as arguments and returns the LCM (Least Common Multiple).  
#    - Hint: LCM of two numbers is the smallest number that is a multiple of both numbers.
#      Formula: LCM(a, b) = (a × b) / GCD(a, b).  

def gcd(a,b):
    while b:
        a, b = b,a%b
    return f'GCD:{a}'


    
print(gcd(105,252))


# 5. WAP that takes a number as an argument and returns the reverse of that number.  
#    - Hint: Convert the number into a string, reverse it, and convert it back to an integer.  

# 6. WAP that takes a number as an argument and returns the sum of its digits.  
#    - Hint: Extract each digit using modulus (%) and division (//) and sum them up.  

# 7. WAP that takes a number as an argument and returns True if it is a Harshad number, otherwise False.  
#    - Hint: A Harshad number is divisible by the sum of its digits (e.g., 18 → 1+8 = 9, and 18 is divisible by 9).  

# 8. WAP that takes a number as an argument and returns True if it is an automorphic number, otherwise False.  
#    - Hint: A number is automorphic if its square ends with the number itself (e.g., 25² = 625).  

# 9. WAP that takes a number as an argument and returns True if it is a perfect square, otherwise False.  
#    - Hint: A perfect square is a number that is the square of an integer (e.g., 16 = 4²). Use math.sqrt().  

# 10. WAP that takes a number as an argument and returns True if it is a Spy number, otherwise False.  
#     - Hint: A Spy number has the sum of its digits equal to the product of its digits (e.g., 123 → 1+2+3 = 6 and 1×2×3 = 6).  

# 11. WAP that takes a number as an argument and returns True if it is a Disarium number, otherwise False.  
#     - Hint: A Disarium number is a number where the sum of its digits raised to their respective positions equals the number (e.g., 89 = 8¹ + 9²).  

# 12. WAP that takes a number as an argument and returns True if it is a Duck number, otherwise False.  
#     - Hint: A Duck number contains at least one zero but does not start with zero (e.g., 102, 703).  

# 13. WAP that takes two numbers as arguments and returns their HCF (Highest Common Factor).  
#     - Hint: HCF is the same as GCD. It is the highest number that divides both numbers without a remainder.  

# 14. WAP that takes two numbers as arguments and returns their sum without using the + operator.  
#     - Hint: Use bitwise operators (&, ^, and <<) to perform addition.  

# 15. WAP that takes a number as an argument and returns the sum of all prime numbers up to that number.  
#     - Hint: Check each number for primality and sum up all prime numbers in the range.  

# 16. WAP that takes a number as an argument and returns True if it is a Kaprekar number, otherwise False.  
#     - Hint: A Kaprekar number’s square can be split into two parts that sum up to the original number (e.g., 45² = 2025 → 20 + 25 = 45).  

# 17. WAP that takes a number as an argument and returns the next palindrome number.  
#     - Hint: A palindrome number reads the same forward and backward. Find the next number greater than the input that satisfies this condition.  

# 18. WAP that takes two numbers as arguments and returns their product without using the * operator.  
#     - Hint: Use repeated addition or bitwise shift operations.  

# 19. WAP that takes a number as an argument and returns the sum of its prime factors.  
#     - Hint: Find all prime factors of the number and sum them up.  

# 20. WAP that takes a number as an argument and returns the number of trailing zeros in its factorial.  
#     - Hint: Count the number of times 5 appears as a factor in the numbers from 1 to n using n // 5 + n // 25 + n // 125 ....