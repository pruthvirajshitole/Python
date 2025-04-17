'''
    upper()
    lower()
    capitalize()
    casefold()
    center()
    endswith()
'''

s = "I am in MUMBAI"
print(s.upper())
print(s.lower())

# capitalize()
s = "I am in MUMBAI.I love it"
print(s.capitalize())  # converts only first letter to capital in string

# casefold()
s = "I am in MUMBAI.I love it"
print(s.casefold())
# Converts the string to lowercase, with additional handling for special Unicode case-folding rules.
# It is more aggressive than lower() in normalizing text

# center()
s = 'apple'
print(s.center(20))
print(s.center(20,'*'))

# endswith()
s = "I love India."
print(s.endswith('India.'))

s = "I love India."
print(s.endswith('love',0,6))

