n=int(input())
graph={}
seen=set()
dependencies={}

def tryFulfill(item):
    global seen
    global dependencies
    if item not in graph:
        return

    for n in graph[item]:



for _ in range(n):
    s=input()
    if ' ' in s:
        s = s.split()
        elem1 = s[1]
        elem2 = s[3]
        res = s[5]
        if s[2] == 'or':
            if elem1 in seen or elem2 in seen:
                seen.add(res)
            else:
                if elem1 not in graph:
                    graph[elem1] = []
                if elem2 not in graph:
                    graph[elem2] = []
                graph[elem1].append(res)
                graph[elem2].append(res)
                if res not in dependencies:
                    dependencies[res] = []
                dependencies[res].append([elem1])
                dependencies[res].append([elem2])
        else:
            if elem1 in seen and elem2 in seen:
                seen.add(res)
            else:
                if res not in dependencies:
                    dependencies[res] = []
                dependencies.append([elem1, elem2])

    else:
        seen.add(s)
