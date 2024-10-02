import sys

n = int(input())

graph = {}
strings = [""] * n

for i in range(n):
    strings[i] = sys.stdin.readline()[:-1]
    graph[i] = i

def find_botton(graph, i):
    if graph[i] == i:
        return i
    return find_botton(graph, graph[i])

last_a = 0

for i in range(n - 1):
    line = sys.stdin.readline().split()
    a = int(line[0]) - 1
    b = int(line[1]) - 1
    
    graph[find_botton(graph, a)] = b
    last_a = a


response = strings[last_a]
curr = last_a

while graph[curr] != curr:
    curr = graph[curr]
    response += strings[curr]
    


print(response)




# n = int(input())

# graph = {}
# strings = []

# for i in range(n):
#     strings.append(input())
#     graph[i] = i

# def find_botton(graph, i):
#     if graph[i] == i:
#         return i
#     return find_botton(graph, graph[i])

# last_a = 0

# for i in range(n - 1):
#     line = input().split()
#     a = int(line[0]) - 1
#     b = int(line[1]) - 1
    
#     graph[find_botton(graph, a)] = b
#     last_a = a


# response = strings[last_a]
# curr = last_a

# while graph[curr] != curr:
#     curr = graph[curr]
#     response += strings[curr]
    
# print(response)

# strings = []
# compositions = []

# for i in range(n):
#     strings.append(input())
#     compositions.append([i])

# last_a = 0
# for i in range(n - 1):
#     line = input().split()
#     a = int(line[0]) - 1
#     b = int(line[1]) - 1
#     for elem in compositions[b]:
#         compositions[a].append(elem)
#     last_a = a

# response = ""
# for i in compositions[last_a]:
#     response += strings[i]
