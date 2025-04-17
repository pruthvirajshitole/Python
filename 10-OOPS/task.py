class User:
    
    def __init__(self):
        self.d = {}
    
    def register(self):
        name = input("Enter your name: ")
        password = input("Enter your password: ")

        if name not in self.d:
            self.d[name] = password
            print('Successfully Registered.')
        else:
            print('User already exist.')
        print(self.d)

    def login(self):
        name = input("Enter your name: ")
        password = input("Enter your password: ")

        for i,j in (self.d).items():
            if i == name:
                if j == password:
                    print('Successfuly logged in.')
                else:
                    print("Entered wrong password.")
                    break
            else:
                print('To login please register first.')
        
        if name not in self.d:
            print('To login please register first.')

u = User()
print('''
------Welcome------
1 - Register
2 - login
0 - Exit
-------------------
''')
n = 1
while n<=3:
    print(f'-----Attempt {n}-----')
    ch = input("Enter your choice: ")

    if ch == '1':
        u.register()
        n+=1

    elif ch == '2':
        u.login()
        n+=1

    elif ch == '0':
        print("Thank you!!!")
        break

    else:
        print("Your choice is INVALID!!!")
    