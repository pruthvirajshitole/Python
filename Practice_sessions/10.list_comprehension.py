# 1. From a list of words, get the length of each word.l=["hello","hii","welcome","thankyou"]

# l=["hello","hii","welcome","thankyou"]
# lenth_words = [len(i) for i in l]
# print(lenth_words)


# 2. Create a list of numbers from 1 to 50 that are divisible by both 3 and 5.[11,23,15,30,67,45]

# l = [i for i in range(1,51) if i%3==0 and i%5==0]
# print(l)


# 3. Get the first letter of each word in a list if the word has more than 3 letters.

# w=["jay","kiya","jefff","lilyy"]
# word = [i[0] for i in w if len(i)>3]
# print(word)


# 4. Print the table of 8.

# t = [f'8*{i}={i*8}' for i in range(1,11)]
# print(t)


# 5. Write a Python program that takes a list of integers and returns the sum of the squares of the even numbers using list comprehension.

# numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]   # Output: 220
# l = [i**2 for i in numbers if i%2==0]
# print(sum(l))


# 6. sentence = "list comprehension is cool" From sentence extract only vowel.

# sentence = "list comprehension is cool"
# vowel = 'aeiou'
# vowels = [i for i in sentence if i in vowel]
# print(vowels)


# 7. Write a Python program that takes a list and returns a new list containing only the unique elements using list comprehension.
#    elements = [1, 2, 3, 2, 4, 5, 6, 3, 7]
#    Output: [1, 4, 5, 6, 7]

# l = [1, 2, 3, 2, 4, 5, 6, 3, 7]
# unique = [i for i in l if l.count(i)==1]
# print(unique)


# 8.  Given a list of integers, return a list with all negative numbers removed.
#    numbers = [-1, 2, -3, 4, -5, 6]
#    Output: [2, 4, 6]

# numbers = [-1, 2, -3, 4, -5, 6]
# n = [i for i in numbers if i>0]
# print(n)


# 9. Find the common elements in two lists using list comperhension.
#    list1 = [1, 2, 3, 4]
#    list2 = [3, 4, 5, 6]
#    Output: [3, 4]

# list1 = [1, 2, 3, 4]
# list2 = [3, 4, 5, 6]
# comman = [i for i in list1 if i in list2]
# print(comman)


# 10.Write a Python program that takes a list of integers and returns the count of the odd numbers using list comprehension.

# l = [1,2,3,4,5,6,8]
# odds = [i for i in l if i%2==1]
# print(len(odds))


# l = list(map(int,input("Enter list of integers seperated by spaces: ").split()))
# print(l)
