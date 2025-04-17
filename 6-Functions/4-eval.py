'''
Eval:

    built-in function that parses and evaluates a string as a valid 
    Python expression. It takes a string input, interprets it as 
    code, and executes it within the program.

'''

print('----------Ex-1----------')
exp = '2+3'
res = eval(exp)
print(f'{exp}={res}')

exp = '3-2'
res = eval(exp)
print(f'{exp}={res}')

exp = '2*5'
res = eval(exp)
print(f'{exp}={res}')

exp = '9/3'
res = eval(exp)
print(f'{exp}={res}')

exp = '2+3-1**4//10*50'
res = eval(exp)
print(f'{exp}={res}')