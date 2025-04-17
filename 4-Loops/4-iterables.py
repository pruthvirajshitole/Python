print('---------Ex-1-----------')
l = [1,2,3,4,5,6,7,8,9,10]

i = 0
while i <= len(l)-1:
    print(i, l[i])
    i += 1
# i is the index to get the elements l[i]


# Ex-2- Even indexed element

print('---------Ex-2-----------')
l=[10,2,30,64,51,36,76,38,99]
i = 0
while i <= len(l)-1:
    if i % 2 == 0:
        print(i, l[i])
    i += 1

# while iterates on the index and for loop iterates on the elements


# Ex-3- Odd indexed element

print('---------Ex-3-----------')
l=[10,2,30,64,51,36,76,38,99]
i = 0
while i <= len(l)-1:
    if i % 2 != 0:
        print(i, l[i])
    i += 1


# Ex-4- Even-odd indexed element

print('---------Ex-4-----------')
l=[10,2,30,64,51,36,76,38,99]
even_indexed = []
odd_indexed = []
i = 0
while i <= len(l)-1:
    if i % 2 == 0:
        even_indexed.append(l[i])   
    else:
        odd_indexed.append(l[i])
    i+=1
print(f'''Even indexed : {even_indexed}, Odd indexed : {odd_indexed}''')

