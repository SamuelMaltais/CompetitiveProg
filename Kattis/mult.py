nums=[]
hasFirst=False
first=0
for _ in range(int(input())):
    n=int(input())
    if not hasFirst:
        hasFirst=True
        first=n
    elif n % first == 0 and n >= first:
        print(n)
        hasFirst=False
    