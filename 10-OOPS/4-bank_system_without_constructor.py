# create Bank class to check balance, deposit and withdrawal using OOPS.

class Bank:
    balance = 1000

    def check_balance(self):
        print(f'Available balance: {self.balance}')

    def deposit(self):
        d = float(input("Enter the amount to deposit: "))
        if d%100==0:
            self.balance += d
        else:
            print("You can deposit only in multiples of 100.")
    
    def withdrawal(self):
        w = float(input("Enter the amount to withdrawal: "))

        if w<=self.balance:
            if w%100!=0:
                print("You can deposit only in multiples of 100.")
            else:
                self.balance -= w
                print(f'Withdrawal of {w} is successful!!!')
        else:
            print("Your balance is not sufficent to withdrawal")

b = Bank()

print(f'''-----Welcome To Bank-----
1 - Check Balance
2 - Deposit
3 - Withdrawal
0 - Exit
-------------------------
''')

n = 1
while n<=3:
    print(f'Attempt {n}')
    ch = input("Pick any one from above options: ")
    if ch == '1':
        b.check_balance()
        n+=1
    elif ch == '2':
        b.deposit()
        n+=1
    elif ch == '3':
        b.withdrawal()
        n+=1
    elif ch == '0':
        print('Happy Banking!!!')
        break
    else:
        print("Your choice is not listed.")




