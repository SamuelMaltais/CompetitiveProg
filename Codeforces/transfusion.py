
n=int(input())
for i in range(n):
    input()
    line=input().split()
    a=0
    b=0
    n1=0
    n2=0
    for i in range(len(line)):
        if i % 2 == 0:
            a+=int(line[i])
            n1+=1
        else:
            b+=int(line[i])
            n2+=1
    
    if n1 == 0 and n2 == 0:
        print('YES')
    elif n1 == 0 or n2 == 0:
        print('NO')
    elif a % n1 == 0 and b % n2 == 0 and (a // n1) == (b // n2):
        print('YES')
    else:
        print('NO')

    