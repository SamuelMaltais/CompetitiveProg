n, m = input().split()
m = int(m)
coins = list(map(int, input().split()))

dp = [float('infinity') for _ in range(10**5)]
dp[0] = 0

for i in range(len(dp)):
    for coin in coins:
        if i + coin < len(dp):
            dp[i + coin] = min(dp[i + coin], dp[i] + 1)

print(dp[0:20])

curr_max = len(dp)


def compute(curr_max, dp, n):
    for i in range(curr_max, n + 1):
        pass

for _ in range(m):
    q, n = input().split()
    n = int(n)

    if q == 'Q':
        if curr_max < n:
            pass
