n = 6
sum = 0
for x in range(1,n):
    if n%x == 0:
        sum+=x
if sum==n:
    print(f"{n} is a perfect number.")
else:
    print(f"{n} is not a perfect number.")