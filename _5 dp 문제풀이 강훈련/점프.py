import sys

n = int(sys.stdin.readline())

arr = []

for i in range(n):
    arr.append(list(map(int, sys.stdin.readline().rstrip().split())))

dp = [[0 for _ in range(n)] for j in range(n)]
dp[0][0] = 1
for i in range(n):
    for j in range(n):
        val = arr[i][j]
        
        if val == 0:
            continue
        if 0 <= i+val < n:
            dp[i+val][j] = dp[i][j] + dp[i+val][j]
            #print(i+val, j, dp[n-1][n-1])
        if 0 <= j+val < n:
            dp[i][j+val] = dp[i][j] + dp[i][j+val]
            #print(i, j+val, dp[n-1][n-1])
#print(dp)
print(dp[n-1][n-1])