# 1. Write a Python function called is_prime that checks if a given number
# is a prime number. Test it with multiple values.

# def is_prime(x):
#     flag = True
#     for i in range(2,x):
#         if x%i==0:
#             flag = False
#             break
#     if flag == True:
#         return 'Prime'
#     else:
#         return 'Not a prime'
# print(is_prime(4))


# 2. Create a function named fibonacci that generates the first n numbers in the Fibonacci sequence.
# Use user input to define n.

# def fab(x):
#     if x == 0:
#         return 0
#     elif x == 1:
#         return 1
#     else:
#         return fab(x-1)+fab(x-2)
#         l = [fab(x) for x in range(5)]
# n = int(input("Enter a number: "))
# l = [fab(x) for x in range(n)]
# print(l)


# 3. Define a function reverse_string that takes a string as input and returns the reversed string.

# def reverse_string(s):
#     rev = ''
#     for i in s:
#         rev = i+rev
#     return rev
# print(reverse_string('hello'))


# 4. Write a lambda function to calculate the square of a number.
# Use it with a map function to find squares of numbers in the list [2, 3, 4, 5, 6].

# l=[2,3,4,5,6]
# sq=[(lambda a:a**2)(x) for x in l]
# print(sq)

# a=list(map(lambda a:a**2,l))
# print(a)


# 5. Create a higher-order function named apply_operation that takes two numbers and a function
# (e.g., add, subtract, multiply) as arguments and returns the result of the operation.

# def apply_operation(n1,n2,ope):
#   return ope(n1,n2)

# def add(x,y):
#   return x+y

# def sub(x,y):
#   return x-y

# def mul(x,y):
#   return x*y
# print(apply_operation(5,3,add))
# print(apply_operation (4,2,sub))
# print(apply_operation(2,4,mul))


# 6. Write a lambda function to filter all odd numbers from a list [10, 15, 21, 30, 35, 40].

# l = [10, 15, 21, 30, 35, 40]
# print(list(filter(lambda x:x%2==1,l)))


# 7. Implement a function calculate_factorial that computes the factorial of a number using recursion.

# def fact(n):
#     if n == 0:
#         return 1
#     else:
#         return n*fact(n-1)
# print(fact(5))


# 8. Use a lambda function with the reduce function from the functools module to find the product
# of all elements in a list [1, 2, 3, 4, 5].

# from functools import reduce

# l = [1,2,3,4,5]

# def product(x,y):
#     return x*y
# print(reduce(product,l))


# 9. Create a function called outer_function that has an inner functionnamed inner_function.
# The inner function should print a message, and the outer function should call it.

# def outer_function():
#     def inner_function():
#         return "You are in inner function."
#     return inner_function()
# print(outer_function())


# 10. Demonstrate the use of global and local variables by creating a function that modifies
# a global variable and prints the result.

# a=3
# def modify():
#   global a
#   a+=4
#   print("Global a inside function",a)

# print("global a before calling",a)

# modify()
# print("global a after calling",a)


# 11. Write a Python function is_palindrome that checks if a string is a palindrome.
# Use lambda functions where appropriate.

# def is_palindrome(s):
#   return (lambda x:x==x[::-1])(s)
# s = input("Enter a string: ")
# k = is_palindrome(s)
# if k == True:
#     print("It's a palindrome.")
# else:
#     print("It's not a palindrome.")


# 12. Use a higher-order function to sort a list of tuples [(1, 'banana'), (2, 'apple'), (3, 'cherry')]
# based on the second element of each tuple.


# 13. Create a function power_function that returns a lambda function.
# The returned lambda function should calculate the power of a number raised to a specified exponent.

# def power_function(a,b):
#     return (lambda x,y:x**y)(a,b)
# print(power_function(2,10))


# 14. Write a function create_multiplier that takes a number n as input and returns a lambda function.
# The lambda function should multiply its input by n.

# def create_multiplier():
#     n = int(input("Enter a number: "))
#     return (lambda x:x**2)(n)
# print(create_multiplier())


# 15. Implement a function called variable_scope_demo to illustrate the difference between local,
# enclosing, and global scopes using variables of the same name.