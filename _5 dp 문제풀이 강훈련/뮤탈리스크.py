import sys
from itertools import permutations

n = int(sys.stdin.readline())

arr = list(map(int, sys.stdin.readline().rstrip().split()))
arr.append(0)
arr.append(0)

dp = [[[0] * 61 for j in range(61)] for i in range(61)]
#dp[arr[0]][arr[1]][arr[2]] = 1

for i in range(60, -1, -1):
    for j in range(60, -1, -1):
        for k in range(60, -1, -1):
            if dp[i][j][k] > 0:
                for com in permutations([9, 3, 1], 3):
                    if i - com[0] >= 0:
                        i_ = i - com[0]
                    else:
                        i_ = 0
                    if j - com[1] >= 0:
                        j_ = j - com[1]
                    else:
                        j_ = 0
                    if k - com[2] >= 0:
                        k_ = k - com[2]
                    else:
                        k_ = 0
                    if dp[i_][j_][k_] == 0 or dp[i][j][k] + 1 < dp[i_][j_][k_]:
                        dp[i_][j_][k_] = dp[i][j][k] + 1

print(dp)
print(dp[0][0][0])