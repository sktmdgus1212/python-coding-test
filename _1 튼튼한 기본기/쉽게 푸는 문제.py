def easyproblem(count):
    index = 0
    c = 1
    sum_val = 0
    while index < count:
        sum_val += c * c
        index += c
        c += 1
    sum_val -= (index - count) * (c-1)
    return sum_val
start, end = map(int, input().split(" "))

print(easyproblem(end)-easyproblem(start-1))

