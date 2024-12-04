import sys

line = input().split()
n = int(line[0])
s = int(line[1])

graph = {}
bag = []

unreached = []


for i in range(n):
    l = input().split()
    graph[i + 1] = []
    bag.append([int(l[0]), int(l[1])])
    unreached.append(i + 1)


for i in range(n - 1):
    l = input().split()
    graph[int(l[0])].append(int(l[1]))
    graph[int(l[1])].append(int(l[0]))

def knapsack_dp(poid_max, indexes, sacs):
    dp = [[0 for i in range(poid_max + 1)] for i in range(len(indexes) + 1)]

    for i in range(len(indexes) + 1):
        for w in range(poid_max + 1):
            if i == 0 or w == 0:
                dp[i][w] = 0
            elif  sacs[indexes[i - 1] - 1][0] <= w:

                poid_item = sacs[indexes[i - 1] - 1][0]
                value = sacs[indexes[i - 1] - 1][1]

                dp[i][w] = max(value + dp[i - 1][w - poid_item], dp[i -1][w])
            else:
                dp[i][w] = dp[i-1][w]

    return dp[len(indexes)][poid_max]



def get_group(graph, include, node, visited, unreached, missed):
    curr = []

    try:
        unreached.remove(node)
    except:
        pass

    to_travel = []

    for voisin in graph[node]:
        if voisin not in visited:
            visited.add(voisin)
            to_travel.append(voisin)
    
    for voisin in to_travel:
        for elem in get_group(graph, not include, voisin, visited, unreached, missed):
            curr.append(elem)

    if include:
        curr.append(node)

    return curr

# STRAIGHT DE GPT
def color_graph(graph):
    n = len(graph) + 1  # Number of nodes
    red_colorings = []  # List to store valid colorings with only red nodes
    colors = {}     # Dictionary to store the color of each node

    def is_valid(node, color):
        """Check if we can color this node with the given color."""
        # If coloring red, check that no neighbor is red
        if color == 'red':
            for neighbor in graph[node]:
                if colors.get(neighbor) == 'red':
                    return False
        return True

    def dfs(node):
        """Depth-first search to try coloring nodes."""
        if node == n:  # If all nodes are colored, store the red nodes
            red_nodes = [node for node, color in colors.items() if color == 'red']
            red_colorings.append(red_nodes)
            return
        
        # Try coloring the node red
        if is_valid(node, 'red'):
            colors[node] = 'red'
            dfs(node + 1)  # Move to the next node
            del colors[node]  # Uncolor the node for backtracking

        # Try coloring the node blue (no restrictions for blue)
        colors[node] = 'blue'
        dfs(node + 1)  # Move to the next node
        del colors[node]  # Uncolor the node for backtracking

    # Start DFS from node 0
    dfs(1)
    return red_colorings


branches = []
n = 2


sys.setrecursionlimit(2000)
# On traite les graphs isoles
def all_graphs(curr_branch, unreached, graph):


    curr_max = -1

    for group in color_graph(graph):
        print(graph)
        curr = knapsack_dp(s, group, bag)
        curr_max = max(curr_max, curr)
        return curr_max

    # else:
    #     curr_max = all_graphs(groupe_a, unreached[:])
    #     curr_max = max(curr_max, all_graphs(groupe_b, unreached[:]))
    #     return curr_max
        
    return curr_max


print(all_graphs([], unreached, graph))



    
