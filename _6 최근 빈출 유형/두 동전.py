import sys
from collections import deque

n, m = map(int, sys.stdin.readline().rstrip().split())

arr = []
z = []
for i in range(n):
    a = list(sys.stdin.readline().rstrip())
    for j in range(len(a)):
        if a[j] == 'o':
            z.append(i)
            z.append(j)    
    arr.append(a)

que = deque([[z[0], z[1], z[2], z[3], 1]])
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]
#visited = [[False for _ in range(m)] for _ in range(n)]
while que:
    x1, y1, x2, y2, cnt = que.popleft()
    if cnt > 10:
        print(-1)
        exit(0)

    for i in range(4):
        a = x1 + dx[i]    
        b = y1 + dy[i]
        c = x2 + dx[i]
        d = y2 + dy[i]
        if (a < 0 or a >= n or b < 0 or b >= m) and (c < 0 or c >= n or d < 0 or d >= m):
            continue
        if  a < 0 or a >= n or b < 0 or b >= m or c < 0 or c >= n or d < 0 or d >= m:
            print(cnt)
            exit(0)
        else:
            if arr[a][b] == "#":
                a, b = x1, y1
            if arr[c][d] == "#":
                c, d = x2, y2
            que.append([a, b, c, d, cnt+1])
