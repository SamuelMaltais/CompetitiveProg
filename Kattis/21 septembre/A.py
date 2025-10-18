input()
prev = float('-infinity')
l=[]
for e in input().split():
    if int(e) >= prev:
            prev = int(e)
            l.append(e)
print(' '.join(l))