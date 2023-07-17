import sys
from collections import deque
n, m, h = map(int, sys.stdin.readline().rstrip().split())
arr = []
visited = [[-1] * m for _ in range(n)]

for _ in range(n):
    s = list(map(str, sys.stdin.readline().rstrip()))
    arr.append(s)

x1, y1, x2, y2 = map(int, sys.stdin.readline().rstrip().split())
x1 -= 1
y1 -= 1
x2 -= 1
y2 -= 1

que = deque([[x1, y1]])
visited[x1][y1] = 0
dx = [-1, 0, 1,0]
dy = [0, 1, 0, -1]
ans = -1
while que:
    i, j = que.popleft()
    #print(i, j, cnt)
    if i == x2 and j == y2:
        ans = visited[i][j]
        break
    for k in range(4):
        cur_x = i
        cur_y = j
        for d in range(1, h+1):
            cur_x = cur_x + dx[k]
            cur_y = cur_y + dy[k]
            
            #print("*", cur_x, dx[k], cur_y, dy[k], k)
            if cur_x<0 or cur_x>=n or cur_y<0 or cur_y>=n: 
                break
            if arr[cur_x][cur_y] == "#":
                break
            if visited[cur_x][cur_y] ==-1:
                #print("=",i, j, cur_x, cur_y, cnt+1)
                que.append([cur_x, cur_y])
                visited[cur_x][cur_y] = visited[i][j] + 1
            elif visited[cur_x][cur_y] == visited[i][j] + 1:
                continue
            else:
                break
        #print("-----")
print(ans)