loc = input()

y = ord(loc[0]) - ord('a')
x = int(loc[1])

dx = [2, 2, -2, -2, -1, -1, 1, 1]
dy = [-1, 1, -1, 1, 2, -2, 2, -2]

count = 0
for i, j in zip(dx, dy):
    nx = x + i
    ny = y + j

    if 1 <= nx <= 8 and 1 <= ny <= 8:
        count += 1

print(count)