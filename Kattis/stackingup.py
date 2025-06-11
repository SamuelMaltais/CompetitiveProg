import math
from collections import deque
input()
l=list(map(int,input().split()))
o=0
deq=deque()

def make_bin_rep(n):
    offset=0
    s='1'
    bits=0
    to_add=0
    while n > 0:
        b = n % 2
        n = n // 2
        if n == 0:
            break
        if b == 1:
            s += 'd'
            bits += 1
        s+="d+"
        to_add += bits
        

    while bits > 1:
        to_add += (bits - 2)
        s+='+'
        bits -= 1
        offset += 1
        
    offset += to_add
    s += '1+'*to_add
    return s, offset

print(make_bin_rep(10))

8

def old_bin_rep(e):
    d=math.floor(math.log(e,2))
    s='1'
    o+=d
    s+='d+'*d
    s+='1+'*(e - 2**d)
    o+=(e - 2**d)
    return s, o

while len(l)>0:
    e=l.pop()+o
    s, o = old_bin_rep(e)
    deq.appendleft(s)

#print(''.join(deq))
c=0
for elem in deq:
    c += len(elem)
print(c)