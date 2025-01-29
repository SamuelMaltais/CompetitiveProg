for _ in range(int(input())):
    n,a,b,c = list(map(int, input().split()))
    start = 3 * (n // (a + b + c))
    left = n % (a + b + c)
    if left > a + b:
        start += 3
    elif left > a:
        start += 2
    elif left > 0:
        start += 1
        
    print(start)