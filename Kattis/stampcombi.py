n,m = input().split()
stamps = list(map(int,input().split()))
curr=0
s1 = [0]
s2 = [0]
for e in stamps:
    curr += e
    s1.append(curr)
curr=0

ma={}
i=1
ma[0] = 0
for e in reversed(stamps):
    curr += e
    ma[curr] = i
    i+=1

s=set()

for _ in range(int(m)):
    q=int(input())
    seen=False
    for i in range(len(s1)):
        if q - s1[i] in ma:
            if ma[q - s1[i]] + i <= len(stamps):
                seen = True
                break
        if q - s1[i] <= 0:
            break

    if seen:
        print("Yes")
    else:
        print("No")