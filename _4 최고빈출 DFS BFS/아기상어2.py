import sys
from collections import deque
n, m = map(int, sys.stdin.readline().rstrip().split())

arr = []

for _ in range(n):
    s = list(map(int, sys.stdin.readline().rstrip().split()))
    arr.append(s)

dx = [-1, 0, 1, 0, 1, 1, -1, -1]
dy = [0, 1, 0, -1, 1, -1, 1, -1]

def bfs(a, b):
    que = deque([[a, b, 1]])
    visited = [[0] * m for _ in range(n)]
    visited[a][b] = 1

    while que:
        i, j, cnt = que.popleft()
        #print(i, j, cnt)
        for k in range(8):
            x = i + dx[k]
            y = j + dy[k]
            if 0 <= x < n and 0 <= y < m:
                if visited[x][y] == 0:
                    if arr[x][y] == 1:
                        return cnt
                    else:
                        visited[x][y] = 1
                        que.append([x, y, cnt+1])
        #print()
    return -1

ans = 0
for i in range(n):
    for j in range(m):
        if arr[i][j] == 0:
            ans = max(ans, bfs(i, j))
            #print("===")
print(ans)