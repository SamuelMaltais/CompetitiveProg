def nums():
    return list(map(int, input().split()))

for _ in range(int(input())):
    words = input().split()
    s = ""
    for w in words:
        s += w[0]
    print(s)