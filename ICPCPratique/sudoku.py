grid = []
rows_blocked = {}
columns_blocked = {}


soFar = 0

for i in range(1,10):
    rows_blocked[i] = []
    columns_blocked[i] = []

madeChange = True

for i in range(9):
    line = input()
    grid.append(list(line))
    for j in range(9):
        if line[j] != '.':
            if i in rows_blocked[int(line[j])]:
                madeChange = False
                soFar = -1

            if j in columns_blocked[int(line[j])]:
                madeChange = False
                soFar = -1

            rows_blocked[int(line[j])].append(i)
            columns_blocked[int(line[j])].append(j)
            soFar += 1


def isLegal(row_start, col_start,grid, rows_blocked, columns_blocked, num):
    isOk = True
    for row in range(row_start, row_start + 3):
            for column in range(col_start, col_start + 3):  
                if grid[row][column] == str(num) and not isOk:
                    return False
                if grid[row][column] == str(num):
                    isOk = False
    return True


for num in range(1,10):
    ok = True
    ok = isLegal(0,0, grid,rows_blocked, columns_blocked, num) and ok
    ok = isLegal(0,3, grid,rows_blocked, columns_blocked, num) and ok
    ok = isLegal(0,6, grid,rows_blocked, columns_blocked, num) and ok
    ok = isLegal(3,0, grid,rows_blocked, columns_blocked, num) and ok
    ok = isLegal(3,3, grid,rows_blocked, columns_blocked, num) and ok
    ok = isLegal(3,6, grid,rows_blocked, columns_blocked, num) and ok
    ok = isLegal(6,0, grid,rows_blocked, columns_blocked, num) and ok
    ok = isLegal(6,3, grid,rows_blocked, columns_blocked, num) and ok
    ok = isLegal(6,6, grid,rows_blocked, columns_blocked, num) and ok

    if not ok:
        madeChange = False
        soFar = -1

def updateSquare(row_start, col_start,grid, rows_blocked, columns_blocked, num):

    toAdd = []

    for row in range(row_start, row_start + 3):
            for column in range(col_start, col_start + 3):  
                if row not in rows_blocked[num] and column not in columns_blocked[num] and grid[row][column] == '.':
                    if toAdd != []:
                        return False
                    else:
                        toAdd = [row, column]

    if toAdd != []:
        grid[toAdd[0]][toAdd[1]] = str(num)
        rows_blocked[num].append(toAdd[0])
        columns_blocked[num].append(toAdd[1])
    
    if not isLegal(row_start, col_start,grid, rows_blocked, columns_blocked, num):
        rows_blocked[num].pop()
        columns_blocked[num].pop()
        grid[toAdd[0]][toAdd[1]] = "."

        return False

    return not toAdd == []

passed = False

while madeChange:
    madeChange = False

    for num in range(1,10):
        madeChange = updateSquare(0,0, grid,rows_blocked, columns_blocked, num) or madeChange
        madeChange = updateSquare(0,3, grid,rows_blocked, columns_blocked, num) or madeChange
        madeChange = updateSquare(0,6, grid,rows_blocked, columns_blocked, num) or madeChange

        madeChange = updateSquare(3,0, grid,rows_blocked, columns_blocked, num) or madeChange
        madeChange = updateSquare(3,3, grid,rows_blocked, columns_blocked, num) or madeChange
        madeChange = updateSquare(3,6, grid,rows_blocked, columns_blocked, num) or madeChange

        madeChange = updateSquare(6,0, grid,rows_blocked, columns_blocked, num) or madeChange
        madeChange = updateSquare(6,3, grid,rows_blocked, columns_blocked, num) or madeChange
        madeChange = updateSquare(6,6, grid,rows_blocked, columns_blocked, num) or madeChange

        passed = passed or madeChange

        


if soFar != -1 and passed:
    ok = []
    for row in grid:
        ok.append("".join(row))

    print("\n".join(ok))

else:
    print("ERROR")