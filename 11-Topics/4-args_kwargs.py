'''
In Python, *args and **kwargs are used to allow functions to accept
an arbitrary number of arguments. These features provide great flexibility
when designing functions that need to handle a varying number of inputs.

Special Symbols Used for passing arguments in Python:
    1- *args (Non-Keyword Arguments)
    2- **kwargs (Keyword Arguments)

'''

# *args (Non-keyword Arguments):
#     Allows a function to accept any number of positional arguments.
#     Arguments are passed as a tuple.

print('------*args-----')
def names(*name):
    for i in name:
        print(i)
names('Virat','Rohit','Miller')

print('------with default------')
def team(captain,*players):
    print(f'Captain: {captain}')
    print(players)
team('Rohit','Virat','Pandya','Varun')


# **kwargs (Keyword Arguments)
#     Allows a function to accept any number of named (keyword) arguments.
#     Arguments are passed as a dictionary.

print('------**kwargs-----')
def names(**name):
    print(name)
    print(type(name))
names(MI='Rohit',RCB='Virat')

print('------**kwargs-----')
def names(**name):
    for i,j in name.items():
        print(f'Team: {i}, Player:{j}')
names(MI='Rohit',RCB='Virat', HYD='Cummins')


# using *args and **kwargs together but *args must come before **kwargs.
print('------*args,**kwargs-----')
def fun(*args, **kwargs):
    print("Positional arguments:", args)
    print("Keyword arguments:", kwargs)

fun(1, 2, 3, a=4, b=5)
