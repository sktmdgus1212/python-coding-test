import sys
from collections import deque
n, k = map(int, sys.stdin.readline().rstrip().split())

visited = [0 for _ in range(100001)]
visited[n] = 1
que = deque([[n, 0]])
min_size = 100001
while que:
    v, cnt = que.popleft()
    if cnt > min_size:
        continue
    if v == k:
        min_size = cnt
        break

    move = [-1, 1]
    
    val = v + v
    if 0<= val < 100001: 
            if visited[val] == 0:
                visited[val] = cnt
                que.appendleft([val, cnt])

    for m in move:
        a = v + m
        if 0<= a < 100001: 
            if visited[a] == 0:
                visited[a] = cnt+1
                que.append([a, cnt+1])
print(min_size)