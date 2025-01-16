from copy import deepcopy

m,n = list(map(int, input().split()))

arr=[]
for _ in range(m):
    arr.append(list(input()))


def get_val(x,y,grid):
    if 0 <= x < len(grid) and 0 <= y < len(grid[0]):
        return grid[x][y]
    return '.'
def check_neighbours(x,y, grid):
    ok = True
    ok = ok and get_val(x + 1, y, grid) == 'T'
    ok = ok and get_val(x - 1, y, grid) == 'T'
    ok = ok and get_val(x, y + 1, grid) == 'T'
    ok = ok and get_val(x, y - 1, grid) == 'T'
    return ok


did_something = True
ring = 1
while did_something:
    did_something = False
    next_arr = deepcopy(arr)
    for x in range(len(arr)):
        for y in range(len(arr[0])):
            if arr[x][y] == 'T':
                if not check_neighbours(x,y, arr):
                    next_arr[x][y] = str(ring)
                did_something = True
    ring += 1
    arr = next_arr

ring -= 2

for row in arr:
    newrow = ''
    
    for elem in row:
        if ring >= 10:
            newrow += (3 - len(str(elem)))*'.' + elem
        else:
            newrow += '.' + elem
    print(newrow)
