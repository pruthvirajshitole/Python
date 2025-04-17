# for elif there must be a if
# there can one or more elif
# use to check multiple conditions after if

age = 3
if age>18:
    print("Can vote")
elif age == 18:
    print("Try next year")
else:
    print("Can't vote")


# 1-take 3 brothers ages as input and tell who is eldest

print('-----------1------------')
alice_age = int(input("Enter your alice_age: "))
bob_age = int(input("Enter your bob_age: "))
jef_age = int(input("Enter your jef_age: "))

if alice_age > bob_age and alice_age > jef_age:
    print("Alice is the eldest")
elif bob_age > alice_age and bob_age > jef_age:
    print("Bob is the eldest")
elif (alice_age == bob_age) and (jef_age < alice_age and jef_age < bob_age):
    print("Alice and Bob are the eldest")
elif (bob_age == jef_age) and (alice_age < bob_age and alice_age < jef_age):
    print("Bob and Jef are the eldest")
elif (alice_age == jef_age) and (bob_age < alice_age and bob_age < jef_age):
    print("Alice and Jef are the eldest")
elif (alice_age == bob_age == jef_age):
    print("all are equal")
else:
    print("Jef is the eldest")


# 2-take 3 brothers ages as input and tell who is youngest

print('-----------2------------')
a = int(input("Enter age of Virat: "))
b = int(input("Enter age of Rohit: "))
c = int(input("Enter age of Dhoni: "))

if a < b and a < c:
    print("Virat is the youngest")
elif b < a and b < c:
    print("Rohit is youngest")
else:
    print("Dhoni is the youngest")


# 3-take 3 brothers ages as input and tell who is middle one

print('-----------3------------')
a = int(input("Enter age of rehman: "))
b = int(input("Enter age of rahim: "))
c = int(input("Enter age of karim: "))

if (a < b and a > c) or (a > b and a < c):
    print("rehman is the middle one")
elif (b < a and b > c) or (b > a and b < c):
    print("rahim is the middle one")
elif (c < a and c > b) or (c > a and c < b):
    print("karim is the middle one")
elif a == b == c:
    print("All are equal")
else:
    print("No middle one")



