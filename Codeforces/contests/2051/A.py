for _ in range(int(input())):
    int(input())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    s = 0
    for i in range(len(a)):
        if i + 1 < len(a):
            if a[i] > b[i + 1]:
                s += a[i] - b[i+1]
        else:
            s += a[i]
    print(s)