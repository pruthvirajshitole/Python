# Peterson number/ Strong number/ Krishnamurthy Number:

# ✅ 145

# Digits: 1, 4, 5
# Factorial sum:
# 1!+4!+5!=1+24+120=145
# Since 145 == 145, it is a Peterson Number ✅


n = int(input("Enter a number: "))
temp = n
s = 0
while n!=0:
    d = n%10
    fact = 1
    for i in range(1,d+1):
        fact *= i
    s += fact
    n = n//10
if temp==s:
    print(f'{temp} is a peterson number.')
else:
    print(f'{temp} is not a peterson number.')
