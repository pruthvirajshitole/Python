'''
Encapsulation: 
    Wrapping/binding/bundling of method and attribute in one class.
    - Encryption
'''

class Details:
    def __init__(self,name,age):
        self.__name = name
        self.__age = age

    def get_name(self):
        return self.__name

    def get_age(self):
        return self.__age     

    def set_name(self,name):
        self.__name = name
    
    def set_age(self,age):
        if age>0:
            self.__age=age
        else:
            print("Age can't be negative.")
    
print('--------getter_method()-------')
d = Details('Tom',33)
print('Name:',d.get_name())
print('Age:',d.get_age())


print('--------setter_method()-------')
name = input("Enter new name: ")
age = int(input("Enter age: "))
d.set_name(name)
d.set_age(age)
print('Name:',d.get_name())
print('Age:',d.get_age())


'''
1. Private Attributes:

__name and __age are private attributes (indicated by the double underscore __ prefix).
These cannot be accessed directly from outside the class, ensuring the data is hidden and secure.


2. Controlled Access:

The get_name() and get_age() methods provide controlled access to the private attributes.
This is the only way to retrieve the values of __name and __age.
 

3. Controlled Modification:

The set_name() and set_age() methods allow controlled modification of private attributes.
For example, in set_age(), a validation check ensures that the age cannot be set to a negative value.


4. Data Security and Integrity:

By restricting direct access to the attributes and using setter methods with validation,
the program maintains data integrity and prevents invalid updates.

'''
print('--------employee-------')

# Create a class Employee with attribute name ,age salary,designation
# desgination(senior engg for salary >30000 else junior engg)

class Employee:
    def __init__(self,name,age,salary,role):
        self.__name = name
        self.__age = age
        self.__salary = salary
        self.__role = role
    
    def get_name(self):
        return self.__name

    def get_age(self):
        return self.__age

    def get_salary(self):
        return self.__salary
    
    def get_role(self):
        return self.__role

    def set_name(self,name):
        self.__name = name

    def set_age(self,age):
        self.__age = age

    def set_salary(self,salary):
        if salary<0:
            print('Salary cant be negative.')
            return
        self.__salary = salary
        if salary<30000:
            self.__role = 'Junior Engg.'
        else:
            self.__role = 'Senior Engg.'

e1 = Employee('tom',22,30000,'Junior Engg.')
print(e1.get_name())
print(e1.get_age())
print(e1.get_salary())
print(e1.get_role())

e1.set_name('Lucifer')
print(e1.get_name())

e1.set_salary(40000)
print(e1.get_salary())
print(e1.get_role())

e2 = Employee('Omkar',40,50000,'Senior Engg.')
print(e2.get_name())
print(e2.get_age())
print(e2.get_salary())
print(e2.get_role())

