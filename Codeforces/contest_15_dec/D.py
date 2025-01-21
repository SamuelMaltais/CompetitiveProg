
for n in range(int(input())):
    input()
    l = list(map(int,input().split()))
    occ = {}

    occ[l[0]] = 1
    currmax = 1
    arr = [l[0]]

    for elem in l[1:]:
        if dict.get(occ,elem, 0) == currmax:
            for i in range(1, len(l) + 1):
                if dict.get(occ,i, 0) != currmax:
                    occ[i] = dict.get(occ,i, 0) + 1
                    arr.append(i)
                    break

        elif dict.get(occ,elem, 0) < currmax:
            arr.append(elem)
            occ[elem] = dict.get(occ,elem, 0) + 1
            if occ[elem] > currmax:
                currmax = occ[elem]

    print(' '.join(list(map(str, arr))))
