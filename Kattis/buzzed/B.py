import sys

sys.setrecursionlimit(999999999)

try:
    aws = []
    next_move = {
        (0, 1): (1, 0),
        (1,0): (0, -1),
        (0, -1): (-1, 0),
        (-1, 0): (0, 1)
    }





    def dfs(i, j, di, dj, m, s, inii, inij, flag):    

        if not (0 <= i < len(m) and 0 <= j < len(m[0])):
            return s
        
        try:
            s += m[i][j]
        except:
            return s

        if i == inii and j == inij:
            if flag:
                flag = False
            else:
                return s

        if not (0 <= i + di < len(m) and 0 <= j + dj < len(m[0])):
            nnext_move = next_move[(di, dj)]
            di = nnext_move[0]
            dj = nnext_move[1]

        return dfs(i + di, j + dj, di, dj, m, s, inii, inij, flag)


    def count_layer(s):
        ss= '1543'
        tot = 0
        if len(s) < len(ss):
            return
        for i in range(len(s)):
            started = 0
            while s[(i + started) % len(s)] == ss[started]:
                started += 1
                if started == len(ss):
                    tot += 1
                    break
            
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

        while m != []:
            try:
                if len(m[0]) == 0:
                    break
                layer = list(dfs(0, 0, 0, 1, m, "", 0, 0, True))
                if len(layer) > 0:
                    layer.pop()
                count = count_layer(layer)
                if count:

                    tot += count_layer(layer)

                if len(m) > 0:
                    m.pop(0)
                if len(m) > 0:
                    m.pop()
                for r in m:
                    if len(r) > 0:
                        r.pop()
                    if len(r) > 0:
                        r.pop(0)
            except:
                tot = 0


        aws += [str(tot)]
    print('\n'.join(aws))
except:
    print(0)