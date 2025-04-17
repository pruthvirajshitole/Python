# 1. Merging Two Dictionaries with Summed Values: Given dict1 = {"a": 10, "b": 20, "c": 30} and
# dict2 = {"a": 5, "b": 15, "d": 25}, merge the dictionaries, summing the values for common keys.

# dict1 = {"a": 10, "b": 20, "c": 30}
# dict2 = {"a": 5, "b": 15, "d": 25}
# summed_dict = {}

# for i,j in dict2.items():
#     if i in dict1:
#         summed_dict[i] = j+dict1[i]
# print('Summed dictionary:',summed_dict)


# 2. Find the key with the highest value in a dictionary.

# dict1 = {"a": 10, "b": 200, "c": 30}
# highest_value = float('-inf')
# for i,j in dict1.items():
#     if j>highest_value:
#         highest_value = j
#         key = i
# print('Highest value in dictionary with key is:',key)


# 3. Write a program to count the occurrence of each element in a list and store it in a dictionary.

# l = [1,4,6,4,45,344,33,44,33,33]
# d = {}
# for i in l:
#     if i not in d:
#         d[i] = 1
#     else:
#         d[i] += 1
# print('The required dictionary is:',d)


# 4. Convert two lists into a dictionary (one as keys, the other as values).

# l1 = [1,2,3,4]
# l2 = [1,4,9,16]
# d = {}
# for i in range(len(l1)):
#     d[l1[i]] = l2[i]
# print('without zip:',d)

# d_zip = zip(l1,l2)
# print('with zip:',dict(d_zip))


# 5. Write a program to sort a dictionary by values.

# dict1 = {"a": 10, "b": 200, "c": 30, "d":33}
# res = dict(sorted(dict1.items(),key=lambda x:x[1]))
# print(res)


# 6. Check if a given key exists in a dictionary.

# dict1 = {"a": 10, "b": 200, "c": 30}
# key = input("Enter a key: ")
# if key in dict1.keys():
#     print(f'{key} is exist in dictionary')
# else:
#     print(f'{key} is not exist in dictionary')


# 7. Write a program to invert keys and values of a dictionary.

# dict1 = {"a": 10, "b": 200, "c": 30}
# inverted_d = {}
# for i,j in dict1.items():
#     inverted_d[j] = i
# print(inverted_d)


# 8. Delete a key from a dictionary if it exists.

# dict1 = {"a": 10, "b": 200, "c": 30}
# key = input("Enter a key: ")
# if key in dict1.keys():
#     dict1.pop(key)
#     print(dict1)
# else:
#     print(f'{key} is not exist in dictionary')


# 9. Find the sum of all values in a dictionary.

# dict1 = {"a": 10, "b": 200, "c": 30}
# print(sum(dict1.values()))


# 10. Write a program to create a dictionary from a string with each character as a key
# and its frequency as the value.

# s = input("Enter a string: ")
# d = {}
# for i in s:
#     if i not in d:
#         d[i] = 1
#     else:
#         d[i] += 1
# print('The required dictionary is:',d)
