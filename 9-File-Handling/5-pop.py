
# read the content of file
with open('9-File-Handling/file1.txt','r') as file:
    lines=file.readlines()

# delete the content / pop the line; lines is a list here
lines.pop(3)


# override the content to add the inserted data in the file
with open('9-File-Handling/file1.txt','w') as file:
    file.writelines(lines)

# read the changes
file=open('9-File-Handling/file1.txt','r')
print(file.read())

