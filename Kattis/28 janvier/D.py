import sys

flooding = {}
hedgehog = {}

sys.setrecursionlimit(999999999)

r, c = input().split()
r = int(r)
m = []
for _ in range(r):
    m.append(list(input()))


def dfs(i, j, m, mem, curr):
    if not (0 <= i < len(m) and 0 <= j < len(m[0])):
        return

    if m[i][j] == 'D' or m[i][j] == 'X' or m[i][j] == 'S':
        return


    if (i,j) in mem:
        if mem[(i,j)] <= curr:
            return
    
    mem[(i,j)] = curr
    dfs(i+1,j,m,mem,curr+1)
    dfs(i-1,j,m,mem,curr+1)
    dfs(i,j+1,m,mem,curr+1)
    dfs(i,j-1,m,mem,curr+1)

def dfs2(i, j, m, mem,flooding, curr):
    if not (0 <= i < len(m) and 0 <= j < len(m[0])):
        return
    
    if (i,j) in flooding:
        if flooding[(i,j)] <= curr:
            return
    
    if m[i][j] == 'X' or m[i][j] == '*':
        return

    if (i,j) in mem:
        if mem[(i,j)] <= curr:
            return
    
    mem[(i,j)] = curr
    dfs2(i+1,j,m,mem,flooding,curr+1)
    dfs2(i-1,j,m,mem,flooding,curr+1)
    dfs2(i,j+1,m,mem,flooding,curr+1)
    dfs2(i,j-1,m,mem,flooding,curr+1)


def in_(i,j):
    if not (0 <= i < len(m) and 0 <= j < len(m[0])):
        return False
    return True
    

def bfs(flooding, current, m):
    toVisitNext = []
    count = 1
    while current != []:
        for node in current:
            for i in [1,-1]:
                if in_(node[0] + i,node[1]):
                    if (node[0] + i,node[1]) not in flooding and m[node[0] + i][node[1]] not in ['D', 'S', 'X']:
                        flooding[(node[0] + i,node[1])] = count
                        toVisitNext.append((node[0] + i,node[1]))
            for j in [1,-1]:
                if in_(node[0],node[1] + j):
                    if (node[0], node[1] + j) not in flooding and m[node[0]][node[1] + j] not in ['D', 'S', 'X']:
                        flooding[(node[0],node[1] + j)] = count
                        toVisitNext.append((node[0],node[1] + j))
        count += 1
        current = toVisitNext
        toVisitNext = []

current = []
for i in range(len(m)):
    for j in range(len(m[0])):
        if m[i][j] == '*':
            current.append((i,j))

bfs(flooding, current, m)

for i in range(len(m)):
    for j in range(len(m[0])):
        if m[i][j] == 'S':
            dfs2(i,j, m, hedgehog, flooding, 0)
            break
    

for i in range(len(m)):
    for j in range(len(m[0])):
        if m[i][j] == 'D':
            if (i,j) in hedgehog:
                print(hedgehog[(i,j)])
                break
            else:
                print('KAKTUS')
                break

