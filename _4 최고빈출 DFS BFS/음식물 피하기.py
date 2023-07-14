import sys
sys.setrecursionlimit(100000)

n, m, k = map(int, sys.stdin.readline().rstrip().split())
arr = [[0] * m for _ in range(n)]
for _ in range(k):
    r, c = map(int, sys.stdin.readline().rstrip().split())
    arr[r-1][c-1] = 1

def dfs(i, j):
    dx = [-1, 0, 1, 0]
    dy = [0, 1, 0, -1]
    global temp
    temp += 1
    arr[i][j] = 0
    for k in range(4):
        x = i + dx[k]
        y = j + dy[k]

        if 0 <= x < n and 0 <= y < m:
            if arr[x][y] == 1:
                dfs(x, y)

ans = 0
for i in range(n):
    for j in range(m):
        if arr[i][j] == 1:
            temp = 0
            dfs(i, j)
            ans = max(ans, temp)
print(ans)