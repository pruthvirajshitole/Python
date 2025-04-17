# 1. Write a recursive function to calculate the factorial of a given number.

# def fact(x):
#     if x == 1:
#         return 1
#     else:
#         return x*fact(x-1)
# n = int(input("Enter a number: "))
# print(fact(n))


# 2. Implement a recursive function to generate the Fibonacci sequence up to the nth term.  

# def fab(n):
#     if n == 0:
#         return 0
#     elif n == 1:
#         return 1
#     else:
#         return fab(n-1)+fab(n-2)
# l = [fab(x) for x in range(5)]
# print(l)


# 3. Create a recursive function to find the sum of digits in a given integer.  

# def sum(x):
#     if x==0:
#         return 0
#     else:
#         return x%10+sum(x//10)
# print(sum(321))


# 4. Write a recursive function to reverse a given string.  

# def rev(x,re):
#     if x == 0:
#         return re
#     else:
#         d = x%10
#         re = re*10+d
#         return (rev(x//10,re))
# print(rev(123,0))


# 5. Implement a recursive function to check if a given number is a palindrome.  

# def rev(x,re):
#     if x == 0:
#         return re
#     else:
#         d = x%10
#         re = re*10+d
#         return (rev(x//10,re))
# n = int(input("Enter a num: "))
# p = rev(n,0)
# if p == n:
#     print("It's a palindrome.")
# else:
#     print("It's not a palindrome.")


# 6. Create a lambda function to calculate the square of a number.  

# n = int(input("Enter a number: "))
# print((lambda n:n**2)(n))


# 7. Use a lambda function to filter out all even numbers from a given list. 

# l=[1,2,3,4,5,6,7,8]
# b=list(filter(lambda a:a%2 ==0 ,l))
# print(b)


# 8. Write a lambda function that sorts a list of tuples based on the second element of each tuple.

# PENDING


# 9. Use the map function to add 5 to every element in a list.

# l = [2,5,6,8,9]
# print(list(map(lambda i:i+5,l)))


# 10. Use map and a lambda function to convert a list of strings into uppercase.  

# l = ['hello','i','am','devil']
# def up(x):
#     return x.upper()
# print(list(map(up,l)))


# 11. Write a program using filter to find all the prime numbers in a list.  

# l = [i for i in range(11)]
# def prime_no(x):
#     flag = True
#     for i in range(2,x):
#         if x%i == 0:
#             flag = False
#     if flag == True:
#         return x
# print(list(filter(prime_no,l)))


# 12. Use the reduce function to calculate the product of all elements in a list.  

# from functools import reduce

# l = [2,3,4,5,6]
# print(reduce(lambda x,y:x*y,l))


# 13. Implement a program that uses map to calculate the square roots of a list of numbers. 

# l = [4,9,15,100]
# print(list(map(lambda x:x**(0.5),l)))


# 14. Write a program using filter to extract words longer than 5 characters from a list of strings. 

# l = ['apple','cricket','dog','devil','helloween']

# def words_f(i):
#         if len(i)>5:
#             return i
# print(list(filter(words_f,l)))


# 15. Create a program that combines map, filter, and reduce to filter even numbers, double their values,
# and find their sum from a given list.

from functools import reduce
l = [1,2,3,4,5,6,7,8,9,10]

even = list(filter(lambda x:x%2==0,l))
print(even)

double = list(map(lambda x:x*2,even))
print(double)

sum = reduce(lambda x,y:x+y,double)
print(sum)