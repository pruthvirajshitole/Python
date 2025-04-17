import math

# help(math)
# help() gives complete description about each function present in that module


print('------dir()------')
# print(dir(math))
# dir returns the list of functions name present in a particular module.


print('------documentation string with help()------')
#  help for a specific function
help(math.factorial)


print('------documentation string------')
# description of the function in the module is defined as documentation string.
# it is written in triple quotes but not considered as comment.
print(math.factorial.__doc__)



print('------main()------')
# Every python file has a variable name called as dunder name. 
# The content inside this variable is based on whether the 
# python file is executed in script mode or imported in other file.  
# If it is executed in script mode, dunder name contains  __main__ 
# If it is imported in other file, dunder name will be same as the file name. 
print(__name__)
