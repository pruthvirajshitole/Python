# 1. WAP to print the sum of all the list items (without using inbuilt function)

# l = [10,20,30,40,50,60,70,80]
# sum = 0
# for i in l:
#     sum += i
# print('sum: ',sum)


# 2. WAP to print the sum of all the even items from the list 

# l = [1,2,3,4,5,6,7,8,9,10]
# even_sum = 0
# for i in l:
#     if i%2 == 0:
#         even_sum += i
# print('even sum: ',even_sum)


# 3. WAP to print the sum of all the odd items from the list 

# l = [1,2,3,4,5,6,7,8,9,10]
# odd_sum = 0
# for i in l:
#     if i%2 != 0:
#         odd_sum += i
# print('odd sum: ',odd_sum)


# 4. WAP to print the sum of all the even positions items from the list 

# l = [1,2,3,4,5,6,7,8,9,10]
# res = []
# for i in range(0,len(l),2):
#     res.append(l[i])
# print(res)
# print('sum of all the even positions item is: ',sum(res))


# 5. WAP print all the palindrom items from the list 

# l = [124,121,343,546,767,877]
# res = []
# for n in l:
#     r = 0
#     t = n
#     while n!=0:
#         d = n%10
#         r = r*10+d
#         n = n//10

#         if r == t:
#           res.append(r)
#     n+=1
# print(res)
    

# 6. WAP check the number is peterson number or not.

# n = int(input("Enter a number: "))
# sum = 0
# t = n
# while t != 0:
#     d = t%10
#     fac = 1
#     for i in range(1,d+1):
#         fac = fac*i
#     sum += fac
#     t = t//10
# if sum == n:
#     print(n,' is a peterson number')
# else:
#     print(n,' is not a peterson number')


# 7. WAP to print the sum of all the odd positions items from the list 

# l = [1,2,3,4,5,6,7,8,9,10]
# res = []
# for i in range(1,len(l),2):
#     res.append(l[i])
# print(res)
# print('sum of all the odd positions item is: ',sum(res))


# 8. WAP to print the Avg  of all the items from the list 

# l = [1,2,3,4,5,6,7,8,9,10]
# sum = 0
# for i in l:
#     sum+=i
# avg = sum/len(l)
# print(avg)


# 9. WAP to print the Avg  of all the even items from the list

# l = [1,2,3,4,5,6,7,8,9,10]
# res = []
# for i in l:
#     if i%2 == 0:
#         res.append(i)
# avg = sum(res)/len(res)
# print(avg)


# 10. WAP check the number is Perfect number or not.

# n = int(input("Enter a number: "))
# sum = 0
# for x in range(1,n):
#     if n%x == 0:
#         sum+=x
# if sum==n:
#     print(f"{n} is a perfect number.")
# else:
#     print(f"{n} is not a perfect number.")


# 11. WAP to print the Avg  of all the odd items from the list 

# l = [1,2,3,4,5,6,7,8,9,10]
# res = []
# for i in l:
#     if i%2 != 0:
#         res.append(i)
# avg = sum(res)/len(res)
# print(avg)


# 12. WAP to print the count all the items from the list

# l = [1,23,4,5,6,7,8]
# count = 0
# for i in l:
#     count+=1
# print(count)


# 13. WAP print all the sum of Armstrong items from the list 

# l = [1,34,5,153,455]
# res = []
# for n in l:
#     n = str(n)
#     l = len(n)
#     n = int(n)
#     t = n
#     arm = 0
#     d = 1
#     while n!=0:
#         d = n%10
#         arm = arm+ d**l
#         n = n//10
#     if t == arm:
#         res.append(t)
# print('sum of all armsrong numbers is:',sum(res))


# 14. WAP to print the count all even  items from the list 

# l = [1,2,3,4,5,6,7,8]
# even = 0
# for i in l:
#     if i%2 == 0:
#         even+=1
# print('Count of even numbers: ',even)


# 15. WAP to print the count all odd  items from the list 

# l = [1,2,3,4,5,6,7,8]
# odd = 0
# for i in l:
#     if i%2 != 0:
#         even+=1
# print('Count of odd numbers: ',odd)


# 16. WAP to print the all the odd positions items from the list

# l = [1,23,54,76,4,75,3,43]
# odd = []
# for i in range(0,len(l),2):
#     odd.append(l[i])
# print('odd positions items: ',odd)


# 17. WAP to print the all the even positions items from the list

# l = [1,23,54,76,4,75,3,43]
# even = []
# for i in range(1,len(l),2):
#     even.append(l[i])
# print('even positions items: ',even)


# 18. seprate the even and odd items from the list in different list 

# list1=[10,18,23,30,59,13,98,65,62,71] 
# even = []
# odd = []
# for i in list1:
#     if i%2 == 0:
#         even.append(i)
#     else:
#         odd.append(i)
# print('even list: ', even)
# print('odd list: ', odd)


# 19. All the zeros (0) should be in left side of the list and 1 should be in right side. 
#     list1=[1,0,1,0,0,1,1]
#     output: [0,0,0,1,1,1,1]

# list = [1,0,1,0,0,1,1]
# l1 = []
# l2 = []
# for i in list:
#     if i == 0:
#         l1.append(i)
#     else:
#         l2.append(i)
# print(l1+l2)


# 20. WAP to check the number is Harshad or not.

num = int(input("Enter a number: "))
t = num
s = 0
while num!=0:
    d = num%10
    s = s+d
    num = num//10
if t%s == 0:
    print(t,' is a hurshad number')
else:
    print(t,' is not a harshad number')