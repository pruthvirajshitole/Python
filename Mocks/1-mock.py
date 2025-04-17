s = int(input("Enter a number: "))
sum = 0

for i in range(1,s):
    if s%i == 0:
        sum += i

print(sum)
if sum < s:
    print(f'{s} is a deficient number.')
else:
    print(f'{s} is not a deficient number.')
