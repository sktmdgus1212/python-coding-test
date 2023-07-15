import sys
from collections import deque

n, k = map(int, sys.stdin.readline().rstrip().split())

visited = [0 for _ in range(100001)]
visited[n] = 1
que = deque([[n, -1, 0]])
min_size = 100001
arr = [-1 for _ in range(100001)]
while que:
    cur, v, cnt = que.popleft()
    arr[cur] = v

    if cnt > min_size:
        continue

    if cur == k:
        min_size = cnt
        break

    move = [cur,-1, 1]
    for m in move:
        val = cur + m
        if 0 <= val < 100001:
            if visited[val] == 0:
                visited[val] = 1
                #print(val, cur)
                que.append([val, cur, cnt+1])
print(min_size)
result = deque([])
w = k
while True:
    result.appendleft(w)
    w = arr[w]
    if w == -1:
        break
    
print(*result)