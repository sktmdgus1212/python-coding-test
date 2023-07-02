m = int(input())
n = int(input())

min_val = 10001
sum_val = 0
for val in range(m, n+1):
    if val == 1:
        continue
    for i in range(2, val):
        if val % i == 0:
            break
    else:
        min_val = min(min_val, val)
        sum_val += val

if sum_val == 0:
    print("-1")
else:
    print(sum_val)
    print(min_val)