'''
Comparsion Operators  (<,>,<=,>=,==,!=)
    To compare between values
    result always in True or False

'''

a = 5
b = 3

print(f"{a} > {b} = {a > b}") # True
print(f"{b} > {a} = {b > a}") # False

print(f"{a} < {b} = {a < b}") # False
print(f"{b} < {a} = {b < a}") # True

print(f"{a} == {b} = {a == b}") # False, equal to
print(f"{a} != {b} = {a != b}") # True, not equal

a = 3
b = 3
print(f"{a} == {b} = {a == b}") # True, equal to
print(f"{a} != {b} = {a != b}") # False, not equal

# <=, >=
x = 11
print(f"{x}<=11 : {x<=11}")  # checks x is less than or equal to 11
print(f"{x}<=12 : {x<12}")  # checks x is less than or equal to 12

print(f"{x}>=11 : {x>=11}")  # checks x is greater than or equal to 11
print(f"{x}>=12 : {x>=12}")  # checks x is greater than or equal to 12