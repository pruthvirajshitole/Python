# 1. Print numbers from 1 to 10 using a while loop.  

# i = 0
# while i<=10:
#     print(i)
#     i+=1


# 2. Print all even numbers between 1 and 20 using a while loop. 

# i = 1
# while i<=20:
#     if i%2==0:
#         print(i)
#     i+=1


# 3. Find the sum of numbers from 1 to 50 using a while loop. 

# i = 1
# sum = 0
# while i<=50:
#     sum+=i
#     i+=1
# print(sum)

 
# 4. Print the multiplication table of 5 using a while loop. 
 
# i = 1
# k = 1
# while i<=50:
    
#     if i%5==0:
#         print(f'{k}*5={i}')
#         k+=1
#     i+=1


# 5. Reverse a given string using a while loop.

# s = input("Enter a string: ")
# i = 1
# rev = ''
# while i<len(s)+1:
#     rev+=s[-i]
#     i += 1
# print(rev)
    

# 6. Print the first 10 natural numbers using a for loop and range().  

# for i in range(1,11):
#     print(i)


# 7. Print all odd numbers from 1 to 15 using a for loop and range(). 

# for i in range(1,16,2):
#     print(i)


# 8. Calculate the factorial of a number using a for loop and range().

# n = int(input("Enter a number: "))
# fact = 1
# for i in range(1,n+1):
#     fact *= i
# print(fact)

  
# 9. Print the square of numbers from 1 to 10 using a for loop and range(). 

# for i in range(1,11):
#     print(i**2)


# 10. Generate a list of the first 10 multiples of 3 using a for loop and range().  

# l = []
# for i in range(1,11):
#     if i%3==0:
#         l.append(i)
# print(l)


# 11. Iterate over a list of names and print each name using a for loop.  

# l = ['Lucifer', 'Chloe', 'Linda', 'Dan']
# for i in l:
#     print(i)


# 12. Find the sum of all elements in a list using a for loop. 

# l = [1,2,3,4,5,6,7,8,9]
# sum = 0
# for i in l:
#     sum += i
# print(sum)


# 13. Print only the vowels from a given string using a for loop. 

# vowels = 'aeiouAEIOU'
# s = input("Enter a string: ")
# for i in s:
#     if i in vowels:
#         print(i)


# 14. Count the occurrences of a specific character in a string using a for loop.

# s = input("Enter a string: ")
# c = input("Enter a specific char: ")
# count = 0
# for i in s:
#     if i == c:
#         count+=1
# print("Total count is: ",count)


# 15. Print all keys of a dictionary using a for loop.

# d = {1:'Virat',2:'Rohit',3:'Rahul',4:'Dhobi'}
# for i in d.keys():
#     print(i)


# 16. Print all values of a dictionary using a for loop.  

# d = {1:'Virat',2:'Rohit',3:'Rahul',4:'Dhobi'}
# for i in d.values():
#     print(i)


# 17. Iterate over a list of tuples and print each tuple's elements using a for loop.  

# l = [(1,2),(3,4),(5,6,7)]
# for i in l:
#     for j in i:
#         print(j)


# 18. Iterate over a list of numbers and print "even" for even numbers and "odd" for odd numbers.  

# l = [1,2,3,4,5,6,7,8,9]

# for i in l:
#     if i%2 == 0:
#         print(i,": even")
#     else:
#         print(i,": odd")


# 19. Print the reverse of a given list using a for loop.

# l = [1,2,3,4,5,6,7,8,9]
# r = []
# for i in l:
#     r.insert(0,i)
# print(r)

  
# 20. Check if a given word is a palindrome using a for loop.

# s = input("Enter a word: ")
# p = ''
# for i in s[::-1]:
#     p+=i
# if s == p:
#     print("It's a palindrome.")
# else:
#     print("It's not a palindrome.")