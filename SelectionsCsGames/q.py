m, n = list(map(int, input().split()))
d={}
for _ in range(m):
    word, val = input().split()
    d[word] = int(val)


curr = 0
while n > 0:
    line = input()
    if line == '.':
        n -= 1
        print(curr)
        curr = 0
        continue
    for word in line.split():
        if word in d:
            curr += d[word]
    