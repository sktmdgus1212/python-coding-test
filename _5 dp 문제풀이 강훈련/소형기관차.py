import sys
n = int(sys.stdin.readline().rstrip())
arr = list(map(int, sys.stdin.readline().rstrip().split()))
train = int(sys.stdin.readline().rstrip())

dp = [[0] * (n+1) for _ in range(4)]
s = [0]
val = 0
for a in arr:
    val += a
    s.append(val)
print(s)

for i in range(1, 4):
    for j in range(i * train, len(dp[i])):
        if i == 1:
            dp[i][j] = max(dp[i][j-1], s[j] - s[j-train])
        else:
            dp[i][j] = max(dp[i][j-1], dp[i-1][j-train] + s[j] - s[j-train])

print(dp[3][n])
print(dp)