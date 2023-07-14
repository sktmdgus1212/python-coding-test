import sys
a, b = map(int, sys.stdin.readline().rstrip().split())

def dfs(a, b, cnt):
    if a == b:
        global ans
        ans = min(ans, cnt+1)
    if a*2 <= b:
        dfs(a*2, b, cnt+1)
    
    val = int(str(a) + "1")
    if val <= b:
        dfs(val, b, cnt+1)

ans = sys.maxsize
dfs(a, b, 0)
if ans == sys.maxsize:
    print(-1)
else:
    print(ans)
