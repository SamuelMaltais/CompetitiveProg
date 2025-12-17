
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

for i in range(1000):
    a, b = dists[i]
    c, d = b
    graph[c].append(d)
    graph[d].append(c)


def travel(visited, curr, graph):
    cir = 1
    for voisin in graph[curr]:
        if voisin not in visited:
            visited.add(voisin)
            cir += travel(visited, voisin, graph)            
    return cir

tot = 1
circuits = []

# print(graph)

visited = set()
for i in range(len(boxes)):
    if i not in visited:
        visited.add(i)
        cir = travel(visited, i, graph)
        circuits.append(cir)


circuits.sort(reverse=True)

tot = 1
for i in range(3):
    tot *= circuits[i]


visited = set()
for i in range(len(boxes)):
    if i not in visited:
        visited.add(i)
        cir = travel(visited, i, graph)
        circuits.append(cir)




print(tot)