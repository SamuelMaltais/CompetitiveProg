n = int(input())

ks = []

def solve(nums):
    mem = {}
    count = 0
    for i in range(len(nums)):
        s = nums[i]
        if s == 47:
            count += 1
        
        for j in range(i + 1, len(nums)):
            s += nums[j]
            mem[(i,j)] = s
            if s == 47:
                count += 1
    print(count)

def solve(nums):
    s
    pass


for _ in range(n):
    input()
    n2 = int(input())
    nums = []
    for c in input().split():
        nums.append(int(c))
    
    solve(nums)
        