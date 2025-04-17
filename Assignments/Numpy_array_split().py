# 1. 2D Array Slicing & Iteration  
#    Given the following 2D NumPy array:
#    arr = np.array([
#        [1, 2, 3, 4],
#        [5, 6, 7, 8],
#        [9, 10, 11, 12]
#    ])    
#    Extract a subarray containing the last two rows and first two columns. Then,
#    iterate over each element of this subarray and print the square of each element.

import numpy as np
# arr = np.array([
#        [1, 2, 3, 4],
#        [5, 6, 7, 8],
#        [9, 10, 11, 12]
#    ]) 
# for i in np.nditer(arr[1:,:2]):
#     print(i**2)


# 2. 3D Array Slicing & Modification  
#    Given the 3D array:  
   
#    arr = np.array([
#        [[1, 2, 3], [4, 5, 6]],
#        [[7, 8, 9], [10, 11, 12]]
#    ])
     
#    Slice and extract a 2D array containing only the second row of both 3D planes.
#    Modify this slice by adding 10 to each element and print both the original and modified arrays.  


arr = np.array([
       [[1, 2, 3], [4, 5, 6]],
       [[7, 8, 9], [10, 11, 12]]
   ])
print(arr[1])


# 3. Reshape and View vs Copy  
#    Given an initial 1D array:  
   
#    arr = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12])
     
#    Reshape it into a 3×4 array and create a view of the reshaped array.
#    Modify the view by replacing all elements in the first row with `-1` and print both 
#    the original array and view. Explain the output.


# 4. Appending & Deleting Elements  
#    Given the 2D array:  
   
# arr = np.array([
#        [10, 20, 30],
#        [40, 50, 60]
#    ])
     
#    - Append a new row `[70, 80, 90]` to the array.  
#    - Delete the second column from the updated array.  
#    - Insert a new column `[100, 110]` at index `1`.

arr = np.array([
       [10, 20, 30],
       [40, 50, 60]
   ])


# 5. Updating Specific Elements in a 3D Array  
#    Given the 3D array:  
   
#    arr = np.array([
#        [[1, 2], [3, 4]],
#        [[5, 6], [7, 8]]
#    ])
     
#    Change all elements greater than `4` to `99` and print the updated array.  

# 6. Concatenation of 1D, 2D, and 3D Arrays  
#    Given the following arrays:  
   
#    arr1 = np.array([1, 2, 3])  
#    arr2 = np.array([[4, 5, 6], [7, 8, 9]])  
#    arr3 = np.array([
#        [[10, 11], [12, 13]],
#        [[14, 15], [16, 17]]
#    ])
     
#    Perform valid concatenations:  
#    - Concatenate `arr1` along axis 0 with a reshaped version of `arr2` to match dimensions.  
#    - Concatenate `arr2` and `arr3` along an appropriate axis.  

# 7. Stacking Operations (hstack, vstack, dstack)  
#    Given:  
   
#    arr1 = np.array([[1, 2, 3], [4, 5, 6]])  
#    arr2 = np.array([[7, 8, 9], [10, 11, 12]])
     
#    - Perform `hstack`, `vstack`, and `dstack` on `arr1` and `arr2`.  
#    - Explain the shape of the output arrays.  

# 8. Tricky Array Split (2D with axis=0 and axis=1)  
#    Given:  
   
#    arr = np.array([
#        [1, 2, 3, 4, 5, 6],
#        [7, 8, 9, 10, 11, 12]
#    ])
     
#    - Split the array into 3 equal parts along `axis=1`.  
#    - Split the array into 2 parts along `axis=0`.  

# 9. 3D Array Split Along Different Axes  
#    Given:  
   
#    arr = np.array([
#        [[1, 2, 3], [4, 5, 6]],
#        [[7, 8, 9], [10, 11, 12]],
#        [[13, 14, 15], [16, 17, 18]]
#    ])
     
#    - Split the array into 3 parts along `axis=0`.  
#    - Split the array into 2 parts along `axis=1`.  
#    - Split the array into 3 parts along `axis=2`.  

# 10. VSplit of a 2D Array (Uneven Split)  
#     Given:  
    
#     arr = np.array([
#         [1, 2, 3],
#         [4, 5, 6],
#         [7, 8, 9],
#         [10, 11, 12],
#         [13, 14, 15]
#     ])
      
#     - Use `vsplit` to divide the array into 3 uneven parts.  

# 11. HSplit on a 2D Array (Challenging Case)  
#     Given:  
    
#     arr = np.array([
#         [1, 2, 3, 4, 5, 6],
#         [7, 8, 9, 10, 11, 12]
#     ])
      
#     - Split this array into 3 equal parts along `axis=1` using `hsplit`.  
#     - Explain what happens if you try to split it into 4 parts.  

# 12. Reshape and Maintain Data Integrity  
#     Given the 1D array:  
    
#     arr = np.arange(24)
      
#     - Reshape it into a 3D array with dimensions `(2, 3, 4)`.  
#     - Flatten it back into a 1D array.  

# 13. Tricky Insert in a 2D Array  
#     Given:  
    
#     arr = np.array([
#         [1, 2, 3],
#         [4, 5, 6]
#     ])
      
#     - Insert a new column `[7, 8]` at index `0`.  
#     - Insert a new row `[9, 10, 11]` at index `1`.  

# 14. Modify an Array Using Indexing  
#     Given the 2D array:  
    
#     arr = np.array([
#         [5, 10, 15],
#         [20, 25, 30],
#         [35, 40, 45]
#     ])
      
#     - Change all even numbers to `0`.  
#     - Change all numbers divisible by `5` but not `10` to `-1`.  

# 15. Delete Elements from a 3D Array  
#     Given:  
    
#     arr = np.array([
#         [[1, 2, 3], [4, 5, 6]],
#         [[7, 8, 9], [10, 11, 12]],
#         [[13, 14, 15], [16, 17, 18]]
#     ])
      
#     - Delete the second row from all 3D planes.  
#     - Delete the last column from the modified array.

