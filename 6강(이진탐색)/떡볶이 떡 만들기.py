n, m = map(int, input().split(" "))


arr = list(map(int, input().split(" ")))

left = 1
right = max(arr)

result = 0
while left <= right:
    mid = (left + right) // 2

    len_sum = 0
    for a in arr:
        if a - mid > 0:
            len_sum += a-mid
 
    # if len_sum == m:
    #     result = mid
    #     break
    # if len_sum > m:
    #     left = mid + 1
    # elif len_sum < m: 
    #     right = mid-1

    if len_sum < m:
        right = mid - 1
    else:
        result = mid 
        left = mid + 1
print(result)