import sys

n = int(sys.stdin.readline())

arr = []

for _ in range(n):
    s = list(map(str, sys.stdin.readline().rstrip()))
    arr.append(s)
ans = 0
def check(arr, n):
    val = 0
    for i in range(n):
        temp = ""
        temp_val = 0
        for j in range(n):
            if j == 0:
                temp = arr[i][j]
                temp_val = 1
            else:
                if temp == arr[i][j]:
                    temp_val += 1
                else:
                    val = max(val, temp_val)
                    temp_val = 1
                    temp = arr[i][j]
        val = max(val, temp_val)
    
    for j in range(n):
        temp = ""
        temp_val = 0
        for i in range(n):
            if i == 0:
                temp = arr[i][j]
                temp_val = 1
            else:
                if temp == arr[i][j]:
                    temp_val += 1
                else:
                    val = max(val, temp_val)
                    temp_val = 1
                    temp = arr[i][j]
        val = max(val, temp_val)
    return val

def swap(arr, i, j):
    temp = arr[i][j]
    arr[i][j] = arr[i][j+1]
    arr[i][j+1] = temp
    return arr

def swap2(arr, i, j):
    temp = arr[i][j]
    arr[i][j] = arr[i+1][j]
    arr[i+1][j] = temp
    return arr

ans = 0
for i in range(n):
    for j in range(n-1):
        swap(arr, i, j)
        ans = max(ans, check(arr, n))
        swap(arr, i, j)

for j in range(n):
    for i in range(n-1):
        swap2(arr, i, j)
        ans = max(ans, check(arr, n))
        swap2(arr, i, j)
print(ans)


