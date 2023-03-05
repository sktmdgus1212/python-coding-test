arr = list(map(int, input()))

result = arr[0]

for i in range(1, len(arr)):
    if arr[i] <= 1 or result <= 1:
        result += arr[i]
    else:
        result *= arr[i]

print(result)
