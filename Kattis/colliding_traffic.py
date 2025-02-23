import math
def get_movement(a, s):
    deg = math.radians(a)
    return math.sin(deg)*s, math.cos(deg)*s


def time_to_collide(boat1,boat2, r):
    x, y, a, s = boat1
    x2, y2, a2, s2 = boat1
    dx, dy = get_movement(a, s)
    dx2,dy2 = get_movement(a2, s2)

    # x + t*x0
    # r = 
    t = 0
    maxIter = 500
    dt = 500
    closer = False
    
    while maxIter > 0 and t >= 0:
        d = (((x + dx*t) - (x2 + dx2*t))**2 + ((y + dy*t) - (y2 + dy2*t))**2)**(0.5)
        if d < r:
            print(d, r)
            break
        t += 0.01
        d2 = (((x + dx*t) - (x2 + dx2*t))**2 + ((y + dy*t) - (y2 + dy2*t))**2)**(0.5)
        prev = closer
        if d < d2:
            prev = True
        else:
            prev = False
        if prev != closer:
            dt /= 2
        closer = prev
        if closer:
            t  += dt
        else:
            t -= dt
        print("SDASDASD")
        maxIter -= 1

    if t < 0 or maxIter == 0:
        return -1
    
    return t

for _ in range(int(input())):
    n, r = list(map(int,input().split()))
    boats = []
    for _ in range(n):
        x, y, a, s = list(map(float,input().split()))
        boats.append((x,y,a,s))

    best = -1
    for i in range(len(boats)):
        for j in range(i + 1, len(boats)):
            t = time_to_collide(boats[i],boats[j], r)
            if t != -1:
                if best != -1:
                    best = min(best, t)
                else:
                    best = t

    print(best)