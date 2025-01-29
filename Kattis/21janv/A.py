for _ in range(int(input())):
    s=1
    strips = list(map(int,input().split()))
    for i in strips[1:]:
        s += (i - 1)
    print(s)