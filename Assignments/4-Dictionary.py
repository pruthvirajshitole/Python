
'''
1. Shopping List Validator:  
Write a program where the user enters a list of items they plan to buy, separated by commas.
Then, take another input asking if they want to "add" or "replace" an item. Depending on
the input, update the list and print the updated version. Ensure the input is handled in a way 
that only valid operations are allowed.
'''
print('''
Welcome to the Shop:
      Our Products are:
      Jeans 
      T-Shirts
      Shirts
      Shoes
''')

items = list(input("Enter your product from the above list:").split(', '))
  
print(f'''
    Your items:{items}
    1-Add
    2-Replace
''')

ch = input("Enter your choice:")
if ch=="1":
    a=input("Enter your new product:")
    items.append(a)
    print(items)

elif ch=="2":
    c=input("Choose the product to replace:")
    d=input("Enter your new product:")
    index=items.index(c)
    items[index]=d
    print(items)


'''
2. Nested Dictionary Tracker:  
Create a nested dictionary representing a library. Each book has a title (key) and details (a dictionary with author and year).
Ask the user to input a title and display its author. If the book doesn't exist, print "Book not found."
'''
library = {
    "To Kill a Mockingbird": {"author": "Harper Lee", "year": 1960},
    "1984": {"author": "George Orwell", "year": 1949},
    "Pride and Prejudice": {"author": "Jane Austen", "year": 1813},
    "The Great Gatsby": {"author": "F. Scott Fitzgerald", "year": 1925},
}

title = input("Enter the title of book: ")
if title in library:
    print(f"Author of {title}: {library[title]['author']}")
else:
    print("Book not found.")


'''
3. Tuple and Dictionary Cross:  
Take a tuple as input from the user (containing two elements). Use the tuple as a key to update a dictionary where
the value is a string provided by the user. Print the dictionary after the update.
'''
tup = tuple(input("Enter two elements separated by comma: ").split(','))
dict = {}
dict[tup[0]] = tup[1]
print(dict)


'''
4. Set for Unique Items:  
Ask the user to input a list of names. Convert it to a set to remove duplicates, then let the user input another name.
Check if the new name is already in the set and print the appropriate message.
'''
l = input("Enter a list of names separated by comma: ").split(',')
s = set(l)
name = input("Enter a new name: ")
if name in s:
    print(f"{name} is already in the list.")
else:
    s.add(name)
print(s)


'''
5. String and Dictionary Slicing:  
Ask the user to input a dictionary where keys are strings and values are integers.
Let the user input a string slice (start and end indices).
Slice all keys in the dictionary and print the modified dictionary.
'''

d = {}
n = 3
while n!=0:
    key = input("Enter a string: ")
    value = int(input("Enter a integer value: "))
    d[key] = value
    n-=1

start = int(input("Enter start index: "))
end = int(input("Enter end index: "))
updated_dictionary = {}
for i,j in d.items():
    updated_dictionary[i[start:end]] = j
print(updated_dictionary)
    

'''
6. Conditional Tuple Mutation:  
Take a tuple of numbers as input. If all numbers are even, convert the tuple into a list and append a new number (input by the user).
Otherwise, print the tuple without changes.
'''
numbers = tuple(map(int, input("Enter numbers separated by spaces: ").split()))

all_even = True
for i in numbers:
    if i % 2 != 0:
        all_even = False
        break

if all_even:
    numbers_list = list(numbers)
    new_number = int(input("Enter a number to append: "))
    numbers_list.append(new_number)
    print("Updated list:", numbers_list)
else:
    print("Original tuple:", numbers)


'''
7. Grocery Item Finder:  
Take a nested dictionary where the keys are categories (like fruits, vegetables) and values are lists of items.
Ask the user to input an item name and find which category it belongs to. If not found, print "Item not found."
'''
grocery = {'fruits': ['apple', 'banana', 'mango'], 'vegetables': ['potato', 'tomato', 'onion']}
item = input("Enter an item: ")

for category, items in grocery.items():
    if item in items:
        print(f"{item} belongs to {category}.")
        break
else:
    print("Item not found.")


'''
8. Conditional Dictionary Updater:  
Create a dictionary with keys as numbers and values as their squares. Let the user input a key. If the key exists,
update its value to its cube. If it doesn't, print "Key not found."
'''
nums = {1: 1, 2: 4, 3: 9, 4: 16}

key = int(input("Enter a key: "))

if key in nums:
    nums[key] = key ** 3
    print("Updated dictionary:", nums)
else:
    print("Key not found.")


'''
9. Tuple to Set Converter:  
Ask the user to input a tuple of numbers. If the tuple has more than 3 elements,
convert it into a set and remove the smallest number. Print the result.
'''

nums = tuple(map(int, input("Enter numbers separated by comma: ").split(',')))
if len(nums) > 3:
    nums_set = set(nums)
    nums_set.remove(min(nums_set))
    print("Updated result:", nums_set)
else:
    print("Tuple has 3 or fewer elements.")


'''
10. List Slicing Game:  
Ask the user to input a list of numbers. Then ask for two indices (start and end).
Slice the list using these indices and check if the sliced part is in ascending order.
'''
numbers = list(map(int, input("Enter numbers separated by comma: ").split(',')))
start = int(input("Enter start index: "))
end = int(input("Enter end index: "))
sliced = numbers[start:end+1]

for i in range(len(sliced) - 1):
    if sliced[i] > sliced[i + 1]:
        print(f"Sliced part {sliced} is not in ascending order.")
        break
else:
    print(f"Sliced part {sliced} is in ascending order.")


'''
11. Set Membership Quiz:  
Create a set of random words and ask the user to input a word. If the word is in the set, remove it; otherwise,
add it. Print the updated set.
'''
words = {'apple', 'banana', 'cherry', 'date'}
word = input("Enter a word: ")
if word in words:
    words.remove(word)
else:
    words.add(word)
print("Updated set:", words)


'''
12. Conditional Nested List Handling:  
Ask the user to input a nested list (a list containing other lists).
If the first element of the first inner list is a number,
change it to zero. Otherwise, leave it unchanged and print the nested list.
'''

l = [1,2,[2,34,4],['a',75,43]]

for i in l:
    if isinstance(i,list):
        if type(i[0])==int:
            i[0] = 0
print(l)


'''
13. Dictionary Slicer:  
Ask the user to input a dictionary with at least 5 key-value pairs. Then let them input two keys.
Create a new dictionary with only the pairs between those keys, inclusively, based on their order in the input.
'''

d = {}
n = 5
while n!=0:
    key = input("Enter a key: ")
    value = input("Enter a value: ")
    d[key] = value
    n-=1
print(d)

key1 = input("Enter first key from above dictionary: ")
key2 = input("Enter second key from above dictionary: ")
new_d = {}
for i,j in d.items():
    if i == key1:
        new_d[i] = j
    elif i == key2:
        new_d[i] = j
print(new_d)


'''
14. List and Dictionary Combo:  
Create a dictionary with names as keys and ages as values. Ask the user to input a list of names.
Print the ages corresponding to the names in the list. If a name doesn't exist, print "Unknown."
'''
d = {'Virat':35, 'Rohit':36, 'Dhoni':50}
names = input("Enter a list of names seperated by spaces: ").split(' ')
for name in names:
    if name in d:
        print(f"{name} is {d[name]} years old")
    else:
        print(f"Unknown")


'''
15. Conditional Set Operations:  
Ask the user to input two sets of numbers. If the two sets are disjoint, combine them. If they overlap, print their intersection.
'''
s1 = set(input("Enter set1: ").split(','))
s2 = set(input("Enter set2: ").split(','))
if s1.isdisjoint(s2):
    print(f"two sets are disjoint: {s1.union(s2)}")
else:
    print(f"The overlaping of two sets: {s1.intersection(s2)}")
