import sys
from collections import deque
n = int(sys.stdin.readline())
arr = []

for _ in range(n):
    s = list(map(int, sys.stdin.readline().rstrip()))
    arr.append(s)

# 0이 방문한 것, 1이 방문안한 것
visited = arr.copy()
dx = [-1, 0, 1, 0]
dy = [0, -1, 0, 1]

def dfs(i, j):
    global val, size
    if val < size:
        val = size
    for k in range(4):
        x = i + dx[k]
        y = j + dy[k]
        if 0<= x < n and 0 <= y < n:
            if arr[x][y] == 1 and visited[x][y] == 1:
                visited[x][y] = 0
                size += 1
                dfs(x, y)
ans = []

for i in range(n):
    for j in range(n):
        val = 0
        size = 1
        if arr[i][j] == 1 and visited[i][j] == 1:
            visited[i][j] = 0
            dfs(i, j)
        if val > 0:
            # print()
            # print(arr)
            # print(visited)
            ans.append(val)

print(len(ans))
ans.sort()
for a in ans:
    print(a)

