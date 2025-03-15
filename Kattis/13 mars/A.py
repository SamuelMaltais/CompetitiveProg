for _ in range(int(input())):
    i,j,k = list(map(int, input().split()))
    print((min(i - 1, j + k) * 2) + 1)


