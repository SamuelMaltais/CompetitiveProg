def find(graph, mem, m):
    changed=False
    for _ in range(m):
        changed = False
        for i in range(len(mem)):
            for neighbor in graph[i]:
                node, w = neighbor
                if mem[i] + w < mem[node]:
                    changed = True
                    mem[node] = mem[i] + w
        # print(mem)
        if not changed:
            break

    # des nodes sont - infinis
    if changed:
        for i in range(2):
            for i in range(len(mem)):
                for neighbor in graph[i]:
                    node, w = neighbor
                    if mem[i] + w < mem[node]:
                        mem[i] = float('-infinity')
                        mem[node] = float('-infinity')
    

isFirst = True
while True:
    n,m,q = list(map(int, input().split()))
    if n == 0 and m == 0 and q == 0:
        break
    if isFirst:
        isFirst=False
    else:
        print()

    graph={}
    for i in range(n):
        graph[i]=[]
    for _ in range(m):
        a,b,w = list(map(int, input().split()))
        graph[a].append((b,w))
    
    super_mem = {}
    for _ in range(q):
        u,v = list(map(int, input().split()))
        if u in super_mem:
            mem = super_mem[u]
            if mem[v] == float('-infinity'):
                print('-Infinity')
            elif mem[v] < float('infinity'):
                print(mem[v])
            else:
                print('Impossible')
        else:
            mem=[float('infinity') for _ in range(n)]
            mem[u] = 0

            find(graph, mem, m)

            if mem[v] == float('-infinity'):
                print('-Infinity')
            elif mem[v] < float('infinity'):
                print(mem[v])
            else:
                print('Impossible')
                
            super_mem[u] = mem
