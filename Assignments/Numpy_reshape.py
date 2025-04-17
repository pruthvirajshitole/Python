#  Q1. Given a 3D NumPy array:  
   
#    arr = np.array([
#        [[1, 2, 3], [4, 5, 6]],
#        [[7, 8, 9], [10, 11, 12]],
#        [[13, 14, 15], [16, 17, 18]]
#    ])
   
#    Extract a subarray containing only the second column of each 2D array and output should be:  
   
#    [[2, 5],  
#     [8, 11],  
#     [14, 17]]

# import numpy as np
# arr = np.array([
#        [[1, 2, 3], [4, 5, 6]],
#        [[7, 8, 9], [10, 11, 12]],
#        [[13, 14, 15], [16, 17, 18]]
#    ])
# print(arr[0:3,0:3,1])


#    Q2. Given a 2D NumPy array:  
   
#    arr = np.array([
#        [10, 20, 30, 40],
#        [50, 60, 70, 80],
#        [90, 100, 110, 120]
#    ])
   
#    Extract a 2x2 subarray from the bottom right corner. Expected output:  
   
#    [[70, 80],  
#     [110, 120]]

# arr = np.array([
#        [10, 20, 30, 40],
#        [50, 60, 70, 80],
#        [90, 100, 110, 120]
#    ])
# print(arr[1:,2:])
    

#    Q3. Given a 3D NumPy array:  
   
#    arr = np.array([
#        [[1, 2, 3], [4, 5, 6]],
#        [[7, 8, 9], [10, 11, 12]],
#        [[13, 14, 15], [16, 17, 18]]
#    ])
#    Replace all elements in the last slice (last 2D array) with their square values.
#    Expected modified array:  
#    [
#        [[1, 2, 3], [4, 5, 6]],
#        [[7, 8, 9], [10, 11, 12]],
#        [[169, 196, 225], [256, 289, 324]]
#    ]

import numpy as np
arr = np.array([
       [[1, 2, 3], [4, 5, 6]],
       [[7, 8, 9], [10, 11, 12]],
       [[13, 14, 15], [16, 17, 18]]
   ])
arr[-1] = arr[2:]**2
print(arr)


#    Q4. Given a 1D array:  
   
#    arr = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12])
   
#    Reshape it into a 3x4 matrix. Expected output:  
   
#    [[1, 2, 3, 4],  
#     [5, 6, 7, 8],  
#     [9, 10, 11, 12]]
     
# arr = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12])
# print(arr.reshape(3,4))



#    Q5. Given a 2D array:  
#    arr = np.array([
#        [1, 2, 3, 4],
#        [5, 6, 7, 8]
#    ])
#    Reshape it into a 4x2 matrix. Expected output:  
   
#    [[1, 2],  
#     [3, 4],  
#     [5, 6],  
#     [7, 8]]
     

#    Q6. Given a 1D array:  
#    arr = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12])
#    Convert it into a 2D array of shape (2, 3, 2). Expected output:  
#    [[[1, 2], [3, 4], [5, 6]],  
#     [[7, 8], [9, 10], [11, 12]]]

# arr = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12])
# print(arr.reshape(2,3,2))


#    Q7. Given a 3D array, reshape it into a 2D array without changing data order:  
#    arr = np.array([
#        [[1, 2], [3, 4]],
#        [[5, 6], [7, 8]]
#    ])
#    Expected output after reshaping to (2, 4):  
#    [[1, 2, 3, 4],  
#     [5, 6, 7, 8]]

# arr = np.array([
#        [[1, 2], [3, 4]],
#        [[5, 6], [7, 8]]
#    ])
# print(arr.reshape(2,4))
     

#    Q8. Given a NumPy array:  
#    arr = np.array([10, 20, 30, 40, 50]) 
#    Create a copy of the array and modify the first element in the copy to 100.
# Ensure the original array remains unchanged.  

# arr = np.array([10, 20, 30, 40, 50])
# copy = arr.copy()
# copy[0] = 100
# print('original array:',arr)
# print('copy of arr:',copy)


#    Q9. Given a NumPy array:  
#    arr = np.array([10, 20, 30, 40, 50])
#    Create a view of the array, modify the second element to 99,
#    and show how it affects the original array.  

# arr = np.array([10, 20, 30, 40, 50])
# view = arr.view()
# view[0] = 100
# print('original array:',arr)
# print('view of arr:',view)


#    Q10. Given a 2D array:  
#    arr = np.array([
#        [1, 2, 3],
#        [4, 5, 6],
#        [7, 8, 9]
#    ])
#    Flatten the array into a 1D array. Expected output:  
#    [1, 2, 3, 4, 5, 6, 7, 8, 9]
     
# arr = np.array([
#        [1, 2, 3],
#        [4, 5, 6],
#        [7, 8, 9]
#    ])
# print(arr.reshape(-1))



#    Q11. Given a 3D array:  
#    arr = np.array([
#        [[1, 2, 3], [4, 5, 6]],
#        [[7, 8, 9], [10, 11, 12]]
#    ])
#    Convert it into a 2D array of shape (3, 4). Expected output: 
#    [[1, 2, 3, 4],  
#     [5, 6, 7, 8],  
#     [9, 10, 11, 12]]

# arr = np.array([
#        [[1, 2, 3], [4, 5, 6]],
#        [[7, 8, 9], [10, 11, 12]]
#    ])
# print(arr.reshape(3,4))


#    Q12. Given a NumPy array:  
#    arr = np.array([[1, 2], [3, 4], [5, 6]])
#    Reshape it into a 1D array. Expected output:  
#    [1, 2, 3, 4, 5, 6]

# arr = np.array([[1, 2], [3, 4], [5, 6]])
# print(arr.reshape(-1))



#    Q13. Given a NumPy array:  
#    arr = np.array([1, 2, 3, 4, 5, 6])  
#    Reshape it into a 3D array of shape (2, 1, 3). Expected output:    
#    [[[1, 2, 3]],  
#     [[4, 5, 6]]]

# arr = np.array([1, 2, 3, 4, 5, 6])
# print(arr.reshape(2,1,3))


#    Q14. Given a NumPy array:  
#    arr = np.array([
#        [1, 2, 3],
#        [4, 5, 6]
#    ])
#    Create a view, change the first element to 99, and confirm if the original
#    array gets updated.

# arr = np.array([
#        [1, 2, 3],
#        [4, 5, 6]
#    ])
# view = arr.view()
# view[0][0] = 99
# print('view:',view)
# print('original array:',arr)


#    Q15. Given a NumPy array:   
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

# arr_1D = arr.reshape(1,-1)
# print(arr_1D)

# arr_3D = arr_1D.reshape(2,2,2)
# print(arr_3D)