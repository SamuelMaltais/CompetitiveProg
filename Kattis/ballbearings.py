from math import asin, pi

for _ in range(int(input())):
    D, d, s = map(float, input().split())
    m = pi / asin((s + d) / (D - d))
    print(int(m))