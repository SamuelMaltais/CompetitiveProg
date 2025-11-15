import sys

sys.setrecursionlimit(99999999)
chapters, dep = list(map(int,input().split()))
chaps_costs =  list(map(int,input().split()))

parents={}
children={}

for i in range(chapters + 1):
    parents[i]=[]
    children[i]=[]
    if i < len(chaps_costs):
        chaps_costs[i] = chaps_costs[i]
    else:
        chaps_costs.append(0)

for _ in range(dep):
    a,b=list(map(int,input().split()))
    a -= 1
    b -= 1

    if a in parents:
        parents[a].append(b)
    else:
        parents[a] = [b]
    if b in parents:
        children[b].append(a)
    else:
        children[b] = [a]

def costOfTopChapter(children, costs, start_node,visited):
    stack = [start_node]
    total_cost = 0
    
    while stack:
        if len(stack) == 0:
            return total_cost
        node = stack.pop()
        if node not in visited:
            visited.add(node)
            if node >= len(costs) or node not in children:
                continue
            total_cost += costs[node]
            for child in children[node]:
                if child not in visited:
                    stack.append(child)

    return total_cost


def findCulminatingChapters(parents):
    culminating = []
    for node in range(chapters):
        if node not in parents:
            continue
        if len(parents[node]) == 0:
            culminating.append(node)
    return culminating


culminatingChapters = findCulminatingChapters(parents)

#print(culminatingChapters)

best=float('inf')
for i in range(len(culminatingChapters)):
    for j in range(i + 1,len(culminatingChapters)):
        visited = set()
        
        s=costOfTopChapter(children,chaps_costs,culminatingChapters[i], visited)
        s+=costOfTopChapter(children,chaps_costs,culminatingChapters[j], visited)

        best = min(best, s)
    
print(best)