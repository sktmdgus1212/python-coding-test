import sys
from collections import deque
n, m, v = map(int, sys.stdin.readline().rstrip().split())

arr = [[] for _ in range(n+1)]

for _ in range(m):
    i, j = map(int, sys.stdin.readline().rstrip().split())
    arr[i].append(j) 
    arr[j].append(i)
for i in range(n+1):
    arr[i].sort()
    
 #dfs
def dfs(val):
    print(val, end=" ")
    for i in arr[val]:
        if visited[i] == 0:
            visited[i] = 1
            dfs(i)

#bfs
def bfs(val):
    que = deque([val])
    while que:
        a = que.popleft()
        print(a, end=" ")
        for i in arr[a]:
            if visited[i] == 0:
                visited[i] = 1
                que.append(i)

visited = [0 for _ in range(n+1)]
visited[v] = 1
dfs(v)
print()

visited = [0 for _ in range(n+1)]
visited[v] = 1
bfs(v)

tn