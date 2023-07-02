from collections import deque

ans_min = 1000000000
ans_max = -1000000000
n = int(input())
num = deque(list(map(int, input().split(" "))))

operator = list(map(int , input().split(" ")))

def recur(count, n, arr, operator):
    global ans_min
    global ans_max

    if n-1 == count:
        ans_max = max(ans_max, arr[0])
        ans_min = min(ans_min, arr[0])
        return
    
    for i in range(4):
        temp_operator = operator.copy()
        if temp_operator[i] > 0:
            temp_arr = arr.copy()
            temp_operator[i] -= 1
            a1 = temp_arr.popleft()
            a2 = temp_arr.popleft()
            temp_arr.appendleft(cal(i, a1, a2))
            recur(count+1, n, temp_arr, temp_operator)

def cal(op, a1, a2):
    if op == 0:
        return a1+a2
    elif op == 1:
        return a1-a2
    elif op == 2:
        return a1 * a2
    elif op == 3:
        if a1 < 0:
            a1 = -1 * a1
            return -1 * (a1 // a2)
        return a1 // a2
    
recur(0, n, num, operator)
print(ans_max)
print(ans_min)





