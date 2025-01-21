for n in range(int(input())):
    i = list(map(int, input().split()))
    row1 = i[0]
    row2 = i[0]

    pref1 = i[1]
    pref2 = i[2]
    nopref = i[3]
    rem = 0


    placed = min(row1, pref1)
    rem += row1 - placed
    
    placed2 = min(row2,pref2)
    rem +=  row2 - placed2

    print(placed +placed2 + min(nopref, rem))
