graph = {}
auths_listed = []


while True:
    line = []
    try:
        line = input().split()
        # if line[0] == "-1":
        #     break
    except:
        break

    og = line[0]

    if og not in graph:
        graph[og] = []

    auths_listed.append(og)


    for person in line[1:]:
        if person in graph:
            graph[person].append(og)
        else:
            graph[person] = [og]

        graph[og].append(person)


distance = 0
distances = {}
toVisit = ['PAUL_ERDOS']
visited = set()
toVisitNext = []
visited.add('PAUL_ERDOS')

while len(toVisit) != 0:
    toVisitNext = []
    for node in toVisit:
        distances[node] = distance
        for neighbor in graph[node]:
            if neighbor not in visited:
                toVisitNext.append(neighbor)
                visited.add(neighbor)


    toVisit = toVisitNext
    distance += 1

#aws = ""
for auth in auths_listed:
    if auth in distances:
        print(auth + " " + str(distances[auth]))
    else:
        print(auth + " no-connection")

