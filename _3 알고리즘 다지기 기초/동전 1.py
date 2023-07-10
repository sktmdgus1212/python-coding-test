import sys
n, k = map(int, sys.stdin.readline().split())

arr = []
dp = [0 for _ in range(k+1)]
dp[0] = 1
for _ in range(n):
    v = int(sys.stdin.readline())
    arr.append(v)

for a in arr:
    for i in range(a, k+1):
        if i - a >= 0:
            dp[i] += dp[i-a]

print(dp[k])