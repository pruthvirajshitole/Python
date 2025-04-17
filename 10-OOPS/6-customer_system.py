# Task Instructions:  
# - Implement the Customer class using OOP principles.  
# - Create an instance of Customer and update its details using the provided methods.  
# - Ensure that customer details are modifiable but customer_id should remain unchanged.  
# ---
#  Expected Output Example:  
#  Input:  
# 1. Create a customer:  
#    - ID: 101  
#    - Name: John Doe  
#    - Email: john@example.com  
#    - Phone: 9876543210  
#    - Address: New York  
# 2. Update customer details:  
#    - Change email to "john.doe@newmail.com"  
#    - Change phone to "9998887776"  
#    - Change address to "Los Angeles"  
# 3. Display updated customer details  
#  Output:  
# Customer ID: 101  
# Name: John Doe  
# Email: john.doe@newmail.com  
# Phone: 9998887776  
# Address: Los Angeles


class Customer:
    def __init__(self):
        self.id = 101
        self.name = input("Enter customer name: ")
        self.mail = input("Enter customer mail: ")
        self.num = input("Enter customer phone: ")
        self.add = input("Enter customer address: ")

    def details(self):
        print(f'''
Customer details
id: {self.id}
name: {self.name}
mail: {self.mail}
phone: {self.num}
address: {self.add}   
''')

    def update_details(self):
        print(f'''choose to update:
1-name
2-mail
3-phone
4-address''')
        i = 1
        while i<5:
            ch = input("Enter your choice: ")
            if ch == '1':
                self.name = input("Enter customer name: ")
                i+=1
            elif ch == '2':
                self.mail = input("Enter customer mail: ")
                i+=1
            elif ch == '3':
                self.num = input("Enter customer phone: ")
                i+=1
            elif ch == '4':
                self.add = input("Enter customer address: ")
                i+=1
            else:
                print("Entered wrong choice.")
                break
        print(f'''
Updated details
id: {self.id}
name: {self.name}
mail: {self.mail}
phone: {self.num}
address: {self.add}   
''')

c1 = Customer()
c1.details()
c1.update_details()
