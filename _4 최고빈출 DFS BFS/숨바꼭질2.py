    import sys
    from collections import deque
    n, k = map(int, sys.stdin.readline().strip().split())

    que = deque([(n, 0)])
    visited = [0 for _ in range(200001)]
    visited[n] = 0
    min_size = 100001
    min_cnt = 0

    while que:
        v, cnt= que.popleft()
        if cnt > min_size:
            continue      
        if v == k:
            if min_size == 100001:
                min_size = cnt
            if min_size == cnt:
                min_cnt +=1

        move = [-1, 1, v]
        for m in move:
            val = v + m
            if 0 <= val < 200001:
                if visited[val] == 0 or visited[val] == cnt+1:
                    visited[val] = cnt+1
                    que.append((val, cnt+1))
    print(min_size)
    print(min_cnt)