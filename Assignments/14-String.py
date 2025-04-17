# 1. Write a program to check if a given string is a palindrome.  

# s=input("Enter a string:").strip()

# if s==s[::-1]: 
#   print("Palindrome")
# else:
#   print("Not palindrome")


# 2. Count the number of vowels and consonants in a string.  

# s = input("Enter a string: ")
# vowels = 0
# consonants = 0
# for i in s:
#     if i.isalpha():
#         if i in 'aeiou':
#             vowels += 1
#         else:
#             consonants += 1
# print(f'vowels = {vowels}, consonants = {consonants}')
    

# 3. Reverse a string without using slicing.

# s="I love Pune"
# x=list(reversed(s))
# s="".join(x)
# print(s)


# 4. Find the first non-repeating character in a string.  

# s = input("Enter a string: ").lower()
# d = {}
# l = []
# for i in s:
#     if i in d:
#         d[i] += 1
#     else:
#         d[i] = 1
# for j in s:
#     if j in d:
#         if d[j]<2:
#             print(j)
#             break


# 5. Check if two strings are anagrams of each other.  

# s1 = (input('Enter first string: ').lower()).strip()
# s2 = (input('Enter second string: ').lower()).strip()

# s3 = sorted(s1)
# s4 = sorted(s2)

# if s3 == s4:
#     print(f'{s1} and {s2} are Anagrams.')
# else:
#     print(f'{s1} and {s2} are not Anagrams.')


# 6. Write a program to remove all duplicate characters from a string. 

# s = input("Enter a string: ")
# str=""
# for char in s:
#     if char not in str:
#         str+=char
# print(str)

 
# 7. Find the longest substring without repeating characters in a string. 

# PENDING


# 8. Count the occurrence of each character in a string.  

# s = input("Enter a string: ").lower()
# d = {}
# for i in s:
#     if i in d:
#         d[i] += 1
#     else:
#         d[i] = 1
# print(d)


# 9. Write a program to check if a string contains only digits.  

# s = input("Enter a string: ")
# if s.isdigit():
#     print("The given string contains only digits.")
# else:
#     print("The given string is a mixed string.")


# 10. Convert a string to uppercase without using the built-in upper() method. 

# PENDING


# 11. Replace all spaces in a string with a hyphen (-).  

# s = input("Enter a string: ")
# print(s.replace(' ','-'))


# 12. Find all substrings of a string that are palindromes.  

# s = input("Enter a string: ")
# l = []
# w = ''
# a = 0
# for j in s:
#     for i in s[a:len(s)+1]:
#         w += i
#         l.append(w)
#     a += 1
#     w = ''
# p = []
# for k in l:
#     if k == k[::-1]:
#         p.append(k)
# print(p)



# 13. Write a program to sort the characters of a string alphabetically.

# s = input("Enter a string: ")
# print(sorted(s))


# 14. Count the number of words in a string. 

# s = input("Enter a string: ")
# w = ''
# l = []
# count = 0
# for i in s:
#     if i != ' ':
#         w+=i
#     else:
#         count += 1
# print(count+1)


# 15. Check if a string starts and ends with the same character.

# s = (input("Enter a string: ").lower()).strip()

# if s[0] == s[-1]:
#     print(f'{s} starts and ends with the same character.')
# else:
#     print(f'{s} not starts and ends with the same character.')
