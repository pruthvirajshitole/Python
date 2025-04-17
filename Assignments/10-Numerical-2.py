# 1. A Secret Cipher: A spy agency encodes messages by reversing the words in a sentence and
# converting each word into uppercase. Write a Python function to take a sentence as input
# and return the encoded message. Use loops and string methods to solve this.

# l = (input("Enter the message: ").upper()).split()
# r = []
# for i in l:
#     r.insert(0,i)
# r = ' '.join(r)
# print(r)


# 2. Forest Adventure: A ranger tracks animal sightings daily and stores the counts in a list.
# Write a program to determine the day with the highest number of sightings and print whether 
# it was a weekday or weekend using conditionals.

# l1 = 'Sunday','Monday','Tuesday','Wednesday','Thursday','Friday','Saturday'
# l2 = [6,7,9,3,12,5,18]

# sort_l = sorted(l1)

# d = dict(zip(l1,l2))

# if sort_l[-1] == d['Sunday']:
#     print(f"Its a weekend. ")
# else:
#     print(f"Its not a weekday.")


# 3. Magic Box Game: A box contains items labeled with numbers. If the sum of the items' numbers is divisible by 3,
# it grants a "magic potion." Write a Python program that checks the sum of a list of numbers and prints the result.

# l = [1,2,3,6]
# sum = 0
# for i in l:
#     sum += i
# if sum%3 == 0:
#     print("Magic option.")
# else:
#     print("No magic potion.")


# 4. Treasure Hunt Puzzle: A treasure map contains a 2D grid of numbers where positive numbers represent
# steps forward, and negative numbers represent steps back. Write a Python program to traverse the grid row-wise,
# calculate the net steps, and determine if the treasure is reachable.

# PENDING


# 5. Student Grade Calculator: A class of students has marks in five subjects stored in a dictionary.
# Write a program to calculate each student's average and grade them as follows: A (>=90),
#  B (80–89), C (70–79), F (<70). Use loops and conditionals.

# d = {'s1':99, 's2':67 ,'s3':87, 's4':34, 's5':52}

# sum = 0
# for i in d.values():
#     sum += i
# avg = sum/5
# print(avg)

# if avg>=90:
#     print("student achieved A grade")
# elif 79 > avg < 90:
#     print("student achieved B grade")
# elif 69 > avg < 79:
#     print("student achieved C grade")
# else:
#     print("student achieved F grade")


# 6. Staircase Challenge: Write a Python program to print a staircase pattern where each row contains consecutive
# numbers starting from 1. The number of rows should be input by the user.

# ****
#  ****
#   ****
#    ****

# r = int(input("Enter a number of rows: "))
# z = 1
# for i in range(r):
#     for k in range(1,i+1):
#         print(' ', end='')
#     for j in range(1,r+1):
#         print(z, end=' ')
#         z+=1
#     print()
    
    
# 7. Mysterious Multiples: A number is considered "mysterious" if it is a multiple of both 3 and 5 but not divisible by 7.
# Write a program to find all such numbers within a range specified by the user.

# start = int(input("Enter start: "))
# end = int(input("Enter end: "))
# l = []
# for i in range(start,end):
#     if i%3 == 0 and i%5 == 0 and i%7 != 0:
#         l.append(i)
# print(l)

        
# 8. Palindrome Quest: A knight receives a string as a message. He must verify whether it’s a palindrome.
# Write a Python function to determine if the string reads the same forwards and backward.

# s="dad" 
# if s==s[::-1]:
#     print("Pallindrome")
# else:
#     print("Not palindrome")


# 9. Weather Statistics: A weather station records daily temperatures for a month. Write a program to
# calculate the average temperature, the hottest day, and the coldest day using loops and conditionals.

# l = [32,43,43,34,33,36,44,42,41,36,45,23,28,24,28,24,27,29,30,31,34,30]
# s_l = sorted(l)
# l1 = s_l[-1]
# l2 = s_l[0]

# sum = 0
# for i in l:
#     sum += i
#     if i == l1:
#         l1 = l.index(i)
#     elif i == l2:
#         l2 = l.index(i)

# avg = sum/len(l)
# print(f'''
# average temp of month is: {avg}
# The hottest day is: day-{l1}
# The coldest day is: day-{l2}''')


# 10. Odd-Even Battle: Two warriors play a game where one adds only even numbers, and the other adds only odd
# numbers from a list. Write a Python program to determine who scored higher and print their total.

# l = [1,2,3,4,5,6,7,8,9,10]
# even = 0
# odd = 0
# for i in l:
#     if i%2 == 0:
#         even += i
#     else:
#         odd += i
# if even>odd:
#     print("The warrior wins who adds even.")
# else:
#     print("The warrior wins who adds odd.")



# 11. Pattern Puzzle: Write a program to print the following pattern, where the number of rows is given by the user:  
#    1  
#    2 3  
#    4 5 6  
#    7 8 9 10  

# k = 1
# for i in range(4):
#     for j in range(i+1):
#         print(k, end=' ')
#         k+=1
#     print()


# 12. Fibonacci Lock: A lock opens only when the user inputs the first n Fibonacci numbers.
# Write a Python program to generate the Fibonacci sequence up to n terms.

# num=int(input("Enter the no. of fibonacci terms:"))
# l=[]
# a=0
# b=1
# l.append(a)
# l.append(b)
# n=3
# while n<=num:
#   c=a+b
#   l.append(c)
#   a=b
#   b=c
#   n+=1
# print(l)


# 13. Prime Treasure Chest: A chest opens only if the user inputs all prime numbers within a given range.
# Write a Python program to generate and validate these prime numbers.

# n1 = int(input("Enter start: "))
# n2 = int(input("Enter end: "))

# l = [i for i in range(n1,n2)]
# prime = []
# for i in l:
#     flag = True
#     for j in range(2,i):
#         if i%j == 0:
#             flag = False
#             break
#     if flag == True:
#         prime.append(i)
# print(prime)


# 14. Vowel Hunt: Write a program to count the number of vowels in a given string and determine if the count is even or odd.
# Use conditionals and loops.

# s = input("Enter a string: ")
# vowels = 0
# consonants = 0
# for i in s:
#     if i.isalpha():
#         if i in 'aeiou':
#             vowels += 1
# if vowels%2 == 0:
#     print(f'Vowels = {vowels}, Vowel count is even.')
# else:
#     print(f'Vowels = {vowels}, Vowel count is odd.')


# 15. Mystic Pyramid: Create a Python program that prints a pyramid of numbers for a given height.
# For example, if the height is 4:  
#          1  
#        2 3  
#      4 5 6  
#    7 8 9 10  

h = int(input("Enter the height: "))
z = 1
for i in range(h):
    for j in range(1,h-i):
        print(' ', end=' ')
    for k in range(0,i+1):
        print(z, end=' ')
        z+=1
    print()