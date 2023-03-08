from collections import deque
import sys

n, m = map(int, input().split())

arr = []

for i in range(n):
    arr.append(list(map(int, input())))

que = deque([[0, 0, 1]])
result = sys.maxsize

while que:
    x, y, count= que.popleft()
    if x == n-1 and y == m-1:
        result = min(result, count)

    if x <= -1 or x >= n or y <= -1 or y >= m:
        continue
    if arr[x][y] == 0:
        continue
    arr[x][y] = 0

    que.append([x+1, y, count+1])
    que.append([x-1, y, count+1])
    que.append([x, y+1, count+1])
    que.append([x, y-1, count+1])

print(result)