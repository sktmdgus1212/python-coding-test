import sys
from collections import deque
tc = int(sys.stdin.readline())
ans = []
for l in range(tc):
    n, k = map(int, sys.stdin.readline().rstrip().split())
    zz = list(map(int, sys.stdin.readline().rstrip().split()))
    obj = [0] + zz
    arr = [[0] * (n+1) for _ in range(n+1)]
    arr_check = [[0] * (n+1) for _ in range(n+1)]
    time = 0
    que = deque([])
    check = [0] + zz
    indegree = [0] * (n+1)
    for _ in range(k):
        a = list(map(int, sys.stdin.readline().rstrip().split()))
        arr[a[0]][a[1]] = 1
        arr_check[a[0]][a[1]] = 1
        indegree[a[1]] += 1
    for i in range(1, n+1):
        if indegree[i] == 0:
            que.append(i)
    final = int(sys.stdin.readline())
    def find(index):
        max_val = check[index]
        for i in range(1, n+1):
            if arr_check[i][index] == 1:
                max_val = max(max_val, check[i] + check[index])
        return max_val
    while que:
        val = que.popleft()
        for i in range(1, n+1):
            if arr[val][i] == 1:
                arr[val][i] = 0
                indegree[i] -= 1
                if indegree[i] == 0:
                    check[i] = find(i)
                    que.append(i)
    #print(check)
    ans.append(check[final])
    #print("--")
for a in ans:
    print(a)