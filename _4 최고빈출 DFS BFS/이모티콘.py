import sys
from collections import deque
n = int(sys.stdin.readline())
c = 0   
arr = [[-1] * (n+1) for _ in range(n+1)]

que = deque([[1, 0]])
arr[1][0] = 0

while que:
    s, c= que.popleft()

    if arr[s][s] == -1: # 복사
        arr[s][s] = arr[s][c] + 1
        que.append([s,s])
    if s+c <= n and arr[s+c][c] == -1: # 붙여넣기
        arr[s+c][c] = arr[s][c] + 1
        que.append([s+c, c])
    if s-1 >= 0 and arr[s-1][c] == -1: # -1
        arr[s-1][c] = arr[s][c] + 1
        que.append([s-1, c])

ans = 1001
for i in range(n+1):
    if arr[n][i] == -1:
        continue
    print(arr[n][i])
    ans = min(ans, arr[n][i])
print(ans)