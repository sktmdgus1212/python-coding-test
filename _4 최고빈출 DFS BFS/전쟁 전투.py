import sys

n, m = map(int, sys.stdin.readline().rstrip().split())

arr = []

for i in range(m):
    l = sys.stdin.readline().rstrip()
    arr.append(list(l))

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]
def dfs(i, j, n, m, val):
    global temp
    
    arr[i][j] = 'O'
    temp += 1
    for k in range(4):
        x = i + dx[k]
        y = j + dy[k]

        if 0 <= x < m and 0 <= y < n:
            if arr[x][y] == val:
                dfs(x, y, n, m, val)
                
white = 0
blue = 0

for i in range(len(arr)):
    for j in range(len(arr[i])):
        if arr[i][j] == 'W':
            temp = 0
            dfs(i, j, n, m, 'W')
            white += temp**2
        elif arr[i][j] == 'B':
            temp = 0
            dfs(i, j, n, m, 'B')
            blue += temp**2
print(white, blue)