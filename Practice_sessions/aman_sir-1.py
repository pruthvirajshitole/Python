# 1. Write a Python program to count the occurrences of a specific character in a string.

# s = input("Enter a string: ")
# char = input("Enter the specific character: ")
# count = 0
# for i in s:
#     if i == char:
#         count+=1
# print("Count:",count)


# 2. Implement a function to check if a string is a palindrome.

# def palindrome(s):
#     if s == s[::-1]:
#         print(f'{s} is a palindrome.')
#     else:
#         print(f'{s} is not a palindrome.')
# s = input("Enter a string: ")
# palindrome(s)


# 3. Write a program to check if two strings are anagrams of each other.

# s1 = sorted(input("Enter first string: ").lower())
# s2 = sorted(input("Enter second string: ").lower())
# if s1==s2:
#     print("Both strings are anagrams.")
# else:
#     print("Both strings are not anagrams.")


# 4. Create a Python function to reverse a string.

# s = input("Enter a string: ")
# def reverse(s):
#     print("Reversed string:",s[::-1])
# reverse(s)


# 5. Write a program to remove duplicate characters from a string.

# s = input("Enter a string: ")
# new_s = ''
# for i in s:
#     if i not in new_s:
#         new_s+=i
# print(new_s)
    

# 6. Implement a function to check if a string contains only digits.

# s = input("Enter a string: ")
# def digits(s):
#     if s.isdigit():
#         print("The string contains only digits")
#     else:
#         print("The string does not contains only digits")
# digits(s)


# 7. Write a Python program to remove whitespace from a string.

# s = input("Enter a string: ")
# new_s = ''
# for i in s:
#     if i!=' ':
#         new_s+=i
# print(new_s)


# 8. Create a program to convert a string to title case.

# s = input("Enter a string: ").capitalize()
# new_s = ''
# word = ''
# for i in range(len(s)):
#     if s[i]!=' ':
#         if s[i-1] == ' ':
#             continue
#         new_s+=s[i]
#     else:
#         new_s += ' '+s[i+1].upper()
# print(new_s)


# 9. Implement a function to find the longest word in a string.

# s = input("Enter a string: ").split()
# def longest_word(s):
#     longest = 0
#     for i in s:
#         if len(i)>longest:
#             longest=len(i)
#             word = i
#     print("Longest word is:",word)
# longest_word(s)


# 10. Write a program to count the number of vowels and consonants in a string.

# s = input("Enter a string: ").lower()
# vowels = 'aeiou'
# consonants = 'bcdfghjklmnpqrsstvwxyz'
# vowels_count,consonants_count = 0,0
# for i in s:
#     if i in vowels:
#         vowels_count+=1
#     elif i in consonants:
#         consonants_count+=1
# print(f'Vowels: {vowels_count}, Consonants: {consonants_count}')


# 11. Create a Python function to check if a string contains only uppercase letters.

# s = input("Enter a string: ")
# def upper_case(s):
#     for i in s:
#         flag = True
#         if i.islower():
#             flag = False
#             break
#     if flag==True:
#         print("string contains only uppercase letters.")
#     else:
#         print("string does not contains only uppercase letters.")
    
# upper_case(s)


# 12. Write a program to find the first non-repeated character in a string.

# s = input("Enter a string: ")
# for i in range(len(s)):
#     if s[i] not in s[i+1:]:
#         if s[i] not in s[:i]:
#             print(s[i])
#             break


# 13. Implement a function to capitalize the first letter of each word in a string.

# s = input("Enter a string: ").capitalize()

# def capitalize_first(s):
#     new_s = ''
#     word = ''
#     for i in range(len(s)):
#         if s[i]!=' ':
#             if s[i-1] == ' ':
#                 continue
#             new_s+=s[i]
#         else:
#             new_s += ' '+s[i+1].upper()
#     print(new_s)
# capitalize_first(s)


# 14. Write a Python program to find the index of a substring in a string.

# s = input("Enter a strig: ").split()
# sub = input("Enter the substring: ")
# for i in range(len(s)):
#     if sub == s[i]:
#         print(i)


# 15. Create a program to check if a string is a valid palindrome ignoring non-alphanumeric characters.

# s = input("Enter a string: ")
# rev,new_s = '',''
# for i in s:
#     if i.isalnum():
#         new_s += i
#         rev = i+rev
# if new_s==rev:
#     print("It's a Palindrome.")
# else:
#     print("It's not a Palindrome.")


# 16. Implement a function to find the longest common prefix among an array of strings.




# 17. Write a program to find all substrings of a string.

# s = input("Enter a string: ")
# substrings = []
# for i in range(len(s)):
#     for j in range(i + 1, len(s) + 1):
#         substrings.append(s[i:j])
# print(substrings)


# 18. Create a Python function to perform string interpolation.



# 19. Implement a function to reverse words in a string without using built-in functions.

# s = input("Enter a string: ").split()
# reversed_s = ''
# for i in s:
#     j = i[::-1]
#     reversed_s = reversed_s+j+' '
# print(reversed_s)


# 20. Write a program to check if a string is a rotation of another string.