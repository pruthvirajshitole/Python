# s="I am in Mumbai"  reverse the words of string using in-built functions
# o/p: s="Mumbai in am I"

s = 'I am in Mumbai'.split()
r = s[::-1]
r = ' '.join(r)
print(r)



s="I am in Mumbai"

l = []
w = ""
for i in s:
    if i != ' ':
        w+=i
    else:
        l.append(w)
        w = ""
l.append(w)
l = l[::-1]

s = ""
for j in l:
    s += j + ' '
print(s)

'''
l = []
w = ""
for i in s:
    if i != ' ':
        w+=i
    else:
        l.append(w)
        w = ""
l.append(w)

i   w          l
------------------------------
I   I    
             ['I']

a   a
m   am
             ['I','am']
     
M   M
u   Mu
m   Mum
b   Mumb
a   Mumba
i   Mumbai
             ['I','am','Mumbai']
'''


# s="India" find all possible substrings

'''
# Substrings
# I , In , Ind, Indi ,India, 
# n, nd, ndi, ndia
# d, di, dia
# i , ia
# a
'''
s = 'India'
l = []
w = ''
a = 0
for j in s:
    for i in s[a:len(s)+1]:
        w += i
        l.append(w)
    a += 1
    w = ''
print(l)

