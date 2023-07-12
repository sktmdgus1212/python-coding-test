import sys
from collections import deque
n = int(sys.stdin.readline())
arr = []

for _ in range(n):
    s = sys.stdin.readline().rstrip()
    arr.append(list(map(int, s.split())))

dp =[[[0]* n for _ in range(n)]for _ in range(3)]

dp[0][0][1] = 1

for i in range(2, n):
    if arr[0][i] == 0:
        dp[0][0][i] = dp[0][0][i-1]

for i in range(1, n):
    for j in range(1, n):
        if arr[i][j] == 0 and arr[i-1][j] == 0 and arr[i][j-1] == 0:
            dp[2][i][j] = dp[0][i-1][j-1] + dp[1][i-1][j-1] + dp[2][i-1][j-1]
        
        if arr[i][j] == 0:
            dp[0][i][j] = dp[0][i][j-1] + dp[2][i][j-1]
            dp[1][i][j] = dp[1][i-1][j] + dp[2][i-1][j]
print(dp[0][n-1][n-1] + dp[1][n-1][n-1] + dp[2][n-1][n-1])  