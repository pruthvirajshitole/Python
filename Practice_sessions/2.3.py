# 1.  Write a program to check if a given character is a vowel, a consonant,
# or neither (e.g., numbers or special characters) using nested if-else statements. 

# vowels = 'aeiouAEIOU'
# consonants = 'bcdfghjklmnpqrstvwxyzBCDFGHJKLMNPQRSTVWXYZ'

# s = input("Enter a character: ")
# if s in vowels:
#     print("It's a vowel.")
# elif s in consonants:
#     print("It's a consonant.")
# else:
#     print("It's neither a vowel nor a consonant.")
    


# 2.  Write a program to check in which quadrant a point (x, y) lies, or if it is on the X-axis, Y-axis, or the origin.

# x = int(input("Enter x: "))
# y = int(input("Enter y: "))

# if x>0 and y>0:
#     print("The point is in 1st quadrant.")
# elif x<0 and y>0:
#     print("The point is in 2nd quadrant.")
# elif x<0 and y<0:
#     print("The point is in 3rd quadrant.")
# elif x>0 and y<0:
#     print("The point is in 4th quadrant.")
# elif x==0 and y!=0:
#     print("The point is on Y-axis.")
# elif x!=0 and y==0:
#     print("The point is on X-axis.")
# elif x==0 and y==0:
#     print("The point is on the origin.")


# 3.  Write a program to classify a given angle as acute, right, obtuse, or straight using if-elif-else. 

# angle = float(input("Enter an angle: "))
# if angle>180:
#     angle=360-angle
#     if angle<90 and angle>0:
#         print("It's an acute angle.")
#     elif angle==90:
#         print("It's a right angle.")
#     elif angle>90 and angle<180:
#         print("It's a obtuse angle.")
#     elif angle==180 or angle==0:
#         print("It's a straight line.")
# elif angle<90 and angle>0:
#     print("It's an acute angle.")
# elif angle==90:
#     print("It's a right angle.")
# elif angle>90 and angle<180:
#     print("It's a obtuse angle.")
# elif angle==180 or angle==0:
#     print("It's a straight line.")


# 4.  Write a program to calculate the income tax based on the income entered by the user, using the following tax slabs:
#     Income up to ₹2,50,000: No tax
#     Income between ₹2,50,001 and ₹5,00,000: Tax rate is 5%
#     Income between ₹5,00,001 and ₹10,00,000: Tax rate is 20%
#     Income above ₹10,00,000: Tax rate is 30%

# income = float(input("Enter your income: "))

# if income<=250000:
#     print("No tax")
# elif income>250000 and income<=500000:
#     tax = income-(income*0.05)
#     print(f'your tax is: {tax}')
# elif income>500001 and income<=1000000:
#     tax = income-(income*0.2)
#     print(f'your tax is: {tax}')
# else:
#     tax = income-(income*0.3)
#     print(f'your tax is: {tax}')


# 5. Write a program that categorizes the input temperature (in degrees Celsius) into one of the following:
# Freezing: Below or equal to 0°C
# Cold: Greater than 0°C and less than 10°C
# Warm: Greater than or equal to 10°C and less than 25°C
# Hot: Greater than or equal to 25°C

# temp = float(input("Enter the temperature: "))
# if temp<=0:
#     print("Freezing")
# elif temp>0 and temp<10:
#     print("Cold")
# elif temp>=10 and temp<25:
#     print("Warm")
# else:
#     print("Hot")


# 6. Write a program where the user inputs the weather condition (e.g., "sunny", "rainy", "snowy"). Based on the input,
# suggest an activity:
# If it's sunny, suggest going for a picnic.
# If it's rainy, suggest staying indoors and reading a book.
# If it's snowy, suggest building a snowman.

# w = input("Enter the weather condition (e.g., sunny, rainy, snowy): ")
# if w == 'sunny':
#     print("it's sunny, suggest going for a picnic.")
# elif w == 'rainy':
#     print("it's rainy, suggest staying indoors and reading a book.")
# elif w == 'snowy':
#     print("it's snowy, suggest building a snowman.")
# else:
#     print("Your input is not valid.")


# 7. Write a program that asks the user for their destination (e.g., "beach", "mountains", "city").
# Based on the destination, suggest what to pack:
# If they choose the beach, suggest sunscreen and swimwear.
# If they choose the mountains, suggest hiking boots and warm clothing.
# If they choose the city, suggest comfortable walking shoes and a camera.

# w = input("Choose a destination (e.g., beach, mountains, city): ")
# if w == 'beach':
#     print("You have to carry sunscreen and swimwear.")
# elif w == 'mountains':
#     print("You have to carry hiking boots and warm clothing.")
# elif w == 'city':
#     print("You can carry comfortable walking shoes and camera.")
# else:
#     print("Your input is not valid.")


# 8. Holiday Activity Planner: Based on the day of the week, decide the activity:
# Monday–Friday: Go to work.
# Saturday: Go shopping.
# Sunday: Relax at home.
# Write a program that takes the day of the week as input and prints the planned activity.

# day = input("Enter the day: ")
# if day == 'Sunday':
#     print("Relax at home.")
# elif day == 'Saturday':
#     print("Go shopping.")
# else:
#     print("Go to work.")


# 9. Write a program that suggests a meal based on the time of day entered by the user (e.g., "morning", "afternoon", "evening", "night").
# If the input is morning, suggest having breakfast.
# If it's afternoon, suggest having lunch.
# If it's evening, suggest a light snack.
# If it's night, suggest having dinner.

# t_day = input("Enter the time of day such as morning, afternoon, evening, night: ")
# if t_day=='morning':
#     print("It's your breakfast.")
# elif t_day=='afternoon':
#     print("It's your lunch.")
# elif t_day=='evening':
#     print("It's time to have a light snack.")
# elif t_day=='night':
#     print("It's your dinner.")
# else:
#     print("Your input is not valid.")


# 10. Age Group Classification:
# Write a program to classify a person based on their age:
# 0–12 years: Child
# 13–19 years: Teenager
# 20–59 years: Adult
# 60+ years: Senior Citizen

# age = int(input("Enter your age: "))
# if age>0 and age<=12:
#     print("Child")
# elif age>12 and age<19:
#     print("Teenager")
# elif age>19 and age<60:
#     print("Adult")
# elif age>=60:
#     print("Senior Citizen")
# else:
#     print("Your input is not valid.")


# 11. Traffic Light System:  A traffic light changes color:
# Green: Proceed.
# Yellow: Slow down.
# Red: Stop.
# Write a program that takes the traffic light color as input and prints the action.

# color = input("Enter the color of traffic light: ")
# if color=='Green':
#     print("Proceed.")
# elif color=='Yellow':
#     print("Slow down.")
# elif color=='Red':
#     print("Stop.")
# else:
#     print("Your input is not valid.")


# 12. Bank ATM Withdrawal
#  An ATM must process withdrawals:
# Check if the withdrawal amount is a multiple of 100.
# Check if the withdrawal amount exceeds the account balance.
# Otherwise, allow the withdrawal.
# Task: Write a program to handle these conditions.

# account_balance = 10000
# amt = float(input("Enter the amount wanted to withdraw: "))
# if amt%100 == 0:
#     print("The withdrawal amount is a multiple of 100.")
#     if amt>account_balance:
#         print("Insufficient balance.")
#     else:
#         account_balance -= amt
#         print(f'''
# Your withdrawal is successful.
# Total available balance: {account_balance}
#          ''')
# else:
#     print("You can withdraw only multiples of 100.")


# 13. Fitness Plan: A fitness coach recommends exercises:
# If the user’s BMI is above 25, recommend weight loss exercises.
# If the user’s BMI is between 18.5 and 25, recommend maintaining their current routine.
# If the user’s BMI is below 18.5, recommend gaining muscle mass.
# Write a program that takes the user's BMI as input and prints the recommendation.

# bmi = float(input("Enter you BMI: "))
# if bmi>=25:
#     print("Weight loss exercises recommended.")
# elif bmi>=18.5 and bmi<25:
#     print("Maintaining their current routine is recommended.")
# elif bmi<18.5:
#     print("Gaining muscle mass is recommended.")
# else:
#     print("Your input is not valid.")


# 14.  Password Strength Checker A password is considered strong if:
# Its length is at least 8 characters.
# It contains both uppercase and lowercase letters.
# It has at least one digit.
# If it satisfies all criteria, print Strong Password.
# If any criteria fail, print which criteria failed.

s = input("Enter the password: ")
l = False
s_upper = False
s_lower = False
s_digits = False
for i in s:
    if l<8:
        l = True
    elif i in s.upper():
        s_upper = True
    elif i in s.lower():
        s_lower = True
    elif i in s.isdigit():
        s_digits = Trlue
if l==True and s_upper==True and s_lower==True and s_digits==True:
    print("Strong Password.")
else:
    print("Weak Password.")
    if l==False:
        print("Password is too short.")
    elif s_upper==False:
        print("Password must contain atleast one uppercase letter.")
    elif s_lower==False:
        print("Password must contain atleast one lowercase letter.")
    elif s_digits==False:
        print("Password must contain at least one digit.")


# 15. Password Validator 
# A user is trying to log in. The program must:
# Check if the username is correct.
# If the username is correct, check the password.
# If the username is incorrect, display an error message.
# Task: Write a program to validate the username and password using nested if.

# user_name = 'pruthvi2003'
# password = '@Pruthvi1234'

# user = input("Enter user name: ")

# if user == user_name:
#     user_pass = input("Enter user password: ")
#     if password == user_pass:
#         print("Login is successful.")
#     else:
#         print("Password is incorrect.")
# else:
#     print("You entered incorrect user name.")


# 16. Student Result Analysis: Given a student’s scores in three subjects:
# Check if the student passed:
# A subject is passed if the score is ≥ 35.
# The student must pass all subjects to be declared Pass.
# If the student passed, check:
# If the average score is ≥ 90, print Distinction.
# If the average is between 60 and 89, print First Class.
# Otherwise, print Second Class.
# If the student failed in any subject, print Fail.

# s1 = int(input("Enter first subject's marks: "))
# s2 = int(input("Enter second subject's marks: "))
# s3 = int(input("Enter third subject's marks: "))

# if s1>=35 and s2>=35 and s3>=35:
#     print("The student is Passed in all subjects.")
#     avg = (s1+s2+s3)/3
#     if avg>=90:
#         print("Passed with Distinction.")
#     elif avg>=60 and avg<90:
#         print("Passed with First Class.")
#     else:
#         print("Passed with Second Class.")
# else:
#     print("student is Failed in any subject.")


# 17.  Car Loan Eligibility: 
#  A car loan eligibility system checks:
# If the person is employed:
# If the annual salary is more than ₹5,00,000, they are Eligible.
# Otherwise, check if they have a guarantor.
# If yes, they are Eligible with guarantor.
# If no, they are Not eligible.
# If the person is unemployed, they are Not eligible.

# role = input("Enter if you are employed, YES or NO : ")
# if role == 'YES':
#     salary = float(input("Enter your annual salary: "))
#     if salary>500000:
#         print("You are eligible for car loan.")
#     else:
#         guarantor = input("If you have a guarantor enter YES else NO : ")
#         if guarantor == 'YES':
#             print("You are eligible for car loan.")
#         else:
#             print("You are Not eligible for car loan.")
# else:
#     print("You are Not eligible for car loan.")


# 18.  Quiz Scoring System: A quiz competition scores participants based on:
# If the participant’s score is greater than 90, they win a Gold medal.
# If the score is between 75 and 90:
# Check if they answered all bonus questions correctly:
# If yes, they win a Silver medal.
# Otherwise, a Bronze medal.
# If the score is below 75, print Better luck next time.

# score = int(input("Enter the score of participant: "))
# if score>90:
#     print("Participant win the Gold medal.")
# elif score>75 and score<=90:
#     que = input("If you answered all bonus questions correctly enter YES else NO :")
#     if que == 'YES':
#         print("The participant win a Silver medal.")
#     else:
#         print("The participant win a Bronze medal.")
# else:
#     print("Better luck next time.")


# 19. Write a program to calculate electricity bills based on the following:
# If the total consumption (units) is less than 100, charge ₹5 per unit.
# If the consumption is between 100 and 300:
# The first 100 units are charged at ₹5 per unit.
# The remaining units are charged at ₹7 per unit.
# If the consumption exceeds 300:
# The first 100 units are charged at ₹5 per unit.
# The next 200 units are charged at ₹7 per unit.
# Any units above 300 are charged at ₹10 per unit.
# Finally, add a fixed surcharge of ₹50 to the total bill.

# unit = float(input("Enter the total consumption of electricity in units: "))
# bill = 0
# if unit<=100:
#     bill = unit*5
# elif unit>100 and unit<=300:
#     bill = 500+(unit-100)*7
# elif unit>300:
#     bill = 500+1400+(unit-300)*10
# bill += 50
# print("Total bill including service charge is: ",bill)


# 20. Write a program to determine the grade of steel based on three properties (hardness, carbon content, tensile strength)
# using nested if-else.  
# A steel grade is determined by the following conditions:
# If the hardness > 50, carbon content < 0.7, and tensile strength > 5600, grade is 10.
# If only the first two conditions are met, grade is 9.
# If the first and last conditions are met, grade is 8.
# If only the last two conditions are met, grade is 7.
# If none of the conditions are met, grade is 6.







