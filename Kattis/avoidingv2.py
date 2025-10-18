from copy import deepcopy
def dfs(node, bottleneck, time_taken, max_time, goals, visited, graph):
    voisins = graph[node]

    if time_taken > max_time:
        return 0

    if node in goals:
        return bottleneck
    
    if bottleneck == 0:
        return 0

    for i in range(len(voisins)):
        v = voisins[i]
        voisin, m, cost = v
        if voisin not in visited and m != 0 and time_taken + cost <= max_time:
            visited.add(voisin)
            res = dfs(voisin, min(bottleneck, m), time_taken + cost, max_time, goals, visited, graph)
            if res != 0:
                #print("Went from node ", node, " to node ", voisin, " and passed ",res, "with time", time_taken + cost)
                voisins[i] = [voisin, m - res, cost]
                return res
    return 0
    
for _ in range(int(input())):
    n=int(input())

    initial_graph = {}
    for i in range(1, n+1):
        initial_graph[i] = []


    start, people, time = list(map(int, input().split()))

    goals = set()

    for _ in range(int(input())):
        goals.add(int(input()))

    for _ in range(int(input())):
        a, b, p, t = list(map(int, input().split()))
        initial_graph[a].append([b, p, t])
        #initial_graph[b].append([a, -p, t])


    visited = set()
    visited.add(start)

    #print("Max time", time, initial_graph)

    tot = 0
    for initial_time in range(time + 1):
        res = 1
        flotte=0
        graph = deepcopy(initial_graph)
        while res != 0:
            visited = set()
            visited.add(start)
            res = dfs(start, float('infinity'), initial_time, time, goals, visited, graph)
            # print(graph, initial_time, visited, time)
            flotte += res
            #print()
        tot += flotte
        if flotte == 0:
            break
        #print("Flotte max", flotte, "Pour temps", initial_time)
        #print()

    print(min(people, tot))