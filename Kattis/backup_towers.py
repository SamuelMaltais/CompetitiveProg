from collections import deque
r,c,n = list(map(int,input().split()))

grid=[[[-1,-1] for _ in range(c)] for _ in range(r)]

tovisit = deque()
visited = {}

for t in range(1,n + 1):
    i,j=input().split()
    i=int(i) - 1
    j=int(j) - 1
    grid[i][j][0] = t
    tovisit.append((t,i,j))
    visited[t] = set()

def go(grid,visited,cell,newi,newj,tovisit):

    if 0 <= newj < len(grid[0]) and 0 <= newi < len(grid):

        if (newi, newj) not in visited[cell]:

            if grid[newi][newj][1] == -1 and cell not in grid[newi][newj]:
                visited[cell].add((newi,newj))
                tovisit.append((cell,newi,newj))
                if grid[newi][newj][0] == -1:
                    grid[newi][newj][0] = cell
                else:
                    grid[newi][newj][1] = cell


while len(tovisit) > 0:
    cell, i, j = tovisit.popleft()
    for di in [1,-1]:
        newi = i + di
        newj = j
        go(grid,visited,cell,newi,newj,tovisit)
    for dj in [1,-1]:
        newi = i
        newj = j + dj
        go(grid,visited,cell,newi,newj,tovisit)

g1=[]
g2=[]
for row in grid:
    l1=[]
    l2=[]
    for c in row:
        l1.append(str(c[0]))
        l2.append(str(c[1]))
    g1.append(" ".join(l1))
    g2.append(" ".join(l2))

print('\n'.join(g1))
print('\n'.join(g2))