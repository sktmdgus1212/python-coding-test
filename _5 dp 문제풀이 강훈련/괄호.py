import sys

n = int(sys.stdin.readline())
val = []

for _ in range(n):
    val.append(int(sys.stdin.readline()))

ans = [0 for _ in range(max(val)+1)]
ans[0] =1 
for n in range(2, max(val)+1, 2):
    for i in range(2,n+1, 2):
        ans[n] += ans[i-2] * ans[n-i]
    ans[n] %= 1000000007

#print(ans)
for v in val:
    print(ans[v])