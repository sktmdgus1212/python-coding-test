import sys

s = sys.stdin.readline().rstrip()
p = sys.stdin.readline().rstrip()

if p in s:
    print(1)
else:
    print(0)