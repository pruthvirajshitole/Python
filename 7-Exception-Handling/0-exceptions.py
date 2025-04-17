'''
Try:
    let you test the block of code

Except:
    let you handle the error/exception

finally:
    let you excecute the block of code
    regardless of the result of try except

else:
    let you excecute the block of code
    if there will be no error in try
'''


print('------try-except------')
x = 4
y = 3
print(x+y)

try:
    print(z)
except:
    print("z is not defined")


print('------try-except (multiple)------')
try:
    print(x+'a')
except TypeError:
    print("Type error")
except NameError:
    print("Name error")
except:
    print("Something went wrong")

# list of errors
# [TypeError, NameError, ValueError, KeyError]


print('------try-except-else------')
try:
    v=4
    print(v)
except:
    print("Something is wrong")
else:
    print("All right")


print('------try-except-finally------')
try:
    w = 9
    print(w)
except:
    print("Something is wrong")
finally:
    print("Finally will run")


print('------try-except-finally------')
try:
    w = 3
    print(w)
except:
    print("Something is wrong")
else:
    print("New error")
finally:
    print("Finally will run")