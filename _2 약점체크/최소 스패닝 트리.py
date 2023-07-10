# 크루스칼 알고리즘
import sys

v, e = map(int, sys.stdin.readline().split())
ans = 0
arr = []
for _ in range(e):
    a, b, c = map(int, sys.stdin.readline().split())
    arr.append([a, b, c])

arr.sort(key= lambda x: x[2])
parent = [i for i in range(v+1)]

def find_parent(x):
    if parent[x] == x:
        return x
    parent[x] = find_parent(parent[x])
    return parent[x]

def union_parent(a, b):
    a = find_parent(a)
    b = find_parent(b)

    if a < b:
        parent[b] = a
    else:
        parent[a] = b

def same_parent(a, b):
    return find_parent(a) == find_parent(b)

for a, b, cost in arr:
    if not same_parent(a, b):
        union_parent(a, b)
        ans += cost
print(ans)
