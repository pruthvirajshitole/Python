# n = 7
# i = 2
# flag = True
# while i<n:
#     if n%i == 0:
#         flag = False
#         break
#     i+=1
# if flag == True:
#     print(f"{n} is a prime number.")
# else:
#     print(f"{n} is not a prime number.")

'''
n   i   n%i==0  Flag
7   2     F      T
    3     F      T
    4     F      T
    5     F      T
    6     F      T
7 is prime
'''


# n = 8
# i = 2
# flag = True
# while i<n:
#     if n%i == 0:
#         flag = False
#         break
#     i+=1
# if flag == True:
#     print(f"{n} is a prime number.")
# else:
#     print(f"{n} is not a prime number.")

'''
n   i   n%i==0  Flag
8   2     T      F
8 is not prime
'''

# WAP to filter prime numbers from a given list:

l = [2,7,14,21,23,9,19]
prime = []
for i in l:
    flag = True
    for j in range(2,i):
        if i%j == 0:
            flag = False
            break
    if flag == True:
        prime.append(i)
print(prime)
