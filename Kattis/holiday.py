def s(n):
    o=0
    for i in range(1, n+2):
        o+=i
    return o-1
for n in range(int(input())):
    line=input().split()
    print(line[0],s(int(line[1])))