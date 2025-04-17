# # implement compile time polymorphism for multiplication of 1 no 2,no and 3 nos

# def mul(a,b=None,c=None):
#     if b==None and c==None:
#         return a
#     elif c==None:
#         return a*b
#     else:
#         return a*b*c
 
# print(mul(3))
# print(mul(1,2))
# print(mul(1,2,3))


# # implement run time polymorphism for Animal class with speak method

# class Animal:
#     def dog(self):
#         print("Dog barks bowww!!")
#     def display(self):
#         print("Dog is also an animal")
    
# class Speak(Animal):
#     def cat(self):
#         print("Cat makes meoww!!!")


# a = Animal()
# a.dog()
# a.display()

# print("----object of Speak----")
# c = Speak()
# c.cat()
# c.display()
# c.dog()


# 1. The Bouncing Ball  
# A ball is dropped from a height H. Each time it hits the ground, it bounces back to H/2.
# The ball stops bouncing when its height is less than 1.  
# Write a program to determine the total number of times the ball touches the ground before stopping.  

# Input:  
# An integer H (initial height).  
# Output:  
# An integer representing the number of bounces.

# h = int(input("Enter the height: "))
# count = 0
# while h>1:
#     if h/2 > 1:
#         count+=1
#     h = h/2

# print(count)


# 2. Reverse Sum Sequence  
# A sequence is formed as follows:  
# - Start with N.  
# - Reverse its digits.  
# - Add the reversed number to N.  
# - Repeat until a palindrome number is formed.  
# Find the first palindrome number obtained.  
# Input:  
# An integer N.
# Output:  
# An integer representing the palindrome number.

# def palindrome(n):
#     temp = n
#     rev = 0
#     while n!=0:
#         d = n%10
#         rev = 10*rev+d
#         n = n//10
#     if temp != rev:
#         new = temp+rev
#         return palindrome(new)
#     else:
#         return f'{temp} is a palindrome.'

# n = int(input("Enter a number: "))
# print(palindrome(n))


# s = '1,2'
# # l[1,2] using list comprehension
# l = [x for x in eval(s)]
# print(l)



