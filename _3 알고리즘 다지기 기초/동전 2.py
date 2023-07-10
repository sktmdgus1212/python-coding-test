import sys
n, k = map(int, sys.stdin.readline().split())

arr = []
dp = [sys.maxsize for _ in range(k+1)]
for _ in range(n):
    v = int(sys.stdin.readline())
    if v > k:
        continue
    if v in arr:
        continue
    arr.append(v)
    dp[v] = 1

for a in arr:
    for i in range(a, k+1):
        if i-a > 0:
            dp[i] = min(dp[i-a]+1, dp[i])

if dp[k] == sys.maxsize:
    print(-1)
else:
    print(dp[k])