i = int(input())

def bin_search(i, j, n, list):
    k = (i + j) // 2
    if list[k] == n:
        return k
    if n > list[k]:
        return bin_search(k + 1, j, n, list)
    else:
        return bin_search(i, k - 1, n, list)
    

aws = []
first = True

while True:

    if first:
        first = False
    else:
        i = int(input())
        if i == 0:
            break
        print()

    list1 = []
    list2 = []
    for _ in range(i):
        list1.append(int(input()))
    order_ini = list1[:]
    list1.sort()
    for _ in range(i):
        list2.append(int(input()))
    list2.sort()
   
    nouv = []
    for elem in order_ini:
        k = bin_search(0, len(list1) - 1 , elem, list1)
        nouv.append(str(list2[k]))

    print("\n".join(nouv))
    