n,m=input().split()
n=int(n)
corr=[]
errs=[]

e = list(map(int, input().split()))

if e[0] != 1:
    if e[0] == 2:
        corr.append('1')
    else:
        corr.append('1-'+str(e[0] - 1))

start = e[0]
end = e[0]

f=False
if e[-1] == n:
    e.append(n + 2)
    f=True
else:
    e.append(n + 1)




for err in e[1:]:
    if err == end + 1:
        end = err
    else:
        if start == end:
            errs.append(str(start))
        else:
            errs.append(str(start)+'-'+str(end))
        
        if end == err - 2:
            corr.append(str(end + 1))
        else:
            corr.append(str(end + 1)+'-'+str(err-1))
        start = err
        end = err


if f:
    corr.pop()

if len(errs) > 1:   
    print('Errors: ' + ", ".join(errs[:len(errs) - 1]) +" and "+str(errs[-1]))
else:
    print('Errors: '+ errs[0])

if len(corr) > 1: 
    print('Correct: ' + ", ".join(corr[:len(corr) - 1]) +" and "+str(corr[-1]))
else:
    print('Correct: ' + corr[0])
