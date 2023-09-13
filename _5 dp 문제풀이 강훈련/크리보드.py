import sys
n = int(sys.stdin.readline())

dp = [0 for _ in range(101)]

dp[1] = 1
dp[2] = 2
dp[3] = 3
dp[4] = 4
dp[5] = 5
# 붙여넣기는 4번쨰부터 손해 -> 그 회차에 전체선택, 복사, 붙여넣기가 더 이득

for i in range(6, n+1):
    max_val = 0
    j = i-3
    max_val = max(max_val, dp[i-3] * 2)
    max_val = max(max_val, dp[i-4] * 3)
    max_val = max(max_val, dp[i-5] * 4)
    max_val = max(max_val, dp[i-1]+1)
    dp[i] = max_val
print(dp[n])
