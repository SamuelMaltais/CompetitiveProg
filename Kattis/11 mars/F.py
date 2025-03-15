import sys

ram = [0 for i in range(1000)]
reg = [0 for i in range(10)]
i=0

for line in sys.stdin:
    reg[i]=line.strip()
    i+=1


