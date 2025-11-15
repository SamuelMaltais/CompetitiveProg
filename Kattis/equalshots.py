a,b = list(map(int,input().split()))

t1 = 0
for _ in range(a):
    c,d = list(map(int,input().split()))
    t1 += c*d

t2 = 0
for _ in range(b):
    c,d = list(map(int,input().split()))
    t2 += c*d

if t1 == t2:
    print("same")
else:
    print("different")