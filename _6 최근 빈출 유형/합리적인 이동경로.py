import sys
import heapq

n, m = map(int, sys.stdin.readline().rstrip().split())
arr = [[0] * (n+1) for _ in range(n+1)]
dist = [sys.maxsize] * (n+1)
dist[2] = 0
heap = []
for _ in range(m):
    x, y, cnt = map(int, sys.stdin.readline().rstrip().split())
    arr[x][y] = cnt
    arr[y][x] = cnt

heapq.heappush(heap, (0, 2))

while heap:
    cost, index = heapq.heappop(heap)
    if dist[index] < cost:
        continue

    for i in range(len(arr[index])): 
        if arr[index][i] > 0:
            if cost +  arr[index][i] < dist[i]:
                dist[i] = cost + arr[index][i]
                heapq.heappush(heap, (dist[i], i))

dp = [0] * (n+1)
def find_path(index):
    if index == 2:
        dp[index] =1
        return 1
    if dp[index] != 0:
        return dp[index]
    
    for i in range(len(arr[index])):
        if arr[index][i] > 0:
            if dist[i] < dist[index]:
                dp[index] += find_path(i)
    return dp[index]

find_path(1)
print(dp[1])