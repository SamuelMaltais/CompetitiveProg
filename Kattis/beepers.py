def dist(curr, dest):
    return abs(curr[0] - dest[0]) + abs(curr[1] - dest[1])

def bruteforce(nodes, visited, curr, origin, traveled, mem):
    obj = tuple((tuple(visited), curr))
    if sum(visited) == len(visited):
        mem[69] = min(dist(curr, origin) + traveled, mem[69])
        return 
    

    if obj in mem:
        if mem[obj] < traveled:
            return
    
    mem[obj] = traveled

    for i in range(len(nodes)):
        if not visited[i]:
            cpy_visited = visited[:]
            cpy_visited[i] = True
            bruteforce(nodes, cpy_visited, nodes[i], origin, dist(curr, nodes[i]) + traveled, mem)

    return 

for  _ in range(int(input())):
    n=input()
    ori=tuple(map(int,input().split()))
    nodes = []
    for _ in range(int(input())):
        x,y=map(int,input().split())
        nodes.append((x,y))
    
    visited = [False for _ in range(len(nodes))]
    t = tuple([True for _ in range(len(nodes))])
    mem = {}
    mem[69] = float('infinity')
    bruteforce(nodes, visited, ori, ori, 0, mem)
    print(mem[69])