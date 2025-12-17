l= []

with open('input.txt') as f:
    lines = f.readlines()
    for line in lines:
        l.append(line.strip())

tot = 0



def mergeRanges(ranges):
    finalRange = []
    for r in ranges:
        low, up = r
        toRemove = []
        for i in range(len(finalRange)):
            low2, up2 = finalRange[i]
            if (low <= low2 and up >= low2) or (low >= low2 and low <= up2):
                toRemove.append(i)
                j = i + 1
                up = max(up, up2)
                low = min(low, low2)
                while j < len(finalRange):
                    low2, up2 = finalRange[j]
                    if up >= low2:
                        up = max(up, up2)
                        low = min(low, low2)
                        toRemove.append(j)
                    else:
                        break
                    j += 1
                

        for elem in reversed(list(set(toRemove))):
            finalRange.pop(elem)

        finalRange.append((low, up))
        finalRange.sort()

    return finalRange

print(mergeRanges([(1,6), (2,6), (3, 6), (0, 9), (15, 20), (18,19), (3000,4000), (3000, 5000)]))

print(mergeRanges([(0, 1), (0, 1),(0, 50), (25, 100), (101, 200), (223, 400), (220, 400)]))
ranges = []
s = set()
passed=False
for line in l:
    if line == "":
        passed = True
        continue
    if not passed:
        #print(line)
        a, b = line.split("-")

        ranges.append((int(a),int(b)))

f = mergeRanges(ranges)
print(f)
#print(f)
for ok in f:
    tot += ok[1] - ok[0] + 1
print(tot)
