def get_y(dx,dy,x,y):
    a = (dy / dx)
    b = y - a * x

    return b


for _ in range(int(input())):
    n, s = list(map(int, input().split()))
    
    balls = []
    

    count = 0
    for _ in range(n):
        dx,dy, x, y = list(map(int, input().split()))
        b = get_y(dx,dy,x,y)
        if b == s or b == 0:
            count += 1
    
    print(count)

