def bank():
    pin = '0000'
    balance = 0

    def deposit():
        nonlocal balance
        deposit_amount = float(input("Enter the amount to deposit: "))
        balance += deposit_amount
        print(f'Your deposit of {deposit_amount} is successful.')
    
    def withdraw():
        nonlocal balance
        atm_pin = input("Enter your pin: ")
        if atm_pin == pin:
            withdraw_amount = int(input("Enter the amount you wanted to withdraw: "))
            if withdraw_amount<=balance:
                balance -= withdraw_amount
                print(f'Your withdrawal of amount {withdraw_amount} is successful.')
            else:
                print("You don't have sufficient balance.")
        else:
            print('Incorrect pin entered!!!')
    
    def balance_check():
        atm_pin = input("Enter your pin: ")
        if atm_pin == pin:
            print(f'Available total balance is: {balance}')
        else:
            print('Incorrect pin entered!!!')

    return deposit,withdraw,balance_check

deposit,withdraw,balance_check = bank()

