import sys
from collections import deque
n, m = map(int, sys.stdin.readline().split())

arr = [[] for _ in range(n+1)]
indegree = [0] * (n+1)

que = deque([])

for _ in range(m):
    x, y = map(int, sys.stdin.readline().split())
    arr[x].append(y)
    indegree[y] += 1


for i in range(1, n+1):
    if indegree[i] == 0:
        que.append(i)

ans = []
while que:
    val = que.popleft()
    ans.append(val)

    for v in arr[val]:
        indegree[v] -= 1
        if indegree[v] == 0:
            que.append(v)


for a in ans:
    print(a, end=" ")