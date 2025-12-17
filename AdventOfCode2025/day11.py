import sys
sys.setrecursionlimit(999999999)

l= []

with open('input.txt') as f:
    lines = f.readlines()
    for line in lines:
        l.append(line.strip())

tot = 0

def choose(moves, curr, seen, buttons):
    global best

    if curr in seen:
        if seen[curr] <= moves:
            return
    
    seen[curr] = moves

    for move in buttons:
        newState = list(curr)
        for m in move:
            if newState[m] == '.':
                newState[m] = "#"
            else:
                newState[m] = '.'
        choose(moves + 1, "".join(newState), seen, buttons)


tot = 0
for line in l:
    print(line)
    line = line.split()
    buttons = line[1:len(line)-1]
    state = line[0][1:len(line[0]) - 1]
    end = line[-1]


    totMoves = []
    for b in buttons:
        s = b[1:len(b) - 1]
        totMoves.append(list(map(int,s.split(","))))

    seen = {}
    choose(0, "." * len(state), seen, totMoves)
    tot += seen[state]
    #print(state, seen[state])

print(tot)


