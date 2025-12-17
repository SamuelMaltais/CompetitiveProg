import sys
sys.setrecursionlimit(999999999)

l= []

with open('input.txt') as f:
    lines = f.readlines()
    for line in lines:
        l.append(line.strip())

tot = 0

solved = False
def choose(moves, curr, seen, buttons, maxes):
    global best

    global solved
    if solved:
        return

    if curr in seen:
        if seen[curr] <= moves:
            return
    
    #print(seen)
    seen[curr] = moves    
    
    if curr == maxes:
        solved = True
        return

    for i in range(len(curr)):
        if curr[i] > maxes[i]:
            return

    for move in buttons:
        maxCoeff = 0

        for m in move:
            maxCoeff = max(maxes[m] - curr[m], maxCoeff)

        while maxCoeff > 0:
            newState = list(curr)
            for m in move:
                newState[m] += maxCoeff
            choose(moves + maxCoeff, tuple(newState), seen, buttons, maxes)
            maxCoeff -= 1

tot = 0
for i in range(len(l)):
    line = l[i]
    print(i + 1, "/", len(l), line)
    line = line.split()
    buttons = line[1:len(line)-1]
    state = line[0][1:len(line[0]) - 1]
    end = tuple(map(int, line[-1][1:len(line[-1]) - 1].split(',')))
    totMoves = []
    for b in buttons:
        s = b[1:len(b) - 1]
        totMoves.append(list(map(int,s.split(","))))

    totMoves.sort(key=lambda k: -len(k))

    seen = {}
    ini = tuple([0 for _ in range(len(end))])
    choose(0,ini, seen, totMoves, end)
    solved = False
    #print(seen[end])
    tot += seen[end]

print(tot)


