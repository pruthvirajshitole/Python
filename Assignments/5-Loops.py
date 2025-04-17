# '''
# 1. Adventure Quest Input:  
# A hero in a game collects gold coins from three different treasure chests. The user inputs the number of coins in each chest.
# Calculate the total coins and determine if the hero collected more than 100 coins. If yes, print "Rich Hero," otherwise "Keep Searching." 
# '''
# coins = (input("Enter the number of coins in each chest: ").split(','))
# l = []

# for i in coins:
#     l.append(int(i))
# if sum(l) > 100:
#     print("Rich Hero")
# else:
#     print("Keep Searching")


# # 2. Time Traveler's Calculator:  
# # A time traveler sets the year he wants to visit (input by the user) and the current year. Calculate how many years are left for the traveler
# # to prepare for the journey and whether the year to visit is in the future or past.

# year = int(input("Enter the current year: "))
# visit_year = int(input("Enter the year you want to visit: "))

# if visit_year > year:
#     print(f"You have {visit_year - year} years to prepare for the future journey.")
# else:
#     print(f"You have {year - visit_year} to travel past in time.")


# # 3. Shopping List Comparison:  
# # A user buys items and inputs their prices one by one (3 inputs). Compare the first and last item's prices and check if the second item’s 
# # price is the median value. Print whether their shopping is "logical" or "random."  

# price1 = int(input("Enter the price of the first item: "))
# price2 = int(input("Enter the price of the second item: "))
# price3 = int(input("Enter the price of the third item: "))
# if ((price1+price3)/2) == price1:
#     print("Logical shopping")
# else:
#     print("Random shopping")


# # 4. Mystery of the Lost Password:  
# # A user creates a password by inputting their favorite number, favorite color (as a number like 1 for Red, 2 for Blue), and birth year.
# # Use operators to create a "password score" by combining these inputs and decide if the password score is greater than 5000.  

# number = int(input("Enter your favourate number: "))
# color = int(input("Enter your favorite color (1 for Red, 2 for Blue): "))
# year = int(input("Enter your birth year: "))
# password_score = (number + color + year) * 2
# if password_score > 5000:
#     print("Password is strong")
# else:
#     print("Password is weak")


# # 5. Rain Check:  
# # A weather app takes the percentage of rainfall chances for three days (user inputs). Check if any of the days have a rainfall chance
# # above 70% and print "Carry an umbrella."  

# day1 = int(input("Enter the rain chance for day 1: "))
# day2 = int(input("Enter the rain chance for day 2: "))
# day3 = int(input("Enter the rain chance for day 3: "))
# if day1 > 70 or day2 > 70 or day3 > 70:
#     print("Carry an umbrella.")
# else:
#     print("No need to carry an umbrella.")


# # 6. Fuel Efficiency Test:  
# # A car’s mileage is tested by entering the distance covered (in km) and the fuel consumed (in liters). Calculate the mileage and determine
# # if it is "Efficient" (above 20 km/l), "Moderate" (between 15 and 20 km/l), or "Inefficient" (below 15 km/l).  

# distance = int(input("Enter the distance travelled by the car: "))
# fuel = int(input("Enter the fuel consumed by the car: "))
# mileage = distance / fuel
# if mileage > 20:
#     print("Efficient")
# elif mileage >= 15 and mileage <= 20:
#     print("Moderate")
# else:
#     print("Inefficient")


# # 7. Age Verifier:  
# # The user inputs the age of three family members. Determine if all of them are adults (18 and above) or not, and print "All adults" or "Not all adults."  

# ages = input("Enter age of three members: ").split(',')
# for i in range(len(ages)):
#     ages[i] = int(ages[i])

# if ages[0]>=18 and ages[1]>=18 and ages[2]>=18:
#     print("All adults")
# else:
#     print("Not all adults")


# # 8. Weightlifting Challenge:  
# # A weightlifter lifts three weights in a day. The user enters the weights (in kg). Calculate the total weight lifted and determine if the weightlifter
# # qualifies for the "1000 kg Club" (total weight ≥ 1000 kg).  

# weights = input("Enter the weights lifted in a day: ").split(',')
# for i in range(len(weights)):
#     weights[i] = int(weights[i])

# total_weight = sum(weights)
# if total_weight >= 1000:
#     print("You qualify for the 1000 kg Club")
# else:
#     print("You don't qualify for the 1000 kg Club")


# # 9. Bank Account Problem:  
# # A user inputs their current account balance and three expenses for the week. Calculate the remaining balance and check if they overspent (balance < 0).
# # If so, print "Budget Exceeded," otherwise "Well Managed."  

# current_balance = int(input("Enter your current account balance: "))
# expenses = input("Enter three expenses for the week: ").split(',')

# for i in range(len(expenses)):
#     expenses[i] = int(expenses[i])

# total_expeses = sum(expenses)
# remaining_balance = current_balance - total_expeses

# if remaining_balance < 0:
#     print("Budget Exceeded")
# else:
#     print("Well Managed")


# # 10. The Number Riddle:  
# # The user thinks of a number and enters it. The program adds 5, multiplies by 3, subtracts 15, and divides by 3.
# # Check if the result is the same as the original number and print "True or False."  

# num = int(input("Enter a number: "))
# result = ((num + 5) * 3 - 15) / 3
# if result == num:
#     print("True")
# else:
#     print("False")


# # 11. Ticket Checker:  
# # A user enters the ticket prices for three movies they plan to watch. Calculate the average ticket price and check if it exceeds 150.
# # Print "Too expensive" or "Affordable fun."  

# prices = input("Enter the ticket prices for three movies: ").split(',')
# for i in range(len(prices)):
#     prices[i] = int(prices[i])

# total_price = sum(prices)
# average_price = total_price / len(prices)

# if average_price > 150:
#     print("Too expensive")
# else:
#     print("Affordable fun")


# # 12. Online Store Discount:  
# # A store offers a discount of 20% if the total purchase is above 500. A user enters the prices of three items.
# #  Calculate the total and apply the discount if applicable. Show the final price.  

# prices = input("Enter the prices of three items: ").split(',')
# for i in range(len(prices)):
#     prices[i] = int(prices[i])

# total_price = sum(prices)

# if total_price > 500:
#     discount = total_price * 0.2
#     final_price = total_price - discount
#     print(f"Final price: {final_price}")
# else:
#     print(f"Final price: {total_price}")


# # 13. Speed Analysis:  
# # The user inputs speeds of a vehicle (in km/hr) for three hours. Calculate the average speed and determine if the vehicle exceeded the speed
# # limit of 80 km/hr during any hour.  

# speed1 = int(input("Enter the speed for the first hour: "))
# speed2 = int(input("Enter the speed for the second hour: "))
# speed3 = int(input("Enter the speed for the third hour: "))

# average_speed = (speed1 + speed2 + speed3) / 3
# if average_speed > 80:
#     print("Exceeded speed limit")
# else:
#     print("Speed limit not exceeded")


# # 14. Temperature Evaluation:  
# # The user enters the temperatures of three cities. Determine the highest temperature, lowest temperature, and if all the temperatures are above 30 degrees.  

# temp1 = int(input("Enter the temperature for the first city: "))
# temp2 = int(input("Enter the temperature for the second city: "))
# temp3 = int(input("Enter the temperature for the third city: "))

# for i in range(3):
#     if temp1 > temp2 and temp1 > temp3:
#         highest_temp = temp1
#     elif temp2 > temp1 and temp2 > temp3:
#         highest_temp = temp2
#     else:
#         highest_temp = temp3
# print(f"The highest temperature is: {highest_temp}")

# for i in range(3):
#     if temp1 < temp2 and temp1 < temp3:
#         lowest_temp = temp1
#     elif temp2 < temp1 and temp2 < temp3:
#         lowest_temp = temp2
#     else:
#         lowest_temp = temp3
# print(f"The lowest temperature is: {lowest_temp}")

# if temp1 > 30 and temp2 > 30 and temp3 > 30:
#     print("All temperatures are above 30 degrees")
    

# # 15. Quiz Winner Check:  
# # Three participants score points in a quiz (input by the user). Calculate the highest score and print the winner's
# # name ("A," "B," or "C") based on their scores. If two or more have the same highest score, print "Tie"  

# scoreA = int(input("Enter the score for participant A: "))
# scoreB = int(input("Enter the score for participant B: "))
# scoreC = int(input("Enter the score for participant C: "))

# if scoreA > scoreB and scoreA > scoreC:
#     print("Participant A is the winner")
# elif scoreB > scoreA and scoreB > scoreC:
#     print("Participant B is the winner")
# elif scoreC > scoreA and scoreC > scoreB:
#     print("Participant C is the winner")
# elif scoreA == scoreB or scoreA == scoreC or scoreB == scoreC:
#     print("Tie")
# else:
#     print("All participants have the same score")



