
print('-------r-mode-----------')
file = open('9-File-Handling/file1.txt','r')
print(file.read())


print('-------readline()-----------')
with open('9-File-Handling/file1.txt','r') as file:
    line=file.readline()
    print(line)


print('-------readlines()-----------')
with open('9-File-Handling/file1.txt','r') as file:
    lines=file.readlines()
    print(lines)

for x in lines:
    print(x)



# append 'Welcome' in first line in file1.txt
print('---------add content in the beginning----------')

with open('9-File-Handling/file1.txt','r') as file:
    content=file.readlines()
    print(content)
cont = ''
for i in content:
    cont+=i

with open('9-File-Handling/file1.txt','w') as file:
    file.write("Welcome\n"+cont)