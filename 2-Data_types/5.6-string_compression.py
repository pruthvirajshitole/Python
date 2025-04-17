s='aaabbcdddd'
def compress(s):
    d = {}
    for i in s:
        if i not in d:
            d[i] = 1
        else:
            d[i] += 1

    c_s = ''
    for j in d.keys():
        c_s += j+str(d[j])

    if len(s)<len(c_s):
        return s
    else:
        return c_s
print(compress(s))


s="aaabbc"
comp=""
i = 0
while i < len(s):
    count=1
    while i+1 < len(s) and s[i]==s[i+1]:
        count+=1
        i +=1
    comp=comp + s[i] + str(count)
    i +=1
print('compresssed:',comp)


# s = 'a3b2c1'  # s='aaabbc'

s = 'a3b2c1'
exp = ''
for i in range(0,len(s),2):
    ch = s[i]
    count = s[i+1]
    exp += ch*int(count)
print(exp)


s = "x2y1z3"
res = ''
for i in range(len(s)):
    if i%2==0:
        res+=s[i]
    else:
        res+=(int(s[i])-1)*(s[i-1])
print(res)


# Write the functions sell() and purchase()
# to find the best pusrchase and best selling date
# and also mention the profit in that term

dates={
       '01/01/2024':100,
       '02/01/2024':200,
       '03/01/2024':50,
       '04/01/2024':150,
       '05/01/2024':1000,
       '06/01/2024':240,
       '07/01/2024':120
    }

prices = list(dates.values())
date = list(dates.keys())

min_p = min(prices)
for i,j in dates.items():
    if j==min_p:
        purchase_date = i

print(f'Best date to purchas stock is: {purchase_date}')

max_p = max(prices[prices.index(min_p)+1:])
for i,j in dates.items():
    if j==max_p:
        sell_date = i

print(f'Best date to sell the stock is: {sell_date}')
print(f"Total profit is: {max_p-min_p}")