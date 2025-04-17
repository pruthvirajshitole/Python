# Q1.

# Create a Car class with encapsulated attributes to represent information about a car.
# The class should have the following attributes: make (string), model (string), year (integer),
# and mileage (float). Implement appropriate methods to retrieve and update each attribute while
# incorporating validation checks. Additionally, demonstrate how encapsulation principles are applied
# to restrict direct access to these attributes.

# 1. Implement the _init_ method to initialize the Car object with the specified attributes.
#    Ensure that the year is a positive integer and the mileage is a non-negative float.

# 2. Write methods (get_make, get_model, get_year, get_mileage) to retrieve the values of the attributes.

# 3. Write methods (set_make, set_model, set_year, set_mileage) to update the values of the attributes.
#    Include validation checks to ensure the correctness of the assigned values
#   (e.g., valid make and model strings, positive integer year, non-negative float mileage).

# 4. Create an instance of the Car class and demonstrate how to use the implemented methods
#    to interact with the object, emphasizing encapsulation.

# class Car:
#     def __init__(self,make,model,year,milage):
#         self.__make = make
#         self.__model = model
#         self.__year = year
#         self.__milage = milage
    
#     def get_make(self):
#         return self.__make
    
#     def set_make(self,make):
#         self.__make = make
    
#     def get_model(self):
#         return self.__model
    
#     def set_model(self,model):
#         self.__model = model
    
#     def get_year(self):
#         return self.__year
    
#     def set_year(self,year):
#         if isinstance(year,int) and year>0:
#             self.__year = year
#         else:
#             print(f'Year can not be negative.')
    
#     def get_milage(self):
#         return self.__milage
    
#     def set_milage(self,milage):
#         if isinstance(milage,float) and milage>0:
#             self.__milage = milage
#         else:
#             print(f'Milage can not be negative.')

# c = Car('Tata','Safari',-2000,23.5)
# print(f'''Make: {c.get_make()}
# Model: {c.get_model()}
# Year: {c.get_year()}
# Milage: {c.get_milage()}''')

# c.set_year(2024)
# print(c.get_year())


# Q2.

# Create a BankAccount class to represent a simple bank account.
# The class should have encapsulated attributes: account_number (string), account_holder (string), balance (float).
# Implement appropriate methods to retrieve and update each attribute while incorporating validation checks.
# Additionally, demonstrate how encapsulation principles are applied to restrict direct access to these attributes.

# 1. Implement the _init_ method to initialize the BankAccount object with the specified attributes.
# Ensure that the account_number is a unique string, account_holder is a non-empty string, and balance is a non-negative float.

# 2. Write methods (get_account_number, get_account_holder, get_balance) to retrieve the values of the attributes.

# 3. Write methods (set_account_holder, set_balance, deposit, withdraw) to update the values of the attributes.
# Include validation checks to ensure the correctness of the assigned values
# (e.g., valid account holder name, non-negative float balance).

# 4. Create an instance of the BankAccount class and demonstrate how to use the implemented methods
# to interact with the object, emphasizing encapsulation.

class BankAccount:
    def __init__(self,account_number,account_holder,balance):
        self.__account_number = account_number
        self.__account_holder = account_holder
        self.__balance = balance
    
    def get_account_number(self):
        return self.__account_number

    def get_account_holder(self):
        return self.__account_holder

    def get_balance(self):
        return self.__balance
    
    def set_account_holder(self, new_holder):
        if not new_holder or not isinstance(new_holder, str):
            print("Account holder name must be a non-empty string.")
        self.__account_holder = new_holder

    def set_balance(self, new_balance):
        if new_balance < 0 or not isinstance(new_balance, (int, float)):
            print("Balance must be a non-negative float.")
        self.__balance = float(new_balance)

    def deposit(self, amount):
        if amount <= 0:
            print("Deposit amount must be positive.")
        self.__balance += amount

    def withdraw(self, amount):
        if amount <= 0:
            print("Withdrawal amount must be positive.")
        if amount > self.__balance:
            print("Insufficient balance.")
        self.__balance -= amount

print('------Account Details-------')
c = BankAccount('9834878793636','Samay',1000)
print(f'''Account No.: {c.get_account_number()}
Account Holder: {c.get_account_holder()}
Balance: {c.get_balance()}''')

print('------Setting Details-------')
c.set_account_holder('Samay Raina')
c.set_balance(100000)
print(f'''Account No.: {c.get_account_number()}
Account Holder: {c.get_account_holder()}
Balance: {c.get_balance()}''')

print('------Deposit------')
c.deposit(5000)
print(f'Upadated Balance: {c.get_balance()}')

print('-----Withdraw------')
c.withdraw(55000)
print(f'Remaining Balance: {c.get_balance()}')