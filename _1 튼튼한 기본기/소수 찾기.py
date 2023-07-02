n = int(input())
arr = list(map(int, input().split(" ")))
count = 0
for a in arr:
    if a == 1:
        continue
    for i in range(2, a):
        if a % i == 0:
            break
    else:
        count += 1
print(count)