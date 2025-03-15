s1 = list(input())
s2 = list(input())

# i = 0
# i2 = 0
# fucked = []
# while i < len(s1):
#     while s1[i] != s2[i2]:
#         fucked.append(s2[i2])
#         i2 += 1
#     else:
#         i2 += 1
#     i += 1
# if i + 1 < len(s2):
#     if s2[-1] == s2[-2] == s1[-1]:
#         fucked.append(s2[-1])
fucked=[]
m = {}
for c in s1:
    m[c] = dict.get(m, c, 0) + 1

m2 ={}

for c in s2:
    m2[c] = dict.get(m2, c, 0) + 1

for c in m:
    if m[c] < m2[c]:
        fucked.append(c)

print(''.join(list(fucked)))


