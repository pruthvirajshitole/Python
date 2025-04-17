# Q1) Check the given no by user is even or odd 

# n = int(input("Enter a number: "))
# if n%2 == 0:
#     print(f'{n} is even.')
# else:
#     print(f'{n} is odd.')


# Q2) Check the given no by user is divisible by 5 or not

# n = int(input("Enter a number: "))
# if n%5 == 0:
#     print(f'{n} is divisible by 5.')
# else:
#     print(f'{n} is not divisible by 5.')


# Q3) Check the given no by user is divisible by 5 and 10 or not


# n = int(input("Enter a number: "))
# if n%5 == 0 and n%10 == 0:
#     print(f'{n} is divisible by 5 and 10.')
# else:
#     print(f'{n} is not divisible by 5 and 10.')


# Q4) Check the given age by user is adult or not

# n = int(input("Enter your age: "))
# if n >= 18:
#     print("You are adult.")
# else:
#     print("You are not adult.")


# Q5) Check the given no by user is between 40 and 100 or not

# n = int(input("Enter a number: "))
# if n>=40 and n<=100 :
#     print(f'The given number {n} is between 40 and 100.')
# else:
#     print(f'The given number {n} is not between 40 and 100.')


# Q6) Print WOOW if score given by user is between 75 to 100 else BOO

# n = int(input("Enter a score: "))
# if n>=75 and n<=100:
#     print(f'The given score {n} is between 75 and 100.')
# else:
#     print(f'The given score {n} is not between 75 and 100..')


# Q7) Print Perfect if no 1 ;Good if no is between 0.9 to 0.6 ;Fine if 0.5;Poor if else than 0.5 and greater than 0    

# n = float(input("Enter a number: "))
# if n == 1:
#     print("Perfect")
# elif n>=0.6 and n<=0.9:
#     print("Good")
# elif n == 0.5:
#     print("Fine")
# else: 
#     print("Poor")


# Q8) Find the elder of two brothers Tim and Jim whose ages are given by user.

# tim = int(input("Enter the age of Tim: "))
# jim = int(input("Enter the age of Jim: "))

# if tim>jim:
#     print("Tim is elder.")
# elif jim>tim:
#     print("Jim is elder.")
# else:
#     print("Jim and Tim both are of same age.")


# Q9) Find the youngest of two sisters Ana and Mary whose ages are given by user.

# ana = int(input("Enter the age of Ana: "))
# mary = int(input("Enter the age of Mary: "))
# if ana>mary:
#     print("Mary is youngest.")
# elif ana<mary:
#     print("Ana is youngest.")
# else:
#     print("Both sisters are of same age.")


# Q10) Print the Grade of student for given percentage (A(75-100),B(60-75),C(50-60),D(40-50),F(s<40))

# n = float(input("Enter percentage of a student: "))
# if n>=75 and n<=100:
#     print("A")
# elif n>=60 and n<=74:
#     print("B")
# elif n>=50 and n<=59:
#     print("C")
# elif n>=40 and n<=49:
#     print("D")
# else:
#     print("F")


# Q11) Print the greatest of 3 nos given by user.

# a = int(input("Enter first number: "))
# b = int(input("Enter second number: "))
# c = int(input("Enter third number: "))

# if a>b and a>c :
#     print("a is greatest.")
# elif b>a and b>c:
#     print("b is greatest.")
# else:
#     print("c is greatest.") 


# Q12) Print the smallest of 3 nos given by user.(using nest conditionals(nested if-else))

# a = int(input("Enter first number: "))
# b = int(input("Enter second number: "))
# c = int(input("Enter third number: "))

# if a<b and a<c :
#     print("a is smallest.")
# elif b<a and b<c:
#     print("b is smallest.")
# else:
#     print("c is smallest.") 


# Q13) Check the temprature given by user is for which season
#      (spring(15-30 °C), summer(30+ °C), autumn(0-10 °C), and winter( 10–15 °C))

# t = int(input("Enter the temperature: "))
# if t>=15 and t<=29:
#     print("spring")
# elif t>=30:
#     pirnt("summer")
# elif t>=0 and t<=9:
#     print("autumn")
# elif t>=10 and t<=14:
#     print("winter")


# Q14) Jacob always choose the middle(favraoute) one of 3 nos given what will that no.
#      Ask Jacob to give three no and tell his favroute no.0


# a = int(input("Enter first number: "))
# b = int(input("Enter second number: "))
# c = int(input("Enter third number: "))

# if a>b and a<c or a<b and a>c:
#     print("a is Jacob's favourate no.")

# elif b>a and b<c or b<a and b>c:
#     print("b is Jacob's favourate no.")
# else:
#     print("c is Jacob's favourate no.")


# Q15) Alice is trying to find a no which is non negative and even and divisble by 3 given by 
#      Alice Tell Alice the no is right or not

# n = int(input("Enter a number: "))
# if n>0 and n%2==0 and n%3==0:
#     print("right no.")
# else:
#     print("Not a right no.")


# Q16) Write a program to print Yes if no which is odd and between 10 to 15 and divisible by 4 given by user

# n = int(input("Enter a number: "))
# if n%2 != 0 and n>10 and n<15 and n%4 == 0:
#     print("Yes")
# else:
#     print("No")


# Q17) Write a program to check the input nos. given by Jeff and Bob are same or not for same "Won" else "Lost"

# n1 = int(input("Enter a given by Jeff: "))
# n2 = int(input("Enter a given by Bob: "))
# if n1 == n2:
#     print("Won")
# else:
#     print("Lost")


# Q18) Create a program using nested if-else where the player chooses between "tea" or "coffee," 
#      and then chooses "hot" or "cold" to get a final drink suggestion.

# a = 'tea'
# b = 'coffe'
# c = input("if you want tea enter tea, and if coffe enter coffe: ")
# print(c)

# if c == 'tea':
#     h_t = 'hot'
#     c_t = 'cold'
#     d = input("if you want hot tea press hot, and if cold tea press cold: ")
#     if d == h_t:
#         print("Player choose hot tea")
#     else:
#         print("Player choose cold tea")
# else:
#     h_c = 'hot'
#     c_c = 'cold'
#     d = input("if you want hot coffe press hot, and if cold coffe press cold: ")
#     if d == h_c:
#         print("Player choose hot coffe")
#     else:
#         print("Player choose cold coffe")


# Q19) Write a program to print youngest middle and eldest of three Employees given by HR.

# a = int(input("Enter the age of first employee: "))
# b = int(input("Enter the age of second employee: "))
# c = int(input("Enter the age of third employee: "))


# if a>b and a>c:
#     eld = a
#     if b>c:
#         mid = b
#         young = c
#     else:
#         mid = c
#         young = b
# elif b>a and b>c:
#     eld = b
#     if a>c:
#         mid = a
#         young = c
#     else:
#         mid = c
#         young = a
# else:
#     eld = c
#     if a>b:
#         mid = a
#         young = b
#     else:
#         mid = b
#         young =a

# print(f'''
# eldest is: {eld}
# youngest is: {young}
# middle one is: {mid}
# '''
# )




# Q20) Write a Python program that takes the user's age and income as input and determines if they 
#      qualify for a loan based on these rules:

#    If the age is less than 18, print "Not eligible for a loan."
#    If the age is between 18 and 60:
#    If the income is less than 20,000, print "Eligible for a basic loan."
#    If the income is between 20,000 and 50,000, print "Eligible for a standard loan."
#    If the income is above 50,000, print "Eligible for a premium loan."
#    If the age is above 60:
#    If the income is less than 30,000, print "Eligible for a senior citizen basic loan."
#    If the income is 30,000 or more, print "Eligible for a senior citizen premium loan."

age = int(input("Enter user's age: "))
i = float(input("Enter user's income: "))

if age<18:
    print("Not eligible for a loan.")

elif age>= 18 and age<= 60:
    if i <= 20000:
        print("Eligible for a basic loan.")
    elif i>20000 and i<=50000:
        print("Eligible for a standard loan.")
    elif i>50000:
        print("Eligible for a premium loan.")

elif age>60:
    if i<30000:
        print("Eligible for a senior citizen basic loan.")
    elif i>=30000:
        print("Eligible for a senior citizen premium loan.")