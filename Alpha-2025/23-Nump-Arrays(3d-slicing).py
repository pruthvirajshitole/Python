import numpy as np
# 1. Input:  
#    Extract the first layer (all rows and columns from the first 2D slice).  

# array = np.array([[[1, 2, 3], [4, 5, 6], [7, 8, 9]],  
#                      [[10, 11, 12], [13, 14, 15], [16, 17, 18]],  
#                      [[19, 20, 21], [22, 23, 24], [25, 26, 27]]])  

# print(array[0])


# 2. Input:  
#    Extract the element 26 from the array.  

# array = np.array([[[5, 6, 7], [8, 9, 10], [11, 12, 13]],  
#                      [[15, 16, 17], [18, 19, 20], [21, 22, 23]],  
#                      [[25, 26, 27], [28, 29, 30], [31, 32, 33]]])  

# print(array[2][0][1])


# 3. Input:  
#    Extract all rows and the last column of the second layer.  

# array = np.array([[[1, 2, 3], [4, 5, 6], [7, 8, 9]],  
#                      [[10, 11, 12], [13, 14, 15], [16, 17, 18]],  
#                      [[19, 20, 21], [22, 23, 24], [25, 26, 27]]])  

# print(array[1,:,2:])


# 4. Input:  
#    Extract the last two layers (all rows and columns from the last two 2D slices).  

# array = np.array([[[2, 4, 6], [8, 10, 12], [14, 16, 18]],  
#                      [[20, 22, 24], [26, 28, 30], [32, 34, 36]],  
#                      [[38, 40, 42], [44, 46, 48], [50, 52, 54]]])  
# print(array[1:])


# 5. Input:  
#    Extract the first two rows and first two columns of the last layer.  

# array = np.array([[[1, 1, 1], [2, 2, 2], [3, 3, 3]],  
#                      [[4, 4, 4], [5, 5, 5], [6, 6, 6]],  
#                      [[7, 7, 7], [8, 8, 8], [9, 9, 9]]])  

# print(array[2,:2,:2])


# 6. Input:  
#    Extract the second column from all layers.  

# array = np.array([[[0, 1, 2], [3, 4, 5], [6, 7, 8]],  
#                      [[9, 10, 11], [12, 13, 14], [15, 16, 17]],  
#                      [[18, 19, 20], [21, 22, 23], [24, 25, 26]]])  

# print(array[:,:,1])


# 7. Input:  
#    Extract all elements from the second row across all layers.  

# array = np.array([[[10, 20, 30], [40, 50, 60], [70, 80, 90]],  
#                      [[15, 25, 35], [45, 55, 65], [75, 85, 95]],  
#                      [[100, 200, 300], [400, 500, 600], [700, 800, 900]]])  
# print(array[:,1])


# 8. Input:  
#    Extract a 2x2x2 sub-array starting from the top-left corner of the array.  

# array = np.array([[[3, 6, 9], [12, 15, 18], [21, 24, 27]],  
#                      [[30, 33, 36], [39, 42, 45], [48, 51, 54]],  
#                      [[57, 60, 63], [66, 69, 72], [75, 78, 81]]])  
# print(array[:2,:2,:2])


# 9. Input:  
#    Extract the last two elements of the third row from the second layer.  

# array = np.array([[[5, 10, 15], [20, 25, 30], [35, 40, 45]],  
#                      [[50, 55, 60], [65, 70, 75], [80, 85, 90]],  
#                      [[95, 100, 105], [110, 115, 120], [125, 130, 135]]])  

# print(array[2:,2,1:])


# 10. Input:  
#     Extract the first column of every row from the second layer.  

# array = np.array([[[2, 4, 6], [8, 10, 12], [14, 16, 18]],  
#                       [[20, 22, 24], [26, 28, 30], [32, 34, 36]],  
#                       [[38, 40, 42], [44, 46, 48], [50, 52, 54]]])  
# print(array[1,:,0])


# 11. Input:  
#     Extract all rows except the last one from all layers.  

# array = np.array([[[1, 1, 1], [2, 2, 2], [3, 3, 3]],  
#                       [[4, 4, 4], [5, 5, 5], [6, 6, 6]],  
#                       [[7, 7, 7], [8, 8, 8], [9, 9, 9]]])  
# print(array[:,:2])


# 12. Input:  
#     Extract all elements except the first two columns from the last layer.  

# array = np.array([[[0, 2, 4], [6, 8, 10], [12, 14, 16]],  
#                       [[18, 20, 22], [24, 26, 28], [30, 32, 34]],  
#                       [[36, 38, 40], [42, 44, 46], [48, 50, 52]]]) 
# print(array[2,:,2])


# 13. Input:  
#     Extract the elements at positions (1, 1, 1) and (2, 2, 2).  

# array = np.array([[[100, 200, 300], [400, 500, 600], [700, 800, 900]],  
#                       [[110, 210, 310], [410, 510, 610], [710, 810, 910]],  
#                       [[120, 220, 320], [420, 520, 620], [720, 820, 920]]]) 
# print(array[[1,2],[1,2],[1,2]])


# 14. Input:  
#     Extract a 2x2x2 sub-array starting from the middle of the array.  

# array = np.array([[[10, 20, 30], [40, 50, 60], [70, 80, 90]],  
#                       [[15, 25, 35], [45, 55, 65], [75, 85, 95]],  
#                       [[100, 200, 300], [400, 500, 600], [700, 800, 900]]])  
# print(array[1:3, 1:3, 1:3])


# 15. Input:  
#     Extract all layers but reverse the row order of the second layer. 

# array = np.array([[[1, 2, 3], [4, 5, 6], [7, 8, 9]],  
#                       [[10, 11, 12], [13, 14, 15], [16, 17, 18]],  
#                       [[19, 20, 21], [22, 23, 24], [25, 26, 27]]])  
# rev = array[1]
# print(rev[::-1])

