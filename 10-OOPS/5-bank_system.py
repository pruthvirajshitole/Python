print('---------bank_system-----------')
class Bank:
    def __init__(self,balance):
        self.bal=balance
    
    def check_balance(self):
        print(f'Balance: {self.bal}')

    def deposit(self):
        amount = float(input("Enter the amount to deposit: "))
        if amount>0:
            self.bal+=amount
            print(f'Balance: {self.bal}')
        else:
            print("Amount can't be negative.")

    def withdrawal(self):
        amount = float(input("Enter the amount to withdraw: "))
        if amount<=self.bal:
            self.bal-=amount
            print(f'Balance: {self.bal}')
        else:
            print('Insufficient amount')

b = Bank(1000)
b.check_balance()
b.deposit()
b.withdrawal()


print('---------bank_system with choice-----------')
class Bank:
    def __init__(self,balance):
        self.bal=balance
    
    def check_balance(self):
        print(f'Balance: {self.bal}')

    def deposit(self):
        amount = float(input("Enter the amount to deposit: "))
        if amount>0:
            if amount%100 == 0:
                self.bal+=amount
                print(f'Balance: {self.bal}')
            else:
                print("Only mulltiple of 100 can be deposited.")
        else:
            print("Amount can't be negative.")

    def withdrawal(self):
        amount = float(input("Enter the amount to withdraw: "))
        if amount<self.bal:
            if amount%100 == 0:
                self.bal-=amoun
                print(f'Balance: {self.bal}')
            else:
                print("Only mulltiple of 100 can be able to withdraw.")
        else:
            print('Insufficient amount')

b = Bank(1000)
print('''
--------Welcome---------
1-Check Balance
2-Deposit
3-Withdraw
0-Exit
-------------------------
''')

i = 1
while i<=4:
    ch = input("Enter you choice: ")
    print(f'-----{i}-----{4-i} attempts remaining.')
    if ch == '1':
        b.check_balance()
        i+=1
    elif ch == '2':
        b.deposit()
        i+=1
    elif ch == '3':
        b.withdrawal()
        i+=1
    elif ch == '0':
        print("Thankyou.")
        break
    else:
        print("Your choice is not listed.")
    pass





