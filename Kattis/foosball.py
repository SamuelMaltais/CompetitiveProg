from collections import deque

input()
players=input().split()
l=input()

q=deque()
white=[players[0], players[2]]
black=[players[1], players[3]]

for p in players[4:]:
    q.append(p)

def lose(team, q):
    new = q.popleft()
    q.append(team[1])
    team[1] = team[0]
    team[0]=new
def win(team):
    t=team[0]
    team[0]=team[1]
    team[1]=t

record=[]
best=0
winning=-1
curr=0
currTeam=()
first=True
for c in l:
    #print(black, white, curr)
    won=False
    if c == 'B':
        lose(white, q)
    else:
        lose(black, q)
        won=True

    if won != winning:
        if curr == best:
            record.append(currTeam)
        elif curr > best:
            record = [currTeam]
            best = curr
        if first:
            currTeam = (white[0], white[1]) if won else (black[0], black[1])
            first = False
        else:
            currTeam = (white[1], white[0]) if won else (black[1], black[0])
        winning = won
        curr = 0
        
    if won:
        win(white)
    else:
        win(black)
    curr+=1

if curr == best:
    record.append(currTeam)
elif curr > best:
    record = [currTeam]
    best = curr

for r in record:
    print(r[0], r[1])

#print(record)