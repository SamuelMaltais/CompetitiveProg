found_neg = False
def dfs(node, graph, mem, curr):
    global found_neg
    if mem[node] < curr:
        return
    mem[node] = float('-infinity') if found_neg else curr

    for edge in graph[node]:
        otherNode, w = edge
        if w < 0:
            found_neg = True
        dfs(otherNode, graph, mem, curr + w)

    
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
        graph[b].append((a,w))

    super_mem = {}
    for _ in range(q):
        u,v = list(map(int, input().split()))
        if u in super_mem:
            mem = super_mem[u]
            if mem[v] < 0:
                print('-Infinity')
            elif mem[v] < float('infinity'):
                print(mem[v])
            else:
                print('Impossible')
        else:
            found_neg = False
            mem={}
            for i in range(n):
                mem[i]=float('infinity')
            dfs(u, graph, mem, 0)
            if mem[v] < 0:
                print('-Infinity')
            elif mem[v] < float('infinity'):
                print(mem[v])
            else:
                print('Impossible')

