import math
res = []
for _ in range(int(input())):
    input()
    l = list(map(int, input().split()))
    s = 0
    happy = 0
    for elem in l:
        s += elem
        if math.sqrt(s) % 1 == 0 and math.sqrt(s) % 2 == 1:
            happy += 1
    res.append(happy)

print('\n'.join(list(map(str, res))))

