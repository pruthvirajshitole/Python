
# 1. Given a list lst = [1, 2, 3, 4, 5, 6], write a Python code to get the sublist [2, 3, 4] using slicing.

lst = [1, 2, 3, 4, 5, 6]
print(lst[1:4])


# 2. Given a list lst = ['a', 'b', 'c', 'd', 'e', 'f'], write a Python code to slice the list and get the last 3 elements.

lst = ['a', 'b', 'c', 'd', 'e', 'f']
print(lst[-3:])


# 3. Write a Python code that slices the list lst = [10, 20, 30, 40, 50, 60] to get every second
# element starting from the first element.

lst = [10, 20, 30, 40, 50, 60]
print(lst[::2])


# 4. Given a nested list lst = [[1, 2, 3], [4, 5, 6], [7, 8, 9]], write Python code to extract
# the second sublist [4, 5, 6].

lst = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
print(lst[1])


# 5. Given a nested list lst = [[1, 2, 3], [4, 5, 6], [7, 8, 9]], slice it to get the element 5 from
# the second sublist.

lst = [[1, 2, 3], [4, 5, 6],[7, 8, 9]]
print(lst[1][1])


# 6. Given a list lst = [[1, 2], [3, 4], [5, 6], [7, 8]], write a Python code to extract every second sublist.

lst = [[1, 2], [3, 4], [5, 6], [7, 8]]
print(lst[::2])


# 7. Given a list lst = [10, 20, 30, 40, 50], slice the list to get the first 3 elements and modify
# them by multiplying each element by 2.

lst = [10, 20, 30, 40, 50]
for i in range(3):
    lst[i] *= 2
print(lst[:3])


# 8. Given a list lst = [['a', 'b'], ['c', 'd'], ['e', 'f']], slice the list to get the second last
# sublist using negative indexing.

lst = [['a', 'b'], ['c', 'd'], ['e', 'f']]
print(lst[-2])


# 9. Given lst1 = [1, 2, 3] and lst2 = [4, 5, 6], write a Python code to concatenate both lists and
# slice the resulting list to get the elements [2, 3, 4].

lst1 = [1, 2, 3]
lst2 = [4, 5, 6]
lst = lst1 + lst2
print(lst[1:4])


# 10. Given lst = [[10, 20], [30, 40], [50, 60]], write Python code to extract the element 60 using nested slicing.

lst = [[10, 20], [30, 40], [50, 60]]
print(lst[2][1])


# 11. Given lst = [[1, 2], [3, 4], [5, 6], [7, 8]], extract the sublist [3, 4] from the list.

lst = [[1, 2], [3, 4], [5, 6], [7, 8]]
print(lst[1])


# 12. Given lst = [[1, 2, 3], [4, 5, 6], [7, 8, 9]], write Python code to extract the first element of
# each inner list using slicing.

lst = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
result = []
for i in lst:
    result.append(i[0])
print(result)


# 13. Given a list lst = [10, 20, 30, 40, 50], slice the list to get the first three elements and
# find the sum of those elements.

lst = [10, 20, 30, 40, 50]
lst = lst[:3]
sum = lst[0] + lst[1] + lst[2]
print(sum)


# 14. Given a nested list lst = [[1, 2], [3, 4], [5, 6]], write Python code to reverse the order
# of the outer list.

lst = [[1, 2], [3, 4], [5, 6]]
print(lst[::-1])


# 15. Given lst = [[1, 2, 3], [4, 5, 6], [7, 8, 9]], write Python code to extract a sublist from
# the first two sublists.

lst = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
result = lst[:2]
print(result)