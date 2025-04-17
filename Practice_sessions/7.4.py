# 1. Find the second most frequent character in a given string using loops and conditionals. 

# s = input("Enter a string: ")
# d = {}
# for i in s:
#     if i not in d:
#         d[i] = 1
#     else:
#         d[i] += 1

# most_freq,second_most_freq = 0,0
# for j in d.values():
#     if j>most_freq:
#         second_most_freq = most_freq
#         most_freq = j
#     elif j>second_most_freq and j!=most_freq:
#         second_most_freq = j
        
# for p,q in d.items():
#     if q == second_most_freq:
#         second_most_freq_char = p

# print(f'Second most frequent character is: {second_most_freq_char}')


# 2. Check if two strings are rotations of each other using loops.

# s = input("Enter first string: ")
# p = input("Enter second string: ")
# rotation = ''
# for i in range(len(s)):
#     if i<len(s)//2:
#         rotation+=s[i]
#     else:
#         rotation = s[i]+rotation
# print(f'Rotated string: {rotation}')

# if rotation == p:
#     print(f'{s} is the rotation of {p}')
# else:
#     print(f'{s} is not the rotation of {p}')


# 3. Remove all consecutive duplicate characters from a string using loops.

# s = input("Enter a string: ")
# res = ''
# for i in range(len(s)-1):
#     if s[i] != s[i+1]:
#         res += s[i]
# res += s[-1]
# print(res)


# 4. Find all substrings of a given string using nested loops.

# s = input("Enter a string: ")
# res = []
# for i in range(len(s)):
#     for j in range(i+1,len(s)+1):
#         res.append(s[i:j])
# print(res)


# 5. Find the longest palindrome substring in a given string using loops.

# s = input("Enter a string: ")
# l = []
# for i in range(len(s)):
#     for j in range(i+1,len(s)+1):
#         l.append(s[i:j])
# longest = 0
# for k in l:
#     if k == k[::-1]:
#         if len(k)>longest:
#             longest = len(k)
#             longest_string = k
# print(f'Longest Palindromic substring is: {longest_string}')


# 6. Replace all spaces with '%20' (like URL encoding) using loops.

# s = input("Enter a string: ")
# res = ''
# for i in s:
#     if i == ' ':
#         res+='%20'
#     else:
#         res+=i
# print(res) 
 

# 7. Extract all numeric substrings from a given string using loops.

# s = input("Enter a string: ")
# res = []
# for i in range(len(s)):
#     for j in range(i+1,len(s)+1):
#         res.append(s[i:j])
# l = []
# for i in res:
#     if i.isnumeric():
#         l.append(i)
# print(l)


# 8. Convert a given sentence to camelCase using loops and conditionals.

# s = input("Enter a string: ") 
# res = ''
# for i in range(len(s)):
#     if i==0:
#         res+=s[i].upper()
#     elif s[i] != ' ':
#         if s[i-1] == ' ':
#             continue
#         res+=s[i]
#     else:
#         res+=s[i+1].upper()
# print(res)


# 9. Find all words that start with a vowel in a given sentence using loops.

# s = (input("Enter a string: ")).split()
# vowels = 'aeiouAEIOU'
# for i in s:
#     if i[0] in vowels:
#         print(i,end=' ')


# 10. Sort the words in a given sentence in ascending order using loops.

# PENDING
s = 'Lucifer is the devil.'





# 11. Find all unique words from two given sentences using loops.

# s1 = input("Enter first string: ")
# s2 = input("Enter second string: ")
# s = (s1+' '+s2).split()
# l = []
# for i in range(len(s)):
#     if s[i] not in s[i+1:]:
#         l.append(s[i])
# print(l)


# 12. Check if a given string follows a specific pattern (e.g., "abba" → "dog cat cat dog") using loops and dictionaries.  

# TRY ONCE MORE

# s = "dog cat cat dog tom"
# pattern = 'abbaz'
# l2 = s.split()
# l1 = list(pattern)
# if len(l1) == len(l2):
#     flag = True
#     for i in range(len(l1)-1):
#         for j in range(i+1,len(l1)):
#             if l1[i] == l1[j]:
#                 if l2[i] != l2[j]:
#                     flag = False
#                     break
#     if flag:
#         print('Strings follows specific patterns.')
#     else:
#         print('String Not follows specific patterns.')
# else:
#     print('Both strings are not equal.')      


# 13. Find the first non-repeating character in a given string using loops.  

# s = input("Enter a string: ")
# for i in range(len(s)):
#         if s[i] not in s[i+1:]:
#                 if s[i] not in s[:i]:
#                         print(s[i])
#                         break


# 14. Remove all adjacent pairs of matching characters from a string using loops (e.g., "aabbcc" → "").



# 15. Implement a basic string compression algorithm (e.g., "aaabbc" → "a3b2c1") using loops.

# s = 'aaabbc'
# d = {}
# for i in s:
#         if i not in d:
#                 d[i] = 1
#         else:
#                 d[i] += 1
# r = ''
# for i,j in d.items():
#         r += i+str(j)
# print(r)


# 16. Convert a given integer to its equivalent string representation manually (without using str()).

# PENDING (-ve values)

# digits = ['0','1','2','3','4','5','6','7','8','9']
# l = [0,1,2,3,4,5,6,7,8,9]
# d = dict(zip(l,digits))
# num = int(input("Enter any integer: "))
# print('Before conversion:',num,type(num))
# res = ''

# if num == 0:
#     res = d[0]

# while num!=0:
#     digit = num%10
#     res = d[digit] + res
#     num = num//10

# print('After conversion',res,type(res))


# 17. Find all anagram substrings in a given string using loops.

# s = input("Enter a string: ")
# s = "abba"
# l = [s[i:j] for i in range(len(s)) for j in range(i+1, len(s)+1)]

# res = set()
# for i in range(len(l)):
#         for j in range(i+1,len(l)):
#                 if sorted(l[i]) == sorted(l[j]) and len(l[i])>1 and len(l[j])>1:
#                         res.add((l[i],l[j]))
# print(list(res))


# 18. Reverse only the words in a sentence while keeping spaces intact using loops.  

# s = 'lucifer was innocent.'
# res = ''
# word = ''
# for i in s:  
#         if i!=' ':
#                 word = i+word
#         else:
#                 res += word+' '
#                 word = ''
# res += word
# print(res)


# 19. Write a function to format a string to title case, capitalizing only non-preposition words.

# prepositions = [
#     "about", "above", "across", "after", "against", "along", "among", "around", "at",
#     "before", "behind", "below", "beneath", "beside", "between", "beyond", "by",
#     "despite", "down", "during", "except", "for", "from", "in", "inside", "into",
#     "like", "near", "of", "off", "on", "onto", "out", "outside", "over", "past",
#     "since", "through", "throughout", "till", "to", "toward", "under", "underneath",
#     "until", "up", "upon", "with", "within", "without"
# ]

# s = input("Enter a string: ").split()
# res = ''
# for i in s:
#     if i not in prepositions:
#         i = i.capitalize()
#         res += i+' '
#     else:
#         res += i+' '
# print(res)


# 20. Find the longest common prefix among multiple given strings using loops.

s=["flower","flow","flight","flag"]

pre=s[0]
for x in range(1,len(s)):
     i=0
     while i<len(s[x]) and i<len(pre) and pre[i]==s[x][i]:
         i+=1
     pre=s[x][:i]
print(pre)