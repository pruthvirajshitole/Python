# Check a number is Automorphic number or not?

num = int(input("Enter a number: "))
sqr = num**2
if str(sqr).endswith(str(num)):
    print("The given number is automorphic.")
else:
    print("The given number is not automorphic.")



# Take input in constructor and display in method, print frequency of each character of String.

class Frequency:
    def __init__(self,string):
        self.string = string
    
    def frq_char(self):
        d = {}
        for i in self.string:
            if i not in d:
                d[i] = 1
            else:
                d[i] += 1
        print(d)

obj = Frequency('Lucifer')
obj.frq_char()