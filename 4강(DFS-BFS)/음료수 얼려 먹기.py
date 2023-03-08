# 배열은 함수에서 참조 가능!

n, m = map(int, input().split(" "))
arr = []

for i in range(n):
    arr.append(list(map(int, input())))

result = 0

def dfs(i, j):
    if i <= -1 or i >= n or j <= -1 or j >= m:
        return False
    
    if arr[i][j] == 0:
        arr[i][j] = 1
        dfs(i+1, j)
        dfs(i-1, j)
        dfs(i, j+1)
        dfs(i, j-1)
        return True
    return False

for i in range(n):
    for j in range(m):
        if dfs(i, j) == True:
            result += 1
print(result)