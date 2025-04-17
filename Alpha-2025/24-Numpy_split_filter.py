import numpy as np

# 1. 2D Array Slicing & Iteration  
#    Given the following 2D NumPy array:      
#    Extract a subarray containing the last two rows and first two columns. Then,
#    iterate over each element of this subarray and print the square of each element.

# arr = np.array([
#        [1, 2, 3, 4],
#        [5, 6, 7, 8],
#        [9, 10, 11, 12]
#    ])
# arr1 = arr[1:,:2]
# print(arr1)

# for i in np.nditer(arr1):
#     print(i**2)


# 2. 3D Array Slicing & Modification  
#    Given the 3D array:  
#  Slice and extract a 2D array containing only the second row of both 3D planes.
#  Modify this slice by adding 10 to each element and print both the original and modified arrays.  

# arr = np.array([
#        [[1, 2, 3], [4, 5, 6]],
#        [[7, 8, 9], [10, 11, 12]]
#    ])
# arr1 = arr[:,1]
# arr1 = arr1+10
# print(f'Original array:\n{arr}')
# print(f'Modified array:\n{arr1}')


# 3. Reshape and View vs Copy  
#    Given an initial 1D array:     
#    Reshape it into a 3×4 array and create a view of the reshaped array.
#    Modify the view by replacing all elements in the first row with `-1` 
#    and print both the original array and view. Explain the output.  

# arr = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12])
# reshape_arr = arr.reshape(3,4)
# view_arr = reshape_arr.view()
# view_arr[0] = [-1,-1,-1,-1]
# print("Original array:\n",arr)
# print("View:\n",view_arr)


# 4. Appending & Deleting Elements  
#    Given the 2D array:  
#    - Append a new row `[70, 80, 90]` to the array.  
#    - Delete the second column from the updated array.  
#    - Insert a new column `[100, 110]` at index `1`.  

# arr = np.array([
#        [10, 20, 30],
#        [40, 50, 60]
#    ])

# new_arr = np.append(arr,[[70, 80, 90]],axis=0)
# print(new_arr)
# new_arr = np.delete(new_arr,1,axis=1)
# print(new_arr)
# new_arr = np.insert(new_arr,1,[100,110],axis=0)
# print(new_arr)


# 5. Updating Specific Elements in a 3D Array  
#    Given the 3D array:       
#    Change all elements greater than `4` to `99` and print the updated array.
  
# arr = np.array([
#        [[1, 2], [3, 4]],
#        [[5, 6], [7, 8]]
#    ])

# arr[arr>4] = 99
# print(f'Updated array:\n{arr}')


# 6. Concatenation of 1D, 2D, and 3D Arrays  
#    Given the following arrays:       
#    Perform valid concatenations:  
#    - Concatenate `arr1` along axis 0 with a reshaped version of `arr2` to match dimensions.  
#    - Concatenate `arr2` and `arr3` along an appropriate axis.  

# PENDING

# arr1 = np.array([1, 2, 3])  
# arr2 = np.array([[4, 5, 6], [7, 8, 9]])  
# arr3 = np.array([
#        [[10, 11], [12, 13]],
#        [[14, 15], [16, 17]]
#    ])
# print(np.concatenate(arr1,arr2))


# 7. Stacking Operations (hstack, vstack, dstack)  
#    Given:    
#    - Perform `hstack`, `vstack`, and `dstack` on `arr1` and `arr2`.  
#    - Explain the shape of the output arrays. 
 
# arr1 = np.array([[1, 2, 3], [4, 5, 6]])  
# arr2 = np.array([[7, 8, 9], [10, 11, 12]])

# hstack_arr = np.hstack([arr1,arr2])
# print(hstack_arr)

# vstack_arr = np.vstack([arr1,arr2])
# print(vstack_arr)

# dstack_arr = np.dstack([arr1,arr2])
# print(dstack_arr)


# 8. Tricky Array Split (2D with axis=0 and axis=1)  
#    Given:     
#    - Split the array into 3 equal parts along `axis=1`.  
#    - Split the array into 2 parts along `axis=0`.  

# arr = np.array([
#        [1, 2, 3, 4, 5, 6],
#        [7, 8, 9, 10, 11, 12]
#    ])
# split_3 = np.array_split(arr,3,axis=1)
# print(split_3)

# split_2 = np.array_split(arr,2,axis=0)
# print(split_2)


# 9. 3D Array Split Along Different Axes  
#    Given:  
#    - Split the array into 3 parts along `axis=0`.  
#    - Split the array into 2 parts along `axis=1`.  
#    - Split the array into 3 parts along `axis=2`.  

# arr = np.array([
#        [[1, 2, 3], [4, 5, 6]],
#        [[7, 8, 9], [10, 11, 12]],
#        [[13, 14, 15], [16, 17, 18]]
#    ])
# split_axis0 = np.split(arr,3,axis=0)
# print(split_axis0)

# split_axis1 = np.split(arr,2,axis=1)
# print(split_axis1)

# split_axis2 = np.split(arr,3,axis=2)
# print(split_axis2)
     

# 10. VSplit of a 2D Array (Uneven Split)  
#     Given:   
#     - Use `vsplit` to divide the array into 3 uneven parts.  
    
# arr = np.array([
#         [1, 2, 3],
#         [4, 5, 6],
#         [7, 8, 9],
#         [10, 11, 12],
#         [13, 14, 15]
#     ])
# v_split = np.vsplit(arr,3)
# print(v_split)

# ValueError: array split does not result in an equal division


# 11. HSplit on a 2D Array (Challenging Case)  
#     Given:      
#     - Split this array into 3 equal parts along `axis=1` using `hsplit`.  
#     - Explain what happens if you try to split it into 4 parts.  

# arr = np.array([
#         [1, 2, 3, 4, 5, 6],
#         [7, 8, 9, 10, 11, 12]
#     ])
# s_arr = np.hsplit(arr,3)
# print(s_arr)


# 12. Reshape and Maintain Data Integrity  
#     Given the 1D array:
#     - Reshape it into a 3D array with dimensions `(2, 3, 4)`.  
#     - Flatten it back into a 1D array.  

# arr = np.arange(24)
# reshaped_arr = np.reshape(arr,(2,3,4))
# print(reshaped_arr)

# flatten_arr = np.reshape(reshaped_arr,-1)
# print(flatten_arr)


# 13. Tricky Insert in a 2D Array  
#     Given:      
#     - Insert a new column `[7, 8]` at index `0`.  
#     - Insert a new row `[9, 10, 11]` at index `1`.  

# arr = np.array([
#         [1, 2, 3],
#         [4, 5, 6]
#     ])
# new_arr = np.insert(arr,0,[[7,8]],axis=1)
# print(new_arr)

# new_arr = np.insert(arr,1,[9,10,11],axis=0)
# print(new_arr)


# 14. Modify an Array Using Indexing  
#     Given the 2D array:    
#     - Change all even numbers to `0`.  
#     - Change all numbers divisible by `5` but not `10` to `-1`.  

# arr = np.array([
#         [5, 10, 15],
#         [20, 25, 30],
#         [35, 40, 45]
#     ])
# arr[arr%2==0] = 0
# print(arr)

# arr[(arr%5==0) & (arr%10!=0)] = -1
# print(arr)



# 15. Delete Elements from a 3D Array  
#     Given:     
#     - Delete the second row from all 3D planes.  
#     - Delete the last column from the modified array.

# arr = np.array([
#         [[1, 2, 3], [4, 5, 6]],
#         [[7, 8, 9], [10, 11, 12]],
#         [[13, 14, 15], [16, 17, 18]]
#     ])

# new_arr = np.delete(arr,1,axis=1)
# print(new_arr)

# new_arr1 = np.delete(new_arr,2,axis=2)
# print(new_arr1)