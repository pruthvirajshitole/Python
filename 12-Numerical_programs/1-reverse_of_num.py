n = 123
t = n
r = 0
while n != 0:      # 123            # 12             # 1
    d = n%10       # 123%10 = 3     # 12%10 = 2      # 1%10 = 1
    r = r*10 + d   # 0*10 + 3 = 3   # 3*10 + 2 = 32  # 32*10 + 1 = 321
    n = n//10      # 123//10 = 12   # 12//10 = 1     # 1//10 = 0
print(f"Reverse of {t} is {r}")



num = int(input("Enter a number: "))
t = n
r = 0
while num != 0:
    d = num % 10
    r = r * 10 + d
    num = num // 10
print(f"Reverse of {t} is {r}")