from copy import deepcopy

def nums():
    return list(map(int, input().split()))


best = float('infinity')

def backtrack(row_choices, row_choosen, row_binds, i,curr_cost, costs):
    global best

    if i >= len(row_choices):
        print(row_choosen, row_choices, curr_cost)
        best = min(best, curr_cost)
        return curr_cost

    choice = row_choices[i]

    if choice[0] in row_choosen:
        return backtrack(row_choices, row_choosen, row_binds, i + 1, curr_cost, costs)

    if choice[1] in row_choosen:
        return backtrack(row_choices, row_choosen, row_binds, i + 1, curr_cost, costs)


    path_1 = deepcopy(row_choosen)
    path_2 = deepcopy(row_choosen)

    path_1.add(choice[0])
    costs1 = curr_cost + costs[choice[0]]
    for elem in row_binds[choice[0]]:
        path_1.add(elem)
        costs1 += costs[elem]

    backtrack(row_choices, path_1, row_binds, i + 1, costs1, costs)

    path_2.add(choice[1])
    costs1 = curr_cost + costs[choice[1]]
    for elem in row_binds[choice[1]]:
        path_2.add(elem)
        costs1 += costs[elem]
    backtrack(row_choices, path_2, row_binds, i + 1, costs1, costs)




for _ in range(int(input())):
    n = int(input())
    grid = []
    for i in range(n):
        grid.append(nums())
    

    row_choices = []
    row_binds = [[] for _ in range(n)]
    
    column_choices = []
    column_binds = [[] for _ in range(n)]

    for i in range(n):
        for j in range(n):
            if i + 1 < n:
                if grid[i][j] == grid[i + 1][j]:
                    if (i, i + 1) not in row_choices:
                        row_choices.append((i, i + 1))
                elif grid[i][j] == grid[i + 1][j] + 1:
                    row_binds[i].append(i + 1)
                elif grid[i][j] == grid[i + 1][j] - 1:
                    row_binds[i + 1].append(i)
            if j + 1 < n:
                if grid[i][j] == grid[i][j + 1]:
                    if (j, j + 1) not in column_choices:
                        column_choices.append((j, j + 1))
                elif grid[i][j] == grid[i][j] + 1:
                    column_binds[j].append(j + 1)
                elif grid[i][j] == grid[i][j + 1] - 1:
                    column_binds[j + 1].append(j)
    
    a = nums()
    b = nums()
    ok = True
    chosen = set()
    backtrack(row_choices=row_choices, row_binds=row_binds, i=0, curr_cost=0, costs=a, row_choosen=chosen)
    if best == float('infinity'):
        ok = False

    tot = best
    best = float('infinity')
    chosen = set()
    print("columns")
    backtrack(row_choices=column_choices, row_binds=column_binds, i=0, curr_cost=0, costs=b, row_choosen=chosen)
    tot += best
    if best == float('infinity'):
        ok = False
    
    if ok:
        print(tot)
    else:
        print(-1)


    