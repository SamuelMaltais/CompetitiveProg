
n = int(input())
g = {}
f = {}
for _ in range(n-1):
    line = input().split()
    a = int(line[0])
    b = int(line[1])
    x = int(line[2])
    t = int(line[3])
    if a in g:
        g[a].append((b, x, t))
    else:
        g[a] = [(b,x,t)]
    if b not in g:
        g[b] = []

water = input().split()
factors = {}

def travel(g, node, water):
    needed = max(0, int(water[node - 1]))
    curr_max = 0
    for neighbour in g[node]:
        if neighbour[2] == 1:
            curr_max = max(curr_max, (travel(g, neighbour[0], water)**(1/2))/(neighbour[1]/100))
        else:
            curr_max = max(curr_max, travel(g, neighbour[0], water)/(neighbour[1]/100))

    return curr_max + needed

print(travel(g, 1, water))