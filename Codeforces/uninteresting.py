def recurse(n):
    if int(''.join(list(map(str, n)))) % 9 == 0:
        return True
    for i in range(len(n)):
        if n[i] == 2 or n[i] == 3:
            eh = n.copy()
            eh[i] = eh[i]**2
            if recurse(eh):
                return True
    return False

for i in range(int(input())):
    n=input()
    
    if recurse(list(map(int, list(n)))):
        print("YES")
    else:
        print("NO")