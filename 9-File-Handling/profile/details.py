'''
1 - create a empty text file

2- Write down your personal information in the file
Name:
Age:

3-Add last line in the file
Address:

4-Insert a line between age and address 
Qualification:

5-Insert a first line
My Profile:

6-Update line address to City:

7-Insert a last line "I am on Linkedin"
Delete the last line 

8-Add all the content in a new file Copy-Profile.txt

9-Delete the first file

'''

open('9-File-Handling/profile/profile.txt','w')

with open('9-File-Handling/profile/profile.txt','w') as f:
    f.writelines(['Name: Pruthviraj\n','Age: 22'])

f = open('9-File-Handling/profile/profile.txt','r')
print(f.read())


print('-------3------')

with open('9-File-Handling/profile/profile.txt','a') as file:
    file.write("\nAddress: Kolhapur")

f = open('9-File-Handling/profile/profile.txt','r')
print(f.read())


print('-------4------')

with open('9-File-Handling/profile/profile.txt','r') as file:
    lines=file.readlines()
print(lines)

lines.insert(2,'Qualification: B-tech\n')

with open('9-File-Handling/profile/profile.txt','w') as file:
    file.writelines(lines)

# reading file
file = open('9-File-Handling/profile/profile.txt','r')
print(file.read())


print('-------5------')

with open('9-File-Handling/profile/profile.txt','r') as file:
    lines=file.readlines()
print(lines)

lines.insert(0,'----My Profile----\n')

with open('9-File-Handling/profile/profile.txt','w') as file:
    file.writelines(lines)

# reading file
file = open('9-File-Handling/profile/profile.txt','r')
print(file.read())


print('-------6------')

with open('9-File-Handling/profile/profile.txt','r') as file:
    lines=file.readlines()
print(lines)

lines[-1] = 'City: Kolhapur'

with open('9-File-Handling/profile/profile.txt','w') as file:
    file.writelines(lines)

# reading file
file = open('9-File-Handling/profile/profile.txt','r')
print(file.read())


print('-------7------')

with open('9-File-Handling/profile/profile.txt','r') as file:
    lines = file.readlines()
print(lines)

with open('9-File-Handling/profile/profile.txt','a') as file:
    file.write("\nI am on Linkedin")

f = open('9-File-Handling/profile/profile.txt','r')
print(f.read())

# delete last line

with open('9-File-Handling/profile/profile.txt','r') as file:
    lines = file.readlines()
print(lines)

lines.pop(-1)

with open('9-File-Handling/profile/profile.txt','w') as file:
    file.writelines(lines)

# # reading file
file = open('9-File-Handling/profile/profile.txt','r')
print(file.read())



print('-------8------')

with open('9-File-Handling/profile/profile.txt','r') as file:
    lines = file.readlines()
print(lines)

with open('9-File-Handling/profile/profile_copy.txt','w') as file:
    file.writelines(lines)


print('-------9------')

f = open('9-File-Handling/profile/profile_copy.txt','r')
f.close()

import os
os.remove('9-File-Handling/profile/profile.txt')