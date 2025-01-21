for n in range(int(input())):
    r = ''
    for c in reversed(input()): 
        if c == 'p':
            r += 'q'
        elif c == 'q':
            r += 'p'
        else:
            r += 'w'
    print(r)