import sys

for line in sys.stdin:
    try:
        n1 = int(line.split()[0])
        n2 = int(line.split()[1])
        res = max(n1,n2) - min(n1,n2)
        print(res)
    except:
        break