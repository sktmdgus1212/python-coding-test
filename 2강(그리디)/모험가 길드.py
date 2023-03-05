n = int(input())
arr = list(map(int, input().split()))
result = 0

arr.sort()
count = 0

for a in arr:
    count += 1
    if count >= a:
        result += 1
        count = 0
    else:
        pass

print(result)