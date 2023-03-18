import sys
import heapq
n, m, c = map(int, input().split(" "))
arr = [[] for i in range(n+1)]

for _ in range(m):
    x, y, z = map(int, input().split(" "))
    arr[x].append([z, y])

distance = [sys.maxsize] * (n+1)

def dijkstra(start):
    distance[start] = 0
    heap = []

    heapq.heappush(heap, (0, start))

    while heap:
        cost, index = heapq.heappop(heap)

        if distance[index] < cost:
            continue

        for a in arr[index]:
            if cost + a[0] < distance[a[1]]:
                distance[a[1]] = cost + a[0]
                heapq.heappush(heap, (distance[a[1]], a[1]))

dijkstra(c)
count = 0
time = 0
print(distance)
for i in range(1, len(distance)):
    if distance[i] != sys.maxsize:
        count += 1
        time = max(distance[i], time)

count -= 1
print(count, time)