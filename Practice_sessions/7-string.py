# 1. How do you create an empty string in Python?

# s = ''
# print('Empty string:',s)


# 2. How do you concatenate two strings in Python?

# s1 = 'a'
# s2 = 'b'
# s = s1+s2
# print('Concatenation:',s)


# 3. How do you find the length of a string in Python?

# s = 'Lucifer'
# print('Length of string:',len(s))


# 4. How do you access the first character of a string in Python?

# s = 'Lucifer'
# print('First char:',s[0])


# 5. How do you access the last character of a string in Python?

# s = 'Lucifer'
# print('Last char:',s[-1])


# 6. How do you slice a string to get the first three characters in Python?

# s = 'Lucifer'
# print('First three chars:',s[:3])


# 7. How do you check if a substring exists within a string in Python?

# s = 'Lucifer'
# sub = 'fer'
# if sub in s:
#     print(True)
# else:
#     print(False)


# 8. How do you convert a string to uppercase in Python?

# s = 'Lucifer'
# print('Upper:',s.upper())


# 9. How do you convert a string to lowercase in Python?

# s = 'Lucifer'
# print('Lower:',s.lower())


# 10. How do you replace a substring within a string in Python?

# s = 'Lucifer was innocent'
# print('Replace:',s.replace('was','is'))



# 11. How do you split a string into a list of words in Python?

# s = 'Lucifer was innocent'.split()
# print('Words:',s)


# 12. How do you join a list of words into a single string in Python?

# Words = ['Lucifer', 'was', 'innocent']
# print('Joined stting:', ' '.join(Words))


# 13. How do you remove whitespace from the beginning and end of a string in Python?

# s = "    Lucifer was innocent     "
# print('White spaces removed:', s.strip())


# 14. How do you find the index of the first occurrence of a substring in a string in Python?

# s = 'Lucifer was innocent'
# print('First occurence on index:',s.index('e'))


# 15. How do you count the occurrences of a substring in a string in Python?

# s = 'Lucifer was innocent'
# print('Count:',s.count('e'))


# 16. How do you check if a string starts with a certain substring in Python?

# s = 'Lucifer was innocent'
# print('Startswith:',s.startswith('Lucifer'))


# 17. How do you check if a string ends with a certain substring in Python?

# s = 'Lucifer was innocent'
# print('Endswith:',s.endswith('t'))


# 18. How do you repeat a string multiple times in Python?

# s = 'X'
# print('Replication:', s*5)


# 19. How do you reverse a string in Python?

# s = 'Lucifer was innocent'
# print('Reverse: ',s[::-1])


# 20. How do you check if a string is a palindrome in Python?

# s = input("Enter a string: ")
# if s == s[::-1]:
#     print("It's a palindrome.")
# else:
#     print("It's not a palindrome")


# 21. How do you convert a string to a list of characters in Python?

# s = 'Lucifer was innocent'
# l = [i for i in s]
# print(l)


# 22. How do you remove all instances of a specific character from a string in Python?

# s = 'Lucifer was innocent'
# char = 'e'
# res = ''
# for i in s:
#     if i==char:
#         continue
#     else:
#         res+=i
# print(res)


# 23. How do you remove all non-alphabetic characters from a string in Python?

# s = 'Lucifer123'
# res = ''
# for i in s:
#     if i.isalpha():
#         res+=i
# print(res)


# 24. How do you find all the unique characters in a string in Python?

# s = 'Lucifer was innocent'
# for i in range(len(s)):
#     if s[i] not in s[i+1:]:
#         if s[i] not in s[:i]:
#             print(s[i], end='')


# 25. How do you find the most frequent character in a string in Python?

# s = 'Lucifer was innocent'
# d = {}
# for i in s:
#     if i not in d:
#         d[i] = 1
#     else:
#         d[i] += 1

# most_freq = 0
# for i,j in d.items():
#     if j>most_freq:
#         most_freq=j
#         char = i
# print('Most frequent character is:',char)


# 26. How do you find the least frequent character in a string in Python?

# s = 'Lucifer was innocent'
# d = {}
# for i in s:
#     if i not in d:
#         d[i] = 1
#     else:
#         d[i] += 1

# least_freq = float('inf')
# for i,j in d.items():
#     if j<least_freq:
#         least_freq=j
#         char = i
# print('Least frequent character is:',char)


# 27. How do you swap the case of all characters in a string in Python?

# s = 'Lucifer Morningstar'
# print(s.swapcase())


# 28. How do you convert a string to title case in Python?

# s = 'Lucifer morningstar'
# print(s.title())


# 29. How do you check if a string is a valid number in Python?

# s = '123'
# if s.isnumeric():
#     print("string is a valid number in Python")
# else:
#     print("string is not  a valid number in Python")


# 30. How do you format a string to include variable values in Python?

# name = 'Pruthviraj'
# age = 22
# print('My name is {}, I am {} years old.'.format(name,age))