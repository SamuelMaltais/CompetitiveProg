def nums():
    return list(map(int, input().split()))

for _ in range(int(input())):
    n, m, l, r = nums()
    
    days = n - m

    for i in range(days):
        if l < 0:
            l += 1
        else:
            r -= 1
    print(l, r)
