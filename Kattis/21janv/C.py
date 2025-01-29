n, pred, steps = list(map(int, input().split()))

for _ in range(steps):
    if str(pred) in input().split()[1:]:
        print('KEEP')
    else:
        print('REMOVE')