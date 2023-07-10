# 벨만 포드: 1 정점 -> 모든 정점
# 다익스트라: 1 정점 -> 모든 정점
# 플로이드 와샬: 모든 정점 -> 모든 정점

import sys
import heapq
n = int(sys.stdin.readline())
m = int(sys.stdin.readline())
arr = [[] for _ in range(n+1)]
dis = [sys.maxsize] * (n+1)

for _ in range(m):
    s, e, c = map(int, sys.stdin.readline().split())
    arr[s].append([c, e])

start, end = map(int, sys.stdin.readline().split(" "))

def dijkstra(start):
    q = []
    heapq.heappush(q, (0, start))
    dis[start] = 0

    while q:
        cost, current = heapq.heappop(q)
        if dis[current] < cost:
            continue
        
        for i in arr[current]:
            c = cost + i[0]
            if c < dis[i[1]]:
                dis[i[1]] = c
                heapq.heappush(q, (dis[i[1]], i[1]))

dijkstra(start)
print(dis[end])