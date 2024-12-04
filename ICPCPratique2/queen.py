import copy

def makeillegal(grid, i, j, n):
    # Column
    for x in range(n):
        grid[x][j] = False

    # Diag
    x, y = i, j
    while x >= 0 and y >= 0:
        grid[x][y] = False
        x -= 1
        y -= 1

    x, y = i, j
    while x < n and y < n:
        grid[x][y] = False
        x += 1
        y += 1

    x, y = i, j
    while x >= 0 and y < n:
        grid[x][y] = False
        x -= 1
        y += 1

    x, y = i, j
    while x < n and y >= 0:
        grid[x][y] = False
        x += 1
        y -= 1


# On assume une queen sur un trou qui n'existait pas avant
# Pour chaque nouveau trou, on soustrait la qte en assumant la queen dessus
# Pour chaque trous eleves, on ajoute la qte en assumant une queen dessus
def smart_backtracking(grid,row_skip, row,  n):

    if row == row_skip:
        return smart_backtracking(grid, row_skip, row + 1, n)

    if row == n:
        return 1

    curr = 0
    for i in range(n):
        # Place queen
        if grid[row][i] == True:
            cpy = copy.deepcopy(grid)
            cpy[row][i] = False
            makeillegal(cpy, row, i, n)
            curr += smart_backtracking(cpy, row_skip, row + 1, n)

    return curr
def backtracking(grid, row, n):
    if row == n:
        return 1

    curr = 0
    for i in range(n):
        # Place queen
        if grid[row][i] == True:
            cpy = copy.deepcopy(grid)
            cpy[row][i] = False
            makeillegal(cpy, row, i, n)
            curr += backtracking(cpy, row + 1, n)

    return curr


computed = {}
computed_sums = {}



while True:

    line = input().split()
    n = int(line[0])
    m = int(line[1])
    if n == 0 and m == 0:
        break

    

    grid = []
    for i in range(n):
        row = []
        for j in range(n):
            row.append(True)
        grid.append(row)

    if n in computed:

        anciens_trous = computed[n]
        curr = computed_sums[n]

        nouveau_trous = []

        for trou in anciens_trous:
            cpy = copy.deepcopy(grid)
            makeillegal(cpy, trou[0], trou[1], n)
            curr += smart_backtracking(cpy, trou[0],0, n)


        for i in range(m):
            pos = input().split()
            nouveau_trous.append([int(pos[0]),int(pos[1])])
            grid[nouveau_trous[-1][0]][nouveau_trous[-1][1]] = False


        
        for trou in nouveau_trous:
            cpy = copy.deepcopy(grid)
            makeillegal(cpy, trou[0], trou[1], n)
            curr -= smart_backtracking(cpy, trou[0], 0, n)

        print(curr - 5)

    else:
        ok = []
        for i in range(m):
           
            pos = input().split()
            ok.append([int(pos[0]),int(pos[1])])

            grid[int(pos[0])][int(pos[1])] = False



        curr = backtracking(grid, 0, n)
        print(curr)
        computed_sums[n] = curr
        computed[n] = ok