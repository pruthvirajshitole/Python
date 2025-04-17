'''
1. Square of Stars 
Your school has been asked to create a square-shaped decorative pattern of stars for the annual event.
Write a program that generates a square pattern of size N x N.  
Example for N=5:  

*****
*****
*****
*****
*****
'''
# i=0
# while i<5:
#     j=0
#     while j<5:
#         print('*',end="")
#         j+=1
#     print()
#     i+=1


'''
2. Rectangle Pattern with Borders 
A magician wants to create a rectangular magical scroll with stars as borders and spaces inside.
Write a program to draw the rectangle with given dimensions L (length) and W (width).  
Example for L=5, W=4:  

*****
*   *
*   *
*   *
*****
'''

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


'''
3. Right-Angled Triangle of Numbers 
A group of hikers wants to create a flag with a right-angled triangle using numbers. Each row should start
from 1 and go up to the current row number. Create the pattern for a flag size of N.  
Example for N=4:  

1
12
123
1234
'''

# i = 1
# while i < 5:
#     j = 1
#     while j <= i:
#         print(j,end="")
#         j+=1
#     print()
#     i+=1
    

'''
4. Inverted Right-Angled Triangle of Stars 
An ancient puzzle involves an inverted right-angled triangle of stars. The top row has N stars, and each subsequent row has one star less. Write the code to reveal the puzzle.  
Example for N=5:  

*****
****
***
**
*
'''

# n = 5
# i=0
# while i<n:
#     j=0
#     while j<n-i:
#         print('*',end="")
#         j+=1
#     print()
#     i+=1

    
'''
5. Combined Pattern: Square Outside, Triangle Inside 
A wizard is designing a spell diagram with a square outline and a right-angled triangle inside it. Write a program to generate the pattern for size N.  
Example for N=5:  

*****
*1  *
*12 *
*123*
*****
'''
# i=0
# while i<5:
#    j=0
#    while j<5:
#       if i==0 or i==4 or j == 0 or j == 4:
#          print('*',end="")
#          n = 1
#       elif j <= i:
#          print(n,end="")
#          n+=1
#       else:
#          print(" ",end="")
#       j+=1
#    print()
#    i+=1


'''
6. Hollow Triangle Pattern 
A secret vault uses a hollow triangle pattern as its key. Generate a right-angled triangle pattern where only the borders are visible,
and the inside is empty.  
Example for N=5:  

*
**
* *
*  *
*****
'''
# i=0
# while i<5:
#     j=0
#     while j<=i:
#         if j == 0 or j == i or i == 4:
#             print('*',end="")
#         else:
#             print(" ",end="")
#         j+=1
#     print()
#     i+=1


'''
7. Checkerboard Rectangle 
A sports team needs a checkerboard pattern in a rectangular shape for their scoreboard. Alternate rows
start with stars and spaces. Write the program for a rectangle with dimensions L and W.  
Example for L=5, W=4:  

* * *
 * * 
* * *
 * * 
* * *
'''
# i=0
# while i<5:
#     j=0
#     while j<3:
#        if i==0 or i==2 or i==4 or j == 1 or j == 2:
#           print('*',end=" ")
#        else:
#           print(" ",end="")
#        j+=1
#     print()
#     i+=1


'''
8. Double-Layered Square 
An artist is drawing a double-layered square pattern with stars. Write a program that generates the pattern for size N.  
Example for N=5:  

*****
*   *
* * *
*   *
*****
'''
# i=0
# while i<5:
#     j=0
#     while j<5:
#         if i == 0 or i == 4 or j == 0  or j == 4 or i == 2 and j == 2:
#             print('*',end="")
#         else:
#             print(" ",end="")
#         j+=1
#     print()
#     i+=1


'''
9. Number Pyramid 
An old temple inscription has numbers arranged in a pyramid. Write a program to generate the pyramid for height N.  
Example for N=4:  

   1   
  1 2  
 1 2 3 
1 2 3 4
'''
# n = 5
# i=0
# while i<n:
#     j=0
#     while j<n-i:
#         print(" ",end="")
#         j+=1
#     k=1
#     while k<=i:

#         print(k,end=" ")
#         k+=1
#     print()
#     i+=1


'''
10. Mirrored Right-Angled Triangle 
An encrypted message contains a mirrored right-angled triangle of stars. Decode it by writing the program for N.  
Example for N=4:  

   *
  **
 ***
****
'''

# n = 4
# i=0
# while i<n:
#     j=0
#     while j<n-i:
#         print(" ",end="")
#         j+=1
#     k=0
#     while k<=i:
#         print("*",end="")
#         k+=1
#     print()
#     i+=1


'''
11. Diamond Inside a Square 
A gem-shaped diamond is drawn inside a square for a logo. Generate the pattern for a square of size N.  
Example for N=5:  

*****
* * *
* * *
* * *
*****
'''
# i=0
# while i<5:
#     j=0
#     while j<5:
#         if i == 0 or i == 4 or j == 0  or j == 4 or j == 2:
#             print('*',end="")
#         else:
#             print(" ",end="")
#         j+=1
#     print()
#     i+=1


'''
12. Hourglass of Stars 
A digital clock displays an hourglass pattern with stars. Write the program to generate the hourglass for size N.  
Example for N=5:  

*****
 ****
  ***
   **
    *
'''
# n=5
# i=0
# while i<n:
#     j=0
#     while j<i:
#         print(" ",end="")
#         j+=1
#     k=0
#     while k<n-i:
#         print("*",end="")
#         k+=1
#     print()
#     i+=1


'''
13. Zigzag Triangle 
A maze has a zigzag pattern that resembles a right-angled triangle. Write a program to generate the pattern for size N.  
Example for N=4:  

1
01
101
0101
'''
# i=0
# while i<4:
#     j=0
#     while j<=i:
#         if (i+j)%2 == 0:
#             print("1",end="")
#         else:
#             print("0",end="")
#         j+=1
#     print()
#     i+=1


'''
14. Staircase of Letters 
A letter staircase puzzle asks you to generate a staircase of alphabets up to row N. Each row repeats the same letter.  
Example for N=4:  

A
BB
CCC
DDDD

HINT:
(To print letters like A, B, C, etc., you can use their ASCII values. Each letter has a unique ASCII code. Here's how you can use them:

The ASCII value of A is 65.

To convert an ASCII value back to a character, use the chr() function.
Example:
print(chr(65))  # This prints 'A'
print(chr(66))  # This prints 'B' )
'''
# i=0
# while i<4:
#     j=0
#     k = 65+i
#     while j<=i:
#         print(chr(k),end="")
#         j+=1
#     print()
#     i+=1


'''
15. Nested Patterns: Rectangle Outside, Triangle Inside 
A piece of ancient artwork has a rectangle on the outside and a right-angled triangle of numbers inside it.
Write a program to generate the pattern for dimensions L and W.  
Example for L=5, W=4:  

*****
*1  *
*12 *
*123*
*****
'''

# i=0
# while i<5:
#    j=0
#    while j<5:
#       if i==0 or i==4 or j == 0 or j == 4:
#          print('*',end="")
#          n = 1
#       elif j <= i: 
#          print(n,end="")
#          n+=1
#       else:
#          print(" ",end="")
#       j+=1
#    print()
#    i+=1