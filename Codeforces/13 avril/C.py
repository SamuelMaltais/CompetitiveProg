def nums():
    return list(map(int, input().split()))

for _ in range(int(input())):
    n = int(input())
    grid = []
    for _ in range(n):
        grid.append(nums())
    

    p = []
    present = set([i for i in range(1, 2*n + 1)])
    x=0
    y=0
    for i in range(2 * n - 1):
        p.append(str(grid[x][y]))
        if grid[x][y] in present:
            present.remove(grid[x][y])
        if i % 2 == 0:
            x += 1
        else:
            y += 1
        
    elem = str(list(present)[0])
    print(" ".join([elem] + p))