h, w = map(int, input().split(" "))

wall = [[0] * w for _ in range(h)]
arr = list(map(int, input().split(" ")))

for index, a in enumerate(arr):
    for i in range(a):
        wall[h-1-i][index] = 1

for i in range(h):
    before_wall_index = -1
    for j in range(w):
        if wall[i][j] == 1: # 벽 나올 경우
            if before_wall_index == -1: # 처음 나온 벽의 경우
                before_wall_index = j
            else: # 두번째 나온 벽의 경우
                for k in range(before_wall_index+1, j):
                    wall[i][k] = 2
                before_wall_index = j

ans = 0
for i in range(h):
    ans += wall[i].count(2)
print(ans)