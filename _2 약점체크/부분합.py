n, s = map(int, input().split(" "))
arr = list(map(int, input().split(" ")))
ans = n+1   
value = arr[0]
j = 1
i = 0

print(arr)
while i < len(arr):
    while value < s and j < len(arr):
        value += arr[j]
        j += 1

    while value >= s:
        print(value, i, j, arr[i:j])
        ans = min(ans, j-i)
        value -= arr[i]
        i += 1
    if j == len(arr):
        break

if ans == n+1:
    print(0)
elif ans == 0:
    print(1)
else:
    print(ans)