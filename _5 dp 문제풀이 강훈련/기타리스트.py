import sys
n, s, m = map(int, sys.stdin.readline().rstrip().split())

arr = list(map(int, sys.stdin.readline().rstrip().split()))

dp = [[0] * (m+1) for i in range(n+1)]
dp[0][s] = 1

for i in range(n):
    for j in range(m+1):
        if dp[i][j] == 1:

            if j + arr[i] <= m:
                dp[i+1][j+arr[i]] = 1
            if j - arr[i] >= 0:
                dp[i+1][j-arr[i]] = 1

print(dp)
for i in range(m, -1, -1):
    if dp[n][i] == 1:
        print(i)
        break
else:
    print(-1)