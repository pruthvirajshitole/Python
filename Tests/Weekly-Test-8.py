# 1. What is a NumPy array, and how is it different from a Python list?  

# Ans: Numpy array is a homogenous, ordered collection of data which is mutable.
#      Numpy arrays are stored in continuous locations known as references in memory. 
#      But list are heterogenous so they are stored at different references.


# 2. Explain the concept of broadcasting in NumPy with an example.  


# 3. What are ufuncs in NumPy? Provide an example.  


# 4. What is the purpose of the numpy.random module? Name three functions it provides.  

# Ans: numpy.random is a module present in numpy library which provides different type of function
#      to test or introducing random numberes or patterns.
#      It includes random.int(), random.rand(), random.choice(), random.shuffle(), random.uniform()


# 5. What is difference between addition and sub

# Ans: addition adds the values where as sub substracts the values.


# 6. What is Discrete difference.

# Ans: Discrete gives only unique values selected from a table. It does not allow duplicate values.


# 7. What is Universal function. Brief any 5 categories in them.


# 8. What is difference between Python list and Numpy Array? 

# Ans: Numpy arrays are stored in continuous locations known as references in memory. 
#      But list are heterogenous so they are stored at different references.


# 9. Measure the time it takes to square each element of a large array created with np.arange(5000)


# 10. Discuss the advantages of using Numpy over Python list.  

# Ans: Numpy arrays are 50X faster than Python list compared with excecution time and efficiency because of thier property of 
#      stroing array elements in continuous location it allow python to access and manipulate them.




# Section B: Correct the Error  

import numpy as np

# 1. arr = np.array[1, 2, 3]

# import numpy as np
# arr = np.array([1, 2, 3])
# print(arr)


# 2. result = np.random.randint(10, 20, size=5, replace=False)

# result = np.random.randint(10, 20, size=5)
# print(result)


# 3. np.add([1, 2, 3], [4, 5])

# print(np.add([1, 2, 3], [4, 5, 6]))


# 4. matrix = np.array([[1, 2], [3, 4]]) print(matrix.T()  

# matrix = np.array([[1, 2], [3, 4]])
# print(matrix)


# 5. inv_matrix = np.linalg.inv([[1, 2], [3, 4]])

# inv_matrix = np.linalg.inv([[1, 2], [3, 4]])
# print(inv_matrix)  


# 6. array=np.sort.[1,2,3]

# array=np.sort([1,2,3])
# print(array)


# 7. result=np.min.(x)

# result=np.min([3,45,34,65,34,24])
# print(result)


# 8. random_arr = np.random.random(2.5)

# random_arr = np.random.rand(2,5) 
# print(random_arr)


# 9. matrix = np.array([1, 2], [3, 4])

# matrix = np.array([[1, 2], [3, 4]])
# print(matrix)


# 10. result=np.max.(x)

# result=np.max([43,434,6,45,34,67,56,55454,4])
# print(result)




# Section C: Write a Program  

# 1. Create a 3x3 NumPy array filled with random integers between 1 and 10.  

print(np.random.randint(1,11,(3,3)))


# 2. Find all substrings of a string that are palindromes.

# PENDING


# 3. Generate a NumPy array of 10 random floats between 0 and 1.  

# print(np.random.uniform(0,1,10))


# 4. Implement a recursive function to check if a given number is a palindrome.

# def palindrome(n):
#     temp = n
#     rev = 0
#     while n!=0:
#         d = n%10
#         rev = 10*rev+d
#         return palindrome(n//10)
#     if temp == rev:
#         print('It is a Palindrome.')
#     else:
#         print('It is not a Palindrome.')
# n = int(input("Enter a number: "))
# palindrome(n)



# 5. Create a NumPy array and apply the np.sqrt ufunc on all its elements.

# arr = np.array([1,2,3,4,5])
# print(np.sqrt(arr))


# 6. Create a 1D NumPy array of 6 zeros using np.zeros and print it. 

# print(np.zeros(6))


# 7. Create a 2x2 array of twos and multiply each element by 5, then print the result. 

# array=([2,2],[2,2])
# for i in range(len(array)):
#   for j in range(len(array)):
#     array[i][j]*=5
# print(array)


# 8. Given a NumPy array:  
#    arr = np.array([
#        [[1, 2], [3, 4]],
#        [[5, 6], [7, 8]]
#    ])
#    Reshape it into a 1D array and then back into a (2, 2, 2) shape.
#    Verify if the reshaped array matches the original. 

# arr = np.array([
#        [[1, 2], [3, 4]],
#        [[5, 6], [7, 8]]
#    ])
# arr_1d = arr.reshape(-1)
# arr_3d = arr.reshape(2,2,2)
# print(arr_1d)
# print(arr_3d)


# 9. Write a program to create a NumPy array of even numbers between 10 and 30.  

# arr=np.arange(10,31,2)
# print(arr)    


# 10. Tricky Insert in a 2D Array  
#     Given: 
#     arr = np.array([
#         [1, 2, 3],
#         [4, 5, 6]
#     ])    
#     - Insert a new column [7, 8] at index 0.  
#     - Insert a new row [9, 10, 11] at index 1

# arr = np.array([
#         [1, 2, 3],
#         [4, 5, 6]
#     ])
# arr = np.insert(arr, 0, [7, 8], axis=1)
# arr = np.insert(arr, 1, [9, 10, 11,12], axis=0)
# print(arr)