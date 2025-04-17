prime = [1]
i = 1
flag = True
while i<len(prime):
    if prime%i == 0:
        flag = True
        prime.append(prime)
    prime+=1
if flag == True:
    print(prime)
    
else:
    print(f"{prime} is not a prime number.")
