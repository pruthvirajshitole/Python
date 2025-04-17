print('------Ex-1------')
i=0
while i<5:
    j=0
    while j<5:
        print('*',end=" ")  # continue next print in same line with space
        j+=1
    print()     # creates new line
    i+=1

# i creates row, j creates column
# for each i j run 0-4
# end=" " to continue in same line
# after completion of inner while we have to write print() to create new line

'''
i        j         print("*", end=" ")
---------------------------------------
0    0,1,2,3,4        * * * *
1    0,1,2,3,4        * * * *
2    0,1,2,3,4        * * * *
3    0,1,2,3,4        * * * *
4    0,1,2,3,4        * * * *

'''


print('------Ex-2------')
'''
* * *
* * *
* * *
* * *
* * *
'''
i=0
while i<3:
    j=0
    while j<5:
        print('*',end=" ")
        j+=1
    print()     
    i+=1


print('------Ex-3------')
'''
* * * *
* * * *
* * * *
* * * *
'''

i=0
while i<4:
    j=0
    while j<4:
        print('*',end=" ")
        j+=1
    print()
    i+=1


print('------Ex-4------')
'''
0 0 0 0
1 1 1 1
2 2 2 2
3 3 3 3
'''
i=0
while i<4:
    j=0
    while j<4:
        print(i,end=" ")
        j+=1
    print()
    i+=1


print('------Ex-5------')
'''
0 1 2 3
0 1 2 3
0 1 2 3
0 1 2 3
'''
i=0
while i<4:
    j=0
    while j<4:
        print(j,end=" ")
        j+=1
    print()
    i+=1


print('------Ex-6------')
'''
0 1 2 3
4 5 6 7
8 9 10 11
12 13 14 15
'''
k=0
i=0
while i<4:
    j=0
    while j<4:
        print(k,end=" ")
        k+=1
        j+=1
    print()
    i+=1


print('------Ex-7------')
'''
 *
 * *
 * * *
 * * * *
 '''

i=0
while i<4:
    j=0
    while j<=i:
        print('*',end=" ")
        j+=1
    print()
    i+=1


print('------Ex-8------')
'''
0 
1 1 
2 2 2 
3 3 3 3 
 '''

i=0
while i<4:
    j=0
    while j<=i:
        print(i,end=" ")
        j+=1
    print()
    i+=1


print('------Ex-9------')
'''
0 
0 1 
0 1 2 
0 1 2 3
 '''

i=0
while i<4:
    j=0
    while j<=i:
        print(j,end=" ")
        j+=1
    print()
    i+=1


print('------Ex-10------')
'''
0 
1 2 
3 4 5 
6 7 8 9 
 '''

k=0
i=0
while i<4:
    j=0
    while j<=i:
        print(k,end=" ")
        k+=1
        j+=1
    print()
    i+=1


print('------Ex-11------')
'''
* * * *
*     *
*     *
* * * *
'''

i=1
while i<5:
   j=1
   while j<5:
      if i==1 or i==4 or j==1 or j==4:
         print('*',end=" ")
      else:
         print(" ",end=" ")
      j+=1
   print()
   i+=1


print('------Ex-12------')
'''
* * * *
* *   *
*   * *
* * * *

'''
i=0
while i<4:
    j=0
    while j<4:
        if i == 0 or i == 3 or j == 0 or j == 3 or i == j:
            print('*',end=" ")
        else:
            print(" ",end=" ")
        j+=1
    print()
    i+=1


print('------Ex-13------')
'''
 *
 * *
 *   *
 * * * *
 '''

i=0
while i<4:
    j=0
    while j<=i:
        if j == 0 or j == i or i == 3:
            print('*',end=" ")
        else:
            print(" ",end=" ")
        j+=1
    print()
    i+=1


print('------Ex-14------')
'''
 * * * *
 * * *
 * *
 * 
 '''

n = 4
i=0
while i<n:
    j=0
    while j<n-i:
        print('*',end=" ")
        j+=1
    print()
    i+=1


print('------Ex-15------')
'''
0 0 0 0
1 1 1
2 2
3
 '''

n = 4
i=0
while i<n:
    j=0
    while j<n-i:
        print(i,end=" ")
        j+=1
    print()
    i+=1


print('------Ex-16------')
'''
0 1 2 3 
0 1 2 
0 1 
0
 '''

n = 4
i=0
k = 0
while i<n:
    j=0
    while j<n-i:
        print(j,end=" ")
        k+=1
        j+=1
    print()
    i+=1


print('------Ex-17------')
'''
0 1 2 3 
4 5 6 
7 8 
9 
 '''

n = 4
i=0
k = 0
while i<n:
    j=0
    while j<n-i:
        print(k,end=" ")
        k+=1
        j+=1
    print()
    i+=1


print('------Ex-18------')
'''
 * * * *
 *   *
 * *
 * 
 '''

n = 4
i=0
while i<n:
    j=0
    while j<n-i:
        if i == 0 or j == 0 or i+j == n-1:
            print("*",end=" ")
        else:
            print(" ",end=" ")
        j+=1
    print()
    i+=1



print('------Ex-19------')
'''
      *
    * *
  * * *
* * * *
 '''

n = 4
i=0
while i<n:
    j=0
    while j<n-i:
        print(" ",end=" ")
        j+=1
    k=0
    while k<=i:
        print("*",end=" ")
        k+=1
    print()
    i+=1


print('------Ex-20------')
'''
    * 
   * * 
  * * * 
 * * * * 
'''

n=4
i=0
while i<n:
    j=0
    while j<n-i:
        print(" ",end="")
        j+=1
    k=0
    while k<=i:
        print("*",end=" ")
        k+=1
    print()
    i+=1


print('------Ex-21------')
'''
      *
    * *
  *   *
* * * *
 '''
# PENDING
n = 4
i=0
while i<n:
    j=0
    while j<n-i:
        print(" ",end=" ")
        j+=1
    k =0
    while k<=i:
        print("*",end=" ")
        if i==2 and j==2:
            print(" ",end=" ")
        k+=1
    print()
    i+=1


