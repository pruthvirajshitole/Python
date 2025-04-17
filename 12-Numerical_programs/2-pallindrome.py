num = int(input("Enter a number: "))
t = num
r = 0
while num != 0:
    d = num % 10
    r = r * 10 + d
    num = num // 10
if t == r:
    print(f"The entered number {t} is a palindrome.")
else:
    print(f"The entered number {t} is not a palindrome.")