mdist = 50 * 20

def get_dist(store1, store2):
    return abs(store1[0] - store2[0]) + abs(store1[1] - store2[1])

def dfs(start, finish, visited, stores):
    if get_dist(start, finish) <= mdist:
        return True

    for i in range(len(visited)):
        if not visited[i]:
            if get_dist(start, stores[i]) <= mdist:
                visited[i] = True
                if dfs(stores[i], finish, visited, stores):
                    return True
                
    return False

for i in range(int(input())):
    n = int(input())
    visited = [False for _ in range(n)]
    stores = []

    store = input().split()
    start = (int(store[0]), int(store[1]))

    for _ in range(n):
        store = input().split()
        stores.append((int(store[0]), int(store[1])))
    
    store = input().split()
    finish = (int(store[0]), int(store[1]))


    if dfs(start, finish, visited, stores):
        print("happy")
    else:
        print('sad')