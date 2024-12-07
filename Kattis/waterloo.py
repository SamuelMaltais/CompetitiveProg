n = int(input())

c = {}
for _ in range(n):
    line = input().split()
    line = list(map(lambda b: int(b), line))
    line.sort()
    t = tuple(line)

    if t in c:
        c[t] += 1
    else:
        c[t] = 1


f = True
m = 0
tie = False

for key in c:
    if f:
        m = c[key]
        f = False
    else:
        if c[key] > m:
            m = c[key]
            tie = False
        if c[key] == m:
            tie = True 

if tie:
    count = 0
    for key in c:
        if c[key] == m:
            count += m

    print(count)

else:
    print(m)