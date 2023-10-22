import sys
from collections import deque
n = int(sys.stdin.readline())
arr = [[] for _ in range(n+1)]
visited = [0] * (n+1)
for _ in range(n-1):
    a = list(map(int, sys.stdin.readline().rstrip().split()))
    arr[a[0]].append(a[1])
    arr[a[1]].append(a[0])
leaf = deque([])
for i in range(len(arr)):
    if len(arr[i]) == 1:
        leaf.append(i)

while leaf:
    val = leaf.popleft()

    for i in arr[val]:
        for j in arr[i]:
            arr[j].remove(i)
            if len(arr[j]) == 1:
                leaf.append(j)
        visited[i] =1
        arr[i] = []
print(sum(visited))
