import sys
from collections import deque
n, m = map(int, sys.stdin.readline().rstrip().split())

arr = []

for _ in range(n):
    s = list(map(int, sys.stdin.readline().rstrip()))
    arr.append(s)

que = deque([[0, 0, 1]])
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]
visited = [[0] * m for _ in range(n)]
visited[0][0] = 1
ans = 10001
while que:
    i, j, count= que.popleft()
    print(i, j, count)
    if i == n-1 and j == m-1:
        ans = min(ans, count)
    for k in range(4):
        x = i + dx[k]
        y = j + dy[k]

        if 0 <= x < n and 0 <= y < m:
            if visited[x][y] == 0 and arr[x][y] == 1:
                visited[x][y] = 1
                que.append([x, y, count+1])
print(ans)