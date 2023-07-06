n ,k = map(int, input().split(" "))
arr = list(map(int, input().split(" ")))
cur = []
ans = 0
for i in range(len(arr)): 
    if arr[i] in cur: # 현재 멀티탭에 필요한 기기가 있을 때
        continue
    else: # 필요한 기기가 없을 때
        if len(cur) < n: # 멀티탭에 남는 자리가 있을 때
            cur.append(arr[i])
        else: # 멀티탭에 남는 자리가 없을 때
            for j in range(len(arr)-1, i, -1): 
                if arr[j] in cur:
                    cur.append(cur.pop(cur.index(arr[j])))
            cur = cur[1:]
            cur.append(arr[i])
            ans += 1
            
print(ans)

