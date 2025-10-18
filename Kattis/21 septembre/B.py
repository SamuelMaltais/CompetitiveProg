import math
for _ in range(int(input())):
    g,n = list(map(int, input().split()))
    l=[]
    for i in range(math.ceil(n / 10)):  
        l = l + list(map(int, input().split()))
    popped = [False for _ in range(len(l))]
    for i in range(len(l)):
        for j in range(i):
            if l[i] < l[j]:
                popped[j] = True
            if l[i] > l[j] and popped[j]:
                popped[i] = True
        
    print(g,sum(popped))