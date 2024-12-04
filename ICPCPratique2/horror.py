line = input().split()

movies = int(line[0])
horror_list_size = int(line[1])
similarities = int(line[2])


l = input().split()

horror_list = []

graph = {}
curr_best = {}

for i in range(movies):
    graph[i] = []
    curr_best[i] = -1



for elem in l:
    horror_list.append(int(elem))
    curr_best[elem] = 0

    

for i in range(similarities):
    line = input().split()
    a = int(line[0])
    b = int(line[1])
    graph[a].append(b)
    graph[b].append(a)


def bfs(graph, start):

    visited = set()
    to_visit = [start]
    dist = 0

    while to_visit != []:

        to_visit_next = []

        for node in to_visit:

            if curr_best[node] == -1:
                curr_best[node] = dist
            else:
                curr_best[node] = min(curr_best[node], dist)
            for voisin in graph[node]:
                if voisin not in visited:
                    visited.add(voisin)
                    to_visit_next.append(voisin)

        to_visit = to_visit_next
        dist += 1    


for film in horror_list:
    bfs(graph, film)

win = 0
score = curr_best[0]


for film in range(movies):
    if(curr_best[film] == -1):
        win = film
        break
    
    if curr_best[film] > score:
        win = film
        score = curr_best[film]

print(win)