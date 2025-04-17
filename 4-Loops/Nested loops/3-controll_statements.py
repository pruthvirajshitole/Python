# break
# break is used to exit a for loop or a while loop

print('------break-------')
for i in range(11):
    if i==5:
        break
    print(i)


# pass
# A placeholder statement that does nothing

print('------pass-------')
def add():
    pass


# continue
# continue is used to skip the current block, and return to the “for” or “while” statement

print('------continue-------')
for x in range(11):
    if x>=5 and x<=7:  # skips 5,6,7
        continue
    print(x)