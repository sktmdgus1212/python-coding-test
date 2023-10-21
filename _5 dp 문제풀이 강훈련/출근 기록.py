import sys

z = list(map(str, sys.stdin.readline().rstrip()))


abc = [0 for i in range(3)]
for val in z:
    if val == 'A':
        abc[0] += 1
    elif val == 'B':
        abc[1] += 1
    else:
        abc[2] += 1
ans = [""] * len(z)

dp = [[[[[False for _ in range(3)] for _ in range(3)] for _ in range(51)] for _ in range(51)] for _ in range(51)]

def dfs(a, b, c, prev):
    if abc[0] == a and abc[1] == b and abc[2] == c:
        print(''.join(ans))
        exit(0)

    if dp[a][b][c][prev[0]][prev[1]]:
        return False
    dp[a][b][c][prev[0]][prev[1]] = True

    if a+1 <= abc[0]:
        ans[a+b+c] = 'A'
        if dfs(a+1, b, c, [prev[1], 0]):
            return True
    if b+1 <= abc[1]:
        ans[a+b+c] = 'B'
        if prev[1] != 1:
            if dfs(a, b+1, c, [prev[1], 1]):
                return True
    if c+1 <= abc[2]:
        ans[a+b+c] = 'C'
        if prev[0] != 2 and prev[1] != 2:
            if dfs(a, b, c+1, [prev[1], 2]):
                return True
    return False

dfs(0, 0, 0, [0, 0])
print(-1)