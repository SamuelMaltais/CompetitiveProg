import math
for _ in range(int(input())):
    n,m,k = list(map(int, input().split()))
    target = n * m
    
    poss = target // (max(1, n / k) * max(1, m / k))
    print(int(poss))