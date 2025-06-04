def toRow(num):
    row = []
    for _ in range(3):
        row.append(num % 2)
        num = num // 2
    return row

def travel(grid, set_grid, i,j,di,dj, initial, curr):
    if curr == 3:
        return True
    if not (0 <= i < 3 and 0 <= j < 3):
        return False
    if not set_grid[i][j]:
        return False
    if grid[i][j] == initial:
        return travel(grid, set_grid, i + di, j + dj, di,dj, initial, curr + 1)
    return False

def find_winner(grid, set_grid):
    for i in range(3):
        for j in range(3):
            for di in [-1,0,1]:
                for dj in [-1,0,1]:
                    if abs(di) + abs(dj) > 0:
                        res=travel(grid,set_grid,i,j,di,dj,grid[i][j],0)
                        if res:
                            return grid[i][j]
    return -1

for _ in range(int(input())):
    s=list(input())

    set_grid=[]
    for _ in range(3):
        if len(s) > 0:
            set_grid.append(toRow(int(s.pop())))
        else:
            set_grid.append(toRow(0))
    grid=[]
    for _ in range(3):
        if len(s) > 0:
            grid.append(toRow(int(s.pop())))
        else:
            grid.append(toRow(0))

    s=0
    for r in set_grid:
        s+=sum(r)
    
    r = find_winner(grid, set_grid)
    if r == 1:
        print('X wins')
    elif r == 0:
        print('O wins')
    else:
        if s == 9:
            print("Cat's")
        else:
            print('In progress')


