# 1.Find the largest palindrome made from the product of two 3-digit numbers.

# mul = []
# for i in range(100,1000):
#     for j in range(i,1000):
#         k = i*j
#         if str(k) == str(k)[::-1]:
#             mul.append(k)
# print(max(mul))


# 2. Find the sum of all multiples of 3 and 5 below 1000.

# l = []
# for i in range(1000):
#     if i%3==0 and i%5==0:
#         l.append(i)
# print(sum(l))


# 3. Implement a function to calculate the nth Fibonacci number using a loop between 10-100.

# n = 11
# l = []
# a,b = 0,1
# l.extend([a,b])
# while n-2!=0:
#     c = a+b
#     a,b = b,c
#     l.append(c)
#     n -= 1
# print(l[-1],l)


# 4. Reverse the digits of an integer without converting it to a string.

# n = 123
# rev = 0
# while n!=0:
#     d = n%10
#     rev = rev*10+d
#     n = n//10
# print(rev)


# 5. Implement a program to check if a number is prime.

# n = 11
# flag = True
# for i in range(1,n):
#     if i==1:
#         continue
#     elif n%i==0:
#         flag = False
#         break
# if flag:
#     print('Prime')
# else:
#     print('Not Prime')
    

# 6. Calculate the sum of the digits of a number raised to a given power.

# n = 12
# p = 2
# i = n**p
# sum = 0
# while i!=0:
#     d = i%10
#     sum += d
#     i = i//10
# print(sum)


# 7. Generate all prime numbers less than a given number

# n = 12
# l = []
# for num in range(1,n):
#     flag = True
#     for i in range(2,num):
#         if num%i==0:
#             flag = False
#             break
#     if flag:
#         if num == 1:
#             continue
#         l.append(num)
# print(l)


# 8. Find the GCD (Greatest Common Divisor) of two numbers

# n1 = 11
# n2 = 13
# l = []
# if n1>n2:
#     for i in range(1,n1):
#         if n1%i==0 and n2%i==0:
#             l.append(i)
# elif n1==n2:
#     l.append(n1)
# else:
#     for i in range(1,n2):
#         if n1%i==0 and n2%i==0:
#             l.append(i)
# print("GCD:",l[-1])


# 9. Find the first 100 prime numbers.

l = []
i = 1
while len(l)<100:
    flag = True
    for j in range(1,i):
        if j==1:
            continue
        elif i%j==0:
            flag = False
            break
    if flag:
        if i!=1:
            l.append(i)
    i+=1
print(l)


# 10. Implement a program to find the number of Armstrong numbers in a given range using while loop.

# count = 0
# n = 200
# for i in range(1,n):
#     temp = i
#     le = len(str(i))
#     arm = 0
#     while i!=0:
#         d = i%10
#         arm = arm+d**le
#         i = i//10
#     if temp == arm:
#         count+=1
# print(count)