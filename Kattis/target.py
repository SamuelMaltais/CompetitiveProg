def dist(p1, p2, shot):
    pass

def hitOrMiss(points,p,n):
    gg=0
    for i in range(0,n-1):
        a=points[i]
        b=points[i+1]

    if (b[1] - p[1]) * (a[1] - p[1]) < 0:
        pass
    elif (b[1] - p[1]) == 0 or (a[1] - p[1]) == 0:
        pass


while True:
    n = int(input())
    if n == 0:
        break

    points = []
    for _ in range(int(input())):
        points.append(tuple(map(int,input().split())))

    for s in int(input()):
        p = tuple(map(int, input().split()))
