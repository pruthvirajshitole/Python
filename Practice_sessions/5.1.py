# 1. WAP print all the perfect number in a range and store in a list.

# start = int(input("Enter start: "))
# end = int(input("Enter end: "))
# l = []
# for n in range(start,end):
#     sum = 0
#     for x in range(1,n):
#         if n%x == 0:
#             sum+=x
#     if sum==n:
#         l.append(n)
# print(l)


# 2. WAP print all the palindrome items from the list.

# l = [123,44544,767,8784,454454,333]
# for i in l:
#     temp = i
#     r = 0
#     while i!=0:
#         d = i%10
#         r = 10*r+d
#         i = i//10
#     if r == temp:
#         print(r,end=" ")


# 3. WAP print all the prime items from the list.

# l = [1,3,7,5,9,22,4,6,89,65]

# for i in l:
#     flag = True
#     if i==1:
#         flag = False
#     for j in range(2,i):
#         if i%j == 0:
#             flag = False
#             break
#     if flag == True:
#         print(i, end=" ")


# 4. WAP print all the armstrong items from the list.

# l = [2,7,5,123,154,145,153,99]
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
#         print(temp, end=" ")


# 5. WAP print all the sum of prime items from the list.

# l = [1,3,7,5,9,22,4,6,89,65]
# prime_sum = 0
# for i in l:
#     flag = True
#     if i==1:
#         flag = False
#     for j in range(2,i):
#         if i%j == 0:
#             flag = False
#             break
#     if flag == True:
#         prime_sum += i
# print(prime_sum)


# 6. WAP print all the sum of palindrome items from the list.

# l = [22,44,121,321]
# palindromic_sum = 0
# for i in l:
#     temp = i
#     r = 0
#     while i!=0:
#         d = i%10
#         r = 10*r+d
#         i = i//10
#     if r == temp:
#         palindromic_sum += r
# print(palindromic_sum)


# 7. WAP print all the sum of Armstrong items from the list.

# l = [2,7,5,123,154,145,153,99]
# arm_sum = 0
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
#         arm_sum += arm
# print(arm_sum)


# 8. WAP print  the count of palindrom items from the list.

# l = [123,44544,767,8784,454454,333]
# palindrom_count = 0
# for i in l:
#     temp = i
#     r = 0
#     while i!=0:
#         d = i%10
#         r = 10*r+d
#         i = i//10
#     if r == temp:
#         palindrom_count += 1
# print("Palindrome count:",palindrom_count)


# 9. WAP print  the count of prime items from the list.

# l = [1,3,7,5,9,22,4,6,89,65]
# prime_count = 0
# for i in l:
#     flag = True
#     if i==1:
#         flag = False
#     for j in range(2,i):
#         if i%j == 0:
#             flag = False
#             break
#     if flag == True:
#         prime_count += 1
# print("Prime count:",prime_count)


# 10. WAP print  the count of Armstrong items from the list.

# l = [2,7,5,123,154,145,153,99]
# arm_count = 0
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
#         arm_count += 1
# print("Armstrong count:",arm_count)