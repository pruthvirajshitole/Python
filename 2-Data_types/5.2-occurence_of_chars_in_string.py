s = input("Enter a string: ").lower()
d = {}
for i in s:
    if i != ' ':
        
        if i in d:
            d[i] += 1
        else:
            d[i] = 1
print(d)

'''

for x in s   if x in d:    d{}           
------------------------------------------------------------

n               F         d['n']=1      d={'n':1}

i               F         d['i']=1      d={'n':1,'i':1}

t               F         d['t']=1      d={'n':1,'i':1,'t':1}

i               T         d['i']+=1=2   d={'n':1,'i':2,'t':1} 

n               T         d['n']+=1=2   d={'n':2,'i':2,'t':1} 

'''
