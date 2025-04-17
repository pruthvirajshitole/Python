# 1. Right-Angled Triangle of Numbers  
# Create a right-angled triangle where each row contains increasing numbers from 1 to the current row number.  
# Example for N=5:  

# 1
# 12
# 123
# 1234
# 12345

# for i in range(1, 6):
#     for j in range(1, i+1):
#         print(j, end="")
#     print()


# 2. Inverted Right-Angled Triangle of Numbers  
# Generate an inverted right-angled triangle where each row starts from the highest number and decrements.  
# Example for N=5:  

# 12345
# 1234
# 123
# 12
# 1

# for i in range(5, 0, -1):
#     for j in range(1, i+1):
#         print(j, end="")
#     print()


# 3. Pyramid of Numbers  
# Create a pyramid pattern with increasing numbers that also mirror themselves in each row.  
# Example for N=4:  

#    1
#   121
#  12321
# 1234321

# for i in range(1, 5):
#     for j in range(1, 5-i):
#         print(" ", end="")
#     for k in range(1, i+1):
#         print(k, end="")
#     for l in range(i-1, 0, -1):
#         print(l, end="")
#     print()


# 4. Number Square  
# Generate a square of numbers where each row contains the same number repeated N times.  
# Example for N=4:  

# 1 1 1 1
# 2 2 2 2
# 3 3 3 3
# 4 4 4 4

# for i in range(1,5):
#     for j in range(1,5):
#         print(i,end=" ")
#     print()


# 5. Hollow Square of Numbers  
# Create a hollow square where the borders are filled with numbers and the inside is empty.  
# Example for N=5:  

# 1 1 1 1 1
# 1       1
# 1       1
# 1       1
# 1 1 1 1 1

# for i in range(1, 6):
#     for j in range(1, 6):
#         if i==1 or i==5 or j==1 or j==5:
#             print("1", end=" ")
#         else:
#             print(" ", end=" ")
#     print()


# 6. Inverted Pyramid of Numbers  
# Generate an inverted pyramid where numbers decrement in each row.  
# Example for N=5:  

# 12345
# 1234
# 123
# 12
# 1

# for i in range(1,6):
#     for j in range(1,6):
#         if j<=6-i:
#             print(j,end="")
#         else:
#             print(" ",end="")
#     print()


# 7. Half Diamond of Numbers  
# Create a half-diamond pattern with numbers.  
# Example for N=4:  

# 1     
# 12
# 123
# 1234
# 123
# 12
# 1

# for i in range(1,8):
#     for j in range(1,5):
#         if j<=i and i<=4:
#             print(j,end="")
#         elif j<=8-i and i>=4:
#             print(j,end="")
#         else:
#             print(" ",end="")
#     print()
    

# 8. Number Rhombus  
# Generate a rhombus shape where numbers increase in the first half and decrease in the second half.  
# Example for N=4:  

#    1
#   121
#  12321
# 1234321
#  12321
#   121
#    1

# for i in range(1,5):
#     for j in range(1,5-i):
#         print(" ",end="")
#     for k in range(1,i+1):
#         print(k,end="")
#     for l in range(i-1,0,-1):
#         print(l,end="")
#     print()

# for i in range(3,0,-1):
#     for j in range(1,5-i):
#         print(" ",end="")
#     for k in range(1,i+1):
#         print(k,end="")
#     for l in range(i-1,0,-1):
#         print(l,end="")
#     print()
       

# 9. Pascal’s Triangle  
# Create Pascal’s triangle for a given number of rows N.  
# Example for N=4:  

#    1
#   1 1
#  1 2 1
# 1 3 3 1

# for i in range(1,5):
#     for j in range(1,5-i):
#         print(" ",end="")
#     for k in range(1,i+1):
#         if i == 1 or i == 2 or i == k or k == 1 :
#             print("1",end=" ")
#         else:
#             print(i-1,end=" ")
#     print()


# 10. Right-Angled Triangle with Decreasing Numbers  
# Generate a right-angled triangle where the numbers in each row start from the row number and decrement to 1.  
# Example for N=5:  

# 5
# 54
# 543
# 5432
# 54321


# 11. Diamond of Numbers  
# Create a full diamond pattern where the numbers increase in the upper half and mirror themselves in the lower half.  
# Example for N=4:  

#    1
#   121
#  12321
# 1234321
# 1234321
#  12321
#   121
#    1

#  SAME AS 8:

# for i in range(1,5):
#     for j in range(1,5-i):
#         print(" ",end="")
#     for k in range(1,i+1):
#         print(k,end="")
#     for l in range(i-1,0,-1):
#         print(l,end="")
#     print()

# for i in range(3,0,-1):
#     for j in range(1,5-i):
#         print(" ",end="")
#     for k in range(1,i+1):
#         print(k,end="")
#     for l in range(i-1,0,-1):
#         print(l,end="")
#     print()


# 12. Increasing Numbers in a Rectangle  
# Generate a rectangle where each row contains numbers starting from 1 and incrementing across the row.  
# Example for L=4, W=6:  

# 1 2 3 4 5 6
# 7 8 9 10 11 12
# 13 14 15 16 17 18
# 19 20 21 22 23 24

# PENDING


# 13. Numbered Hollow Right-Angled Triangle  
# Create a hollow right-angled triangle where the borders are numbers and the inside is empty.  
# Example for N=5:  

# 1
# 12
# 1 3
# 1  4
# 12345

# for i in range(1,6):
#     for j in range(1,i+1):
#         if i == 5 or j == 1 or i == j:
#             print(j,end="")
#         else:
#             print(" ",end="")
#     print()


# 14. Pyramid with Decreasing Numbers  
# Create a pyramid where the numbers in each row start from a higher number and decrease.  
# Example for N=4:  

#    4
#   434
#  43234
# 4321234


# 15. Zigzag Numbers in a Triangle

# Create a pattern where the numbers increase row by row, but the direction alternates for each row. For odd rows, print the numbers from left to right, and for even rows, print the numbers from right to left.
# Example for N=5:

# 1
# 2 3
# 6 5 4
# 7 8 9 10
# 15 14 13 12 11

# Hint:
# 1. Row-wise Traversal: Loop through each row from 1 to N.
# 2. Odd Rows: Print numbers from left to right in increasing order.
# 3. Even Rows: Print numbers from right to left in decreasing order.
# 4. Number Tracking: Use a variable to keep track of the next number to be printed in the pattern.

# n=1
# for i in range(1,6):
#     if i%2 == 0:
#         for j in range(1, i+1):
#             print(n,end=" ")
#             n+=1

#     else:
#         start = n+i-1
#         for j in range(i,0,-1):
#             print(start, end=" ")
#             start-=1
#     n+=i
#     print()

