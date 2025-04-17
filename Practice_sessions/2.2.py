# 1. A student needs to know if they passed their exam. Write a program that checks their score and prints "Pass"
# if it is 40 or more, otherwise "Fail."  

# n = float(input("Enter score of a student: "))
# if n>=40:
#     print("Pass")
# else:
#     print("Fail")


# 2. A store gives a 10% discount if the purchase is above $100 and a 20% discount if it is above $200.
# Write a program to calculate the final bill after applying the discount. 
 
# p = int(input("Enter the cost of purchase: "))
# bill = p
# if p>=100:
#     bill = bill-bill*(0.1)
# elif p>=200:
#     bill = bill-bill*(0.2)
# print(f'final bill is: {bill}')


# 3. A movie theater offers different ticket prices: $10 for children, $15 for adults, and $12 for seniors.
# Write a program to calculate the ticket price based on the age of the customer.
  
# age = int(input("Enter age: "))
# if age<=14:
#     print("$10 for children.")
# elif age>=60:
#     print("$12 for seniors.")
# else:
#     print("$15 for adults.")


# 4. A farmer wants to check if a crop needs watering. If the temperature is above 30°C and humidity is below 40%,
# print "Water Needed," otherwise print "No Water Needed." 

# t = float(input("Enter temp: "))
# h = int(input("Enter humidity: "))
# if t>30 and h<40:
#     print("Water needed.")
# else:
#     print("No Water Needed.")


# 5. Write a program to classify a number as positive, negative, or zero.  

# n = int(input("Enter a number: "))
# if n>0:
#     print("Number is positive.")
# elif n<0:
#     print("Number is negative.")
# else:
#     print("zero")


# 6. A company gives bonuses based on years of service: 5% for less than 5 years, 10% for 5-10 years,
# and 20% for more than 10 years. Write a program to calculate the bonus.

# yr = int(input("Enter years of service: "))
# s = 30000
# if yr<=5:
#     s += s*(0.1)
#     print(f"Your bonus is 5% of your salary, which is {s}.")
# elif yr>5 and yr<10:
#     s += s*(0.1)
#     print(f"Your bonus is 10% of your salary, which is {s}.")
# else:
#     s += s*(0.2)
#     print(f"Your bonus is 20% of your salary which is {s}.")


# 7. A travel agency offers discounts on train tickets: 5% for students, 10% for senior citizens,
# and no discount otherwise. Write a program to calculate the final ticket price.

# age = int(input("Enter your age: "))
# ticket = 300
# if age>=18 and age<60:
#     ticket -= ticket*(0.05)
#     print(f'Yor are a student and your ticket is: {ticket}')
# elif age>=60:
#     ticket -= ticket*(0.1)
#     print(f'Yor are a senior citizen and your ticket is: {ticket}')
# else:
#     print(f"Yor are not eligible for discount and your ticket is: {ticket}")


# 8. A food delivery app charges $5 for delivery. If the order amount is above $50,
# delivery is free. Write a program to calculate the total cost.

# t = int(input("Enter amount order: "))
# cost = t
# if t>=50:
#     print(f'The total amount of order including delivery is: {cost}')
# else:
#     cost += 5
#     print(f'The total amount of order including delivery is: {cost}')


# 9. Write a program to check if a year is a leap year. A year is a leap year if it is divisible
# by 4 but not divisible by 100, except if it is divisible by 400.

# yr = int(input("Enter the year: "))
# if yr%4 == 0:
#     if yr%100 == 0:
#         if yr%400 == 0:
#             print(f'{yr} is a leap year.')
#         else:
#             print(f'{yr} is not a leap year.')
#     else:
#         print(f'{yr} is a leap year.')
# else:
#     print(f'{yr} is not a leap year.')


# 10. A car rental service charges $20 per day. If the customer rents for more than 7 days, they get a $50 discount.
# Write a program to calculate the total rental cost.

# rent = 20
# days = int(input("Enter the number of days of rental service consumed: "))
# total_rent = 0
# if days>7:
#     total_rent = (rent*days)-50
# else:
#     total_rent = rent*days
# print(f'Total rent is: {total_rent}')


# 11. A gym offers membership discounts: 10% for students, 15% for teachers, and no discount otherwise.
# Write a program to calculate the membership fee.  

# fee = 2000
# role = input("Enter the your occupation: ")

# if role == 'student':
#     applicable_fee = fee-(fee*0.1)
# elif role == 'teacher':
#     applicable_fee = fee-(fee*0.15)
# else:
#     applicable_fee = fee

# print(f'Your memebership fee is: {applicable_fee}')


# 12. A bank offers loans at different interest rates: 5% for loans under $50,000,4% for loans between
# $50,000 and $100,000, and 3% for loans above $100,000. Write a program to calculate the interest amount. 

# loan = float(input("Enter the amount of loan you wanted: "))
# if loan<50000:
#     i = (loan/100)*4
# elif loan>=50000 and loan<100000:
#     i = (loan/100)*4
# elif loan>=100000:
#     i = (loan/100)*3
# print(f'Total interest is: {i}')

 
# 13. A restaurant categorizes its menu based on cuisine: Indian, Italian, or Chinese.
# Write a program that asks the user for their choice and prints the respective menu.  

# indian = ['Chicken','Fish','Mutton Biryani','Kolhapuri Thali']
# italian = ['Chicken Parmigiana','Spaghetti alle Vongole','Bistecca alla Fiorentina']
# chinese = ['Chicken Noodles','Chiken tikka','Chicken fries']

# order = input("Enter type of food you want to order: ")

# if order == 'indian':
#     print(f'Menu of Indian food: {indian}')
# elif order == 'italian':
#     print(f'Menu of Italian food: {italian}')
# elif order == 'chinese':
#     print(f'Menu of Chinese food: {chinese}')


# 14. Write a program to check if a person is eligible to vote. The minimum voting age is 18 years.

# age = int(input("Enter your age: "))

# if age>=18:
#     print("You are eligible to vote.")
# else:
#     print("You are not eligible to vote.")


# 15. A person wants to buy a mobile phone. If the phone's price is within their budget,
# print "Affordable," otherwise print "Expensive."  

# mobile_price = 30000
# budget = float(input("Enter your budget: "))
# if mobile_price>budget:
#     print("Expensive")
# else:
#     print("Affordable")


# 16. A grading system assigns grades based on marks: A for 90 and above, B for 80-89, C for 70-79,
# D for 60-69, and F for below 60. Write a program to determine the grade.  

# marks = int(input("Enter the marks of student: "))
# if marks>=90:
#     print("A")
# elif marks>=80 and marks<=89:
#     print("B")
# elif marks>=70 and marks<=79:
#     print("C")
# elif marks>=60 and marks<=69:
#     print("D")
# else:
#     print("F")


# 17. Write a program to check if a triangle is equilateral, isosceles, or scalene based on the lengths of its three sides.
  
# a = int(input("Enter first side of triangle: "))
# b = int(input("Enter second side of triangle: "))
# c = int(input("Enter third side of triangle: "))

# if a == b == c:
#     print("Equilateral triangle.")
# elif a == b or b == c or a == c:
#     print("Isosceles triangle.")
# else:
#     print("Scalene triangle.")


# 18. A weather app categorizes the weather as "Cold" if the temperature is below 15°C,"Warm" if it is
# between 15°C and 25°C, and "Hot" if it is above 25°C. Write a program to determine the weather.  

# temp = int(input("Enter the temperature: "))
# if temp<=15:
#     print("Cold")
# elif temp > 15 and temp<=25:
#     print("Warm")
# else:
#     print("Hot")
2

# 19. A library charges a late fee of $1 per day for the first 5 days, $2 per day for the next 5 days,
# and $5 per day after 10 days. Write a program to calculate the fine based on the number of late days.  

# late = int(input("Enter the number of late days: "))
# charge = 1
# if late<=5:
#     charge *= late
# elif late>5 and late<=10:
#     charge = (5*charge)+(2*(late-5))
# else:
#     charge = (5*charge)+(2*5)+(late*5)
# print(f'total chages are: {charge}$')


# 20. A company offers a salary increment based on performance ratings: 20% for "Excellent," 10% for "Good,"
# and no increment for "Average." Write a program to calculate the new salary.

salary  = 30000
performance = input("Enter the performance of employee: ")

if performance == 'Excellent':
    salary += salary*0.2
elif performance == 'Good':
    salary += salary*0.1
elif performance == 'Average':
    salary = salary
print(f"Your new salary is: {salary}")