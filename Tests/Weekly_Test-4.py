# Section A: Theory (10 Questions)

# Q1.What are the key differences between lists and arrays in Python?

# Ans: lists can store heterogenous data while arrays are used to store homogenous data.


# Q2.Explain the concept of a set in Python. How does it differ from a list?
# Provide examples to illustrate your answer.

# Ans: Set is a collection of heterogenous data. Compared to list it does not allow duplicates.


# Q3.Describe how a dictionary works in Python. What are the primary operations you can perform on dictionaries?

# Ans: Dictionary contains key-value pairs as element where keys are unique and the values can be duplicates.
# We can add elemets or updates using update(),remove().


# Q4.What are the advantages of using sets over lists in Python?

# Ans: If we use sets over lists we can store only non-repeatative value which can save memmory.


# Q5.How can you iterate over a list in Python? Discuss different methods and their use cases.

# Ans: We can iterate over a list using loops.
# for loop and while loop are two different methods, where for loop is used to iterate over the elements
# of list and while loop is used to iterate over the indexes of list.


# Q6.How can you update a dictionary in Python? Explain the methods with examples.

# Ans: We can update dictionary using d['key'] = 'value' if the key is already present
# in the dictionary it will remain unchanged, if not the new key with value is added. 


# Q7.What is string? Is string mutable or not and iterable or not, explain.

# Ans: String is a ordered collection of characters. String is immutable and iterable.


# Q8.What is frozen set, explain how different it is from set.

# Ans: Froze set is type of set, once the frozen set is defined we can't change it.

 
# Q9. What is dictionary comprehension? give an example.

# Ans: Dictionary comprehension is reduce the code size or shorten the code.


# Q10. What is Function, brief it.

# Ans: Function is a collection of statements or instruction which will execute when it is called.



# Section B: Correct the Code (10 Questions)

# Q1.

# data = [1, 2, "three", 4, "five"]
# total = 0
# for item in data:
#     total += item 
# print(f"Total: {total}")

# data = [1, 2, "three", 4, "five"]
# total = 0
# for item in range(len(data)):
#     total += item 
# print(f"Total: {total}")


# Q2.

# my_list = [1, 2, 3, 4]
# for i in range(5):
#     print(my_list[i])

# CORRECTED CODE

# my_list = [1, 2, 3, 4]
# for i in my_list:
#     print(i)


# Q3.

# def calculate_area(radius):
#     return 3.14 * radius ** 2

# area = calculate_area()
# print(area)

# CORRECTED CODE

# def calculate_area(radius):
#     return 3.14 * radius ** 2

# area = calculate_area(2)
# print(area)


# Q4. 

# def greet(name)
#     print("Hello, " + name)

# CORRECTED CODE

# def greet(name):
#     print("Hello, " + name)

# greet('Pruthviraj')


# Q5.

# numbers = [1, 2, 3]
# print(numbers[3])

# CORRECTED CODE

# numbers = [1, 2, 3]
# print(numbers)


# Q6.

# def print_numbers():
# for i in range(5):
#     print(i)

# CORRECTED CODE

# def print_numbers():
#     for i in range(5):
#         print(i)
# print_numbers()


# Q7.

# print(message)
# message = "This is a test message."

# CORRECTED CODE

# message = "This is a test message."
# print(message)


# Q8.

# def sum_even(numbers):
#     total = 0
#     for num in numbers:
#         if num % 2 == 0:
#             total += num
#         else:
#             return total

# print(sum_even([1, 2, 3, 4, 5, 6]))

# CORRECTED CODE

# def sum_even(numbers):
#     total = 0
#     for num in numbers:
#         if num % 2 == 0:
#             total += num
#     return total

# print(sum_even([1, 2, 3, 4, 5, 6]))


# Q9.

# data = {"name": "Alice", "age": 30}
# print(data["address"])

# CORRECTED CODE

# data = {"name": "Alice", "age": 30}
# print(data["name"])


# Q10.

# def my_func(x, y):
# return x + y
#    result = my_func(5)
#    print(result)

# CORRECTED CODE

# def my_func(x, y):
#     return x + y
# result = my_func(5,3)
# print(result)


# Section C: Write Code For (10 Questions) 

# Q1. WAP and Check a string is Anagrams or not?

# s1 = (input('Enter first string: ').lower()).strip()
# s2 = (input('Enter second string: ').lower()).strip()

# s3 = sorted(s1)
# s4 = sorted(s2)

# if s3 == s4:
#     print(f'{s1} and {s2} are Anagrams.')
# else:
#     print(f'{s1} and {s2} are not Anagrams.')


# Q2. WAP and Check a number is Harshad or not?

# num = int(input("Enter a number: "))
# t = num
# s = 0
# while num!=0:
#     d = num%10
#     s = s+d
#     num = num//10
# if t%s == 0:
#     print(t,' is a hurshad number')
# else:
#     print(t,' is not a harshad number')


# Q3. Write a program to find the second largest number in a list.(without using inbuilt function)

# l = (input("Enter a list: ")).split(',')
# lst = []
# for i in l:
#     lst.append(i)
# lst = sorted(l)
# print(lst[-2])


# Q4. string="hello"
#     find all the possible sub-string.

# s = "hello"
# l = []
# w = ''
# a = 0
# for j in s:
#     for i in s[a:len(s)+1]:
#         w += i
#         l.append(w)
#     a += 1
#     w = ''
# print(l)


# Q5. Check if a given string is a palindrome.(without using inbuilt function)

# s = input("Enter a string: ")
# r = ''
# for i in s:
#     if i != ' ':
#         r += i
# if r == r[::-1]:
#     print(f'{s} is a palindrome.')
# else:
#     print(f'{s} is not a palindrome.')


# Q6. WAP and count the number of vowels and consonants in the string.

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


# Q7. Write a Python program to count the occurrences of each character in a given string using a dictionary.

# s = input("Enter a string: ").lower()
# d = {}
# for i in s:
#     if i in d:
#         d[i] += 1
#     else:
#         d[i] = 1
# print(d)


# Q8. input_list=[1,2,3,4,5] 
#     expected_output: [1,4,9,16,25] using lambda function.

# input_list = [1,2,3,4,5]

# output_list = list(map(lambda x: x ** 2, input_list))

# print(output_list)


# Q9. WAP takes the input of elements in the list and prints all Armstrong no from it.

l1 = [231,341,543,654,1,3,153]
l2 = []

for n in l1:
    n = str(n)
    l = len(n)                     
    n = int(n)                  
    t = n
    arm = 0
    while n != 0:        
        d = n % 10     
        arm = arm + d**l   
        n = n // 10        
    if t == arm:
        l2.append(t)
print(l2)


# Q10. Implement user defined function that works as split().

# s= input("Enter a string: ")

# l = []
# w = ""
# for i in s:
#     if i != ' ':
#         w+=i
#     else:
#         l.append(w)
#         w = ""
# l.append(w)
# print(l)