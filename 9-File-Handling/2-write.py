# with- context manager

'''

Context Manager:

    A Context Manager in Python is an object that manages resources by defining 
    a runtime context. It ensures that resources like files, database connections, 
    and network sockets are properly acquired and released when no longer needed.

'''


print('--------w - write-----------')
with open('9-File-Handling/file1.txt','w') as file:
    file.write("welcome\nHello,\nI love Python.")


print('-------a - append-----------')
with open('9-File-Handling/file1.txt','a') as file:
    file.write("Good evening!!!")


print('-------writelines-----------')
with open('9-File-Handling/file1.txt','a') as file:
    file.writelines(['\nGood Morning\n','Good Afternoon\n','Good Night'])






