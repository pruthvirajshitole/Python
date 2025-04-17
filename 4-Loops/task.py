s='aaabbc'

def compress(s):
    d = {}
    for i in s:
        if i not in d:
            d[i] = 1
        else:
            d[i] += 1
    c_s = 'a'+str(d['a']) + 'b'+str(d['b']) + 'c'+str(d['c'])
    if len(s)<len(c_s):
        return s
    else:
        return c_s
print(compress(s))