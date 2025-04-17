# 1. Reverse a String: Write a function to reverse a string without using Python's built-in functions.

# def reverse_string(s):
#     res = ''
#     for i in s:
#         res = i+res
#     print(res)
# s = input("Enter a string: ")
# reverse_string(s)


# 2. Check if a String is Palindrome: Implement a function to check if a string reads the same forward and backward.

# def palindrome(s):
#     res = ''
#     for i in s:
#         res = i+res
#     if s == res:
#         print('It is a palindrome.')
#     else:
#         print('It is not a palindrome.')
# s = input("Enter a string: ")
# palindrome(s)


# 3. Count Vowels in a String: Write a function to count the number of vowels in a given string.

# def vowel_count(s):
#     vowels = 'aeiouAEIOU'
#     v_count = 0
#     for i in s:
#         if i in vowels:
#             v_count += 1
#     print('Vowel count:',v_count)
# s = input("Enter a string: ")
# vowel_count(s)


# 4. Check for Anagram: Write a function to check if two strings are anagrams of each other.

# def anagrams(s1,s2):
#     if sorted(s1.strip()) == sorted(s2.strip()):
#         print('Both strings are anagrams.')
#     else:
#         print('Both strings are not anagrams.')

# s1 = input("Enter first string: ")
# s2 = input("Enter second string: ")
# anagrams(s1,s2)


# 5. First Non-Repeating Character: Write a function to find the first non-repeating character in a string.

# def non_repeater(s):
#     for i in range(len(s)):
#         if s[i] not in s[i+1:]:
#             if s[i] not in s[:i]:
#                 print(s[i])
#                 break
# s = input("Enter a string: ")
# non_repeater(s)


# 6. Remove Duplicates: Implement a function that removes duplicate characters from a string while preserving the order.

# def duplicate(s):
#     res = ''
#     for i in range(len(s)):
#         if s[i] not in s[i+1:]:
#             if s[i] not in s[:i]:
#                 res += s[i]
#     print(res)
# s = input("Enter a string: ")
# duplicate(s)


# 7. Count Substring Occurrences: Write a function to count the occurrences of a substring in a given string.

# def count_substrings(s):
#     count_s = 0
#     for i in range(len(s)):
#         for j in range(i+1,len(s)+1):
#             count_s+=1
#     print(count_s)
# s = input("Enter a string: ")
# count_substrings(s)


# 8. Compress a String: Write a function to compress a string with counts of repeated characters (e.g., "aaabb" becomes "a3b2").

# s = 'aaabb'

# def compress(s):
#     d = {}
#     for i in s:
#         if i not in d:
#             d[i] = 1
#         else:
#             d[i] += 1
#     res = ''
#     for i,j in d.items():
#         res += i+str(j)
#     print(res)
# s = input("Enter a string: ")
# compress(s)


# 9. Check if String Contains Only Digits: Write a function to check if a string contains only numeric digits.

# def only_digits(s):
#     if s.isdigit():
#         print('String contains only numeric digits.')
#     else:
#         print('String does not contains only numeric digits.')
# s = input("Enter a string: ")
# only_digits(s)


# 10. Longest Common Prefix: Write a function to find the longest common prefix among an array of strings.

