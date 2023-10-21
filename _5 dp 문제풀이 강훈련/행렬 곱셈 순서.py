import sys

n = int(sys.stdin.readline())

arr = []
for _ in range(n):
    arr.append(list(map(int, sys.stdin.readline().rstrip().split())))

dp = [[0]* n for _ in range(n)]

for term in range(1, n):
    for start in range(0, n):
        if start + term >= n:
            break
        dp[start][start+term] = sys.maxsize
        for i in range(start, start+term):
            dp[start][start+term] = min(dp[start][start+term], dp[start][i] + dp[i+1][start+term] + arr[start][0] * arr[i][1]  * arr[start+term][1])
print(dp[0][n-1])
