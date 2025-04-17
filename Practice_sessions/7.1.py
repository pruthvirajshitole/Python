# 1. Write a Python program to reverse a string without using any built-in functions.

# s = input("Enter a string: ")
# rev = ''
# for i in s:
#     rev = i+rev
# print(rev)


# 2. Check if a given string is a palindrome.

# s = input("Enter a string: ")
# rev = ''
# for i in s:
#     rev = i+rev
# if s==rev:
#     print('It is a palindrome.')
# else:
#     print('It is not a palindrome.')


# 3. Count the number of vowels in a string.

# s = input("Enter a string: ")
# vowels = 'aeiouAEIOU'
# vowel_count = 0
# for i in s:
#     if i in vowels:
#         vowel_count+=1
# print('Vowel count:',vowel_count)


# 4. Find the frequency of each character in a string.

# s = input("Enter a string: ")
# d = {}
# for i in s:
#     if i not in d:
#         d[i] = 1
#     else:
#         d[i] += 1
# print(d)


# 5. Write a program to replace all occurrences of a substring in a string.

# s = input("Enter a string: ")
# old = input("Enter sunbstring need to replace: ")
# new = input("Enter the new string wanted to replace: ")
# print(s.replace(old,new))


# 6. Find the longest substring without repeating characters.

# s = input("Enter a string: ")
 
s = 'hellomruni'
substrings = []
for i in range(len(s)):
    for j in range(i + 1, len(s) + 1):
        substrings.append(s[i:j])

l = []
for j in substrings:
    non_repeating = ''
    for k in range(len(j)):
        if j[k] not in j[k+1:]:
            non_repeating+=j[k]
        else:
            break
    l.append(non_repeating)

longest = 0
for m in l:
    if len(m)>longest:
        longest = len(m)
        longest_substring = m
print('longest substring:',longest_substring)


# 7. Write a program to check if two strings are anagrams of each other.

# s1 = (input('Enter first string: ').lower()).strip()
# s2 = (input('Enter second string: ').lower()).strip()

# s3 = sorted(s1)
# s4 = sorted(s2)

# if s3 == s4:
#     print(f'{s1} and {s2} are Anagrams.')
# else:
#     print(f'{s1} and {s2} are not Anagrams.')


# 8. Convert the first character of each word in a string to uppercase.

# s = input("Enter a string: ").split()
# res = ''
# for i in s:
#     i = i.capitalize()
#     res = res+i+' ' 
# print(res)


# 9. Remove all special characters from a string and keep only alphanumeric characters.

# s = 'Lucifer123@!!!'
# res = ''
# for i in s:
#     if i.isalnum():
#         res+=i
# print(res)


# 10. Write a program to find the number of words in a string.

# s = input("Enter a string: ").split()
# word_count = 0
# for i in s:
#     word_count+=1
# print('Word count:',word_count)
