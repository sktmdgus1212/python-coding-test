import sys

s = int(sys.stdin.readline())
sum_val = 0
cnt = 0

while sum_val <= s:
    cnt += 1
    sum_val += cnt

print(cnt-1)