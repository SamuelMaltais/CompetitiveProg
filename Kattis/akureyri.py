from typing import Counter


c = Counter()
c.setdefault(0)

for i in range(int(input())):
    input()
    c[input()] += 1

for k in c:
    if k:
        print(k, c[k])