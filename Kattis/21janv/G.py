events=[]
for _ in range(int(input())):
    a,b,c,d = input().split()
    events.append((a,b,c,d))

k = int(input())

cheese = 0
gloory = 0

for e in events:
    if int(e[1]) < k:
        if e[0] == 'CAUGHT':
            cheese += int(e[2])
            gloory += int(e[3])
        else:
            cheese -= int(e[2])
            gloory -= int(e[3])

print(cheese, gloory)
