# 1. Write a Python program to count the number of vowels in a given string using a loop and conditionals.

# s = input("Enter a string: ")
# vowels = 'aeiouAEIOU'
# vowel_count = 0
# for i in s:
#     if i in vowels:
#         vowel_count+=1
# print(f'Vowels count in string: {vowel_count}')


# 2. Check if a given string is a palindrome using a loop.

# s = input("Enter a string: ").strip()
# res = ''
# for i in s:
#     res = i+res
# if s == res:
#     print("It is a Palindrome.")
# else:
#     print("It is not a Palindrome.")


# 3. Write a program to count the number of spaces in a given string using a loop.

# s = input("Enter a string: ")
# no_spaces = 0
# for i in s:
#     if i == ' ':
#         no_spaces+=1
# print(f'Number of spaces: {no_spaces}')


# 4. Find the first occurrence of a given character in a string using a loop.

# s = input("Enter a string: ")
# c = input("Enter a character: ")
# for i in range(len(s)):
#     if s[i] == c:
#         print(f'First occurence of {c} on index :{i}')
#         break


# 5. Write a program to reverse a string using a loop.

# s = input("Enter a string: ")
# rev = ''
# for i in s:
#     rev = i+rev
# print("Reverse:",rev)


# 6. Count the number of words in a string using a loop and conditionals.

# WITHOUT SPLIT()

# s = input("Enter a string: ").split()
# word_count = 0
# for i in s:
#     word_count+=1
# print(f"Word count is: {word_count}")


# 7. Replace all vowels in a string with '*' using a loop.

# s = input("Enter a string: ")
# vowels = 'aeiouAEIOU'
# res = ''
# for i in s:
#     if i in vowels:
#         res += '*'
#     else:
#         res += i
# print(res)


# 8. Count the number of uppercase and lowercase letters in a given string using a loop.

# s = input("Enter a string: ")
# lower_count, upper_count = 0,0
# for i in s:
#     if i.isupper():
#         upper_count+=1
#     elif i.islower():
#         lower_count+=1
# print(f'Upper count: {upper_count}\nLower count: {lower_count}')


# 9. Write a program to find the longest word in a given sentence using a loop and conditionals.

# s = input("Enter a string: ").split()
# longest = 0
# for i in s:
#     if len(i)>longest:
#         longest = len(i)
#         longest_word = i
# print(f'Longest word is: {longest_word}')


# 10. Remove all digits from a given string using a loop.

# s = input("Enter a string: ")
# res = ''
# for i in s:
#     if i.isdigit():
#         pass
#     else:
#         res+=i
# print(res)


# 11. Write a program to remove all special characters from a string using a loop.

# s = input("Enter a string: ")
# res = ''
# for i in s:
#     if i.isalnum():
#         res += i
# print(res)


# 12. Find the frequency of each character in a string using a loop.

# s = input("Enter a string: ")
# d = {}
# for i in s:
#     if i not in d:
#         if i == ' ':
#             pass
#         else:
#             d[i] = 1
#     else:
#         d[i] += 1
# print(d)


# 13. Write a program to check if two strings are anagrams using loops and conditionals. 

# s1 = (input('Enter first string: ').lower()).strip()
# s2 = (input('Enter second string: ').lower()).strip()

# if sorted(s1) == sorted(s2):
#     print(f'{s1} and {s2} are Anagrams.')
# else:
#     print(f'{s1} and {s2} are not Anagrams.')


# 14. Count the occurrences of a specific word in a given sentence using a loop.

# s = input("Enter a string: ").split()
# word = input("Enter a word: ")
# occurence = 0
# for i in s:
#     if i == word:
#         occurence+=1
# print(f'Occurunces of {word}: {occurence}')


# 15. Write a program to capitalize the first letter of each word in a string using a loop.

# s = input("Enter a string: ").split()
# res = ''
# for i in s:
#     word = ''
#     for j in range(len(i)):
#         if j == 0:
#             word += i[j].upper()
#         else:
#             word += i[j]
#     res += word+' '
# print(f'Capitalized string: {res}')


# 16. Write a program to check if a string contains only digits using a loop and conditionals.

# s = input("Enter a string: ")
# digits = '0123456789'
# flag = True
# for i in s:
#     if i not in digits:
#         flag = False
#         break
# if flag == True:
#     print("String contains only digits.")
# else:
#     print("String not contains only digits.")


# 17. Convert all lowercase letters in a string to uppercase using a loop.

# s = input("Enter a string: ")
# res = ''
# for i in s:
#     if i.islower():
#         res += i.upper()
#     else:
#         res += i
# print(res)


# 18. Find the index of all occurrences of a given character in a string using a loop.

# s = input("Enter a string: ")
# char = input("Enter a character: ")
# for i in range(len(s)):
#     if s[i] == char:
#         print(i)


# 19. Write a program to remove duplicate characters from a string using a loop.

# s = input("Enter a string: ")
# res = ''
# for i in range(len(s)):
#     if s[i] in s[i+1:]:
#         pass
#     else:
#         res+=s[i]
# print(res)


# 20. Write a program to insert a space before every uppercase letter in a given string using a loop.

# s = input("Enter a string: ")
# res = ''
# for i in s:
#     if i.isupper():
#         res += ' '+i
#     else:
#         res += i
# print(res)
