import sys

n = int(sys.stdin.readline())
arr = []

for _ in range(n):
    t, p = map(int, sys.stdin.readline().rstrip().split())
    arr.append([t, p])

dp = [0 for _ in range(n+1)]

for i in range(1, n+1):
    dp[i] = max(dp[i], dp[i-1]) # 해당 날짜의 이익은 전날 이익보다 크거나 같다
    fin_date = i + arr[i-1][0] -1 # 해당 날짜의 상담했을 경우 날짜

    if fin_date <= n:
        dp[fin_date] = max(dp[fin_date], dp[i-1] + arr[i-1][1]) # 해당 날짜는 상담을 해야하므로 이전 날짜의 최대값과 해당 날 상담 했을 때 값 vs 기존값

print(max(dp))