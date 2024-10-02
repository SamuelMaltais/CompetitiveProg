while True:
    is_taking = False
    n = int(input())
    last_num = 0
    s1 = 0
    s2 = 0
    if(n == 0):
        break
    for _ in range(n):
        line = input().split()
        num = int(line[1])
        if(line[0] == "DROP"):
            print("DROP 1 " + str(num))
            s1 += num
        else:
            if(num > s2):
                if(s2 != 0):
                    print("TAKE 2 " + " "+ str(s2))
                print("MOVE 1->2" + " "+ str(s1))
                print("TAKE 2 " + " "+ str(num - s2))
                s2 = (s1 + s2 - num)
                s1 = 0
            else:
                print("TAKE 2 " + " "+ str(num))
                s2 -= num
    print()