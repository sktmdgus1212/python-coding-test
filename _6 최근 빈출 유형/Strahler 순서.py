import sys
from collections import deque
tc = int(sys.stdin.readline())
ans = []
for _ in range(tc):
    k, m, p = map(int, sys.stdin.readline().rstrip().split())
    arr = [[0] * (m+1) for _ in range(m+1)]
    arr_check = [[0] * (m+1) for _ in range(m+1)]
    indegree = [0] * (m+1)
    value = [0] * (m+1)
    que = deque([])
    for _ in range(p):
        a = list(map(int, sys.stdin.readline().rstrip().split()))
        arr[a[0]][a[1]] = 1
        arr_check[a[0]][a[1]] = 1
        indegree[a[1]] += 1


    for i in range(len(indegree)):
        if indegree[i] == 0:
            value[i] = 1
            que.append(i)
    def check(index):
        val_list = []
        for i in range(1, m+1):
            if arr_check[i][index] == 1:
                val_list.append(value[i])
        if val_list:
            if val_list.count(max(val_list)) == 1:
                value[index] = max(val_list)
            else:
                value[index] = max(val_list) + 1

    while que:
        now = que.pop()

        for i in range(1, m+1):
            if arr[now][i] == 1:
                arr[now][i] = 0
                indegree[i] -= 1
                if indegree[i] == 0:
                    check(i)
                    que.append(i)
    ans.append([k, max(value)])
for a in ans:
    print(a[0], a[1])