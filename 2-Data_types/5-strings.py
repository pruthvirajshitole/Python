'''
Sequence Type:
    collection of hetrogenous(different type) data,
    indexed and ordered,
    immutable(unchangable),
    allows duplicate values,
    elements written in (' '," ",''' ''',""" """)
'''

'''
upper()
lower()
strip()
replace()
split()
join()
format()

escape characters: 
\' , \"
\n  new line
\r  carriage return
\t  tab
\b  backspace

count()
find()
index()

isalpha()
isnumeric()
isdigit()
isalnum()
isspace()
isupper()
islower()
partition()
zfill()

reversed()
sorted()

'''

print('--------String--------')

s = 'I am in Pune, 405025'
print(s)

print('--------Multi-line string--------')

s = '''
I like Python.
Python is best for me
'''
print(s)

print(type(s))  # <class 'str'>


# Slicing

print('--------Slicing--------')

s = 'I am in Pune, 405025'
print(s[0])
print(s[-1])
print(s[2:4])
print(s[-6::])
print(s[::-1])


# Modifying string

print('--------upper()--------')

print(s.upper(),s)

print('--------lower()--------')

print(s.lower(),s)


# strip()

print('--------strip()--------')

a = '    ABCD'
print(a.strip())  # removes the whitespaces at beginning
print(a)


# replace()

print('--------replace()--------')

s = "Hello,World!!!"
print(s.replace('H','h'),s)   # hello,World!!! Hello,World!!!

print(s.replace('Hello', 'Hii'))    # Hii,World!!!


# split()

print('--------split()--------')

s = "Good Evening!!! Welcome to Pune"
print(s.split()[2])


# name = input("Enter your full name: ").split()
# your_name = name[0]
# middle_name = name[1]
# last_name = name[2]
# print('Your name is: ', your_name)
# print('Your father name is: ', middle_name)
# print('Your last name is: ', last_name)


# join()

print('--------join()--------')

# reverse the user input by words
name = input("Enter the name: ").split()

# print(name[-1],name[-2],name[-3])

s = name[::-1]
rev = ' '.join(s)
print(f'reversed string {rev}')


# concatenate

print('--------Concatenate--------')

a = 'Virat'
b = 'Kohli'
c = a+' '+b
print(a,b,c)


# format

print('--------format()--------')

city = 'Pune'
state = 'Maharashtra'
s = 'I love {},{}'      # {}- Placeholder
print(s.format(city,state))

s = 'I love {1},{0}'
print(s.format(state,city))


# escape characters

print('--------escape characters--------')

# 1- \', \"  to add quotes in string
txt = "I am \"Lucifer.\" from LA"
print(txt)

txt = "I like \\ backshlashes"
print(txt)

# 2- \n  new line
txt = "I am Tom.\nI am from California."
print(txt)

# 3- \r carriage return
txt = "I am Chloe.\rI am from Los Vegas"
print(txt)

# cursor will move to first character and replace the character with new strig
txt = "I am   Amendeal.\rMyself"
print(txt)

# 4- \t  tab
txt = "Hello \t World"
print(txt)

# 5- \b  backspace
txt = "Helloo\b Worldz\b"
print(txt)

txt = "hwll\b"
print(txt)

# octal values (0-7)
txt = "\110\145\154\154\157"
print(txt)

# hexa values (0-9 A-F)
txt = "\x48\x65\x6c\x6c\x6f"
print(txt)

# A - 101 in octal value
txt="\101"
print(txt)

# A - x41 in hexa value
txt="\x41"
print(txt)


# count() - counts the number of occurences of elements in string.

print('--------count()--------')

s = 'I like apple, and apple is the best.'
print(s.count('apple'))

print(s.count('apple',1,14))


# find()

print('--------find()--------')

s = 'I love Pune.'
print(s.find('Pune'))  # 'Pune' is on 7 index
print(s.find('e'))  # first occurence of 'e' is on index 5

print(s.find('e',-4,-1)) # 'e' is on indiex 10 in given range


# index()

print('--------index()--------')

s = 'I love Pune.'
print(s.index('Pune'))  # 'Pune' is on 7 index
print(s.index('e'))  # first occurence of 'e' is on index 5

print(s.index('e',-4,-1)) # 'e' is on indiex 10 in given range

# find() vs index()
s = 'I love Pune'
print(s.find('z'))  # -1 for element not in string

# print(s.index('z'))  # ValueError: substring not found


# isalpha()

s = 'IlovePune'
print(s.isalpha())  # True - only if all are alphabets in given string


# isnumeric()

s = '123565'
print(s.isnumeric())  # True - only if all are numbers in given string

s = "Ⅻ"  # Roman numeral for 12
print(s.isnumeric())  # True


# isdigit()

s = '1234'
print(s.isdigit())  # True - only if all are digits in given string

s = "Ⅻ"  # Roman numeral for 12
print(s.isdigit())  # False

x = '12.3'
print(x.isdigit())  # False


# isalnum()

s = 'And'
print(s.isalnum())  # True

s = '2435'
print(s.isalnum())  # True

s = 'And5656'
print(s.isalnum())  # True

s = 'And.45'
print(s.isalnum())  # False


# isspace()

s = ' '
print(s.isspace())  # True

s = ' j  '
print(s.isspace())  # False


# isupper()

s = 'HELLO'
print(s.isupper())  # True


# islower()

s = 'hello.'
print(s.islower())  # True


# partition()

print('--------partition()--------')

s = 'I am in Pune and in Baner.'
p = s.partition('in')
print(p)   # ('I am ', 'in', ' Pune and in Baner.')  # output is a tuple
# tuple of:
# (part before special str, special str, part after special str)


# zfill()

print('--------zfill()--------')

z = '50'
a = z.zfill(10)
print(a)   # 0000000050

b = z.zfill(3)
print(b)  # 050


'''

isdecimal()
istitle()
splitlines()
rstrip()
lstrip()
rpartition()
isidentifier()
rjust()
ljust()

'''

# sorted()

print('--------sorted()--------')

s = 'I love Pune'
l = sorted(s)
s = ' '.join(l)
print(s)  #     I P e e l n o u v  # whitespaces considered first


# reversed()

print('--------reversed()--------')

s = 'I love Pune'
r = list(reversed(s))
# reverse = ''.join(r)
print(r)
