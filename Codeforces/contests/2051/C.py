for _ in range(int(input())):
    s = []
    line = input().split()
    n = int(line[0])
    questions = input().split()
    knows = input().split()
    if len(knows) == n:
        for _ in range(len(questions)):
            print('1', end='')
        print()
        continue
    if len(knows) < n - 1:
        for _ in range(len(questions)):
            print('0', end='')
        print()
        continue
    mia = 'f'
    for q in questions:
        if mia == 'f':
            if q not in knows:
                mia = q
                print('1',end='')
            else:
                print('0', end='')
        else:
            if q == mia:
                print('1',end='')
            else:
                print('0', end='')


    print()