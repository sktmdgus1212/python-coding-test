import sys

n = int(sys.stdin.readline())

arr = []
for _ in range(n):
    arr.append(int(sys.stdin.readline()))

max_val = max(arr)

dp = [[0] * 4 for i in range(max_val+1)]

dp[1][1] = 1
dp[1][2] = 0
dp[1][3] = 0

dp[2][1] = 1
dp[2][2] = 1
dp[2][3] = 0

dp[3][1] = 1
dp[3][2] = 1
dp[3][3] = 1

for i in range(4, len(dp)):
    dp[i][1] = dp[i-1][1]
    dp[i][2] = dp[i-2][1] + dp[i-2][2]
    dp[i][3] = dp[i-3][1] + dp[i-3][2] + dp[i-3][3]

for a in arr:
    print(sum(dp[a]))

