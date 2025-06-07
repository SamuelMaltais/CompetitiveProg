s=set()
toFulfill=[]
for _ in range(int(input())):
    l=input()
    if " " in l:
        toFulfill.append(l.split())
    else:
        s.add(l)

gotOne = True
while gotOne:
    gotOne = False
    for f in toFulfill:
        if f[-1] in s:
            continue
        else:
            if f[2] == 'or':
                for i in range(1, len(f) - 2, 2):
                    if f[i] in s:
                        s.add(f[-1])
                        gotOne=True
                        break
            else:
                allPresent=True
                for i in range(1, len(f) - 2, 2):
                    if f[i] not in s:
                        allPresent=False
                        break
                if allPresent:
                    s.add(f[-1])
                    gotOne=True
           
print(len(s))