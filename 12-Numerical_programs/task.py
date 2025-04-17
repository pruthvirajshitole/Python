# # reverse of a number:
# n = input("Enter a number: ")
# l = len(n)
# n = int(n)
# r = 0
# t = n
# while n!=0:
#     d = n%10
#     r = 10*r + d
#     n = n//10
# print(f'reverse of {t} is: {r}')


# palindrome

# n = input("Enter a number: ")
# l = len(n)
# n = int(n)
# r = 0
# t = n
# while n != 0:
#     d = n%10
#     r = 10*r + d
#     n = n//10

# if r == t:
#     print(f"Entered number {t} is a palindrome")
# else:
#     print(f"Entered number {t} is not a palindrome")


# armstrong

# n = input("Enter a number: ")
# l = len(n)
# n = int(n)
# r = 0
# t = n

# while n!=0:
#     d = n%10
#     r = r + d**l
#     n = n//10

# if r == t:
#     print(f"Entered number {t} is an armstrong")
# else:
#     print(f"Entered number {t} is not armstrong")


# 4-i/p: [231,341,543,654,789]
#   o/p: [132,143,345,456,987] 

# l1 = [231,341,543,654,789]
# l2 = []

# for i in l1:
#     r = 0
#     while i!=0:
#         d = i%10
#         r = 10*r + d
#         i = i//10
#     l2.append(r)

# print(l2)


# 5- i/p: [232,341,545,654,989]
#    o/p: [232,545,989] 

# l1 = [232,341,545,654,989]
# l2 = []

# for n in l1:
#     r = 0
#     t = n
#     while n != 0:
#         d = n%10
#         r = 10*r + d
#         n = n//10
#         if r == t:
#             l2.append(r)
# print(l2)


# 6-

# l1 = []
# for n in range(0,1000):
#     t = n
#     n = str(n)
#     l = len(n)
#     n = int(n)
#     print(type(n))
   

#     r = 0

#     while n!=0:
#         d = n%10
#         r = r + d**l
#         n = n//10
        
#         r = str(r)
#         if r == t and str(len(r)) == 3:
#             l1.append(r)
# print(l1)


# find the product of digits of a given no by user

# n = int(input("Enter a number: "))
# product = 1
# while n!=0:
#     d = n%10
#     product *= d
#     n = n//10
# print("Product:",product)


# find the sum of even digits of a given no by user

# n = int(input("Enter a number: "))
# even_sum = 0
# while n!=0:
#     d = n%10
#     if d%2==0:
#         even_sum += d
#     n = n//10
# print("Even digit sum:",even_sum)


# find the sum of alternate digits of a given no by user

# n = int(input("Enter a number: "))
# alt_sum = 0
# while n!=0:
#     d = n%10
#     alt_sum += d
#     n = n//100
# print("Alternate sum:",alt_sum)


# find the count of digits of a given no by user

# n = int(input("Enter a number: "))
# digit_count = 0
# while n!=0:
#     digit_count += 1
#     n = n//10
# print("Digit count:",digit_count)


# find the diffenrence between sum of even and odd digits of a given no by user

# n = int(input("Enter a number: "))
# even_sum = 0
# odd_sum = 0
# while n!=0:
#     d = n%10
#     if d%2==0:
#         even_sum += d
#     else:
#         odd_sum += d
#     n = n//10
# print("Even digit sum:",even_sum-odd_sum)


# Check all the digits are unique in a given no by user

# n = int(input("Enter a number: "))
# l = []
# flag = True
# while n!=0:
#     d = n%10
#     if d in l:
#         flag = False
#         break
#     l.append(d)
#     n = n//10
# if flag == True:
#     print("All digits are unique")
# else:
#     print("All digits are not unique")


# Sort the digits in ascending order of given no by user

# n = int(input("Enter a number: "))
# l = []
# while n!=0:
#     d = n%10
#     l.append(d)
#     n = n//10
# for i in range(len(l)):
#     for j in range(i+1,len(l)):
#         if l[i]>l[j]:
#             l[i],l[j] = l[j],l[i]
# s = ''
# for i in l:
#     s =+ str(i)
# print(s)
            

# Sort the digits in descending order of given no by user

# n = int(input("Enter a number: "))
# l = []
# while n!=0:
#     d = n%10
#     l.append(d)
#     n = n//10


# Replace each digit with square of that digit of given no by user

# n = int(input("Enter a number: "))
# new_num = ''
# d = 0
# while n!=0:
#     d = n%10
#     new_num = str(d**2)+new_num
#     n = n//10
# print(new_num)


l = [3,5,75,4,7,8,4,5]
print(sorted(l))
