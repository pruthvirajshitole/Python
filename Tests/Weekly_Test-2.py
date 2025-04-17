# Section A: Theory (10 Questions)
'''
1. How does Python handle input from the user and what precautions should be taken while using it?  
Ans: Python handles user input with the help of built-in function such as input().
Precautions : Always check the type of input such as int, float and string before using it.

2. Explain how slicing can be used to extract specific portions of a string or list.  
Ans: Slicing is useful to extract only the required part or portion from a string or list. It works on the concept of indexes .
It is only used where the variable is ordered.

3. What happens if you mix if-elif-else conditions with logical operators inappropriately?  
Ans: Mixing if-elif-else conditions with logical operators inappropriately will throgh unexpected errors or incorrect results.

4. How do you determine whether a variable in Python is mutable or immutable?  
Ans: Try to mutate the variable if it throughs errors it will be immutable otherwise it is mutable.

5. What is the difference between using input() to receive a string versus converting it into another data type?  
Ans: The input() function always returns a string. If you want to get other data types, you need to convert it using functions 
like int(), float(), etc.

6. Describe a scenario where nested conditionals would simplify decision-making in a program.  
Ans: Nested conditionals are useful when you have to make a decision based on multiple conditions.
Ex: When there are three brothers with different ages and you want to now who is the oldest, youngest and middle one.

7. How does the not operator behave when combined with a loop condition?  
Ans: The not operator is used to describe negative the condition of a loop. It will loop until the condition is false.

8. Why is it important to validate user input before performing operations like slicing or type conversion?  
Ans: It is important to validate user input before performing operations like slicing or type conversion because it prevents
 unexpected errors. 

9. How do conditionals interact with loops, and what are potential pitfalls?  
Ans: Conditionals interact with loops by controlling the loop execution. Potential pitfalls are infinite loops and unexpected errors.

10. What are the implications of using the wrong slicing indices for a list or string?
Ans: The implications of using the wrong slicing indices for a list or string are unexpected errors or incorrect results.

'''


#  Section B: Correct the Code (10 Questions)  
     
# num = int(input("Enter a number: "))  
# if num % 2 == 0:
#     print("Even number")    
     
# text = "Python Programming"  
# print(text[:7:]) 
     


     
# age = int(input("Enter your age: "))  
# if age > 18:
#     print("You are an adult")  
# else:
#     print("You are a minor")  
     

     
# data = ["apple", "banana", "cherry"]  
# for fruit in data:
#       if "a" in fruit:
#           print(fruit)  
     

  
# num = 10  
# while num > 0 :
#     print(num)  
#     num -= 1  

 
     
# name = input("Enter your name: ")
# if len(name) > 5 and len(name) < 10:
#      print("Moderate length name")  
# elif len(name) >= 10:
#      print("Long name")
# else:
#      print("Short name")
     


# sentence = "Python is great"  
# words = sentence.split()  
# print("Total words: ", len(words))  
     

 
     
# score = int(input("Enter your score: "))  
# if score >= 90:
#       print("A grade")  
# elif score >= 75:
#       print("B grade")  
# else:
#      print("C grade")  
     

     
# list_data = [10, 20, 30, 40]  
# print(list_data[2:4:1])  


#  Section C: Write Code For (10 Questions)

# # 1. Write a program that asks the user for a string and checks if the string contains any numeric characters.
# # If it does, print their positions in the string. 

# s = input("Enter a string: ")
# for i in range(len(s)):
#     if s[i].isdigit():
#         print(f"Digit {s[i]} found at position {i+1}")
    

# # 2. Create a program that accepts a username and password, and only allows access if both are correct. Allow three attempts.  

# username = "Codenera"
# password = "1234"
# attempts = 0
# while attempts < 3:
#     user = input("Enter your username: ")
#     passw = input("Enter your password: ")
#     if user == username and passw == password:
#         print("Access granted")
#         break
#     else:
#         attempts += 1
#         print(f"Access denied. {3-attempts} attempts remaining")

# 3. Write a program that takes a list of 5 integers from the user and prints only the odd numbers in reverse order.  

# num = list(int(input("Enter 5 numbers: ")))
# odd_num = []
# for i in range(len(num)):
#     if num[i] % 2 != 0:
#         odd_num.append(num[i])
# print(odd_num)


# 4. Ask the user for a string, then slice and display the string without the first and last characters. Check if the resulting string contains any vowels.  

# string = input("Enter a string: ")
# string = string[1:-1]
# print(string)
# for i in string:
#     if i.lower() in 'aeiou':
#         print(f"String contains a vowel: {i}")


# 5. Create a program where the user provides their name and favorite number. If the number is divisible by 3 or 5, print the reversed name; otherwise, print the name in uppercase.  

# name = input("Enter your name: ")
# num = int(input("Enter your favorite number: "))
# if num % 3 == 0 or num % 5 == 0:
#     print(name[::-1])
# else:
#     print(name.upper())


# 6. Write a program that accepts an input string and splits it into words. For each word, check if it starts and ends with the same letter. Print such words.  

# 7. Take a string as input and slice it into two halves. Check if the first half has more vowels than the second half.  

string = input("Enter a string: ")
half = len(string) // 2
first_half = string[:half]
second_half = string[half:]
for i in first_half:
    if i.lower() in 'aeiou':
        count += 1
        print(count)

# 8. Write a program that takes a list of strings and prints only those that have an odd length and contain the letter a.  

# 9. Take a sentence as input and count how many words in the sentence have their first and last characters as vowels.  

# Here’s the updated version where the player provides a list of character information:  

# 10.You are working on a game. The player provides their character information as a list in this format:  
# ["Name:Hero", "Level:15", "Weapon:Sword", "Energy:80"]  
# - Extract the name and level from the list.  
# - If the level is above 10, print "Advanced Player."  
# - If the energy is less than 50, print "Low Energy Warning." 
# - Otherwise, print "Player Ready."

