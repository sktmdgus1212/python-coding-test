tc = int(input())

ans = []
for t in range(tc):
    arr = list(map(int, input().split(" ")))
    arr.sort(reverse=True)
    ans.append(arr[2])

for a in ans:
    print(a)