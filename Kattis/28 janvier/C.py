s=0
for _ in range(int(input())):
    t, i = list(map(int, input().split()))
    if t == 1:
        s = max(0, s - i)
    else:
        s += i
print(s)
