import sys
sys.setrecursionlimit(999999999)

a=input()
b=input()


dp = [[0 for _ in range(len(a) + 1)] for _ in range(len(b) + 1)]

dp[0] = [i for i in range(len(a) + 1)]

for i in range(len(b) + 1):
    dp[i][0] = i


for j in range(1, len(b) + 1):
    for i in range(1, len(a) + 1):

        option1 = dp[j][i - 1] + 1 
        option2 = dp[j - 1][i] + 1

        option3 = dp[j - 1][i - 1] + 1 if a[i - 1] == b[j - 1] else float('infinity')
        dp[j][i] = min(option1, option2, option3)


def travelDp(a,b,i, j, dp, curr):
    if i == 0 and j == 0:
        return curr
    
    if i == 0:
        return travelDp(a,b, i, j - 1, dp, curr) + b[j - 1]
    if j == 0:
        return travelDp(a,b, i - 1, j, dp, curr) + a[i - 1]

    option1 = dp[j][i - 1] 
    option2 = dp[j - 1][i]
    option3 = dp[j - 1][i - 1] if a[i - 1] == b[j - 1] else float('infinity')

    if option1 < option2 and option1 < option3:
        return travelDp(a,b, i - 1, j, dp, curr) + a[i - 1]

    if option2 < option3:
        return travelDp(a,b, i, j - 1, dp, curr) + b[j - 1]

    return travelDp(a,b, i - 1, j - 1, dp, curr) + a[i - 1]


# print(len("IThe misso ysoup iso muexch!!!ellent!"))
# print(len("TheI miso s youp iso exmucellenth!!!!"))

res = travelDp(a,b,len(a), len(b), dp, "")
print(res)

