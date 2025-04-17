# 1. Find the second largest element in a list.(without using inbuilt-function)

# GO ONCE MORE

# l = [18,1,17,3,5,6,8,9,4,2,12]
# largest = float('-inf')
# second_largest = float('-inf')
# for i in l:
#     if i>largest:
#         second_largest = largest
#         largest = i
#     elif i>second_largest and i!=largest:
#         second_largest = i

# print("Second largest is: ",second_largest)


# 2. Write a function to find the sum of all prime numbers below a given integer n.
# Implement this using a for loop, checking for primality within each iteration.

# n = int(input("Enter a number: "))
# sum = 0
# for i in range(2,n):
#     flag = True
#     for j in range(2,i):
#         if i%j==0:
#             flag = False
#             break
#     if flag == True:
#         sum += i
# print(sum)


# 3. Implement a program to print all possible combinations of characters from two strings.
# Use a nested for loop to generate each combination.

# s1 = input("Enter a first string: ")
# s2 = input("Enter second string: ")

# for i in s1:
#     for j in s2:
#         print(i+j, end=' ')


# 4. Given a list of strings, write a function to find the most common character across all strings using iterative loops.

# l = ['apple','banana','lemon','papaya']

# d = {}
# for i in l:
#     for j in i:
#         if j not in d:
#             d[j] = 1
#         else:
#             d[j]+=1

# count = 0
# for k,l in d.items():
#     if l>count:
#         most_occured_char = k
#         count = l
#         print(count)
# print(f'most comman char={most_occured_char} with count={count}')
        

# 5. Write a program to flatten a nested list.

# l=[['a',['b','c']] ,['d', 'e']]

# l1=[]
# for x in l:
#   if isinstance(x,list):
#     for y in x:
#       l1.extend(y)
#   else:
#       l1.append(x)
# print(l1)


# def flatten(l):
#     res = []
#     for i in l:
#         if isinstance(i,list):
#             res.extend(flatten(i))
#         else:
#             res.append(i)
#     return res
    
# l = [[1,2,3,[5,6]],[4,6],[9,8]]
# print(flatten(l))



# if nested list includes tuples also

# def flatten(l):
#     res = []
#     for i in l:
#         if isinstance(i,(list,tuple)):
#             res.extend(flatten(i))
#         else:
#             res.append(i)
#     return res
    
# l = [[1,2,3,[5,6]],[4,6,(7,8)],[9,8]]
# print(flatten(l))


# 6. Implement a function to merge two sorted lists without using built-in functions.
# Use loops to traverse and compare elements from both lists.

# l1 = [1,2,3,4,5,6]
# l2 = [11,14,15,18,23]
# merged_l = []

# i,j = 0,0
# while i<len(l1) and j<len(l2):
#         if l1[i]<l2[j]:
#             merged_l.append(l1[i])
#             i+=1
#         else:
#             merged_l.append(l2[j])
#             j+=1
# merged_l.extend(l1[i:])
# merged_l.extend(l2[j:])

# # while i < len(l1):
# #     merged_l.append(l1[i])
# #     i += 1
    
# # while j < len(l2):
# #     merged_l.append(l2[j])
# #     j += 1

# print(merged_l)


# 7. Given a list of integers, write a function to find all pairs of numbers that
# add up to a target sum. Implement this with a nested for loop.

# l = [2,3,4,5,6,7,8,9,1]

# target_sum = int(input("Enter a target sum: "))
# temp = target_sum
# l1 = []
# for i in l:
#     target_sum = temp
#     if i<target_sum:
#         target_sum -= i
#         if target_sum in l:
#             if i != target_sum :
#                 l1.append((i,target_sum))
    
# print(l1)

# num= [1,2,3,4,5,6]
# target_sum=int(input("Enter a target number: "))

# pairs=[]
# s=set()
# for i in num:
    
#     diff=target_sum-i 
#     if diff in s:
#         pairs.append((diff,i))
#     s.add(i)
# print(pairs)


# 8. Find the frequency of each character in a string.

# s = input("Enter a string: ")
# d = {}

# for i in s:
#     if i not in d:
#         d[i] = 1
#     else:
#         d[i] += 1
# print(d)


# 9. Given a number n, implement a for loop to find all divisors of n.
#  Return them in a sorted list.

# n = int(input("Enter a number: "))
# l = []
# for i in range(1,n+1):
#     if n%i==0:
#         l.append(i)
# print(sorted(l))


# 10. Write a program that calculates the Fibonacci sequence up to the
# n-th term using a while loop, where n is the input.

# n = int(input("Enter a number: "))

# a=0
# b=1
# l = []
# k=1
# l.append(a)
# l.append(b)
# while k<n-1:
#     c = a+b
#     l.append(c)
#     a,b = b,c
#     k+=1
# print(l)
    

# 11. Implement a program that prints all the prime numbers up to a given number n using a for loop.

# n = int(input("Enter a number: "))
# l = []
# for i in range(2,n+1):
#     flag = True
#     for j in range(2,i):
#         if i%j==0:
#             flag = False
#             break
#     if flag == True:
#         l.append(i)
# print(l)


# 12. Given a string, write a function to reverse it using a while loop without
# using Python's built-in string reversal methods.

# s = input("Enter a string: ")
# rev = ''
# i = len(s)-1
# while len(s)!=len(rev):
#     rev = rev+s[i]
#     i-= 1
# print(rev)


# 13. Check a given number is Strong or not by using while loop.

# n = int(input("Enter a number: "))
# temp = n
# s = 0
# while n!=0:
#     d = n%10
#     fact = 1
#     for i in range(1,d+1):
#         fact *= i
#     s += fact
#     n = n//10
# if temp==s:
#     print(f'{temp} is a strong number.')
# else:
#     print(f'{temp} is not a strong number.')


# 14. Write a function that prints all the Armstrong number from a list.

# l = [1,3,7,34,145,253,153,9]
# res = []
# for i in l:
#     temp = i
#     i = str(i)
#     length = len(i)
#     i = int(i)
#     arm = 0
#     while i!=0:
#         d = i%10
#         arm = arm+d**length
#         i = i//10
#     if temp == arm:
#         res.append(temp)
# print(res)


# 15. Write a program to remove duplicates from a list without using set().

# l = [1,4,5,6,7,5,3,5,7,54,3,2,3,8]
# res = []
# for i in l:
#     if i not in res:
#         res.append(i)
# print(res)


# 16. WAP and prints longest word from list.

# l = ['apple','Lucifer is devil','india','Python','longest one']
# longest = 0
# for i in l:
#     if len(i)>longest:
#         longest = len(i)
#         word = i
# print(f'longest word is: {word}')


# 17. Check if a list is a palindrome.(without using slicing)

# l = ['r','a','d','a','r']
# r = []
# for i in l:
#     r.insert(0,i)
# if l==r:
#     print("It's a palindrome.")
# else:
#     print("It's not a palindrome.")


# 18. WAP and count how many even and odd numbers are given a list.

# l = [1,2,3,4,5,6,7,8,9,11]
# even_count, odd_count = 0,0

# for i in l:
#     if i%2 == 0:
#         even_count+=1
#     else:
#         odd_count+=1
# print(f'''
# even count is:{even_count}
# odd count is:{odd_count}''')


# 19.Find the key with the highest value in a dictionary.

# d = {'a':5, 'g':333, 'b':3, 'c':7, 'v':18, 'r':45}
# high_value = 0
# for i in d:
#     if d[i]>high_value:
#         high_value = d[i]
#         high_key = i
# print(f'The key with the highest value is: {high_key}')


# 20. Write a program to find the cumulative sum of a list.

# l = [1,2,3,4,56,5,3,4,6]

# c_sum = 0
# res = []
# for i in l:
#     c_sum += i
#     res.append(c_sum)
# print(res)