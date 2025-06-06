n,m=input().split()
n=int(m)
corr=[]
errs=[(0,0)]
for e in input().split():
    e=int(e)
    diff = e - errs[-1][1]
    if diff == 1:
        errs[-1] = (errs[-1][0], e)
    else:
        corr_diff = e - (errs[-1][1] + 1)
        if corr_diff == 1:
            pass