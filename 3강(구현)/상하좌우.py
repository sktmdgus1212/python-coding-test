n = int(input())
direction = list(map(str, input().split()))

cur_x, cur_y = 1, 1
arr = [[0 for j in range(n+1)]for i in range(n+1)]

for d in direction:
    if d == 'R':
        if 1 <= cur_y+1 < n+1:
            cur_y += 1
    elif d == 'L':
        if 1 <= cur_y-1 < n+1:
            cur_y -= 1
    elif d == 'U':
        if 1 <= cur_x-1 < n+1:
            cur_x -= 1
    else:
        if 1 <= cur_x+1 < n+1:
            cur_x += 1
print(cur_x, cur_y)
            
