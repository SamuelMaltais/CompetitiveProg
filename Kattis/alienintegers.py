s=input()
d = list(map(str,[0,1,2,3,4,5,6,7,8,9]))
for c in s:
    if c in d and c != s[0]:
        d.remove(c)

i = d.index(s[0])
d.remove(s[0])
if len(d) == 0:
    print('Impossible')
else:
    biggest = d[-1]
    smallest = d[0]
    options = []
    if i > 0:
        options.append(d[i - 1]+(len(s)-1)*biggest)
        
    if i < len(d):
        options.append(d[i]+(len(s)-1)*smallest)

    options.append(biggest*(len(s)-1))
    if smallest != "0":
        options.append(smallest*(len(s)+1))
    else:
        if len(d) > 1:
            options.append(d[1]+len(s)*smallest)
    
    diff = float('infinity')
    s=int(s)
    res=[]
    for op in options:
        if op == '':
            continue
        d = abs(s - int(op))
        if d < diff:
            res = [op]
            diff = d
        elif d == diff:
            res.append(op)
            diff = d
    if len(res) == 1:
        print(res[0])
    else:
        print(res[0], res[1])
