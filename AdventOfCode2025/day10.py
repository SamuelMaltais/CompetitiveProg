triangles = []

with open('input2.txt') as f:
    lines = f.readlines()
    for line in lines:
        triangles.append(list(map(int, line.strip().split(','))))

def IsItIn(point, edges):
    p1, p2 = point

    count_x = 0
    count_y = 0
    for i in range(len(edges) - 1):
        x1, y1 = edges[i]
        x2, y2 = edges[i + 1]

        if x1 == x2:
            if min(y1, y2) < p2 < max(y1,y2):
                toAdd = 1 if x1 > p1 else -1
                count_x += toAdd

        if y1 == y2:
            if min(x1, x2) < p1 < max(x1,x2):
                toAdd = 1 if y1 > p1 else -1
                count_y += toAdd
    
    x1, y1 = edges[0]
    x2, y2 = edges[-1]
    if x1 == x2:
        if min(y1, y2) < p2 < max(y1,y2):
            toAdd = 1 if x1 >= p1 else 0
            count_x += toAdd
    if y1 == y2:
        if min(x1, x2) < p1 < max(x1,x2):
            toAdd = 1 if y1 > p1 else -1
            count_y += toAdd

    return count_x == 0 and count_y == 0

best = 0
for i in range(len(triangles)):
    for j in range(i + 1, len(triangles)):
        mid_x = (triangles[i][0] + triangles[j][0]) // 2
        mid_y = (triangles[i][1] + triangles[j][1]) // 2

        x, y = triangles[i]
        x2, y2 = triangles[j]

        if (abs(x - x2) + 1) * (abs(y2 - y) + 1) < best:
            continue

        if(j == i + 1):
            print(str(i) + " / " + str(len(triangles)))
        
        if IsItIn((mid_x, mid_y), triangles):
            prev = best
            best = max(best,(abs(x - x2) + 1) * (abs(y2 - y) + 1))
            if best > prev:
                print("CURR :", best)

print(best)
