# 1. Hollow Square

# Write a program to generate a hollow square of stars for a given size N.  
# Example for N=5:  
# *****
# *   *
# *   *
# *   *
# *****

# i=0
# while i<5:
#     j=0
#     while j<5:
#        if i==0 or i==4 or j == 0 or j == 4:
#           print('*',end="")
#        else:
#           print(" ",end="")
#        j+=1
#     print()
#     i+=1


# 2. Rectangle with Alternating Borders

# Create a rectangle where the borders alternate between * and #.  
# Example for L=6, W=4:  

# *#*#*#
# *    *
# *    *
# *#*#*#

# i=0
# while i<4:
#     j=0
#     while j<6:
#        if i==0 or i==3:
#          if j%2==0:
#             print('*',end="")
#          else:
#             print("#",end="")
#        elif j==0 or j==5:
#            print("*",end="")
#        else:
#            print(" ",end="")
#        j+=1
#     print()
#     i+=1


# 3. Right-Angled Triangle of Stars

# Write a program to print a right-angled triangle of stars for a given size N.  
# Example for N=4:  

# *
# **
# ***
# ****

# i=0
# while i<4:
#     j=0
#     while j<=i:
#         print('*',end="")
#         j+=1
#     print()
#     i+=1


# 4. Inverted Right-Angled Triangle of Numbers

# Generate an inverted right-angled triangle pattern where each row contains numbers starting from 1.  
# Example for N=4:  

# 1234
# 123
# 12
# 1

# n = 5
# i=1
# while i<n:
#     j=1
#     while j<n-i+1:
#         print(j,end="")
#         j+=1
#     print()
#     i+=1


# 5. Combined Square and Triangle

# Create a square of size N where a right-angled triangle of stars is embedded inside.  
# Example for N=5:  

# *****
# *1  *
# *12 *
# *123*
# *****

# i=0
# while i<5:
#     j=0
#     while j<5:
#          if i==0 or i==4 or j == 0 or j == 4:
#              print('*',end="")
#          elif j<=i:
#               print(j,end="")
#          else:
#               print(" ",end="")
#          j+=1
#     print()
#     i+=1


# 6. Triangle inside a Rectangle

# Generate a rectangle of dimensions L and W, with a right-angled triangle pattern inside it.  
# Example for L=6, W=5:  

# ******
# *1   *
# *12  *
# *123 *
# *1234*
# ******

# i=0
# while i<6:
#     j=0
#     while j<6:
#          if i==0 or i==5 or j == 0 or j == 5:
#              print('*',end="")
#          elif j<=i:
#               print(j,end="")
#          else:
#               print(" ",end="")
#          j+=1
#     print()
#     i+=1


# 7. Mirrored Right-Angled Triangle

# Write a program to create a mirrored right-angled triangle pattern of stars.  
# Example for N=4:  

#    *
#   **
#  ***
# ****

# i=0
# n=4
# while i<4:
#     j=0
#     while j<n:
#         if j<n-i-1:
#             print(" ",end="")
#         else:
#             print("*",end="")
#         j+=1
#     print()
#     i+=1


# 8. Double-Layered Square 

# Create a square pattern where the inner and outer borders are filled with stars.  
# Example for N=5:  

# *****
# *   *
# * * *
# *   *
# *****

# i=0
# while i<5:
#     j=0
#     while j<5:
#         if j==0 or j==4 or i==0 or i==4 or i==j and i+j==4:
#             print('*',end="")
#         else:
#             print(' ',end="")
#         j+=1
#     print()
#     i+=1


# 9. Diamond inside a Square

# Generate a square of size N with a diamond shape of stars in the center.  
# Example for N=5:  

# *****
# * * *
# * * *
# * * *
# *****

# i=0
# while i<5:
#     j=0
#     while j<5:
#         if j==0 or j==4 or i==0 or i==4 or j==2:
#             print('*',end="")
#         else:
#             print(' ',end="")
#         j+=1
#     print()
#     i+=1


# 10. Right-Angled Triangle with Borders Only  
# Write a program to generate a hollow right-angled triangle where only the borders are stars.  
# Example for N=5:  

# *
# **
# * *
# *  *
# *****

# i=0
# while i<5:
#     j=0
#     while j<5:
#         if j==0 or i==4 or i==j:
#             print('*',end="")
#         else:
#             print(' ',end="")
#         j+=1
#     print()
#     i+=1


# 11. Square with Inverted Triangle Inside

# Create a square pattern with an inverted right-angled triangle of numbers embedded inside.  
# Example for N=5:  

# *****
# *123*
# *12 *
# *1  *
# *****

# i=0
# n=5
# while i<5:
#     j=0
#     while j<5:
#         if i==0 or i==4 or j==0 or j==4:
#             print('*',end="")
#         elif j<n-i:
#             print(j,end="")
#         else:
#             print(" ",end="")
#         j+=1
#     print()
#     i+=1


# 12. Rectangle with Mirrored Triangle Inside

# Generate a rectangle where a mirrored right-angled triangle is embedded inside.  
# Example for L=6, W=4:  

# ****** 
# *   *
#  *  *
#   ***
# ******

# i=0
# while i<5:
#     j=0
#     while j<6:
#         if i==0 or i==4 or j==4:
#             print("*",end="")
#         elif i-j==1 or i==3 and j==3:
#             print("*",end="")
#         else:
#             print(" ",end="")
#         j+=1
#     print()
#     i+=1


# 13. Staircase Pattern in a Rectangle

# Write a program to create a rectangle where each row contains a right-angled triangle pattern of stars.  
# Example for L=5, W=4:  

# *    
# **   
# ***  
# **** 
# *****  

# i=0
# while i<5:
#     j=0
#     while j<5:
#         if j<=i:
#             print("*",end="")
#         else:
#             print(" ",end="")
#         j+=1
#     print()
#     i+=1


# 14. Hollow Inverted Right-Angled Triangle

# Generate a hollow inverted right-angled triangle of stars.  
# Example for N=5:  

# ***** (0,0) (0,1) (0,2) (0,3) (0,4)
# *  *  (1,0) (1,1) (1,2) (1,3) (1,4)
# * *   (2,0) (2,1) (2,2) (2,3) (2,4)
# **    (3,0) (3,1) (3,2) (3,3) (3,4)
# *     (4,0) (4,1) (4,2) (4,3) (4,4)

# i=0
# n=5
# while i<5:
#     j=0
#     while j<5:
#         if j==0 or i==0:
#             print("*",end="")
#         elif i+j==4:
#             print("*",end="")
#         else:
#             print(" ",end="")
#         j+=1
#     print()
#     i+=1


# 15. Combined Pattern: Square and Triangle Borders

# Create a square of size N with a triangle border inside it.  
# Example for N=5:  

# *****
# *   *
# * * *
# *   *
# *****

# i=0
# while i<5:
#     j=0
#     while j<5:
#         if j==0 or j==4 or i==0 or i==4 or i==j and i+j==4:
#             print('*',end="")
#         else:
#             print(' ',end="")
#         j+=1
#     print()
#     i+=1
