n, p = list(map(int, input().split()))

taken = set()
paths = []
for _ in range(n):
    l=input().split()
    path = []
    for i in range(1, len(l), 4):
        path.append((int(l[i + 2]), l[i + 3]))
    paths.append(path)

c=0
for _ in range(p):
    best = 0
    best_i=0
    for i in range(len(paths)):
        val=0
        for j in reversed(range(len(paths[i]))):
            node = paths[i][j]
            if node[1] in taken:
                break
            val += node[0]
        if val > best:
            best_i = i
            best = val
    c += best
    for p in paths[best_i]:
        taken.add(p[1])
# print(taken)
print(c)