def dfs(node, people, steps, time, goals, visisted):
    if steps > time:
        return 0
    if node in goals:
        return people * (time - steps + 1)
    
    if people == 0:
        return 0

    survivors = 0
    voisins = graph[node]

    for v in voisins:
        voisin, m, cost = v
        if voisin not in visisted:
            # Try send max
            visisted.add(node)
            survivors += dfs(voisin, min(people,m), steps + cost, time, goals, visisted)
            
    return survivors
    
for _ in range(int(input())):
    n=int(input())

    graph = {}
    for i in range(1, n+1):
        graph[i] = []


    start, people, time = list(map(int, input().split()))

    goals = set()

    for _ in range(int(input())):
        goals.add(int(input()))

    for _ in range(int(input())):
        a, b, p, t = list(map(int, input().split()))
        graph[a].append([b, p, t])

    visited = set()
    visited.add(start)
    print(min(people,dfs(start, people,0, time, goals, visited)))