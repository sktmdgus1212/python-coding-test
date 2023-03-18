import heapq
import sys
n, m = map(int, input().split(" "))
arr = [[sys.maxsize] * (n+1) for _ in range(n+1)]

for i in range(1, n+1):
    arr[i][i] = 0

for _ in range(m):
    i, j = map(int, input().split(" "))
    arr[i][j] = 1
    arr[j][i] = 1


x, k = map(int, input().split(" "))


for k in range(1, n+1):
    for i in range(1, n+1):
        for j in range(1, n+1):
            arr[i][j] = min(arr[i][k] + arr[k][j], arr[i][j])

dis = arr[1][k] + arr[k][x]

if dis == sys.maxsize:
    print(-1)
else:
    print(dis)