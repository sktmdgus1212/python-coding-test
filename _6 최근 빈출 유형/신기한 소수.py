import sys
n = int(sys.stdin.readline().rstrip())
arr = ["2", "3", "5", "7"]

def check(val):
    for a in range(2, val):
        if val % a == 0:
            return False
    return True

for k in range(n-1):
    temp = []
    for i in range(len(arr)):
        for j in range(1, 10, 2):
            val = arr[i] + str(j)
            if check(int(val)):
                temp.append(val)
    arr = temp

for a in arr:
    print(a)