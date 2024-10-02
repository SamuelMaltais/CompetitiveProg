n = int(input())

awns = [1]
qte = [1,0,0,0,0]

# (x, y) coord
def chooseNode(candidates):
    if len(candidates) == 1:
        return candidates

    i = candidates[0]
    m = qte[candidates[0] - 1]

    for cand in candidates:
        if qte[cand - 1] < m:
            i = cand
            m = qte[cand - 1]

    qte[i - 1] += 1
    return i

directions = [[1,1],[0, 1], [-1,1]gh, [-1, -1], [0,-1], [1, -1]]

def get_neighbors(dict, x, y):

    candidates = [1,2,3,4,5]
    for mouv in directions:
        new_x = mouv[0] + x
        new_y = mouv[1] + y
        if((new_x, new_y) in dict):
            candidates.remove(dict[(new_x, new_y)])

    print("ITER")
    print((x, y))
    print(dict)
    print(candidates)


    return candidates

def next_node(dict, x, y, currDirr):
    
    voisins = get_neighbors(dict, x + currDirr[0], y + currDirr[1])
    awns.append(chooseNode(voisins))
    newCoord = (x + currDirr[0], y + currDirr[1])
    dict[newCoord] = awns[-1]
    return newCoord


repeat = 1
dict = {}
pos = (0,0)
dict[pos] = 1
curr = 0

for _ in range(n):
    nth = int(input())
    
    premier = True
    while curr < nth:
        for mouv in directions:
            r = repeat
            if mouv == [0,1]:
                r -= 1
            for i in range(r):
                pos = next_node(dict, pos[0], pos[1], mouv)
                curr += 1
        repeat += 1


        print(awns)
    print(awns[nth - 1])