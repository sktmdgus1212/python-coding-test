testcase = int(input())
result = []
for _ in range(testcase):
    n, m = map(int, input().split(" "))
    arr = list(map(int, input().split(" ")))

    dp = []
    index = 0
    for i in range(n):
        dp.append(arr[index:index+m])
        index += m

    for i in range(1, m):
        for j in range(n):
            if j == 0:
                dp[j][i] = max(dp[j][i-1] + dp[j][i], dp[j+1][i-1] + dp[j][i])
            elif j == n - 1:
                dp[j][i] = max(dp[j-1][i-1] + dp[j][i], dp[j][i-1] + dp[j][i])
            else:
                dp[j][i] = max(dp[j-1][i-1] + dp[j][i], dp[j][i-1] + dp[j][i], dp[j+1][i-1] + dp[j][i])
    
    max_val = 0
    for i in range(n):
        if dp[i][m-1] > max_val:
            max_val = dp[i][m-1]

    result.append(max_val)

for a in result:
    print(a)