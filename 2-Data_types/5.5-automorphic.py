# check the given number by user is automorphic or not
s = int(input("Enter a number: "))
square = s**2

if str(square).endswith(str(s)):
    print(f"{s} is Automorphic.")
else:
    print(f"{s} is not Automorhic.")

# Enter a number: 25
# 25 is Automorphic.
# Enter a number: 46
# 46 is not Automorhic.
