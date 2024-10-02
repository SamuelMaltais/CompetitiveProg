height = 0
offset = 0

def nodes(n):
    return 2**(n + 1) - 1

def go_up(p, q, direction):
    if p == q == 1:
        return 1
    
    if p == 1:
        go_up(d)
    


for i in range(int(input())):
    line = input().split()
    p = line[1].split('/')[0]
    q = line[1].split('/')[1]
    go_up(p, q)

