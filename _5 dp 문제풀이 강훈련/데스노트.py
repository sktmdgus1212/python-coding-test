import sys
sys.setrecursionlimit(2500)
n, m = map(int, sys.stdin.readline().rstrip().split())

arr = []

for i in range(n):
    arr.append(int(sys.stdin.readline().rstrip()))
maxNum = m * m * n
dp = [maxNum] * (n+1)
dp[n] = 0

def recur(index):
    if dp[index] < maxNum:
        return dp[index]
    
    remain = m - arr[index]

    for i in range(index+1, n+1):
        if remain >= 0:
            if i == n: # 끝줄까지 다 간 경우
                dp[index] = 0
                break
            dp[index] = min(dp[index], remain * remain + recur(i))
            remain -= arr[i] + 1 # 하나 빼고 진행
    return dp[index]

print(recur(0))