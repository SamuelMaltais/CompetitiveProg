def nums():
    return list(map(int, input().split()))

for _ in range(int(input())):
    n = int(input())
    line = input()
    bt = line.count('>')
    lt = line.count('<')

    lt_queue = [i for i in range(1, lt + 1)]
    bt_queue = [i for i in reversed(range(lt + 1, n + 1))]
    
    response = [str(bt_queue.pop())]
    for c in line:
        if c == '<':
            response.append(str(lt_queue.pop()))
        else:
            response.append(str(bt_queue.pop()))
    
    
    print(" ".join(response))