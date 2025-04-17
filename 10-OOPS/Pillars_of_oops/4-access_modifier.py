'''
Access Modifier/ Access Specifier:
    Controls the accesesibility of the class members(attributes,methods)

Types:
1-public    : access by everyone
2-protected : access by the same class and child classes
3-private   : access by the same class only

'''

class A:
    def __init__(self,a,b,c):
        self.a = a     # public
        self._b =b     # protected
        self.__c = c   # private

    def get_c(self):
        return self.__c

    def _protected_method(self):
        print("I am protected method of A.")

    def __private_method(self):
        print("I am private method of A.")
    
    def access_private(self):
        self.__private_method()

class B(A):
    def show(self):
        print('----Accessing through child class----')
        self._b
        self._protected_method()


x = A(2,3,5)
print('Public attribute: ',x.a)
print('Protected attribute: ',x._b)

# print('Private attribute: ',x.__c)
# AttributeError: 'A' object has no attribute '__c'

print('Private attribute: ',x._A__c)

'''
name mangling is a mechanism used to avoid name conflicts in classes, 
particularly when dealing with inheritance. 
It is applied to attributes that have two leading 
underscores (__) but no trailing underscores.

'''

print('------Accessing private attribute using method--------')
print('Accessing private attribute using method: ',x.get_c())


print('------Accessing protected method using method--------')
x._protected_method()

# x.__private_method()
# AttributeError: 'A' object has no attribute '__private_method'.

print('------Accessing private method using method(from child class)--------')
x.access_private()

y = B(1,2,3)
print(y._b)
y.show()
y._protected_method()