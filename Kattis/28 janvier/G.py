import math
def get_movement(a):
    deg = math.radians()
    return math.cos(deg), math.sin(deg)
def time_to_collide(boat1,boat2):
    x, y, a, s = boat1
    x2, y2, a2, s2 = boat1
    dx,dy = get_movement(a)
    dx2,dy2 = get_movement(a2)



for _ in range(int(input())):
    n, r = list(map(int,input().split()))
    boats = []
    for _ in range(n):
        x, y, a, s = list(map(float,input().split()))
        boats.append(x,y,a,s)

    best = -1
    for i in range(len(boats)):
        for j in range(i + 1, len(boats)):
            t = time_to_collide(boats[i],boats[j])
            if t != -1:
                if best != -1:
                    best = min(best, t)
                else:
                    best = t
            