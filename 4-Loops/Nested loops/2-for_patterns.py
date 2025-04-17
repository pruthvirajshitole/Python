print('-------Ex-1-------')
'''
* * * * 
* * * * 
* * * * 
* * * *
'''
for i in range(4):
    for j in range(4):
        print("*",end=" ")
    print()
    

print('-------Ex-2-------')
'''
* * * *
*     *
*     *
* * * *
'''
for i in range(4):
    for j in range(4):
        if i==0 or i==3 or j==0 or j==3:
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()


print('-------Ex-3-------')
'''
* 
* *   
*   * 
* * * *
'''
for i in range(4):
    for j in range(4):
        if i==3 or j==0 or j==i:
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()


print('-------Ex-4-------')
'''
* * * *(0,3)
*   *(1,2) 
*  *(2,1) 
* *(3,0)
*(0,1) 

'''
for i in range(5):
    for j in range(5):
        if i==0 or j==0 or i+j==4:
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()


print('-------Ex-5-------')
'''
      *
    * *  
  *   *  
* * * * 
'''

for i in range(4):
    for j in range(4):
        if i==3 or j==3 or i+j==3:
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()



print('-------Ex-6-------')

'''
   *
  * *  
 * * *  
* * * * 
'''
for i in range(4):
    for k in range(4-i):
        print(" ",end="")
    for j in range(i+1):
            print("*",end=" ")
    print()
