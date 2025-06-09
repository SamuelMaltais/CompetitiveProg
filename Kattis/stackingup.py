import math
from collections import deque
input()
l=list(map(int,input().split()))
o=0
deq=deque()
while len(l)>0:

    e=l.pop()+o
    d=math.floor(math.log(e,2))
    s='1'
    o+=d
    s+='d+'*d
    s+='1+'*(e - 2**d)
    o+=(e - 2**d)
    deq.appendleft(s)

#print(''.join(deq))
c=0
for elem in deq:
    c += len(elem)
print(c)