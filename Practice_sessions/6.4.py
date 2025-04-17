# 1. Sum of List Elements:
#    Write a Python function that takes a list of numbers as input and
#    returns the sum of all the numbers in the list.

# l = input("Enter the numbers saperated by spaces: ").split()
# def sum_of_nums(l):
#     sum_l = 0
#     for i in l:
#         sum_l+=int(i)
#     print("Sum:",sum_l)
# sum_of_nums(l)


# 2. Find Maximum in List:
#    Write a Python function that finds and returns the maximum value in a list
#    of numbers without using the max() function.

# l = [24,5,344,56,67,45,3,444,34,56]

# def max_l(l):
#     max_num = float('-inf')
#     for i in l:
#         if i>max_num:
#             max_num = i
#     print("Max value is:",max_num)
# max_l(l)


# 3. List Reversal:
#    Write a Python function to reverse a list in-place. Do not use any built-in list reversal functions.

# l = [24,5,344,56,67,3]
# def reversed_list(l):
#     rev = len(l)-1
#     for i in range(len(l)//2):
#         l[i],l[rev] = l[rev], l[i]
#         rev -= 1       
#     print("Reversed list:",l)
# reversed_list(l)


# 4. Count Occurrences:
#    Write a Python function that takes a list and a value as input and returns
#    the number of times the value appears in the list.

# l = input("Enter the values separated by spaces: ").split()
# value = input("Enter the value: ")
# def value_count(l,value):
#     count = 0
#     for i in l:
#         if i == value:
#             count+=1
#     print(f'Count of {value} is: {count}')
# value_count(l,value)


# 5. Remove Duplicates:
#    Write a Python function that takes a list as input and returns a new list
#    with duplicate elements removed while preserving the original order of elements.

# l = input("Enter the values seperated by spaces: ").split()
# unique_list = []
# unique = set()
# for i in l:
#     if i not in unique:
#         unique.add(i)
#         unique_list.append(i)
# print(unique_list)


# 6. List Comprehension:
#    Create a list comprehension that generates a list of squares of all even numbers from 1 to 20.

# print([x**2 for x in range(1,21) if x%2==0])


# 7. Function with Default Argument:
#    Write a Python function that takes two arguments: a string and an integer (with a default value of 1).
#    The function should return the input string repeated the specified number of times.

# string = input("Enter the string: ")
# integer = int(input("Enter the number of repeatations: "))
# def repeated(string,integer=1):
#     print(string*integer)
# repeated(string,integer)


# 8. Function to Filter Odd Numbers:
#    Write a Python function that takes a list of numbers and returns a new list
#    containing only the odd numbers from the original list.

# l = input("Enter numbers seperated by spaces: ").split()
# def odds(l):
#     new_l = [int(i) for i in l if int(i)%2==1]
#     print(new_l)
# odds(l)


# 9. List Sum of Even and Odd:
# Write a Python function that takes a list of numbers and returns a tuple
# containing the sum of even and odd numbers separately.

# l = input("Enter numbers seperated by spaces: ").split()
# def odds(l):
#     even_sum, odd_sum = 0,0
#     for i in l:
#         i = int(i)
#         if i%2==0:
#             even_sum+=i
#         else:
#             odd_sum+=i
#     print(f'(Even sum:{even_sum}), (Odd sum:{odd_sum})')
# odds(l)


# 10. WAP to find 2nd max element from list

# l = [24,5,344,56,67,3]
# max_l = float('-inf')
# second_max = float('-inf')
# for i in l:
#     if i>max_l:
#         second_max = max_l
#         max_l = i
#     elif i>second_max and i!=max_l:
#         second_max = i
# print("Second max:",second_max)