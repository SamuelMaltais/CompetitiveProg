def nums():
    return list(map(int, input().split()))

for _ in range(int(input())):
    original = input()
    modified = input()


    p1 = 0
    p2 = 0

    ok = True
    while p2 < len(modified) and p1 < len(original):
        if original[p1] != modified[p2]:
            ok = False
            break
    
        initial = original[p1]
        p1 += 1
        p2 += 1
        count_original = 1
        count_modified = 1
        while p1 < len(original) and original[p1] == initial:
            p1 += 1
            count_original += 1
        while p2 < len(modified) and modified[p2] == initial:
            p2 += 1
            count_modified += 1
        if count_modified > 2*count_original:
            ok = False
            break
        if count_original > count_modified:
            ok = False
            break
        #print(count_modified, count_original, initial)
    if ok and p1 == len(original) and p2 == len(modified):
        print('YES')
    else:
        print('NO') 