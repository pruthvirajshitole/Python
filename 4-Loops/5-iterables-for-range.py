l = [11,22,33,44]

print('---------Ex-1-----------')
for i in range(len(l)):
    print(i,':',l[i])

print('---------Ex-2-----------')
for i in range(len(l)):
    if i % 2 == 0:
        print(i,':',l[i])

print('---------Ex-3-----------')
for i in range(len(l)):
    if i % 2 != 0:
        print(i,':',l[i])

print('---------Ex-4-----------')
even_indexed = []
odd_indexed = []
for i in range(len(l)):
    if i % 2 == 0:
        even_indexed.append(l[i])
    else:
        odd_indexed.append(l[i])
print(f'''Even indexed: {even_indexed}, Odd indexed: {odd_indexed}''')