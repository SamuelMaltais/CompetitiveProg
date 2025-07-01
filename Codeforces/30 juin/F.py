import math
for _ in range(int(input())):
    n, m, d = list(map(int, input().split()))
    
    grid = []
    for _ in range(n):
        grid.append(input())
    
    vertical_reach = math.floor((d**2 - 1)**(1/2))

    ways = [[0 for _ in range(m)] for _ in range(n)]

    for i in range(m):
        if grid[0][i] == 'X':
            ways[0][i] = 1

    row = 0
    oldRow = ways[row][:]
    for i in range(m):
            if grid[row][i] == 'X':
                curr_ways = oldRow[i]
                for j in range(max(0, i - d), min(m, i + d + 1)):
                    if i != j:
                        curr_ways += oldRow[j]
                ways[row][i] = curr_ways

    for row in range(1, n):
        for i in range(m):
            if grid[row][i] == 'X':
                # Voyons si nous pouvons atteindre une rangee en haut
                curr_ways = 0
                for j in range(max(0, i - vertical_reach), min(m, i + vertical_reach + 1)):
                    curr_ways += ways[row - 1][j]
                ways[row][i] = curr_ways
        # On ajuste pour les chemin ou on saute horizontalement
        oldRow = ways[row][:]
        s=0
        psum = []
        for e in oldRow:
            s += e
            psum.append(s)

        for i in range(m):
                if grid[row][i] == 'X':
                    curr_ways = oldRow[i]
                    for j in range(max(0, i - d), min(m, i + d + 1)):
                        if i != j:
                            curr_ways += oldRow[j]
                    ways[row][i] = curr_ways 

    print(sum(ways[-1]) % 9982443530)