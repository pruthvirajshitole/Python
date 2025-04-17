# 1. Write a program that prints all the prime numbers from 1 to 100 using a for loop.

# prime = []
# for i in range(2,101):
#     flag = True
#     for j in range(2,i):
#         if i%j == 0:
#             flag = False
#             break
#     if flag == True:
#         prime.append(i)
# print(prime)


# 2. Create a program that prints the sum of all even numbers from 1 to n using a for loop.

# n = int(input("Enter a number: "))
# sum = 0
# for i in range(1,n+1):
#     if i%2==0:
#         sum+=ii = 1
# print(sum)


# 3. Write a program using a while loop to calculate the factorial of a number.

# n = int(input("Enter a number: "))
# i = 1
# fact = 1
# while i<=n:
#     fact *= i
#     i+=1
# print(fact)


# 4. Implement a program that prints a sequence of numbers where each number is the
# sum of the two previous numbers, starting with 0 and 1, using a while loop.

# i = 0
# j = 1
# l = []
# n = int(input("Enter a number: "))
# l.append(0)
# l.append(1)
# a = 0
# while a<n-2:
#     k = i+j
#     l.append(k)
#     i = j
#     j = k
#     a+=1
# print(l)


# 5. Write a program that counts the number of digits in a given number using a while loop.

# n = int(input("Enter a number: "))
# t = n
# count = 0
# while n!=0:
#     d = n%10
#     count += 1
#     n = n//10
# print(f'count of total digits in number {t} is: {count}')


# 7. Implement a program that checks if a number is a palindrome using a while loop.

# n = int(input("Enter a number: "))
# t = n
# r = 0
# while n!=0:
#     d = n%10
#     r = r*10+d
#     n = n//10
# if t == r:
#     print("It's a palindrome.")
# else:
#     print("It's not a palindrome.")


# 8. Write a program that computes the sum of all odd numbers from 1 to n using a for loop.

# n = int(input("Enter a number: "))
# sum = 0
# for i in range(1,n+1):
#     if i%2 == 1:
#         sum+=i
# print(sum)


# 9. Implement a program that prints every third number between 1 and 50 using a while loop.

# i = 1
# while i<=50:
#     print(i)
#     i+=3


# 10. Write a program that prints the multiplication table of a number up to n using a for loop.

# n = int(input("Enter a number: "))
# k = 1
# for i in range(1,11):
#     print(n,'*',i,'=',n*i)


# 11. Create a program that prints the first n multiples of 5 using a for loop.

# n = int(input("Enter a number: "))
# for i in range(1,n+1):
#     if i%5 == 0:
#         print(i)


# 12. Write a program that calculates the sum of digits of a given number using a while loop.

# n = int(input("Enter a number: "))
# s = 0
# while n!=0:
#     d = n%10
#     s = s+d
#     n = n//10
# print("Sum: ",s)


# 13. Write a program that check a given number is Harshad or not by using while loop.

# num = int(input("Enter a number: "))
# t = num
# s = 0
# while num!=0:
#     d = num%10
#     s = s+d
#     num = num//10
# if t%s == 0:
#     print(t,' is a harshad number')
# else:
#     print(t,' is not a harshad number')


# 14. Implement a program that removes all negative numbers from a list using a for loop.

# l = [1,2,-4,-6,9,16,-1]
# l1 = []
# for i in l:
#     if i>0:
#         l1.append(i)
# print(l1)


# 15. Write a program that prints all numbers divisible by both 3 and 5 between 1 and n using a while loop.

# n = int(input("Enter a number: "))
# i = 1
# while i<=n:
#     if i%3==0 and i%5==0:
#         print(i)
#     i+=1


# 16. Create a program that prints the reverse of a given string using a while loop.

# s = input("Enter a string: ")
# rev = ''
# k = 0
# while k<len(s):
#     rev = s[k]+rev
#     k+=1

# print(rev)


# 17. Write a program that finds the largest number in a list using a for loop.

# l = [2,6,8,0,5,4,9,1]
# largest = 0
# for i in l:
#     if i>largest:
#         largest = i
# print(largest)    
            

# 18. Implement a program that generates the squares of numbers from 1 to n using a for loop.

# n = int(input("Enter a number: "))
# for i in range(1,n+1):
#     print(i**2)


# 19. Write a program that prints a pattern of numbers in the following format using a for loop:
    
#     1
#     2
#     3
#     4

# for i in range(1,5):
#     print(i)
    

# 20. Create a program that finds the sum of all numbers in a list that are divisible by 2 using a for loop.

# l = [1,2,3,4,5,6,7,8,9]
# sum = 0
# for i in l:
#     if i%2==0:
#         sum+=i
# print(sum)