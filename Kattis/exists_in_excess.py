import random
import copy

n, m = input().split()
n = int(n)
original = {}
for i in range(1, n + 1):
    original[str(i)] = []

for i in range(int(m)):
    a, b = input().split()
    original[a].append((b, i + 1))


graph = {}
visited = []
count = 0
toRemove = []

def make_visits():
    global toVisit
    global visited
    global count
    global graph
    while len(toVisit) > 0:
        toVisitNext = []
        for node in toVisit:
            i = 0
            while i < len(graph[node]):
                neighbour = graph[node][i][0]
                if visited[int(neighbour) - 1]:
                    elem = graph[node].pop(i)
                    i -= 1
                    count += 1
                    toRemove.append(elem[1])
                else:
                    visited[int(neighbour) - 1] = True
                    toVisitNext.append(neighbour)
                i += 1
        toVisit = toVisitNext

while True:
    visited = [False for _ in range(n)]
    count = 0
    toRemove = []
    graph = copy.deepcopy(original)
    
    
    while sum(visited) < len(visited):
        i = random.randint(1, n)
        if not visited[i-1]:
            toVisit = [str(i)]
            visited[i-1] = True
            make_visits()
            for i in range(1, n + 1):
                if not visited[n - 1]:
                    break
    if count <= int(m) / 2:
        break

print(count)
for elem in toRemove:
    print(elem)
