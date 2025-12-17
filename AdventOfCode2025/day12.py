l= []

with open('input.txt') as f:
    lines = f.readlines()
    for line in lines:
        l.append(line.strip())


graph = {}

for line in l:
    a, b = line.split(":")
    root = a
    outputs = b.split()


    graph[root] = []
    for o in outputs:
        graph[root].append(o)

def travel(graph, curr, target, reach):
    global tot

    if curr in reach:
        return reach[curr]

    if curr == target:
        return 1

    if curr not in graph:
        return 0

    f = 0
    for voisin in graph[curr]:
        f += travel(graph, voisin, target, reach)

    reach[curr] = f
    return f

r = {}
a = travel(graph, "svr", "fft", r)
print(r)
b = travel(graph, "fft", "dac", {})

c = travel(graph, "dac", "out",{})


print(a*b*c)