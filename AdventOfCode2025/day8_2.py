
boxes = []

with open('input.txt') as f:
    lines = f.readlines()
    for line in lines:
        boxes.append(list(map(int, line.strip().split(","))))

tot = 0

graph = {}
for i in range(len(boxes)):
    graph[i] = []

def dist(box1, box2):
    x, y, z = box1
    x2, y2, z2 = box2

    return ((x - x2)**2 + (y - y2)**2 + (z - z2)**2) ** (1/2)

dists = []

for i in range(len(boxes)):
    for j in range(i + 1, len(boxes)):
        d = dist(boxes[i], boxes[j])
        if i == 0 and j == len(boxes) - 1:
            print(d)
        dists.append((d, (i,j)))

dists.sort()

def travel(visited, curr, graph):
    cir = 1
    for voisin in graph[curr]:
        if voisin not in visited:
            visited.add(voisin)
            cir += travel(visited, voisin, graph)            
    return cir

ok = True
i = 0

while ok:
    a, b = dists[i]
    c, d = b
    graph[c].append(d)
    graph[d].append(c)

    visited = set()
    cir = travel(visited, 0, graph)

    if cir == len(boxes) + 1:
        print("RES", boxes[c][0] * boxes[d][0])
        print(boxes[c][0], boxes[d][0])
        ok = False

    i += 1