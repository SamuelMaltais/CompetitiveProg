from collections import deque


for _ in range(int(input())):
    inversed = False
    curr = 0

    arr = deque()
    s=0

    for _ in range(int(input())):
        computeSum = True
        i = input()
        b=0
        if " " in i:
            line = i.split()
            i = line[0]
            b = int(line[1])
        i = int(i)
    
        if i == 1:
            if inversed:
                arr.append(arr.popleft())
            else:
                ok = arr.pop()
                arr.appendleft(ok)
        elif i == 2:
            inversed = not inversed
        else:
            computeSum = False
            
            if inversed:
                arr.appendleft(b)
            else:
                arr.append(b)
            s += len(arr)*b
        
        if computeSum:
            s=0
            if inversed:
                i = 1
                for elem in reversed(arr):
                    s += elem*i
                    i += 1
            else:
                i=1
                for elem in arr:
                    s += elem*i
                    i += 1
        print(s)


