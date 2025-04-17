# 1.  Write a Python program to reverse a list without using the reverse() method.

# l = [1,2,3,4,5,6,7,8]
# print(f"reversed list is : {l[::-1]}")


# 2.  How can you remove all occurrences of a specific element from a list?

# l = [1,2,3,4,3,5,3,3,4,7]
# l = [i for i in l if i!=3]
# print(l)


# 3.  Write a function that takes a list of numbers and returns the sum of even numbers in the list.

# l = input("Enter a list of numbers: ").split(',')
# res = []
# for i in l:
#     i = int(i)
#     if i%2 == 0:
#         res.append(i)
# print(sum(res))


# 4.  Create a tuple with elements of mixed data types, and write a program to count the occurrences of a specific element.

# t = (1,3,3.33,'apple',9.99,4,'cat',3.33,11,1,'apple')
# el = input('Enter the specific element which is present in list: ')
# count = 0
# for i in t:
#     if str(i) == el:
#         count += 1
# print(count)


# 5.  Write a Python program to convert a tuple into a list and vice versa.

# l1 = [1,2,3,4]
# if l1 == list(l1):
#     l2 = tuple(l1)
# else:
#     l2 = list(l1)
# print(l1,':',type(l1))
# print(l2,':',type(l2))


# 6.  How would you find the index of a specific element in a tuple?

# t = (1,2,5,4,6,8)
# print(t)
# e = input("Enter a specific element from above tuple: ")

# for i in range(0,len(t)):
#     if str(t[i]) == e:
#         print(i)


# 7.  Write a Python program that takes two sets and returns their union, intersection, and difference.

# s1 = input("Enter set1: ").split(',')
# s2 = input("Enter set2: ").split(',')
# s1,s2 = set(s1),set(s2)
# print("union is: ", s1.union(s2))
# print("intersection is: ", s1.intersection(s2))
# print("difference is: ", s1-s2)


# 8.  How can you remove all elements from a set without deleting the set itself?

# use clear()


# 9.  Write a Python program that checks whether two sets are disjoint (i.e., have no common elements).

# s1 = input("Enter set1: ").split(',')
# s2 = input("Enter set2: ").split(',')

# s1,s2 = set(s1),set(s2)

# if s1.isdisjoint(s2):
#     print("both sets are disjoint")
# else:
#     print("both sets are not disjoint")


# 10.  Write a Python program to merge two dictionaries into one.

# d1 = {'name':'Pruthviraj', 'age':22}
# d2 = {'city':'Kolhapur'}
# d3 = {**d1, **d2}
# print(d3)


# 11.  How would you find the maximum value from a dictionary where the values are numerical?

# d = {1:2, 2:5, 4:9, 3:12, 8:92}
# d = [i for i in d.values() ]
# print(max(d))


# 12.  Write a Python program to find the key with the maximum value in a dictionary.

# d = {1:2, 2:5, 4:9, 3:12, 8:92}
# d = [i for i in d.keys() ]
# print(max(d))


# 13.  Write a list comprehension that generates a list of squares of all even numbers from 1 to 20.

# l = [i**2 for i in range(1,21) if i%2==0]
# print(l)


# 14.  Using dictionary comprehension, write a program that creates a dictionary where keys are the numbers from 1 to 10, and values are their squares.

# d = {i:i**2 for i in range(1,11)}
# print(d)

# 15.  Write a set comprehension to generate a set of all the unique vowels from a given string.

s = 'pruthviraj'
vowels = {i for i in s if i in 'aeiou'}
print(vowels)