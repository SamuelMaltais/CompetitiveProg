n=int(input())
m=int(input())
s=input().split()
a=[0 for _ in range(n)]
for _ in range(m):
    i = input().split()
    for e in range(n):
        a[e] += int(i[e])
print(s[a.index(max(a))])