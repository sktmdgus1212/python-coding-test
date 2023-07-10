from itertools import combinations
import sys

n = int(sys.stdin.readline())

arr = []
for i in range(1, 11):
    for j in combinations(range(10), i):
        val = list(j)
        val.sort(reverse=True)
        arr.append(int(''.join(map(str, val))))

arr.sort()

if n >= len(arr):
    print(-1)
else:
    print(arr[n])