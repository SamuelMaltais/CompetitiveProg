r, c=list(map(int, input().split()))

a=list(map(int, input().split()))
b=list(map(int, input().split()))
a.sort()
b.sort()
arr=[]
while len(arr) < r:
    bigger = b.pop()
    row = [bigger]
    for i in range(c - 1):
        j = a.index(max(a))
        a.remove()

