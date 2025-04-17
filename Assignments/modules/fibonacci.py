def fib(n):
    n = n-2
    a=0
    b=1
    l = []
    l.extend([a,b])
    while n!=0:
        c = a+b
        l.append(c)
        a,b = b,c
        n-=1
    return l