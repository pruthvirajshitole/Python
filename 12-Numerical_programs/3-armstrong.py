# Armstrong

'''

An Armstrong number (also known as a narcissistic number) is

a number that is equal to the sum of its digits raised to 

the power of the number of digits.


1-Digit Armstrong Numbers:

All single-digit numbers (0-9) are Armstrong numbers because 

Numbers: 0, 1, 2, 3, 4, 5, 6, 7, 8, 9


2-Digit Armstrong Numbers:

There are no 2-digit Armstrong numbers because the sum of any two 

digits raised to the power of 2 will never equal the original number.


3-Digit Armstrong Numbers:

These numbers satisfy abc=a**3 + b**3 + c**3

Numbers: 153, 370, 371, 407


4-Digit Armstrong Numbers:

These numbers satisfy abcd=a**4 + b**4 + c**4 + d**4 

Numbers: 1634, 8208, 9474

153 = no of digits = 3

153 = 3*3*3 + 5*5*5 + 1*1*1

    = 27 + 125 + 1

    = 153

'''

n = input("Enter a number: ")  # 153 str
l = len(n)                     # 3
n = int(n)                     # 153 int
t = n
arm = 0

while n != 0:          # 153            # 15               # 1
    d = n % 10         # 153%10 = 3     # 15%10 = 5        # 1%10 = 1
    arm = arm + d**l   # 0 + 3**3 = 27  # 27 + 5**3 = 152  # 152 + 1**3 = 153
    n = n // 10        # 153//10 = 15   # 15//10 = 1       # 1//10 = 0

if t == arm:
    print(f"{t} is an Armstrong number")
else:
    print(f"{t} is not an Armstrong number")