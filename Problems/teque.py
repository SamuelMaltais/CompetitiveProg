n = int(input())
front = []
back = []

for _ in range(n):
    line = input().split()
    i = int(line[1])
    match line[0]:
        case "push_back":
            front.append(i)
        case "push_front":
            back.append(i)
        case "push_middle":
            k = (len(back) + len(front) + 1) // 2
            if(len(front) >= len(back)):
                k = k - len(back)
                front.insert(k, i)
            else:
                #Fix here
                index = k - len(front) - 1
                if index == 1:
                    back.append(i)
                else:
                    back.insert(len(back) - index, i)


                
        case "get":
            if(i >= len(back)):
                print(front[i - len(back)])
            else:
                print(back[-i - 1])