# 1. You are given a nested list: my_list = [[1, 2], [3, 4], [5, 6]].
# How can you access the number 4 from this list using slicing?

my_list = [[1, 2], [3, 4], [5, 6]]
print(my_list[1][1])


# 2. A friend of yours is trying to change a tuple my_tuple = (1, 2, 3, 4)by changing the
# value of index 2. They are confused because tuples are immutable. What can you tell them about this problem?
'''
I can tell tuples are immutable, so you can't change the value of an index in a tuple.
'''


# 3. You have two lists, list1 = [1, 2, 3] and list2 = [4, 5, 6].
# How can you concatenate both lists together to form [1, 2, 3, 4, 5, 6]?

list1 = [1, 2, 3]
list2 = [4, 5, 6]
print(list1 + list2)


# 4. Your task is to modify the following list in place: list_data = [1, 2, [3, 4]].
# You need to change the second element inside the nested list to 7. What will you do?

list_data = [1, 2, [3, 4]]
list_data[2][1] = 7
print(list_data)


# 5. Consider the tuple my_tuple = (1, 2, (3, 4)). You need to access the number 3 inside
# the nested tuple using slicing. How would you do this?

my_tuple = (1, 2, (3, 4))
print(my_tuple[2][0])


# 6. You have a list my_list = [10, 20, 30, 40, 50]. If you want to create a new list that
# includes elements from index 1 to 3, how will you slice it?

my_list = [10, 20, 30, 40, 50]
print(my_list[1:4])


# 7. Your list has the following structure: nested_list = [[1, 2], [3, 4], [5, 6]].
# How can you use slicing to access the second element in the second sublist, which is 4?

nested_list = [[1, 2], [3, 4], [5, 6]]
print(nested_list[1][1])


# 8. You are given two lists: list1 = ['a', 'b', 'c'] and list2 = ['d', 'e', 'f'].
# Can you concatenate these two lists and access the last element of the combined list?

list1 = ['a', 'b', 'c']
list2 = ['d', 'e', 'f']
list = list1 + list2
print(list[-1])


# 9. A tuple is provided: tuple_data = (5, 6, 7, (8, 9)). You want to access the number 9 using slicing.
# How can you do that?

tuple_data = (5, 6, 7, (8, 9))
print(tuple_data[3][1])


# 10. A large dataset is structured as a nested tuple: nested_tuple = ((1, 2), (3, 4), (5, 6)).
# Using slicing, how can you extract the second number in the third tuple, which is 6?

nested_tuple = ((1, 2), (3, 4), (5, 6))
print(nested_tuple[2][1])


# 11. Your friend is creating a list: my_list = [5, 10, 15] and wants to multiply each element by 2.
# Can you help them by creating a list with the doubled values?

my_list = [5, 10, 15]
lst = []
for i in my_list:
    lst.append(i*2)
print(lst)


# 12. You're tasked with combining two lists: list1 = [1, 2] and list2 = [3, 4], but this time,
# the order of elements matters. You must concatenate them in such a way that the result is [1, 2, 3, 4].
# How can this be achieved?

list1 = [1, 2 ]
list2 = [3, 4]
print(list1 + list2)


# 13. A tuple tup = (1, 2, 3) is provided. You need to create a new tuple that excludes the last element.
# How would you accomplish this?

tup = (1, 2, 3)
print(tup[:-1])


# 14. You are given a list my_list = [1, [2, 3], [4, 5]] and need to replace the element [4, 5] with [6, 7].
# How would you modify the list?

my_list = [1, [2, 3], [4, 5]]
my_list[2] = [6, 7]
print(my_list)


# 15. Consider the following list of tuples: list_of_tuples = [(1, 2), (3, 4), (5, 6)].
# You need to create a list that contains only the second elements from each tuple. What approach would you take?

list_of_tuples = [(1, 2), (3, 4), (5, 6)]
lst = []
for i in list_of_tuples:
    lst.append(i[1])
print(lst)