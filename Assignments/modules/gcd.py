def gcd(a,b):
    l=[]
    for i in range(1,a+1):
        if a%i==0 and b%i==0:
            l.append(i)
    return l[-1]
