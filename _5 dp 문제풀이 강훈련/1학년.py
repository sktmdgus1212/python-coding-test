import sys

n = int(sys.stdin.readline())
arr = list(map(int, sys.stdin.readline().rstrip().split()))
res = arr.pop()

dp = [[0] *21 for _ in range(len(arr))]
dp[0][arr[0]] = 1

for i in range(1, len(arr)):
    #print(arr[i])
    for j in range(21):
        if dp[i-1][j] > 0:
            if j + arr[i] <= 20:
                #print(i, j+arr[i])
                dp[i][j+arr[i]] += dp[i-1][j] 
            if j - arr[i] >= 0:
                #print(i, j-arr[i])
                dp[i][j-arr[i]] += dp[i-1][j] 
#print(dp)
print(dp[len(arr)-1][res])