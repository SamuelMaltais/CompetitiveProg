def floyd(grid):
    n=len(grid)
    
    for k in range(n):
        for i in range(n):
            for j in range(n):
                if grid[i][j] > grid[i][k] + grid[k][j]:
                    grid[i][j] = grid[i][k] + grid[k][j]
    
    for k in range(n):
        # ceci veut dire que notre path est negatif
        if grid[k][k] < 0:
            for i in range(n):
                for j in range(n):
                    if grid[i][k] != float('infinity') and grid[k][j] != float('infinity'):
                        grid[i][j] = float('-infinity')



isFirst = True
while True:
    n,m,q = list(map(int, input().split()))
    if n == 0 and m == 0 and q == 0:
        break
    if isFirst:
        isFirst=False
    else:
        print()


    grid = []
    for _ in range(n):
        grid.append([float('infinity') for _ in range(n)])
    for i in range(n):
        grid[i][i] = 0

    for _ in range(m):
        a,b,w = list(map(int, input().split()))
        if w < grid[a][b]:
            grid[a][b] = w
    floyd(grid)

    for _ in range(q):
        u,v = list(map(int, input().split()))

        if grid[u][v] == float('-infinity'):
            print('-Infinity')
        elif grid[u][v] < float('infinity'):
            print(grid[u][v])
        else:
            print('Impossible')
            