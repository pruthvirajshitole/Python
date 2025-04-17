
# else must have if
# else have no condition
# if can have only one else

a = 5
b = 3
if a>b:
    print("a is greater than b")
else:
    print("b is greater than a")

if a<b:
    print("a is smaller than b")
else:
    print("b is smaller than a")


age = int(input("Enter your age: "))
if age >= 18:
    print("You are eligible for voting")
else:
    print("You are not eligible for voting")


# 1-Take score from user and check in which grade he/she is in pass or fail

print('-----------1------------')
score = int(input("Enter your score: "))
if score>=40:
    print("you are pass")
else:
    print("you are fail")


# 2-Check the given age by user is correct or not

print('-----------2------------')
age = int(input("Enter your age: "))
if age>0:
    print("Entered age is correct")
else:
    print("Entered age is incorrect")


# 3-Check the user input is 100 tell him 'woow' or for other 'boo'

print('-----------3------------')
num = input("Enter any input: ")
if num == "100":
    print('woow')
else:
    print('boo')


# 4-check the user input is number

print('-----------4------------')
num = input("Enter any number: ")
if num is str:
    print("You entered a string")
else:
    print("You have entered a number")


# 5-Check the user input is in the range of 18 to 100 tell hi other are for other bye

print('-----------5------------')
num = int(input("Enter any number: "))
if 18 <= num <= 100:
    print("Hello")
else:
    print("Bye")