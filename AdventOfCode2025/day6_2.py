grid = []

with open('input.txt') as f:
    lines = f.readlines()
    for line in lines:
        grid.append(line)

nums = []

tot = 0
lastOp = "+"

for i in range(len(grid[0])):
    elements = ""
    for line in grid:
        try:
            elements += line[i]
        except:
            break


    arr = elements.split()
    
    for e in reversed(range(len(arr))):
        if arr[e] == "":
            arr.pop(e)

    actual = "".join(arr)

    if len(actual) > 0:
        if actual[-1] == '*' or actual[-1] == "+":
            if lastOp == "*" and len(nums) != 0:
                curr = 1
                for n in nums:
                    curr *= n
                tot += curr
                print(curr, lastOp, nums)
            else:
                curr = 0
                for n in nums:
                    curr += n
                tot += curr
                print(curr, lastOp, nums)
            nums = []
            lastOp = actual[-1]
            actual = actual[:len(actual)-1]
            nums.append(int(actual))
        else:
            nums.append(int(actual))
    
if lastOp == "*" and len(nums) != 0:
                curr = 1
                for n in nums:
                    curr *= n
                tot += curr
                print(curr, lastOp, nums)
else:
    curr = 0
    for n in nums:
        curr += n
    tot += curr
    print(curr, lastOp, nums)

print(tot)