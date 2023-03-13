# 바텀 업
n = int(input())
arr = [0 for i in range(n+1)]

# 1인 경우는 횟수가 0이므로 2부터
for i in range(2, n+1):
    arr[i] = arr[i-1] + 1

    if i % 2 == 0:
        arr[i] = min(arr[i // 2] + 1, arr[i])
        
    if i % 3 == 0:
        arr[i] = min(arr[i // 3] + 1, arr[i])
        
    if i % 5 == 0:
        arr[i] = min(arr[i // 5] + 1, arr[i])

print(arr[n])