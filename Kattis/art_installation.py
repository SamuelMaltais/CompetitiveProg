a,b,c = list(map(int, input().split()))
d,e,f = list(map(int, input().split()))
rg,gb = list(map(int, input().split()))

need_red = max(0, a - d)
need_greed = max(b - e, 0)
need_blue = max(c - f, 0)

# print(need_red, need_greed, need_blue)

if need_red > rg:
    print(-1)
elif need_blue > gb:
    print(-1)
else:
    rg -= need_red
    gb -= need_blue

    if need_greed > rg + gb:
        print(-1)
    else:
        print(need_red + need_greed + need_blue)