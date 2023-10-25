import sys

_s, _n = map(str, sys.stdin.readline().rstrip().split())
s = int(_s)

arr = []

def one(draw):
    for i in range(1, s+1):
        draw[0][i] = "-"
     
def two(draw):
    for i in range(1, s+1):
        draw[i][0] = "|"

def three(draw):
    for i in range(1, s+1):
        draw[i][s+1] = "|"
           
def four(draw):
    for i in range(1, s+1):
        draw[s+1][i] = "-"

def five(draw):
    for i in range(s+2, 2 * s + 2):
        draw[i][0] = "|"

def six(draw):
    for i in range(s+2, 2 * s + 2):
        draw[i][s+1] = "|"

def seven(draw):
    for i in range(1, s+1):
        draw[2 * s +2][i] = "-"

def find(val, draw):
    if val in [2, 3, 5, 6, 7, 8, 9 ,0]:
        one(draw)
    if val in [4, 5, 6, 8, 9, 0]:
        two(draw)
    if val in [1, 2, 3, 4, 7, 8, 9, 0]:
        three(draw)
    if val in [2, 3, 4, 5, 6, 8, 9]:
        four(draw)
    if val in [2, 6, 8, 0]:
        five(draw)
    if val in [1, 3, 4, 5, 6, 7, 8, 9, 0]:
        six(draw)
    if val in [2, 3, 5, 6, 8, 9, 0]:
        seven(draw)

for val in _n:
    draw = [[' '] * (s+2) for _ in range(2 * s + 3)]
    find(int(val), draw)
    arr.append(draw)

ans = [[] for _ in range(2 * s + 3)]
for index in range(2 * s +3):
    for num in range(len(_n)):
        ans[index] += arr[num][index]
        ans[index] += " "

for a in ans:
    print(''.join(a))