next = {
    '1':'5',
    '5': '4',
    '4': '3',
    '3': '69'
}

next_move = {
    (0, 1): (1, 0),
    (1,0): (0, -1),
    (0, -1): (-1, 0),
    (-1, 0): (0, 1)
}


def dfs(i, j, m, di, dj, next_number ,ini_i, ini_j):

    t1 = ini_j
    t2 = ini_i

    if i < min(ini_i, ini_j):
        return
    if i > max(ini_i, ini_j):
        return
    if j > max(ini_i, ini_j):
        return
    if j < max(ini_i, ini_j):
        return


    if not (0 <= i < len(m) and 0 <= j < len(m[0])):
        return 0
    
    tot = 0
    if m[i][j] != next_number:
        return 0

    next_number = next[next_number]
    if next_number == '69':
        if not flag:
            return 0
        return 1



    tot += dfs(i + di, j + dj, m, di, dj, next_number,ini_i, ini_j)
    
    


    nnext_move = next_move[(di, dj)]
    di = nnext_move[0]
    dj = nnext_move[1]


    tot += dfs(i + di, j + dj, m, di, dj, next_number,ini_i, ini_j)

    return tot


aws = []
for _ in range(int(input())):
    n, m = input().split()
    n = int(n)
    m = []
    for _ in range(n):
        row = list(input())
        m.append(row)
    
    tot = 0
    for i in range(len(m)):
        for j in range(len(m[0])):
            if m[i][j] == '1':
                #print(i, j)
                tot += dfs(i, j, m, 0, 1, '1', i, j)
                
    aws += [str(tot)]








print('\n'.join(aws))

    
    