for _ in range(int(input())):
    n, j, k = input().split()
    
    k = int(k)
    j = int(j)

    p = list(map(int, input().split()))

    if k >= 2:
        print('YES')
        continue

    if k == 1:
        if p[j - 1] == max(p):
            print('YES')
        else:
            print('NO')
            