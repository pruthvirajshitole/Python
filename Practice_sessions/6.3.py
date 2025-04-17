# 1)  l=[1,3,('a',[1,'mark',66,(22,"zakurberg","l")]),[44,[45,('Elliot'),
# {'a':1,'Company':['Facebook',2001],'b':'Meta'},93],90]] 
# o/p: Mark Elliot Zuckerberg is an American businessman who co-founded 
# the social media service Facebook and its parent company Meta Platforms.

# l=[1,3,('a',[1,'mark',66,(22,"zakurberg","l")]),[44,[45,('Elliot'),{'a':1,'Company':['Facebook',2001],'b':'Meta'},93],90]]

# print((l[2][1][1]).capitalize(),(l[2][1][3][1]).capitalize(),'is an American businessman who co-founded the social media service',l[3][1][2]['Company'][0],
# 'and its parent company',l[3][1][2]['b'],'Platforms.')


# 2) Find the greatest smallest and the middle from nos given by user.

# a = int(input("Enter first number: "))
# b = int(input("Enter second number: "))
# c = int(input("Enter third number: "))

# if a>b and a>c:
#     greatest = a
#     if b>c:
#         middle = b
#         smallest = c
#     else:
#         middle = c
#         smallest = b
# elif b>c and b>a:
#     greatest = b
#     if c>a:
#         middle = c
#         smallest = a
#     else:
#         middle = a
#         smallest = c
# else:
#     greatest = c
#     if a>b:
#         middle = a
#         smallest = b
#     else:
#         middle = b
#         smallest = a
# print(f'''Greatest : {greatest}
# Middle: {middle}
# Smallest: {smallest}''')


# 3) Write a lambda function to filter nos. greater than 20. [1,7,30,20,32,60,3,7,19,21,47]

# l = [1,7,30,20,32,60,3,7,19,21,47]
# print(list(filter(lambda x:x if x>20 else 0,l)))


# 4) Write a program that checks whether a given year is a leap year or not. 
#    A leap year is determined based on the following rules:
#    If the year is divisible by 4, it might be a leap year.
#    However, if the year is divisible by 100, it is not a leap year unless.
#    The year is also divisible by 400, in which case it is a leap year.

# n = int(input("Enter the year: "))

# if n%4==0:
#     leap = True
#     if n%100==0:
#         leap = False
#         if n%400==0:
#             leap = True
# else:
#     leap = False

# if leap == True:
#     print(f'{n} is a leap year.')
# else:
#     print(f'{n} is not a leap year.')


# 5) You are given a list of dictionaries, where each dictionary contains information about a student (their name and age). 
#       Write a list comprehension to create a list of the names of all students who are over 18 years old.
#       students = [{"name": "Alice", "age": 17},{"name": "Bob", "age": 20},{"name": "Charlie", "age": 19},
#       {"name": "David", "age": 22},{"name": "Eve", "age": 16}]
#       o/p: ["Bob", "Charlie", "David"]

# students = [{"name": "Alice", "age": 17},{"name": "Bob", "age": 20},{"name": "Charlie", "age": 19},
#             {"name": "David", "age": 22},{"name": "Eve", "age": 16}]

# studs = [i['name'] for i in students if i['age']>18 ]
# print(studs)


# 6) The Treasure Hunt Map
#  You’re part of a team searching for a hidden treasure on an island. 
#  The map you have is in the form of a list of coordinates (x, y). 
#  However, some coordinates are incomplete or contain errors, such as strings instead of integers. 
#  Your task is to count how many valid coordinates are provided and which ones are usable for your search.
# coordinates = [(1, 2), (3, "4"), ("5", 6), (7, 8), ("10", "11"), (9, 10)]

# coordinates = [(1, 2), (3, "4"), ("5", 6), (7, 8), ("10", "11"), (9, 10)]
# count = 0
# for i in coordinates:
#     if type(i[0])==int and type(i[1])==int:
#         print(i, end=' ')
#         count+=1
# print(f'\nThe count of valid coordinates is: {count}')


# 7) Write a Python program to check if a string contains only digits.

# s = input("Enter a string: ")
# if s.isdigit():
#     print("string contains only digits.")
# else:
#     print("string does not contains only digits")


# 8) Implement a function to replace multiple spaces in a string with a single space.

# s = input("Enter a string: ")
# def spaces(s):
#     new_s = ''
#     for i in range(len(s)):
#         if s[i] ==' ' and s[i+1]==' ':
#             continue
#         else:
#             new_s+=s[i]
#     print(new_s)
# spaces(s)


# 9) Implement a function to remove a given character from a string.

# s = input("Enter a string: ")
# c = input("Enter the characted to remove: ")
# def remove_char(s,c):
#     new_s = ''
#     for i in s:
#         if i!=c:
#             new_s+=i
#     print(new_s)
# remove_char(s,c)


# 10) Write a Python program to find the most frequent character in a string.

s = input("Enter a string: ")
d = {}
for i in s:
    if i not in d:
        d[i] = 1
    else:
        d[i]+=1

most_freq = 0
for m,n in d.items():
    if n>most_freq:
        if m == ' ':
            continue
        most_freq = n
        most_freq_char = m
print(f'Most frequent character in string is: {most_freq_char}')