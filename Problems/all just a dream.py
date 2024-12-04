n = int(input())
eventsToIndex = {}
stack = []

for _ in range(n):
    line = input().split()

    match(line[0]):
        case "E":
            eventsToIndex[line[1]] = len(stack)
            stack.append(line[1])
        case "D":
            for i in range(min(int(line[1]), len(stack))):
                event = stack.pop()
                del eventsToIndex[event]
        case "S":
            toCheck = line[2:]
            toRemove = len(stack)
            needed = -1
            found = set()

            skip = False
            needsRemove = False
            hasNeeded = False
            for c in toCheck:
                if c in found:
                        skip = True
                        print("Plot Error")
                        break
                
                if c[0] == '!':
                    if c[1:] in eventsToIndex:
                        needsRemove = True
                        toRemove = min(toRemove, eventsToIndex[c[1:]])
                    found.add(c[1:])
                else:
                    if c not in eventsToIndex:
                        skip = True
                        print("Plot Error")
                        break
                    else:
                        hasNeeded = True
                        needed = max(needed, eventsToIndex[c])
                    found.add('!' + c)
            if not skip:
                if needed >= toRemove and needsRemove and hasNeeded:
                    print("Plot Error")
                else:
                    if(len(stack) - toRemove <= 0):
                        print("Yes")
                    else:
                        print(str(len(stack) - toRemove) + " Just a Dream")
