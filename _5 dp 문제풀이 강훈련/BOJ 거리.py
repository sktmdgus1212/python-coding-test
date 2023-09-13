import sys
n = int(sys.stdin.readline())

arr = list(sys.stdin.readline().rstrip())
dp = [sys.maxsize for _ in range(len(arr))]
def dis(i, j):
        return int((i - j)**2)
dp[0]= 0

for i in range(len(arr)):
    for j in range(0, i):
        if arr[i] == 'B' and arr[j] == 'J':
            dp[i] = min(dp[i], dp[j] + dis(i, j))
        elif arr[i] == 'O' and arr[j] == 'B':
            dp[i] = min(dp[i], dp[j] + dis(i, j))
        elif arr[i] == 'J' and arr[j] == 'O':
            dp[i] = min(dp[i], dp[j] + dis(i, j))
if(dp[n-1] == sys.maxsize):
     print(-1)
else:
     print(dp[n-1])