# i = 0
# l = []
# while i<=10:
#     if i%2 != 0:
#         l.append(i)
#     i+=1
# print(l)


l = [i for i in range(11) if i%2!=0]
print(l)