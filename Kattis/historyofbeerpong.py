def solve():

    n = int(input())
    knows = False
    side = True
    previous = list(map(int, input().split()))
    a, b = previous

    if a < 10 and b < 10:
        print('invalid')
        return
    
    if a < 9 or b < 9:
        print('invalid')
        return

    if a < 10:
        knows = True
    if b < 10:
        knows = True
        side = False

    for _ in range(n - 1):
        a,b = list(map(int, input().split()))
        if a > previous[0] or b > previous[1]:
            print('invalid')
            return
        if a != previous[0] and b != previous[1]:
            print("invalid")
            return
        
        if previous[0] - a > 2 or previous[1] - b > 2:
            print("invalid")
            return
        
        if knows:
        
            if side and a != previous[0]:
                print("invalid")
                return
            
            if not side and b != previous[1]:
                print("invalid")
                return
        
            side = not side

        else:
            if a != previous[0]:
                side = True
                knows = True
            elif b != previous[1]:
                side = False
                knows = True
            
        previous = (a,b)

    
    if previous[0] == 0 and previous[1] == 0:
        print('invalid')
        return
    if previous[0] == 0 or previous[1] == 0:
        print("finished")
    else:
        print("ongoing")

solve()