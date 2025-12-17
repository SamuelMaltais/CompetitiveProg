grid= []

with open('input.txt') as f:
    lines = f.readlines()
    for line in lines:
        grid.append(list(line.strip()))


ini_j = grid[0].index('S')

grid[0][ini_j] = 1

grid.append(["." for _ in range(len(grid[0]))])

debut = 1
for i in range(0, len(grid) - 1):
    for j in range(len(grid[0])):
        if grid[i][j] != "." and grid[i][j] != '^':
            if grid[i + 1][j] == "^":
                if j - 1 >= 0:
                    if grid[i + 1][j - 1] == ".":
                        grid[i + 1][j - 1] = grid[i][j]
                    else:
                        grid[i + 1][j - 1] += (grid[i][j])
                if j + 1 < len(grid[0]):
                    if grid[i + 1][j + 1] == ".":
                        grid[i + 1][j + 1] = grid[i][j]
                    else:
                        grid[i + 1][j + 1] += grid[i][j]
            else:
                if grid[i + 1][j] == ".":
                    grid[i + 1][j] = grid[i][j]
                else:
                    grid[i + 1][j] += grid[i][j]


tot=0
for elem in grid[-1]:
    if elem != '.':
        tot += elem
print(tot)




