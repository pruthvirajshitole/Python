# 1. Implement a program to find the number of prime numbers in a given range using while loop.

# start = int(input("Enter start: "))
# end = int(input("Enter end: "))

# while start<=end:
#     i = 2
#     flag = True
#     if start == 1:
#         flag = False
#     while i<start:
#         if start%i==0:
#             flag = False
#             break
#         i+=1
#     if flag == True:
#         print(start, end=' ')
#     start+=1


# 2. Find the number of unique characters in a string.

# s = input("Enter a string: ")
# no_unique = 0
# for i in range(len(s)):
#     if s[i] not in s[i+1:]:
#         if s[i]!=' ':
#             no_unique+=1
# print(f'Number of unique characters: {no_unique}')


# 3.  Calculate the sum of all even Fibonacci numbers less than N and print the sequence.

# n = int(input("Enter a number: "))
# l = []
# a,b = 0,1
# l.append(a)
# l.append(b)
# k = 1
# while k<n:
#     c = a+b
#     a,b = b,c
#     l.append(c)
#     k+=1
# even_sum = 0
# even_fab = []
# for i in l:
#     if i%2==0:
#         even_sum+=i
#         even_fab.append(i)
# print(f'sum of all even Fibonacci numbers: {even_sum}')
# print("Sequence:",even_fab)


# 4. Python function to check if a number is magical number or not
# 1,19,1729

# n = int(input("Enter a number: "))
# def sum_digits(n):
#     sum_n = 0
#     while n!=0:
#         d = n%10
#         sum_n += d
#         n = n//10
#     if sum_n<10:
#         if sum_n == 1:
#             print("It is a magical number.")
#         else:
#             print('It is not a magical number.')
#     else:
#         return sum_digits(sum_n)
# sum_digits(n)


# 5. WAP print all the sum of Armstrong items from the list.

# l = [1,2,3,4,5,7,34,65,153,154]
# sum_arms = 0
# for i in l:
#     temp = i
#     l_num = len(str(i))
#     arm = 0
#     while i!=0:
#         d = i%10
#         arm += d**l_num
#         i = i//10
#     if temp == arm:
#         sum_arms+=arm
# print("sum of Armstrong items from the list: ",sum_arms)


# 6.Find the second largest element in a list.(without using inbuilt function)

# l = [2,4,7,5,9,3,8]
# largest = float('-inf')
# second_largest = float('-inf')
# for i in l:
#     if i>largest:
#         second_largest = largest
#         largest = i
#     elif i>second_largest and second_largest!=i:
#         second_largest = i
# print("Second largest number is:",second_largest)


# 7. Write a program to flatten a nested list.

# l=[1,2,3,[4,6,7,8],9,15,[3,4,5],(1,2,3,4,5),4,5]

# def flatten(l):
#     flatten_list = []
#     for i in l:
#         if isinstance(i,(list,tuple)):
#             flatten_list.extend(flatten(i))
#         else:
#             flatten_list.append(i)
#     return flatten_list
# print(flatten(l))


# 8. Remove all 3 from list.

# l=[1,2,3,4,8,9,3,6,5,3,1,3,54,3,12,9,3]
# for i in l:
#     if i==3:
#         l.remove(i)
# print(l)


# 9.Reverse words in a given string
#   input: s = “python quiz practice code” 
#   Output: s = “code practice quiz python”

# s = 'python quiz practice code'
# rev = ''
# word = ''
# for i in s:
#     if i != ' ':
#         word+=i
#     else:
#         rev = ' '+word+rev
#         word = ''
# rev = word+rev
# print(rev)


# 10.Reverse the words, order should be maintained
#    str="Hello world "
#    output: "olleh dlrow"

# s="Hello world "
# rev = ''
# word = ''
# for i in s:
#     if i != ' ':
#         word+=i
#     else:
#         rev = rev+word[::-1]+' '
#         word = ''
# print(rev)


# 11. Write a Python program to check if two strings are anagrams.

# s1 = (input('Enter first string: ').lower()).strip()
# s2 = (input('Enter second string: ').lower()).strip()

# s3 = sorted(s1)
# s4 = sorted(s2)

# if s3 == s4:
#     print(f'{s1} and {s2} are Anagrams.')
# else:
#     print(f'{s1} and {s2} are not Anagrams.')


# 12. Check a number is Automorphic or not.

# s = int(input("Enter a number: "))
# square = s**2

# if str(square).endswith(str(s)):
#     print(f"{s} is Automorphic.")
# else:
#     print(f"{s} is not Automorhic.")


# 13. Write a Python program to count the number of vowels in a given string.

# s = input("Enter a string: ")
# vowels = 'aeiouAEIOU'
# vowel_count = 0
# for i in s:
#     if i in vowels:
#         vowel_count+=1
# print("Vowels count:",vowel_count)


# 14. Write a Python program to find the first non-repeating character in a string.

# s = input("Enter a string: ")
# d = {}
# for i in s:
#     if i not in d:
#         if i == '.':
#             continue
#         d[i] = 1
#     else:
#         d[i] += 1
# for m,n in d.items():
#     if n == 1:
#         print(m)
#         break      


# 15. Given a string, write a Python program to find the frequency of each character using a dictionary.

# s = input("Enter a string: ")
# d = {}
# for i in s:
#     if i not in d:
#         if i == '.':
#             continue
#         d[i] = 1
#     else:
#         d[i] += 1
# print(d)