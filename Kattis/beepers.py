def dist(curr, dest):
    return abs(curr[0] - dest[0]) + abs(curr[1] - dest[1])

def bruteforce(nodes, visited, curr, origin, traveled):
    if sum(visited) == len(visited):
        return dist(curr, origin) + traveled
    best = float('infinity')
    for i in range(len(nodes)):
        if not visited[i]:
            cpy_visited = visited[:]
            cpy_visited[i] = True
            score = bruteforce(nodes, cpy_visited, nodes[i], origin, traveled + dist(curr, nodes[i]))
            best = min(score, best)

    return best

for  _ in range(int(input())):
    n=input()
    ori=tuple(map(int,input().split()))
    nodes = []
    for _ in range(int(input())):
        x,y=map(int,input().split())
        nodes.append((x,y))
    
    visited = [False for _ in range(len(nodes))]
    print(bruteforce(nodes, visited, ori, ori, 0))