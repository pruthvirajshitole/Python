# 1. WAP to print the sum of all the list items

# l = [1,2,3,4,5,6,7,8,9]
# sum = 0
# for i in l:
#     sum += i
# print(sum)


# 2. WAP to print the sum of all the even items from the list 

# l = [1,2,3,4,5,6,7,8,9]
# sum_even = 0
# for i in l:
#     if i%2==0:
#         sum_even += i
# print(sum_even)


# 3. WAP to print the sum of all the odd items from the list 

# l = [1,2,3,4,5,6,7,8,9]
# sum_odd = 0
# for i in l:
#     if i%2!=0:
#         sum_odd += i
# print(sum_odd)


# 4. WAP to print the sum of all the even positions items from the list

# l = [1,2,3,4,5,6,7,8,9]
# sum_even = 0
# for i in range(0,len(l),2):
#         print(i)
#         sum_even += i
# print(sum_even)


# 5. WAP to print the sum of all the odd positions items from the list

# l = [1,2,3,4,5,6,7,8,9]
# sum_odd = 0
# for i in range(1,len(l)+1,2):
#         sum_odd += i
# print(sum_odd)


# 6. WAP to print the Avg  of all the items from the list

# l = [1,2,3,4,5,6,7,8,9]
# sum = 0
# for i in l:
#     sum+=i
# avg = sum/len(l)
# print("average: ",avg)


# 7. WAP to print the Avg  of all the even items from the list 

# l = [1,2,3,4,5,6,7,8,9]
# sum_even = 0
# l1 = []
# for i in l:
#     if i%2==0:
#         sum_even += i
#         l1.append(i)
# avg_even = sum_even/len(l1)


# 8. WAP to print the Avg  of all the odd items from the list


# 9. WAP to print the count all the items from the list

# l = [1,2,3,4,5,6,7,8,9]

# count = 0
# for i in l:
#     count += 1
# print(count)


# 10. WAP to print the count  all even  items from the list

# l = [1,2,3,4,5,6,7,8,9]

# count_even = 0
# for i in l:
#     if i%2==0:
#         count_even += 1
# print(count_even)


# 11. WAP to print the count  all odd  items from the list


# l = [1,2,3,4,5,6,7,8,9]

# count_odd = 0
# for i in l:
#     if i%2==1:
#         count_odd += 1
# print(count_odd)


# 13. seprate the even and odd items from the list in different list 

# list1=[10,10,20,30,5,3,9]
# even = []
# odd = []
# for i in list1:
#     if i%2==0:
#         even.append(i)
#     else:
#         odd.append(i)
# print(f'''
# even: {even}
# odd: {odd}
# ''')


# 14. all the even itmes shoud be in left side and odd items should be in right side. 

# list1=[10,10,20,30,5,3,9]
# even = []
# odd = []
# for i in list1:
#     if i%2==0:
#         even.append(i)
#     else:
#         odd.append(i)
# print(even+odd)


# 15. all the zeros (0) should be in left side of the list and 1 should be in right side.

# l = [1,0,1,1,0,0,0,0,1,1,0,1]
# res = []
# for i in l:
#     if i==0:
#         res.insert(0,i)
#     else:
#         res.append(i)
# print(res)