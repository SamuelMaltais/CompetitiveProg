for _ in range(int(input())):
    
    n = int(input())

    l = ["-1" for _ in range(n)]

    ["1",-1,-1,-1,-1]

    offset = 0
    ok = True
    for i in range(n):
        if l[(i + offset) % n] != "-1":
            ok = False
            break
        l[(i + offset) % n] = str(i + 1)
        offset += 1

    if ok:
        print(" ".join(l))
    else:
        print(-1)