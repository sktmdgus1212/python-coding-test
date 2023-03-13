n, m = map(int, input().split(" "))

arr = [0] * (n+1)
dp = [10001] * (m+1)

for i in range(1, n+1):
    val = int(input())
    arr[i] = val
    if val <= m:
        dp[val] = 1


for i in range(1, m+1):
    for a in arr:
        if 0 <= i + a < m+1:
            dp[i+a] = min(dp[i+a], dp[i] + 1)


if dp[m] == 10001:
    print(-1)
else:
    print(dp[m])

