for _ in range(int(input())):
    n=int(input())

    initial_graph = []
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