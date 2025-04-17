# 1. Implement a custom strip() function to remove leading and trailing spaces from a string without using strip().
  
# s = input("Enter a string: ")
# r = s[::-1]
# for i in range(len(s)):
#     if s[i] != ' ':
#         start = i
#         break
# for j in range(len(r)):
#     if r[j] != ' ':
#         end = j
#         break
# print(s[start:-(end)])


# 2. Find the longest repeating non-overlapping substring in a given string.

# PENDING

# s = 'Hell a'
# l = []
# for i in range(len(s)):
#     for j in range(i+1,len(s)+1):
#         l.append(s[i:j])
# print(l)


# 3. Implement a function to check if a string is a valid IPv4 address.  

# s = "192.168.99.1"
# count = 0   
# for i in range(len(s)):
#     if s[i] == '.':
#         count += 1

# flag,octate = True,True
# for i in s.split('.'):
#     if i.isdigit():
#         i = int(i)
#         if i>0 and i<256:
#             flag = True
#         else:
#             flag = False
#             break           
#     else:
#         octate = False
#         break

# zero = True
# for i in s.split('.'):
#     if i[0] == '0':
#         zero = False
#         zero_i = i
#         break

# if count == 3:
#     if zero == True:
#         if flag == True:
#             if octate == True:
#                 print("It is a valid IPv4 address")
#             else:
#                 print("IPv4 address should contain only digits.")

#         else:
#             print("It is Not a valid IPv4 address")
#     else:
#         print(f"Leading zero in found in '{zero_i}'")
# else:
#     print("It is Not a valid IPv4 address")


# 4. Convert a given sentence into "snake_case" and "kebab-case" using loops and conditionals.  

# s = input("Enter a sentence: ")
# snake_case,kebab_case = '',''
# for i in s:
#     if i == ' ':
#         snake_case += '_'
#         kebab_case += '-'
#     else:
#         snake_case += i
#         kebab_case += i
# print(f'snake_case: {snake_case}')
# print(f'kebab-case: {kebab_case}')


# 5. Given two strings, find the shortest string that contains both as subsequences (Shortest Common Supersequence).

'''
Given Strings:

X = "abc", Y = "ac"

Possible supersequences: "abc", "acb", "abac", etc.
Shortest Common Supersequence: "abc"
"abc" contains both "abc" and "ac" as subsequences.
It is the shortest possible sequence.

'''


# 6. Find all possible permutations of a given string using recursion.


# # Input string
# s = "ABCD"
# arr = list(s)  # Convert string to list for easy swapping

# # Step 1: Sort the array to start from the smallest lexicographical order
# arr.sort()

# # Step 2: Print the first permutation
# print("".join(arr))

# # Step 3: Generate permutations iteratively
# while True:
#     # Step 3.1: Find the rightmost character that is smaller than the next character
#     i = -1
#     for k in range(len(arr) - 2, -1, -1):  # Traverse from second last to first character
#         print('k=',k)
#         if arr[k] < arr[k + 1]:  # First decreasing element found
#             i = k
#             break
#     print('i=',i)
#     if i == -1:  # If no such character is found, we reached the last permutation
#         break  # Exit loop, as all permutations are printed

#     # Step 3.2: Find the rightmost character larger than arr[i]
#     for j in range(len(arr) - 1, i, -1):
#         if arr[j] > arr[i]:
#             # Step 3.3: Swap arr[i] and arr[j]
#             arr[i], arr[j] = arr[j], arr[i]
#             break
        
#     # Step 3.4: Reverse the sequence aIfter index i
#     arr[i + 1:] = arr[i + 1:][::-1]  # Reverse the subarray directly

#     # Step 3.5: Print the next permutation
#     print("".join(arr))




# from itertools import permutations
# res = []
# res=[''.join(i) for i in permutations(s)]

# print(res)




# 7. Convert a Roman numeral string to an integer.

roman_dict = {
        'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100,
        'D': 500, 'M': 1000
    }
num = 'XLIX'
num = num[::-1]
total = 0
for i in range(len(num)-1):
    if num[i] in roman_dict:
        print(num[i])
        if roman_dict[num[i]] > roman_dict[num[i+1]] :
            total += roman_dict[num[i]]
        else:
            total -= roman_dict[num[i]]
    

print(total)
        


# 8. Find the lexicographically next permutation of a given string.  
# 9. Implement a basic text justification algorithm to format a paragraph to a given line width.  
# 10. Check if a string follows a given regular expression pattern without using re module.  
# 11. Implement a function to check if a string is a valid scrambled version of another.  
# 12. Find the minimum number of edits (insertions, deletions, replacements) to convert one string into another (Levenshtein Distance).  
# 13. Given a dictionary and a jumbled string, find all valid words that can be formed.  
# 14. Find the longest common substring between two given strings.  
# 15. Determine if a string can be broken into a sequence of valid dictionary words (Word Break Problem).  
# 16. Find the smallest window in a string that contains all characters of another string.  
# 17. Implement a function to convert a string into a ZigZag pattern and read row-wise.  
# 18. Compress a string using Run-Length Encoding (RLE) and decompress it back.  
# 19. Check if a given string can be rearranged to form a palindrome (Palindrome Permutation).  
# 20. Implement a function to decode a string encoded with a shifting cipher (e.g., Caesar cipher).