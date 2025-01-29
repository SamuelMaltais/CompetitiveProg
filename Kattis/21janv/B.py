best=0
curr_t=0
curr_d=0
for i in range(int(input())):
    t, d = list(map(int, input().split()))
    dt = t - curr_t
    dd = d - curr_d
    if dt != 0:
        best = max(best, dd // dt)
    curr_t = t
    curr_d = d

print(best)
