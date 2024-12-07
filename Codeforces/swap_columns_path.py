import sys

for n in range(int(input())):
    columns = int(input())
    row1 = list(map(int, input().split()))
    row2 = list(map(int, input().split()))
    tot = 0
    # best pivot is the
    best_pivot = -sys.maxsize
    for i in range(columns):
        if row1[i] > row2[i]:
            tot += row1[i]
            if row2[i] > best_pivot:
                best_pivot = row2[i]
        else:
            tot += row2[i]
            if row1[i] > best_pivot:
                best_pivot = row1[i]

    print(tot + best_pivot)
        

