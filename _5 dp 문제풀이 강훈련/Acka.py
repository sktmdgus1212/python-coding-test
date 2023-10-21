import sys

a = list(map(int, sys.stdin.readline().rstrip().split()))

n = a[0]
arr = a[1:]
dp = [[[[-1] * 51 for i in range(51)] for j in range(51)] for k in range(51)]

def find(s, a, b, c):
    if s == 0:
        if a == 0 and b == 0 and c == 0:
            return 1
        else:
            return 0
    
    res = dp[s][a][b][c]
    if res != -1: # 이미 계산됐다면
        return res

    # 처음 계산이라면
    res = 0 

    res += find(s-1, a-1, b, c)
    res += find(s-1, a, b-1, c)
    res += find(s-1, a, b, c-1)
    res += find(s-1, a-1, b-1, c)
    res += find(s-1, a, b-1, c-1)
    res += find(s-1, a-1, b, c-1)
    res += find(s-1, a-1, b-1, c-1)
    res %= 1000000007
    dp[s][a][b][c] = res
    return res

find(n, arr[0], arr[1], arr[2])
print(dp[n][arr[0]][arr[1]][arr[2]])
