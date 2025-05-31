def nums():
    return list(map(int, input().split()))

for _ in range(int(input())):
    input()
    n = nums()
    ak = max(n)
    ak2 = min(n)
    s=0
    for num in n:
        s += ak ^ num
    s2 = 0
    for num in n:
        s2 += ak2 ^ num

    print(max(s, s2))