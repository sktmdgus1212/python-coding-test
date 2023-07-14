import sys

n = int(sys.stdin.readline())
m = int(sys.stdin.readline())
arr = [[] for _ in range(n+1)]

for _ in range(m):
    i, j = map(int ,sys.stdin.readline().rstrip().split())
    arr[i].append(j)
    arr[j].append(i)

visited = [0 for _ in range(n+1)]
visited[1] = 1
def dfs(val):
    global ans
    ans += 1
    visited[val] = 1
    for v in arr[val]:
        if visited[v] == 0:
            dfs(v)

ans = 0
dfs(1)
print(ans-1)