import numpy as np

# 1. Given a 3D NumPy array, extract all elements from the second row
# of every 2D slice along the third axis.  

# arr = np.arange(12).reshape(3,2,2)
# print(arr)

# print(arr[:,1])


# 2. Create a 2D NumPy array and write a function to swap two specific columns without using a loop.  

# arr = np.array([
#     [1,2,3],
#     [4,5,6]
# ])

# print('-----method-1-----')
# arr[:,[0,2]] = arr[:,[2,0]]
# print(arr)

# print('-----method-2-----')
# def swap(arr):
#     temp = arr[:,0].copy()
#     arr[:,0] = arr[:,2]
#     arr[:,2] = temp
#     print(arr)

# swap(arr)


# 3. Given a 3D NumPy array, write a function to reverse the order of elements along the second axis. 

# arr = np.array([
#                 [
#                     [1,2,3],
#                     [11,12,13]
#                 ],
#                 [
#                     [4,5,6],
#                     [14,15,16]
#                 ],
#                 [
#                     [7,8,9],
#                     [17,18,19]
#                 ]
#                 ])

# def reverese(arr):
#     print(arr[:,::-1,:])
# reverese(arr)


# 4. Create a NumPy array and split it into multiple smaller arrays based on user-defined column indices.  

# PENDING


# 5. Join two 2D NumPy arrays along rows and then sort the resulting array based on the values in the second column.  

# 6. Write a NumPy function to find the indices of all occurrences of a given value in a 3D array.  

# 7. Given a NumPy array, filter out all elements that are not within a given range without using a loop.  

# 8. Create a NumPy array with random integers and sort each row individually without using explicit loops.  

# 9. Given a 2D NumPy array, write a function to find and replace all even numbers with -1.  

# 10. Generate a random NumPy array with values between 1 and 100 and filter out all prime numbers.  

# 11. Using the NumPy random module, generate a 3D array with normally distributed values and compute the mean along the last axis.  

# 12. Create a function that generates a 2D NumPy array with random floating-point numbers and normalizes each row between 0 and 1.  

# 13. Write a program to generate a 3D NumPy array of random integers and replace all elements greater than a certain threshold with the threshold value.  

# 14. Generate a 1D NumPy array of random numbers and return only those that fall within one standard deviation of the mean.  

# 15. Write a function that creates a 3D NumPy array filled with random values, sorts each 2D slice along the first axis, and returns the sorted array. 

# from numpy import random
# def random_array():
#     arr = random.randint(0,100,(2,2,2))
#     print(arr)
# random_array()
