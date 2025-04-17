# 1. Write a function that takes a list of n-1 unique numbers from 1 to n (unordered)
# and finds the missing number without using the sum formula.  

# def unique():
#     l = [1,3,5,4,7,8,6,9]



# 2. Implement a function that compresses a string using the counts of repeated characters.
# Example: "aaabbcdd" → "a3b2c1d2". If the compressed string is longer, return the original.  

# s='aaabbcdd'

# def compress(s):
#     d = {}
#     for i in s:
#         if i not in d:
#             d[i] = 1
#         else:
#             d[i] += 1
#     c_s = ''
#     for m,n in d.items():
#         c_s += m+str(n)
#     if len(s)<len(c_s):
#         return s
#     else:
#         return c_s
# print(compress(s))


# 3. Given a nested list of integers, write a function to return a sorted list of
# unique elements across all lists. Example: [[1,2,3], [3,4,5], [5,6]] → [1,2,3,4,5,6].  

# l = [[1,2,3], [3,4,5], [5,6]]
# l1 = []
# for i in l:
#     if len(i)>1:
#         l1.extend(i)
#     else:
#         l1.append(i)
# print(l1)



# 4. Write a function that takes a list of integers and returns True if it contains three consecutive even numbers, otherwise False.  

# 5. Implement a function that finds the longest contiguous subarray with an equal number of 0s and 1s.  

# 6. Write a function that takes a string containing only ( and ) and checks if it is balanced. Example: "(()())" → True, "(()" → False.  

# 7. Given a list of tuples where each tuple contains a person's name and age, write a function to sort the list first by age (ascending) and then by name (alphabetically).  

# 8. Implement a function that takes a list and returns a dictionary where keys are unique elements and values are their frequencies.  

# 9. Write a function that finds the second largest number in a list without using sorting.  

# 10. Implement a function to find all pairs in a list that sum up to a given target.  

# 11. Write a lambda function to check if a given number is a prime number.  

# 12. Create a lambda function to sort a list of dictionaries based on a given key.  

# 13. Implement a recursive function to find the sum of digits of a given number.  

# 14. Demonstrate the difference between local, global, and nonlocal scopes with an example that modifies a variable inside nested functions.  

# 15. Write a function using global and nonlocal keywords to increment a counter across multiple function calls.  
